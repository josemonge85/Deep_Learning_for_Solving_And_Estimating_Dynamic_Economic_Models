#!/usr/bin/env bash
# Reference recipe for the 2-parameter (rho, pi2) DICE-DEQN surrogate pipeline.
#
# IMPORTANT: this script documents how the committed _pt_solutions/2p/ cache was
# produced. That cache (the *_det.npz point solutions, gp_anchors_25.json, and
# the GP / Sobol / univariate figures) is checked into the repository, so the
# classroom notebook lecture_17_09_DICE_2P_UQ_Analysis.ipynb runs with no GPU and
# without re-running anything here. Stages A and B require a GPU and several
# wall-clock hours; CI does not run them.
#
# Stages:
#   A: 5 fixed-theta point solutions (the (rho, pi2) corners).  ~25 min at the
#      classroom budget. The 20 additional anchor solutions referenced by
#      gp_anchors_25.json (pt_ref_*, pt_smk_*, ho_*, ho2_*) were produced by
#      further `train_dice_2p_pointsolutions.py` runs with explicit
#      `--theta`/`--out-tag`; collect their (tag, rho, pi2) entries into the
#      theta-batch manifest JSON read by Stage D (THETA_BATCH below).
#   B: (rho, pi2)-parameterised surrogate (~2-3 h at production budget). Used as
#      *design guidance* only -- nothing downstream (Stage D or the notebook)
#      reads its weights; it is wired in here for completeness.
#   D: GP per target year + Sobol indices + univariate effects, anchored on the
#      EXACT point-solution SCCs. Needs the THETA_BATCH manifest above.
#
# Idempotent: each stage skips if its sentinel exists in _pt_solutions/2p/.
# Override budgets via env vars: PT_EPISODES, SG_EPISODES, SG_WIDTH, THETA_BATCH, etc.

set -euo pipefail

# Resolve ROOT relative to this script's location so the pipeline runs from
# whichever checkout of the repository it lives in.
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"
mkdir -p _pt_solutions/2p/figures

PT_EPISODES="${PT_EPISODES:-200}"
PT_WIDTH="${PT_WIDTH:-512}"
SG_EPISODES="${SG_EPISODES:-600}"
SG_WIDTH="${SG_WIDTH:-768}"
SG_ANCHOR_SHARE="${SG_ANCHOR_SHARE:-0.0}"
SG_ARCH="${SG_ARCH:-film}"
SG_CVAR_ALPHA="${SG_CVAR_ALPHA:-0.2}"
SG_REPLAY_FRACTION="${SG_REPLAY_FRACTION:-0.25}"
# Manifest of {tag, rho, pi2} entries covering every anchor whose <tag>_det.npz
# lives in _pt_solutions/2p/ (the 5 Stage-A corners plus the 20 additional
# anchors -- see the header). Stage D reads this; it is not produced automatically.
THETA_BATCH="${THETA_BATCH:-_pt_solutions/2p/theta_batch.json}"

echo "== Stage A: 5 fixed-theta point solutions =="
python3 -u train_dice_2p_pointsolutions.py \
  --episodes "$PT_EPISODES" --width "$PT_WIDTH" \
  2>&1 | tee -a _pt_solutions/2p/stage_A.log

echo "== Stage B: surrogate over (rho, pi2)  (design guidance only) =="
python3 -u train_dice_2p_surrogate.py \
  --episodes "$SG_EPISODES" --width "$SG_WIDTH" \
  --arch "$SG_ARCH" \
  --cvar-alpha "$SG_CVAR_ALPHA" \
  --anchor-share "$SG_ANCHOR_SHARE" \
  --replay-fraction "$SG_REPLAY_FRACTION" \
  --replay-pt-width "$PT_WIDTH" \
  2>&1 | tee -a _pt_solutions/2p/stage_B.log

echo "== Stage D: GP + Sobol + univariate effects =="
# Anchored on the EXACT point-solution SCCs in _pt_solutions/2p/ via the
# THETA_BATCH manifest. Writes gp_anchors_25.json and the GP/Sobol/univariate
# figures consumed by lecture_17_09_DICE_2P_UQ_Analysis.ipynb.
python3 -u compute_dice_2p_gp_anchors.py \
  --anchor-jsons "$THETA_BATCH" \
  --out-prefix gp_anchors_25 \
  2>&1 | tee -a _pt_solutions/2p/stage_D.log

echo "== Pipeline complete =="
