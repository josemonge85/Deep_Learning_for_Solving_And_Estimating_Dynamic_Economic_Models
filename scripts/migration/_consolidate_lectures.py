#!/usr/bin/env python3
"""_consolidate_lectures.

Re-coarsen the destination repo from 30 lecture folders + 2 toolkits to
17 + 3, per the user-confirmed mapping (see plan.md / tranquil-napping-flame.md).

For each fragment lecture (carved out of a Geneva source deck during the
rejected per-page split), this script:
  1. Moves its notebooks/, code/, readings/ contents into the consolidated
     lecture's matching subfolder, renaming files so the `lecture_XX_BYY_`
     prefix matches the new lecture ID.
  2. Deletes the now-empty fragment folder via `git rm -r`.

For each kept lecture, the script `git mv`s the folder to its new name.

Three new things land:
  - toolkit/toolkit_03_T3_agentic_programming_exercises/  (new)
  - L17 already has 10_Wrap_Up.tex/.pdf  (no slide swap needed)
  - L09 (Heterogeneous Agents / Young's method) absorbs L16 fragment

Usage:
  python scripts/migration/_consolidate_lectures.py            # dry-run
  python scripts/migration/_consolidate_lectures.py --apply    # execute
"""
from __future__ import annotations
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LECTURES = ROOT / "lectures"
TOOLKIT = ROOT / "toolkit"
GENEVA = Path(
    "/home/simon/projects/lectures/Deep_Learning_Econ_Finance_Geneva_2026"
)

# (current_folder_name, new_folder_name, new_lecture_NN, new_block_BYY)
KEEP_RENAME: list[tuple[str, str, int, str]] = [
    ("lecture_01_B00_orientation_setup_reproducibility",
     "lecture_01_B00_orientation_setup_reproducibility", 1, "B00"),
    ("lecture_02_B01_why_deep_learning",
     "lecture_02_B01_intro_deep_learning", 2, "B01"),
    ("lecture_06_B05_deqn_central_idea",
     "lecture_03_B02_deep_equilibrium_nets", 3, "B02"),
    ("lecture_11_B10_irbc_with_deqns",
     "lecture_04_B03_irbc_with_deqns", 4, "B03"),
    ("lecture_12_B11_architecture_search_loss_balancing",
     "lecture_05_B04_nas_loss_normalization", 5, "B04"),
    ("lecture_10_B09_autodiff_for_deqns",
     "lecture_06_B05_autodiff_for_deqns", 6, "B05"),
    ("lecture_17_B16_sequence_space_deqns",
     "lecture_07_B06_sequence_space_deqns", 7, "B06"),
    ("lecture_13_B12_olg_models_deqns",
     "lecture_08_B07_olg_models_deqns", 8, "B07"),
    ("lecture_15_B14_krusell_smith_young_method",
     "lecture_09_B08_heterogeneous_agents_youngs_method", 9, "B08"),
    ("lecture_18_B17_pinn_foundations",
     "lecture_10_B09_pinns", 10, "B09"),
    ("lecture_20_B19_continuous_time_ha_theory",
     "lecture_11_B10_continuous_time_ha_theory", 11, "B10"),
    ("lecture_21_B20_continuous_time_ha_numerics",
     "lecture_12_B11_continuous_time_ha_numerics", 12, "B11"),
    ("lecture_22_B21_deep_surrogate_models",
     "lecture_13_B12_surrogates_and_gps", 13, "B12"),
    ("lecture_26_B25_structural_estimation_smm",
     "lecture_14_B13_structural_estimation_smm", 14, "B13"),
    ("lecture_27_B26_climate_economics_iams",
     "lecture_15_B14_climate_economics_iams", 15, "B14"),
    ("lecture_29_B28_deep_uq_policy",
     "lecture_16_B15_deep_uq_pareto_improving_policy", 16, "B15"),
    ("lecture_30_B29_synthesis_method_choice",
     "lecture_17_B16_course_wrap_up", 17, "B16"),
]

# (fragment_folder_name, target_consolidated_new_folder_name)
# The consolidated target is the *new* name (post-rename). The script must
# move fragment notebooks BEFORE the rename to avoid moving across renamed
# paths.
ABSORB: list[tuple[str, str]] = [
    # Day 1 fragments → L02 (Intro to Deep Learning)
    ("lecture_03_B02_training_neural_networks", "lecture_02_B01_why_deep_learning"),
    ("lecture_04_B03_generalization_sequence_models", "lecture_02_B01_why_deep_learning"),
    ("lecture_05_B04_function_approximation_loss_design", "lecture_02_B01_why_deep_learning"),
    # Day 2 fragments → L03 (DEQNs)
    ("lecture_07_B06_brock_mirman_deterministic_deqn", "lecture_06_B05_deqn_central_idea"),
    ("lecture_08_B07_brock_mirman_uncertainty_integration", "lecture_06_B05_deqn_central_idea"),
    ("lecture_09_B08_constraints_residual_kernels_loss_design", "lecture_06_B05_deqn_central_idea"),
    # Day 4 OLG fragment → L08
    ("lecture_14_B13_large_olg_benchmark", "lecture_13_B12_olg_models_deqns"),
    # Day 4 Young's fragment → L09
    ("lecture_16_B15_continuum_agents_deqn_method_comparison",
     "lecture_15_B14_krusell_smith_young_method"),
    # Day 6 PINN fragment → L10
    ("lecture_19_B18_pinn_economic_pdes", "lecture_18_B17_pinn_foundations"),
    # Day 7 Surrogates fragments → L13
    ("lecture_23_B22_gp_bayesian_active_learning", "lecture_22_B21_deep_surrogate_models"),
    ("lecture_24_B23_scaling_gps_active_subspaces_deep_kernels", "lecture_22_B21_deep_surrogate_models"),
    ("lecture_25_B24_gps_for_dynamic_programming", "lecture_22_B21_deep_surrogate_models"),
    # Day 8 fragment → L15
    ("lecture_28_B27_solving_dice_with_deqns", "lecture_27_B26_climate_economics_iams"),
]

# Lookup: fragment-folder current_name → (new_lecture_NN, new_block_BYY) of the
# absorbing target, derived from KEEP_RENAME.
def target_id(consolidated_current_name: str) -> tuple[int, str]:
    for cur, _new, nn, byy in KEEP_RENAME:
        if cur == consolidated_current_name:
            return nn, byy
    raise KeyError(consolidated_current_name)


def run(cmd: list[str], apply: bool) -> None:
    print("$", " ".join(cmd))
    if apply:
        subprocess.run(cmd, check=True, cwd=ROOT)


def relocate_files(fragment_dir: Path, target_dir: Path,
                   new_nn: int, new_byy: str, apply: bool) -> None:
    """Move all non-slide files from fragment_dir into target_dir's matching
    subfolders, renaming any file whose basename starts with
    ``lecture_NN_BYY_`` to use the consolidated lecture's new IDs."""
    # Subfolders to migrate; slides/ is excluded (whole deck lives only in
    # the consolidated folder; fragment slides will be deleted with the
    # folder).
    SUBDIRS = ["notebooks", "code", "readings", "figures", "notes"]
    for sub in SUBDIRS:
        src = fragment_dir / sub
        if not src.exists():
            continue
        for path in src.rglob("*"):
            if path.is_dir():
                continue
            rel = path.relative_to(src)
            new_basename = path.name
            # rewrite lecture_XX_BYY_ prefix in filename
            for old_nn in range(1, 31):
                for old_byy in (f"B{n:02d}" for n in range(0, 30)):
                    prefix = f"lecture_{old_nn:02d}_{old_byy}_"
                    if new_basename.startswith(prefix):
                        new_basename = (
                            f"lecture_{new_nn:02d}_{new_byy}_"
                            + new_basename[len(prefix):]
                        )
                        break
            target = target_dir / sub / rel.parent / new_basename
            target.parent.mkdir(parents=True, exist_ok=True) if apply else None
            run(["git", "mv", str(path.relative_to(ROOT)),
                 str(target.relative_to(ROOT))], apply)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true",
                    help="execute git mv / git rm; default is dry-run.")
    args = ap.parse_args()

    # Phase 1: relocate fragment contents into the still-old-named
    # consolidated folder. Renames happen in phase 2.
    for frag, target_old in ABSORB:
        fragment_dir = LECTURES / frag
        target_dir = LECTURES / target_old
        if not fragment_dir.exists():
            print(f"!! fragment missing, skipping: {frag}")
            continue
        new_nn, new_byy = target_id(target_old)
        print(f"\n# absorb {frag}  →  {target_old}  (new L{new_nn:02d} {new_byy})")
        relocate_files(fragment_dir, target_dir, new_nn, new_byy, args.apply)

    # Phase 2: delete now-bare fragment folders.
    print("\n# delete fragment folders")
    for frag, _ in ABSORB:
        if (LECTURES / frag).exists():
            run(["git", "rm", "-r", f"lectures/{frag}"], args.apply)

    # Phase 3: rename consolidated folders to their new names.
    print("\n# rename consolidated folders")
    for cur, new, _nn, _byy in KEEP_RENAME:
        if cur == new:
            continue
        run(["git", "mv", f"lectures/{cur}", f"lectures/{new}"], args.apply)

    # Phase 4: create T3 toolkit folder; copy the Geneva exercises deck.
    print("\n# create T3 toolkit folder")
    t3 = TOOLKIT / "toolkit_03_T3_agentic_programming_exercises"
    if not t3.exists():
        if args.apply:
            (t3 / "slides").mkdir(parents=True, exist_ok=True)
        for src_name in ("05_Agentic_Programming_Exercises.tex",
                         "05_Agentic_Programming_Exercises.pdf"):
            src = GENEVA / "lectures/day5/slides" / src_name
            dst = t3 / "slides" / src_name
            if src.exists():
                if args.apply:
                    shutil.copy2(src, dst)
                print(f"$ cp {src} {dst.relative_to(ROOT)}")
            else:
                print(f"!! source missing: {src}")
        # placeholder README so git tracks the folder
        readme = t3 / "README.md"
        if args.apply and not readme.exists():
            readme.write_text(
                "# Toolkit T3: Agentic programming - exercise handout\n\n"
                "Self-paced exercises that accompany toolkits T1 and T2. "
                "See the slide deck for the full set.\n"
            )
        print(f"$ write {readme.relative_to(ROOT)}")
        if args.apply:
            run(["git", "add", str(t3)], apply=True)

    if not args.apply:
        print("\n(dry-run; pass --apply to execute)")
    else:
        print("\nDone. Verify with `git status` then run validators.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
