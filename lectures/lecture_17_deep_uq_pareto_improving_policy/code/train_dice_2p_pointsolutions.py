"""Stage A: train five fixed-(rho, pi2) CDICE-DEQN point solutions.

Each tag in dice_2p_surrogate_lib.ANCHOR_THETAS gets its own 7-D net trained
at the same hyperparameters as notebook 02. Idempotent: skips a tag if its
weights file already exists. Logs unbuffered (stdout flushed every print).

Run with `python -u train_dice_2p_pointsolutions.py` to monitor live.

Sentinel: writes _pt_solutions/2p/stage_A_done.json when all 5 tags are done.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from typing import Optional

import numpy as np
import tensorflow as tf

import dice_2p_surrogate_lib as L

os.environ.setdefault('TF_CPP_MIN_LOG_LEVEL', '2')


def train_one(tag: str, rho: float, pi2: float,
              n_episodes: int, n_inner: int, n_traj: int, n_steps: int,
              batch: int, width: int, seed: int,
              out_tag: Optional[str] = None,
              init_from: Optional[str] = None,
              force: bool = False) -> dict:
    np.random.seed(seed); tf.random.set_seed(seed)
    L.ensure_dirs()
    out_tag = out_tag or tag
    weights_path = os.path.join(L.ARTIFACTS_DIR, f'{out_tag}.weights.h5')
    sim_path = os.path.join(L.ARTIFACTS_DIR, f'{out_tag}_det.npz')

    if not force and os.path.exists(weights_path) and os.path.exists(sim_path):
        print(f'[{out_tag}] cached -> skip', flush=True)
        with np.load(sim_path) as z:
            return {'tag': out_tag, 'rho': rho, 'pi2': pi2, 'cached': True,
                    'scc_2015': float(z['scc'][0]),
                    'scc_2050': float(z['scc'][35]),
                    'scc_2100': float(z['scc'][85])}

    print(f'[{out_tag}] rho={rho:.4f} pi2={pi2:.5f} -> training', flush=True)
    net = L.build_net(input_dim=7, width=width, name=f'pt_net_{out_tag}')
    if init_from is not None:
        if not os.path.exists(init_from):
            raise FileNotFoundError(f'--init-from path not found: {init_from}')
        net.load_weights(init_from)
        print(f'[{out_tag}] warm-started from {init_from}', flush=True)
    loss_fn = L.make_loss_fn(net, augmented=False)
    opt = tf.keras.optimizers.Adam(learning_rate=5e-5, clipvalue=1.0)
    LR_SCHED = {0: 5e-5, int(0.4 * n_episodes): 2e-5, int(0.8 * n_episodes): 1e-5}

    @tf.function
    def train_step(s, r, p):
        with tf.GradientTape() as tape:
            Lv = loss_fn(s, r, p)
        g = tape.gradient(Lv, net.trainable_variables)
        opt.apply_gradients(zip(g, net.trainable_variables))
        return Lv

    rho_arr = np.full(n_traj, rho, dtype='float32')
    pi2_arr = np.full(n_traj, pi2, dtype='float32')
    rng = np.random.default_rng(seed)
    losses: list[float] = []
    t0 = time.time()
    for ep in range(n_episodes):
        if ep in LR_SCHED:
            opt.learning_rate.assign(LR_SCHED[ep])
        states, rho_full, pi2_full = L.gen_traj(net, rho_arr, pi2_arr,
                                                augmented=False,
                                                n_traj=n_traj, n_steps=n_steps,
                                                rng=rng)
        for _ in range(n_inner):
            idx = rng.choice(len(states), batch, replace=False)
            s_b = states[idx]; r_b = rho_full[idx]; p_b = pi2_full[idx]
            Lv = train_step(s_b, r_b, p_b)
            losses.append(float(Lv.numpy()))
            if not np.isfinite(losses[-1]):
                raise RuntimeError(f'[{out_tag}] NaN at episode {ep}')
        if ep % 20 == 0:
            print(f'[{out_tag}] ep {ep:3d}  L={losses[-1]:.3e}  ({time.time()-t0:.0f}s)', flush=True)

    net.save_weights(weights_path)
    res = L.simulate(net, rho, pi2, augmented=False, n_steps=300)
    np.savez_compressed(sim_path,
        year=res['year'], k_abs=res['k_abs'], k_eff=res['k_eff'],
        MAT_GtC=res['MAT_GtC'], TAT=res['TAT'], TOC=res['TOC'],
        mu=res['mu'], con_abs=res['con_abs'], scc=res['scc'],
        carbon_tax=res['carbon_tax'], Eind_GtCO2=res['Eind_GtCO2'],
        losses=np.array(losses, dtype='float32'),
        rho=np.float32(rho), pi2=np.float32(pi2))
    print(f'[{out_tag}] done {(time.time()-t0)/60:.1f} min  '
          f'SCC(2015)={res["scc"][0]:.2f}  SCC(2100)={res["scc"][85]:.2f}  '
          f'TAT(2100)={res["TAT"][85]:.2f}', flush=True)
    return {'tag': out_tag, 'rho': rho, 'pi2': pi2, 'cached': False,
            'scc_2015': float(res['scc'][0]),
            'scc_2050': float(res['scc'][35]),
            'scc_2100': float(res['scc'][85]),
            'TAT_2100': float(res['TAT'][85]),
            'mu_2100': float(res['mu'][85])}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--episodes', type=int, default=200,
                    help='Episodes per point solution (200=classroom, 1000=production).')
    ap.add_argument('--inner', type=int, default=100)
    ap.add_argument('--n-traj', type=int, default=64)
    ap.add_argument('--n-steps', type=int, default=300)
    ap.add_argument('--batch', type=int, default=512)
    ap.add_argument('--width', type=int, default=512)
    ap.add_argument('--seed-base', type=int, default=42)
    ap.add_argument('--only', type=str, default=None,
                    help='Comma-separated list of tags; default = all 5.')
    ap.add_argument('--out-tag', type=str, default=None,
                    help='Override output filename (e.g. "pt_LL_warm"). Implies --only with one tag.')
    ap.add_argument('--init-from', type=str, default=None,
                    help='Path to .weights.h5 to warm-start from.')
    ap.add_argument('--force', action='store_true',
                    help='Re-train even if cached weights exist.')
    ap.add_argument('--theta', type=str, default=None,
                    help='Custom (rho,pi2) e.g. "0.008,0.0015". Requires --out-tag, ignores --only.')
    ap.add_argument('--theta-batch', type=str, default=None,
                    help='Path to JSON list of {tag,rho,pi2} dicts for batch custom-theta runs.')
    args = ap.parse_args()

    L.ensure_dirs()

    # Custom-theta paths bypass the ANCHOR_THETAS dict entirely.
    custom_jobs = []
    if args.theta is not None:
        if args.out_tag is None:
            raise SystemExit('--theta requires --out-tag.')
        rho_v, pi2_v = (float(x) for x in args.theta.split(','))
        custom_jobs.append((args.out_tag, rho_v, pi2_v))
    if args.theta_batch is not None:
        with open(args.theta_batch) as fh:
            for entry in json.load(fh):
                custom_jobs.append((entry['tag'], float(entry['rho']), float(entry['pi2'])))

    summaries = []
    if custom_jobs:
        for i, (tag, rho, pi2) in enumerate(custom_jobs):
            summaries.append(train_one(
                tag, rho=rho, pi2=pi2,
                n_episodes=args.episodes, n_inner=args.inner,
                n_traj=args.n_traj, n_steps=args.n_steps,
                batch=args.batch, width=args.width,
                seed=args.seed_base + i,
                out_tag=tag, init_from=args.init_from,
                force=args.force))
    else:
        tags = list(L.ANCHOR_THETAS.keys()) if args.only is None else [t.strip() for t in args.only.split(',')]
        if args.out_tag is not None and len(tags) != 1:
            raise SystemExit('--out-tag requires --only with a single tag.')
        for i, tag in enumerate(tags):
            rho, pi2 = L.ANCHOR_THETAS[tag]
            summaries.append(train_one(
                tag, rho=rho, pi2=pi2,
                n_episodes=args.episodes, n_inner=args.inner,
                n_traj=args.n_traj, n_steps=args.n_steps,
                batch=args.batch, width=args.width,
                seed=args.seed_base + i,
                out_tag=args.out_tag, init_from=args.init_from,
                force=args.force))

    sentinel = os.path.join(L.ARTIFACTS_DIR, 'stage_A_done.json')
    with open(sentinel, 'w') as f:
        json.dump({'summaries': summaries,
                   'episodes': args.episodes, 'width': args.width}, f, indent=2)
    print(f'Stage A complete. Sentinel -> {sentinel}', flush=True)


if __name__ == '__main__':
    main()
