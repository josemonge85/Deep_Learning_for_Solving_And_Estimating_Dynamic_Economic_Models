#!/usr/bin/env python3
"""Update each consolidated slide deck's ``\\title[...]{...}`` and
``\\subtitle{...}`` lines to the new (post-consolidation) lecture number,
block, and title."""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# (slide_relative_path, new_NN, new_BYY, new_title, new_subtitle_or_None)
DECKS: list[tuple[str, int, str, str, str | None]] = [
    ("lectures/lecture_02_B01_intro_deep_learning/slides/01_Intro_to_DeepLearning.tex",
     2, "B01", "Introduction to deep learning",
     "From basic ML through DNNs to sequence models for economic time series"),
    ("lectures/lecture_03_B02_deep_equilibrium_nets/slides/02_DeepEquilibriumNets.tex",
     3, "B02", "Deep Equilibrium Nets",
     "From representative-agent Brock--Mirman through stochastic models, KKT constraints, and loss kernels"),
    ("lectures/lecture_04_B03_irbc_with_deqns/slides/03_IRBC.tex",
     4, "B03", "IRBC with DEQNs",
     "Solving nonlinear dynamic stochastic models in 4 to 100+ dimensions"),
    ("lectures/lecture_05_B04_nas_loss_normalization/slides/04_Neural_Architecture_Search.tex",
     5, "B04", "Neural architecture search",
     "Random search and Hyperband for DEQN architectures"),
    ("lectures/lecture_05_B04_nas_loss_normalization/slides/05_Loss_Normalization.tex",
     5, "B04", "Loss normalization and balancing",
     "ReLoBRaLo and gradient-conflict mitigation in multi-equation residual losses"),
    ("lectures/lecture_06_B05_autodiff_for_deqns/slides/05b_AutoDiff_for_DEQN.tex",
     6, "B05", "Automatic differentiation for DEQNs",
     "From the Lagrangian primitive to two-tape Euler residuals"),
    ("lectures/lecture_07_B06_sequence_space_deqns/slides/06_SequenceSpace_DEQNs.tex",
     7, "B06", "Sequence-space DEQNs",
     "Azinovic--Yang--Zemlicka: shock-history inputs for high-dimensional models"),
    ("lectures/lecture_08_B07_olg_models_deqns/slides/07_OLG_Models_DEQNs.tex",
     8, "B07", "OLG models with DEQNs",
     "Overlapping generations, borrowing constraints, Fischer--Burmeister complementarity"),
    ("lectures/lecture_09_B08_heterogeneous_agents_youngs_method/slides/08_Heterogeneous_Agents_Youngs_Method.tex",
     9, "B08", "Heterogeneous agents and Young's method",
     "Histogram non-stochastic distribution updates, Krusell--Smith, continuum-of-agents DEQN"),
    ("lectures/lecture_10_B09_pinns/slides/06_PINNs.tex",
     10, "B09", "Physics-informed neural networks",
     "Foundations, boundary conditions, applications to ODEs and economic PDEs"),
    ("lectures/lecture_11_B10_continuous_time_ha_theory/slides/07_CT_Heterogeneous_Agents_Theory.tex",
     11, "B10", "Continuous-time heterogeneous agents, theory",
     "HJB, Kolmogorov forward, Aiyagari in continuous time"),
    ("lectures/lecture_12_B11_continuous_time_ha_numerics/slides/08_CT_Heterogeneous_Agents_Numerical.tex",
     12, "B11", "Continuous-time heterogeneous agents, numerics",
     "Finite-difference and PINN solvers for the HJB+KFE system"),
    ("lectures/lecture_13_B12_surrogates_and_gps/slides/07_Surrogates_and_GPs.tex",
     13, "B12", "Surrogates and Gaussian processes",
     "Deep surrogates, GPs, Bayesian active learning, deep kernels, GP-VFI, active subspaces"),
    ("lectures/lecture_14_B13_structural_estimation_smm/slides/08_Exercise_Structural_Estimation.tex",
     14, "B13", "Structural estimation via SMM",
     "Surrogate-based simulated method of moments in the Brock--Mirman model"),
    ("lectures/lecture_15_B14_climate_economics_iams/slides/08_Climate_Economics_IAMs.tex",
     15, "B14", "Climate economics and integrated assessment models",
     "DICE, CDICE, the carbon cycle, temperature dynamics, deterministic baseline"),
    ("lectures/lecture_16_B15_deep_uq_pareto_improving_policy/slides/09_Deep_UQ_and_Optimal_Policies.tex",
     16, "B15", "Deep uncertainty quantification and Pareto-improving climate policy",
     "Stochastic IAMs with DEQNs, GP surrogates, Sobol/Shapley, constrained Pareto-improving carbon-tax design"),
    ("lectures/lecture_17_B16_course_wrap_up/slides/10_Wrap_Up.tex",
     17, "B16", "Course wrap-up", "Key takeaways, method choice, and outlook"),
]

TOOLKIT_DECKS: list[tuple[str, str, str, str | None]] = [
    ("toolkit/toolkit_03_T3_agentic_programming_exercises/slides/05_Agentic_Programming_Exercises.tex",
     "T3", "Agentic programming, exercise handout",
     "Workshop and self-study exercises for the agentic-programming toolkit"),
]

TITLE_RE = re.compile(r"\\title\[[^\]]*\]\{[^}]*\}")
SUBTITLE_RE = re.compile(r"\\subtitle\{[^}]*\}")


def patch(path: Path, label: str, new_title: str, new_subtitle: str | None) -> bool:
    if not path.exists():
        print(f"missing: {path}")
        return False
    txt = path.read_text(encoding="utf-8")
    new = TITLE_RE.sub(
        f"\\\\title[{label}]{{{label}: {new_title}}}",
        txt, count=1)
    if new_subtitle is not None:
        new = SUBTITLE_RE.sub(
            f"\\\\subtitle{{{new_subtitle}}}", new, count=1)
    if new == txt:
        print(f"unchanged: {path}")
        return False
    path.write_text(new, encoding="utf-8")
    print(f"patched: {path}")
    return True


def main() -> int:
    for rel, nn, byy, title, subtitle in DECKS:
        label = f"Lecture {nn:02d} ({byy})"
        patch(ROOT / rel, label, title, subtitle)
    for rel, tcode, title, subtitle in TOOLKIT_DECKS:
        label = f"Toolkit {tcode}"
        patch(ROOT / rel, label, title, subtitle)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
