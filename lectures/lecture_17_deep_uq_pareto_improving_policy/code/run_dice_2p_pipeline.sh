#!/usr/bin/env bash
# Driver for the three-stage 2-parameter (rho, pi2) DICE-DEQN surrogate pipeline.
#
# Stages:
#   A: 5 fixed-theta point solutions   (~25 min total at classroom budget)
#   B: 9-D parameterised surrogate     (~2-3 h at production budget)
#   D: GP + Sobol + univariate effects (anchored on Stage-A SCCs)
#
# Idempotent: each stage skips if its sentinel exists in _pt_solutions/2p/.
# Override budgets via env vars: PT_EPISODES, SG_EPISODES, SG_WIDTH, etc.

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

echo "== Stage A: 5 fixed-theta point solutions =="
python3 -u train_dice_2p_pointsolutions.py \
  --episodes "$PT_EPISODES" --width "$PT_WIDTH" \
  2>&1 | tee -a _pt_solutions/2p/stage_A.log

echo "== Stage B: surrogate over (rho, pi2) =="
python3 -u train_dice_2p_surrogate.py \
  --episodes "$SG_EPISODES" --width "$SG_WIDTH" \
  --arch "$SG_ARCH" \
  --cvar-alpha "$SG_CVAR_ALPHA" \
  --anchor-share "$SG_ANCHOR_SHARE" \
  --replay-fraction "$SG_REPLAY_FRACTION" \
  --replay-pt-width "$PT_WIDTH" \
  2>&1 | tee -a _pt_solutions/2p/stage_B.log

echo "== Stage D: GP + Sobol + univariate effects =="
# Anchored on the Stage-A point-solution SCCs cached in _pt_solutions/2p/
# (see _pt_solutions/2p/gp_anchors_25.json for the 25-point reference cube).
python3 -u compute_dice_2p_gp_anchors.py \
  2>&1 | tee -a _pt_solutions/2p/stage_D.log

echo "== Pipeline complete =="
