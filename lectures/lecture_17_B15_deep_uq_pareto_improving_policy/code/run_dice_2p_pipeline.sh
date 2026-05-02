#!/usr/bin/env bash
# Driver for the four-stage 2-parameter (rho, pi2) DICE-DEQN surrogate pipeline.
#
# Stages:
#   A: 5 fixed-theta point solutions   (~25 min total at classroom budget)
#   B: 9-D parameterised surrogate     (~2-3 h at production budget)
#   C: validation against the 5 corners
#   D: GP + Sobol + univariate effects
#
# Idempotent: each stage skips if its sentinel exists in _pt_solutions/2p/.
# Override budgets via env vars: PT_EPISODES, SG_EPISODES, SG_WIDTH, etc.

set -euo pipefail

ROOT="/home/simon/projects/lectures/Deep_Learning_Econ_Finance_Geneva_2026/lectures/day8/code"
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
GP_DESIGN="${GP_DESIGN:-256}"

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

echo "== Stage C: validate surrogate vs point solutions =="
python3 -u validate_dice_2p_surrogate.py --width "$SG_WIDTH" --arch "$SG_ARCH" --soft \
  2>&1 | tee -a _pt_solutions/2p/stage_C.log

echo "== Stage D: GP + Sobol + univariate effects =="
python3 -u compute_dice_2p_gp_sobol.py \
  --width "$SG_WIDTH" --arch "$SG_ARCH" --n-design "$GP_DESIGN" \
  2>&1 | tee -a _pt_solutions/2p/stage_D.log

echo "== Pipeline complete =="
