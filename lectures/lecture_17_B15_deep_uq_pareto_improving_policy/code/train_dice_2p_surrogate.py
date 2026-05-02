"""Stage B: train the (rho, pi2)-parameterised CDICE-DEQN surrogate.

Architecture: 9-D input (7 economic states + 2 normalized pseudo-states),
768-wide ReLU MLP, 8 outputs (same as the fixed-theta net).

Training protocol applies the B1 fix from the prior 3-parameter EZ failure
(see memory/project_day8_surrogate_v1_v2_status.md):
  - one (rho, pi2) per trajectory (consistent within rollout)
  - 80% Sobol QMC sampling over the (rho, pi2) cube + 20% anchored on the
    five fixed-theta point-solution corners (forces point-solution-like
    state distributions during training)
  - curriculum: cube width grows from 50% (ep 0) to 100% (ep 100) and then
    full-cube sampling
  - corner-vs-center loss diagnostic logged every 20 episodes; if the ratio
    exceeds the kill threshold for too long, abort.

Sentinel: writes _pt_solutions/2p/stage_B_done.json on success.
"""
from __future__ import annotations

import argparse
import json
import os
import time

import numpy as np
import tensorflow as tf

import dice_2p_surrogate_lib as L

os.environ.setdefault('TF_CPP_MIN_LOG_LEVEL', '2')


def diagnostic_thetas(n_corner: int = 64, n_centre: int = 64) -> tuple[np.ndarray, np.ndarray]:
    """Two diagnostic batches: corners (5 anchors, repeated) and center cluster."""
    anchor = np.array(list(L.ANCHOR_THETAS.values()), dtype='float32')  # (5, 2)
    reps = (n_corner + len(anchor) - 1) // len(anchor)
    corners = np.tile(anchor, (reps, 1))[:n_corner]
    rho_c = 0.5 * (L.RHO_MIN + L.RHO_MAX); pi2_c = 0.5 * (L.PI2_MIN + L.PI2_MAX)
    center = np.stack([np.full(n_centre, rho_c, dtype='float32'),
                       np.full(n_centre, pi2_c, dtype='float32')], axis=1)
    return corners, center


def sample_episode_thetas(n_traj: int, episode: int, total_episodes: int,
                          anchor_share: float, narrow_until: int,
                          rng: np.random.Generator) -> np.ndarray:
    """Mix curriculum-Sobol with anchored corners. Returns (n_traj, 2)."""
    n_anchor = int(round(anchor_share * n_traj))
    n_sobol = n_traj - n_anchor
    out = []
    if n_sobol > 0:
        out.append(L.curriculum_thetas(n_sobol, episode, total_episodes,
                                       narrow_until=narrow_until,
                                       seed=int(rng.integers(0, 2**31 - 1))))
    if n_anchor > 0:
        anchor = np.array(list(L.ANCHOR_THETAS.values()), dtype='float32')
        idx = rng.integers(0, len(anchor), size=n_anchor)
        out.append(anchor[idx])
    th = np.concatenate(out, axis=0)
    rng.shuffle(th, axis=0)
    return th


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--episodes', type=int, default=600)
    ap.add_argument('--inner', type=int, default=100)
    ap.add_argument('--n-traj', type=int, default=64)
    ap.add_argument('--n-steps', type=int, default=300)
    ap.add_argument('--batch', type=int, default=512)
    ap.add_argument('--width', type=int, default=768)
    ap.add_argument('--anchor-share', type=float, default=0.20)
    ap.add_argument('--narrow-until', type=int, default=100)
    ap.add_argument('--loss-form', choices=['absolute', 'relative'], default='absolute',
                    help="'absolute' = MSE/CVaR on raw squared FOC residuals; "
                         "'relative' = each FOC residual divided by its own LHS/RHS "
                         "magnitude (per-sample), restoring gradient parity at low-pi2.")
    ap.add_argument('--cvar-alpha', type=float, default=1.0,
                    help='Loss reduction. 1.0 = MSE (default). 0.2 = mean of worst 20% '
                         'of per-sample residuals (CVaR-0.2). Lower alpha -> more '
                         'aggressive on the worst (state, theta) tail.')
    ap.add_argument('--corner-kill-ratio', type=float, default=5.0,
                    help='Abort if L_corner/L_centre exceeds this for too long.')
    ap.add_argument('--corner-kill-grace', type=int, default=40,
                    help='Number of consecutive 20-episode logs above kill ratio before abort.')
    ap.add_argument('--seed', type=int, default=2024)
    ap.add_argument('--lr-fixed', type=float, default=None,
                    help='If set, hold LR constant at this value (skip the 5e-5 -> 1e-5 schedule).')
    ap.add_argument('--resume', action='store_true', help='Continue from saved weights.')
    ap.add_argument('--anchor-set', type=str, default=None,
                    help='Path to JSON list [{tag,rho,pi2}, ...] overriding ANCHOR_THETAS for '
                         'replay buffer + distillation. If None, uses the default 5 corners+center.')
    ap.add_argument('--sensitivity-weight', type=float, default=0.0,
                    help='Weight on parameter-sensitivity residual loss (Section 13). '
                         '0 disables. ~1.0 typical. Doubles per-step compute.')
    ap.add_argument('--distill-weight', type=float, default=0.0,
                    help='Weight on supervised MSE loss between surrogate and corner-net '
                         'outputs at replay states. 0 disables. Requires replay-fraction > 0.')
    ap.add_argument('--replay-fraction', type=float, default=0.25,
                    help='Fraction of each minibatch drawn from the corner-solution '
                         'replay buffer. 0 disables. The buffer pins corner state '
                         'distributions, addressing the v1 on-policy mismatch.')
    ap.add_argument('--replay-pt-width', type=int, default=512,
                    help='Width of the Stage A point-solution networks. Must match '
                         'PT_WIDTH used to train them.')
    ap.add_argument('--arch', choices=['sequential', 'film'], default='film',
                    help="Surrogate architecture. 'film' = theta enters via per-layer "
                         "(gamma, beta) modulation (structurally prevents lazy learning); "
                         "'sequential' = theta concatenated to state input (legacy).")
    args = ap.parse_args()

    np.random.seed(args.seed); tf.random.set_seed(args.seed)
    L.ensure_dirs()
    weights_path = os.path.join(L.ARTIFACTS_DIR, 'surrogate_2p.weights.h5')
    sentinel = os.path.join(L.ARTIFACTS_DIR, 'stage_B_done.json')

    if os.path.exists(sentinel):
        print(f'Stage B sentinel exists: {sentinel} -> skip', flush=True)
        return

    net = L.build_surrogate_net(args.arch, width=args.width, name='surrogate_2p')
    if args.resume and os.path.exists(weights_path):
        net.load_weights(weights_path)
        print(f'Resumed weights from {weights_path}', flush=True)
    print(f'Surrogate net ({args.arch}): {net.count_params()} params', flush=True)

    loss_fn = L.make_loss_fn(net, augmented=True, cvar_alpha=args.cvar_alpha,
                             loss_form=args.loss_form,
                             sensitivity_weight=args.sensitivity_weight)
    print(f'Loss form: {args.loss_form}  reduction: '
          f'{"MSE (mean)" if args.cvar_alpha >= 1.0 else f"CVaR-{args.cvar_alpha:.2f}"}  '
          f'sens_w={args.sensitivity_weight:.2f}', flush=True)
    init_lr = args.lr_fixed if args.lr_fixed is not None else 5e-5
    opt = tf.keras.optimizers.Adam(learning_rate=init_lr, clipvalue=1.0)
    if args.lr_fixed is not None:
        LR_SCHED = {0: args.lr_fixed}
        print(f'LR schedule: fixed at {args.lr_fixed}', flush=True)
    else:
        LR_SCHED = {0: 5e-5,
                    int(0.4 * args.episodes): 2e-5,
                    int(0.8 * args.episodes): 1e-5}

    distill_w = tf.constant(float(args.distill_weight), dtype=tf.float32)

    @tf.function
    def train_step(s, r, p, teacher_out, replay_mask):
        with tf.GradientTape() as tape:
            L_foc = loss_fn(s, r, p)
            # Distillation: masked MSE between surrogate and teacher outputs.
            raw = net(L.make_input(tf.cast(s, tf.float32),
                                   tf.cast(r, tf.float32),
                                   tf.cast(p, tf.float32),
                                   augmented=True))
            kp, lh, mu, nuAT, nuUO, nuLO, etAT, etOC = L.split_policy(raw)
            surr_out = tf.concat([kp, lh, mu, nuAT, nuUO, nuLO, etAT, etOC], axis=1)
            sq_diff = tf.reduce_mean((surr_out - teacher_out) ** 2, axis=-1)  # (B,)
            denom = tf.maximum(tf.reduce_sum(replay_mask), 1.0)
            L_dist = tf.reduce_sum(sq_diff * replay_mask) / denom
            Lv = L_foc + distill_w * L_dist
        g = tape.gradient(Lv, net.trainable_variables)
        opt.apply_gradients(zip(g, net.trainable_variables))
        return Lv

    rng = np.random.default_rng(args.seed)
    losses: list[float] = []
    diag: list[dict] = []
    t0 = time.time()
    above_kill = 0

    # Build the corner-solution replay buffer once. With replay_fraction=0 we
    # skip this and behave identically to v3.
    anchor_set = None
    if args.anchor_set is not None:
        with open(args.anchor_set) as fh:
            entries = json.load(fh)
        anchor_set = {e['tag']: (float(e['rho']), float(e['pi2'])) for e in entries}
        print(f'Anchor set override: {len(anchor_set)} anchors from {args.anchor_set}', flush=True)

    use_replay = args.replay_fraction > 0.0
    use_distill = args.distill_weight > 0.0 and use_replay
    replay_states = replay_rho = replay_pi2 = replay_teacher = None
    if use_replay:
        active_anchors = anchor_set if anchor_set is not None else L.ANCHOR_THETAS
        print(f'Building replay buffer from {len(active_anchors)} anchor solutions '
              f'(pt_width={args.replay_pt_width}, distill={"on" if use_distill else "off"}) ...',
              flush=True)
        if use_distill:
            replay_states, replay_rho, replay_pi2, replay_teacher = (
                L.build_replay_buffer_with_teacher(
                    n_traj_per_corner=args.n_traj, n_steps=args.n_steps,
                    seed=args.seed, pt_width=args.replay_pt_width,
                    anchor_set=anchor_set))
        else:
            replay_states, replay_rho, replay_pi2 = L.build_replay_buffer(
                n_traj_per_corner=args.n_traj, n_steps=args.n_steps,
                seed=args.seed, pt_width=args.replay_pt_width,
                anchor_set=anchor_set)
        print(f'  replay buffer: {replay_states.shape[0]} (state, theta) pairs '
              f'(replay_fraction={args.replay_fraction:.2f}, distill_weight={args.distill_weight:.2f})',
              flush=True)
    n_replay = int(round(args.batch * args.replay_fraction)) if use_replay else 0
    n_onpolicy = args.batch - n_replay

    # Pre-sample corner / center diagnostic states once we have a rough policy
    # (recomputed every 20 episodes against the current policy).
    corners_th, centre_th = diagnostic_thetas(64, 64)

    for ep in range(args.episodes):
        if ep in LR_SCHED:
            opt.learning_rate.assign(LR_SCHED[ep])
        thetas = sample_episode_thetas(
            args.n_traj, ep, args.episodes,
            anchor_share=args.anchor_share,
            narrow_until=args.narrow_until,
            rng=rng)
        rho_arr = thetas[:, 0]; pi2_arr = thetas[:, 1]
        states, rho_full, pi2_full = L.gen_traj(net, rho_arr, pi2_arr,
                                                augmented=True,
                                                n_traj=args.n_traj, n_steps=args.n_steps,
                                                rng=rng)
        for _ in range(args.inner):
            onp_idx = rng.choice(len(states), n_onpolicy, replace=False)
            s_b = states[onp_idx]; r_b = rho_full[onp_idx]; p_b = pi2_full[onp_idx]
            if n_replay > 0:
                rep_idx = rng.choice(len(replay_states), n_replay, replace=False)
                s_b = np.concatenate([s_b, replay_states[rep_idx]], axis=0)
                r_b = np.concatenate([r_b, replay_rho[rep_idx]], axis=0)
                p_b = np.concatenate([p_b, replay_pi2[rep_idx]], axis=0)
            # Build teacher_out + replay_mask aligned with the batch.
            if use_distill:
                t_b = np.zeros((args.batch, 8), dtype='float32')
                t_b[n_onpolicy:] = replay_teacher[rep_idx]
                m_b = np.zeros((args.batch,), dtype='float32')
                m_b[n_onpolicy:] = 1.0
            else:
                t_b = np.zeros((args.batch, 8), dtype='float32')
                m_b = np.zeros((args.batch,), dtype='float32')
            Lv = train_step(s_b, r_b, p_b, t_b, m_b)
            losses.append(float(Lv.numpy()))
            if not np.isfinite(losses[-1]):
                raise RuntimeError(f'NaN loss at episode {ep}')

        if ep % 20 == 0:
            # Corner-vs-center diagnostic: roll a short trajectory under the
            # current policy at corner thetas vs center thetas, evaluate loss.
            rho_c = corners_th[:, 0]; pi2_c = corners_th[:, 1]
            rho_m = centre_th[:, 0]; pi2_m = centre_th[:, 1]
            sC, rC, pC = L.gen_traj(net, rho_c, pi2_c, augmented=True,
                                    n_traj=len(rho_c), n_steps=args.n_steps,
                                    rng=rng)
            sM, rM, pM = L.gen_traj(net, rho_m, pi2_m, augmented=True,
                                    n_traj=len(rho_m), n_steps=args.n_steps,
                                    rng=rng)
            iC = rng.choice(len(sC), min(args.batch, len(sC)), replace=False)
            iM = rng.choice(len(sM), min(args.batch, len(sM)), replace=False)
            L_corner = float(loss_fn(sC[iC], rC[iC], pC[iC]).numpy())
            L_centre = float(loss_fn(sM[iM], rM[iM], pM[iM]).numpy())
            ratio = L_corner / max(L_centre, 1e-12)
            diag.append({'ep': ep, 'L': losses[-1],
                         'L_corner': L_corner, 'L_centre': L_centre, 'ratio': ratio,
                         'wall_s': time.time() - t0})
            print(f'  ep {ep:3d}  L={losses[-1]:.3e}  '
                  f'corner/center={L_corner:.3e}/{L_centre:.3e} ratio={ratio:.2f}  '
                  f'({time.time()-t0:.0f}s)', flush=True)
            if ratio > args.corner_kill_ratio:
                above_kill += 1
                if above_kill >= args.corner_kill_grace:
                    raise RuntimeError(
                        f'Corner-vs-center ratio above {args.corner_kill_ratio} '
                        f'for {above_kill} consecutive logs. Aborting (B1 diagnostic).')
            else:
                above_kill = 0

        # Periodic snapshot in case of crash
        if ep % 100 == 0 and ep > 0:
            net.save_weights(weights_path)

    net.save_weights(weights_path)
    losses_arr = np.array(losses, dtype='float32')
    np.savez_compressed(os.path.join(L.ARTIFACTS_DIR, 'surrogate_2p_losses.npz'),
                        losses=losses_arr,
                        diag_ep=np.array([d['ep'] for d in diag], dtype='int32'),
                        diag_L=np.array([d['L'] for d in diag], dtype='float32'),
                        diag_corner=np.array([d['L_corner'] for d in diag], dtype='float32'),
                        diag_centre=np.array([d['L_centre'] for d in diag], dtype='float32'),
                        diag_ratio=np.array([d['ratio'] for d in diag], dtype='float32'))

    with open(sentinel, 'w') as f:
        json.dump({'episodes': args.episodes,
                   'width': args.width,
                   'arch': args.arch,
                   'cvar_alpha': args.cvar_alpha,
                   'anchor_share': args.anchor_share,
                   'replay_fraction': args.replay_fraction,
                   'final_loss': float(losses[-1]),
                   'final_ratio': diag[-1]['ratio'] if diag else None,
                   'wall_min': (time.time() - t0) / 60.0}, f, indent=2)
    print(f'Stage B complete: final L={losses[-1]:.3e}  ratio={diag[-1]["ratio"]:.2f}  '
          f'time={(time.time()-t0)/60:.1f} min', flush=True)


if __name__ == '__main__':
    main()
