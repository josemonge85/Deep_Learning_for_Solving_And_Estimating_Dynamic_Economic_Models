"""GP + Sobol + univariate effects from EXACT point-solution SCCs.

Reads cached _det.npz files for a list of theta values, fits a GP per target
year (2020/2050/2100) directly to the exact SCC values, then computes Sobol
indices and univariate effects on the GP predictive mean.

This is option (C) from the d=2 reflection: use the surrogate's smooth
interpolation as guidance only, and anchor downstream UQ on EXACT ground truth
at every theta where we trained Stage A. No surrogate residual leaks into the
GP training set.
"""
from __future__ import annotations

import argparse
import json
import os

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import qmc
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, Matern, WhiteKernel

import dice_2p_surrogate_lib as L

os.environ.setdefault('TF_CPP_MIN_LOG_LEVEL', '2')

YEAR_INDEX = {'2020': 5, '2050': 35, '2100': 85}


def load_anchor_sccs(theta_jsons: list[str]) -> list[dict]:
    points = []
    seen_tags = set()
    for path in theta_jsons:
        with open(path) as fh:
            entries = json.load(fh)
        for e in entries:
            tag = e['tag']
            if tag in seen_tags:
                continue
            sim = os.path.join(L.ARTIFACTS_DIR, f'{tag}_det.npz')
            if not os.path.exists(sim):
                print(f'WARNING: missing {sim}, skipping {tag}')
                continue
            with np.load(sim) as z:
                row = {'tag': tag, 'rho': float(e['rho']), 'pi2': float(e['pi2'])}
                for ylab, idx in YEAR_INDEX.items():
                    row[f'scc_{ylab}'] = float(z['scc'][idx])
            points.append(row); seen_tags.add(tag)
    return points


def fit_gp_per_year(points: list[dict]):
    rho = np.array([p['rho'] for p in points])
    pi2 = np.array([p['pi2'] for p in points])
    X_norm = np.stack([(rho - L.RHO_MIN) / (L.RHO_MAX - L.RHO_MIN),
                       (pi2 - L.PI2_MIN) / (L.PI2_MAX - L.PI2_MIN)], axis=1)

    gps = {}
    for year in YEAR_INDEX.keys():
        y = np.array([p[f'scc_{year}'] for p in points])
        # Log-SCC for the GP target: the SCC is right-skewed, so log is closer to homoscedastic.
        y_log = np.log(np.maximum(y, 1e-12))
        y_mean = y_log.mean(); y_std = y_log.std()
        y_z = (y_log - y_mean) / y_std

        kernel = (ConstantKernel(1.0, (1e-3, 1e3))
                  * Matern(length_scale=[0.3, 0.3],
                           length_scale_bounds=(1e-3, 10.0), nu=2.5)
                  + WhiteKernel(noise_level=1e-6, noise_level_bounds=(1e-12, 1e-2)))
        gp = GaussianProcessRegressor(kernel=kernel, normalize_y=False,
                                      n_restarts_optimizer=8, random_state=0)
        gp.fit(X_norm, y_z)

        # Leave-one-out
        loo_pred_z = np.zeros(len(X_norm))
        for i in range(len(X_norm)):
            mask = np.ones(len(X_norm), dtype=bool); mask[i] = False
            gp_loo = GaussianProcessRegressor(kernel=kernel, normalize_y=False,
                                              n_restarts_optimizer=2, random_state=0)
            gp_loo.fit(X_norm[mask], y_z[mask])
            loo_pred_z[i] = gp_loo.predict(X_norm[i:i+1])[0]
        loo_pred_log = loo_pred_z * y_std + y_mean
        loo_pred_scc = np.exp(loo_pred_log)
        loo_rmse_scc = float(np.sqrt(np.mean((loo_pred_scc - y) ** 2)))
        loo_r2 = float(1.0 - np.var(loo_pred_z - y_z) / np.var(y_z))

        gps[year] = {'gp': gp, 'y_mean': y_mean, 'y_std': y_std,
                     'loo_rmse_scc': loo_rmse_scc, 'loo_r2': loo_r2,
                     'kernel_str': str(gp.kernel_)}
        print(f'GP[{year}]: N={len(X_norm)}  LOO R^2={loo_r2:.4f}  '
              f'RMSE_SCC={loo_rmse_scc:.3f}  kernel={gps[year]["kernel_str"]}',
              flush=True)
    return gps, X_norm


def gp_predict_scc(gps_yr: dict, X_norm: np.ndarray) -> np.ndarray:
    z = gps_yr['gp'].predict(X_norm)
    return np.exp(z * gps_yr['y_std'] + gps_yr['y_mean'])


def compute_sobol(gps: dict, n_saltelli: int = 4096):
    from SALib.sample import saltelli
    from SALib.analyze import sobol
    problem = {'num_vars': 2, 'names': ['rho', 'pi2'],
               'bounds': [[0.0, 1.0], [0.0, 1.0]]}
    sample = saltelli.sample(problem, n_saltelli, calc_second_order=False)
    out = {}
    for year, gpd in gps.items():
        y_pred = gp_predict_scc(gpd, sample)
        Si = sobol.analyze(problem, y_pred, calc_second_order=False, print_to_console=False)
        out[year] = {
            'S1_rho': float(Si['S1'][0]), 'S1_pi2': float(Si['S1'][1]),
            'ST_rho': float(Si['ST'][0]), 'ST_pi2': float(Si['ST'][1]),
            'S1_rho_conf': float(Si['S1_conf'][0]), 'S1_pi2_conf': float(Si['S1_conf'][1]),
            'ST_rho_conf': float(Si['ST_conf'][0]), 'ST_pi2_conf': float(Si['ST_conf'][1]),
        }
        print(f'Sobol[{year}]: '
              f'S1=(rho={out[year]["S1_rho"]:.3f}, pi2={out[year]["S1_pi2"]:.3f})  '
              f'ST=(rho={out[year]["ST_rho"]:.3f}, pi2={out[year]["ST_pi2"]:.3f})',
              flush=True)
    return out


def compute_univariate_effects(gps: dict, n_grid: int = 50, n_marg: int = 1024,
                               seed: int = 0):
    rng = np.random.default_rng(seed)
    grid = np.linspace(0.0, 1.0, n_grid)
    out = {}
    for year, gpd in gps.items():
        out[year] = {}
        for j, name in enumerate(['rho', 'pi2']):
            means = np.zeros(n_grid); p05 = np.zeros(n_grid); p95 = np.zeros(n_grid)
            theta_other = rng.uniform(0, 1, size=n_marg)
            for k, x_val in enumerate(grid):
                if j == 0:
                    X = np.stack([np.full(n_marg, x_val), theta_other], axis=1)
                else:
                    X = np.stack([theta_other, np.full(n_marg, x_val)], axis=1)
                z, z_std = gpd['gp'].predict(X, return_std=True)
                # SCC samples in physical units via lognormal:
                scc_samples = np.exp(z * gpd['y_std'] + gpd['y_mean'])
                means[k] = scc_samples.mean()
                p05[k] = np.percentile(scc_samples, 5)
                p95[k] = np.percentile(scc_samples, 95)
            out[year][name] = {'grid_norm': grid.tolist(),
                                'mean': means.tolist(),
                                'p05': p05.tolist(),
                                'p95': p95.tolist()}
    return out


def plot_sobol(sobol_results: dict, out_path: str):
    years = list(sobol_results.keys())
    fig, axes = plt.subplots(1, len(years), figsize=(4*len(years), 4), sharey=True)
    if len(years) == 1: axes = [axes]
    for ax, year in zip(axes, years):
        s = sobol_results[year]
        x = np.arange(2); w = 0.35
        ax.bar(x - w/2, [s['S1_rho'], s['S1_pi2']], w,
               yerr=[s['S1_rho_conf'], s['S1_pi2_conf']], label='S₁', color='C0')
        ax.bar(x + w/2, [s['ST_rho'], s['ST_pi2']], w,
               yerr=[s['ST_rho_conf'], s['ST_pi2_conf']], label='Sₜ', color='C1')
        ax.set_xticks(x); ax.set_xticklabels([r'$\rho$', r'$\pi_2$'])
        ax.set_ylim(0, 1); ax.set_title(f'SCC({year})')
        ax.grid(axis='y', alpha=0.3); ax.legend()
    fig.suptitle('Sobol indices (GP fit to exact anchor SCCs)', y=1.02)
    fig.tight_layout()
    fig.savefig(out_path, bbox_inches='tight')
    fig.savefig(out_path.replace('.pdf', '.png'), dpi=110, bbox_inches='tight')
    print(f'wrote {out_path}', flush=True)


def plot_univariate(uni: dict, out_path: str):
    years = list(uni.keys())
    fig, axes = plt.subplots(2, len(years), figsize=(4.5*len(years), 7), sharex='col')
    if len(years) == 1: axes = axes.reshape(2, 1)
    for j, name in enumerate(['rho', 'pi2']):
        for k, year in enumerate(years):
            ax = axes[j, k]
            d = uni[year][name]
            grid_phys = (np.array(d['grid_norm']) *
                         (L.RHO_MAX - L.RHO_MIN) + L.RHO_MIN if name == 'rho'
                         else np.array(d['grid_norm']) *
                         (L.PI2_MAX - L.PI2_MIN) + L.PI2_MIN)
            ax.plot(grid_phys, d['mean'], 'C0-', lw=2, label='mean')
            ax.fill_between(grid_phys, d['p05'], d['p95'], alpha=0.25,
                            color='C0', label='[5%, 95%]')
            ax.set_xlabel(rf'$\{name}$' if name == 'rho' else r'$\pi_2$')
            ax.set_ylabel(f'SCC({year})')
            ax.set_title(f'M_{{{name}}}({year})')
            ax.grid(alpha=0.3)
            if j == 0 and k == 0: ax.legend(loc='upper left', fontsize=9)
    fig.suptitle('Univariate effects (GP fit to exact anchor SCCs)', y=1.01)
    fig.tight_layout()
    fig.savefig(out_path, bbox_inches='tight')
    fig.savefig(out_path.replace('.pdf', '.png'), dpi=110, bbox_inches='tight')
    print(f'wrote {out_path}', flush=True)


def plot_contour_2100(gps: dict, points: list[dict], out_path: str):
    n = 80
    grid = np.linspace(0, 1, n)
    R, P = np.meshgrid(grid, grid)
    X = np.stack([R.ravel(), P.ravel()], axis=1)
    Z = gp_predict_scc(gps['2100'], X).reshape(n, n)
    rho_grid = grid * (L.RHO_MAX - L.RHO_MIN) + L.RHO_MIN
    pi2_grid = grid * (L.PI2_MAX - L.PI2_MIN) + L.PI2_MIN
    Rp, Pp = np.meshgrid(rho_grid, pi2_grid)

    fig, ax = plt.subplots(figsize=(7, 5))
    cs = ax.contourf(Rp, Pp, Z, levels=20, cmap='viridis')
    ax.contour(Rp, Pp, Z, levels=10, colors='white', alpha=0.4, linewidths=0.6)
    fig.colorbar(cs, ax=ax, label=r'SCC(2100) (USD/tCO$_2$)')
    rho_anchor = np.array([p['rho'] for p in points])
    pi2_anchor = np.array([p['pi2'] for p in points])
    ax.scatter(rho_anchor, pi2_anchor, c='red', edgecolors='white', s=40,
               linewidths=0.8, label=f'{len(points)} exact anchors')
    ax.set_xlabel(r'$\rho$'); ax.set_ylabel(r'$\pi_2$')
    ax.set_title('GP-interpolated SCC(2100) over (ρ, π₂)')
    ax.legend(loc='upper left', fontsize=9)
    fig.tight_layout()
    fig.savefig(out_path, bbox_inches='tight')
    fig.savefig(out_path.replace('.pdf', '.png'), dpi=110, bbox_inches='tight')
    print(f'wrote {out_path}', flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--anchor-jsons', nargs='+', required=True,
                    help='List of JSON files with [{tag,rho,pi2}, ...]; SCCs read from cached _det.npz.')
    ap.add_argument('--n-saltelli', type=int, default=4096)
    ap.add_argument('--n-grid', type=int, default=50)
    ap.add_argument('--n-marg', type=int, default=1024)
    ap.add_argument('--out-prefix', type=str, default='gp_anchors')
    args = ap.parse_args()

    L.ensure_dirs()
    points = load_anchor_sccs(args.anchor_jsons)
    print(f'\nLoaded {len(points)} exact anchor points across {len(args.anchor_jsons)} JSON files.\n',
          flush=True)

    gps, X_norm = fit_gp_per_year(points)
    sobol_results = compute_sobol(gps, n_saltelli=args.n_saltelli)
    uni = compute_univariate_effects(gps, n_grid=args.n_grid, n_marg=args.n_marg)

    out_json = {
        'n_anchors': len(points),
        'gp': {y: {'loo_r2': gpd['loo_r2'],
                   'loo_rmse_scc': gpd['loo_rmse_scc'],
                   'kernel': gpd['kernel_str']}
               for y, gpd in gps.items()},
        'sobol': sobol_results,
        'univariate_effects': uni,
        'anchors': [{'tag': p['tag'], 'rho': p['rho'], 'pi2': p['pi2'],
                     'scc_2020': p['scc_2020'], 'scc_2050': p['scc_2050'],
                     'scc_2100': p['scc_2100']} for p in points],
    }
    out_path_json = os.path.join(L.ARTIFACTS_DIR, f'{args.out_prefix}.json')
    with open(out_path_json, 'w') as fh:
        json.dump(out_json, fh, indent=2)
    print(f'wrote {out_path_json}', flush=True)

    fig_dir = os.path.join(L.ARTIFACTS_DIR, 'figures')
    os.makedirs(fig_dir, exist_ok=True)
    plot_sobol(sobol_results, os.path.join(fig_dir, f'{args.out_prefix}_sobol.pdf'))
    plot_univariate(uni, os.path.join(fig_dir, f'{args.out_prefix}_univariate.pdf'))
    plot_contour_2100(gps, points, os.path.join(fig_dir, f'{args.out_prefix}_contour.pdf'))


if __name__ == '__main__':
    main()
