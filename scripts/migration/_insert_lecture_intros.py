#!/usr/bin/env python3
"""Insert an "About this lecture" frame into each split deck.

The 20 decks I produced from the 7 source decks shipped without any
intro slide explaining what the lecture covers, what it builds on, and
where it leads. This script writes that frame in, just after the title
page, using per-deck content drawn from course.yml and my reading of
each deck.
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# (deck_path_relative, covers, builds_on, leads_to)
INTROS: dict[str, dict[str, list[str]]] = {
    # --- Day 1 splits ---
    "lectures/lecture_02_B01_why_deep_learning/slides/01_Intro_to_DeepLearning.tex": {
        "covers": [
            "Why deep learning matters for economics and finance, with concrete applications",
            "The supervised, unsupervised, and reinforcement-learning paradigms",
            "The end-to-end machine-learning pipeline (data, model, loss, optimization, validation)",
        ],
        "builds_on": ["Basic linear algebra, calculus, probability"],
        "leads_to": ["Lecture 03 (training neural networks): SGD, backpropagation, optimizer choice"],
    },
    "lectures/lecture_03_B02_training_neural_networks/slides/02_Training_Neural_Networks.tex": {
        "covers": [
            "From the perceptron to multilayer feedforward networks; activation functions",
            "Gradient descent, stochastic gradient descent, mini-batches",
            "Backpropagation, modern optimizers (Adam / AdamW), weight initialization, batch normalization",
        ],
        "builds_on": ["Lecture 02 (motivation, the ML pipeline)"],
        "leads_to": [
            "Lecture 04 (generalization, regularization, sequence models)",
            "Lecture 05 (function approximation and loss design)",
        ],
    },
    "lectures/lecture_04_B03_generalization_sequence_models/slides/03_Generalization_Sequence_Models.tex": {
        "covers": [
            "Overfitting vs underfitting, train / validation / test splits",
            "Regularization: $L_2$ penalty, dropout, early stopping; the deep-double-descent surprise",
            "Sequence models: RNNs, LSTMs, attention, the transformer block",
        ],
        "builds_on": ["Lecture 03 (training neural networks)"],
        "leads_to": ["Lecture 05 (loss design)", "Lecture 06+ (DEQNs as a specific architecture)"],
    },
    "lectures/lecture_05_B04_function_approximation_loss_design/slides/04_Function_Approximation_Loss_Design.tex": {
        "covers": [
            "Universal approximation: what neural networks can and cannot represent",
            "Loss-function design beyond MSE: robust losses, asymmetric losses, choosing a loss",
            "Function approximation in moderate-to-high dimensions and the curse of dimensionality",
        ],
        "builds_on": ["Lecture 03 (training mechanics)", "Lecture 04 (regularization)"],
        "leads_to": ["Lecture 06 (Deep Equilibrium Nets, where the loss IS the equilibrium residual)"],
    },
    # --- Day 2 splits (DEQN block) ---
    "lectures/lecture_06_B05_deqn_central_idea/slides/02_DeepEquilibriumNets.tex": {
        "covers": [
            "Why DSGE models are computationally hard: heterogeneity and high-dimensional state spaces",
            "The ergodic set is not a hypercube; volumes scale badly in high dimensions",
            "The Deep Equilibrium Net (DEQN) approach in abstract: what is being learned, and against what target",
        ],
        "builds_on": ["Lectures 02-05 (deep learning foundations)"],
        "leads_to": [
            "Lecture 07 (Brock-Mirman deterministic case, end-to-end)",
            "Lecture 08 (uncertainty and integration)",
            "Lecture 09 (constraints and loss-kernel design)",
        ],
    },
    "lectures/lecture_07_B06_brock_mirman_deterministic_deqn/slides/02_BrockMirman_Deterministic_DEQN.tex": {
        "covers": [
            "Neural-network architecture for DEQNs: layer structure, activations, supervised vs unsupervised framing",
            "The Brock-Mirman deterministic growth model: setup, Euler equation, closed-form policy",
            "End-to-end DEQN training pass on a model whose true solution is known analytically",
        ],
        "builds_on": ["Lecture 06 (DEQN central idea)", "Lectures 03-05 (training mechanics, loss design)"],
        "leads_to": [
            "Lecture 08 (adding stochastic shocks; Gauss-Hermite quadrature)",
            "Lecture 09 (constraints and loss kernels)",
        ],
    },
    "lectures/lecture_08_B07_brock_mirman_uncertainty_integration/slides/02_BrockMirman_Uncertainty_Integration.tex": {
        "covers": [
            "Stochastic Brock-Mirman: residual, expectation, loss",
            "Numerical integration: Gauss-Hermite, monomial (Stroud-3) rules, cost trade-offs",
            "Training diagnostics: what does \"converged\" actually look like?",
        ],
        "builds_on": ["Lecture 07 (deterministic DEQN end-to-end)"],
        "leads_to": ["Lecture 09 (constraints, residual kernels, loss design)"],
    },
    "lectures/lecture_09_B08_constraints_residual_kernels_loss_design/slides/02_Constraints_Residual_Kernels.tex": {
        "covers": [
            "Hard vs soft constraints in equilibrium models (KKT, Fischer-Burmeister)",
            "Six families of loss kernels; how the kernel choice changes convergence behavior",
            "Data parallelism and multi-GPU scaling for DEQN training",
        ],
        "builds_on": ["Lecture 07 (deterministic Brock-Mirman)", "Lecture 08 (residual + integration)"],
        "leads_to": ["Lecture 10+ (autodiff for DEQNs, IRBC, OLG, larger models)"],
    },
    # --- Day 4 splits (OLG) ---
    "lectures/lecture_13_B12_olg_models_deqns/slides/07_OLG_Models_DEQNs.tex": {
        "covers": [
            "Why overlapping-generations models matter; the cohort structure",
            "Krueger-Kuebler 2004 analytic 6-cohort OLG model end-to-end",
            "DEQN architecture, sampling, training results vs the analytic benchmark",
        ],
        "builds_on": ["Lectures 06-09 (DEQN block)", "Lecture 11 (IRBC) for multi-shock training patterns"],
        "leads_to": ["Lecture 14 (large 56-cohort OLG benchmark)"],
    },
    "lectures/lecture_14_B13_large_olg_benchmark/slides/07_OLG_Large_Benchmark.tex": {
        "covers": [
            "AGS 2022 benchmark: 56 cohorts, bond market, lifecycle capital",
            "DEQN architecture and equilibrium conditions for the larger model",
            "Training, consumption profiles by aggregate state, reading the diagnostics",
        ],
        "builds_on": ["Lecture 13 (analytic 6-cohort OLG)"],
        "leads_to": ["Lecture 15 (heterogeneous agents and Young's method)"],
    },
    # --- Day 4 splits (KS / heterogeneous agents) ---
    "lectures/lecture_15_B14_krusell_smith_young_method/slides/08_KrusellSmith_Young.tex": {
        "covers": [
            "From representative to heterogeneous agents; the infinite-dimensional state-space problem",
            "The Krusell-Smith insight: approximate aggregation",
            "Young's (2010) non-stochastic distribution update; the traditional Krusell-Smith outer loop",
        ],
        "builds_on": ["Lecture 14 (large OLG)", "Lecture 06 (DEQN central idea)"],
        "leads_to": ["Lecture 16 (continuum-agent DEQNs and the method-comparison landscape)"],
    },
    "lectures/lecture_16_B15_continuum_agents_deqn_method_comparison/slides/08_KrusellSmith_DEQN.tex": {
        "covers": [
            "Embedding Young's method inside a DEQN training loop",
            "Three deep-learning recipes for KS: all-in-one, DeepHAM, histogram-DEQN",
            "Head-to-head: when to use which architecture",
        ],
        "builds_on": ["Lecture 15 (Young's method, traditional KS)"],
        "leads_to": ["Lecture 17 (sequence-space DEQNs)", "Lecture 20+ (continuous-time HA)"],
    },
    # --- Day 6 splits (PINNs) ---
    "lectures/lecture_18_B17_pinn_foundations/slides/06_PINN_Foundations.tex": {
        "covers": [
            "Discrete-time DEQN vs continuous-time PINN: what changes in the loss",
            "Automatic differentiation for PDEs; collocation points",
            "PINN training pipeline (Adam $\\to$ L-BFGS in fp64), network architecture, why tanh",
        ],
        "builds_on": ["Lecture 06 (DEQN loss as residual)"],
        "leads_to": ["Lecture 19 (boundary conditions and economic PDEs: HJB, Black-Scholes)"],
    },
    "lectures/lecture_19_B18_pinn_economic_pdes/slides/06_PINN_Economic_PDEs.tex": {
        "covers": [
            "Soft vs hard boundary-condition enforcement; trial-solution decomposition",
            "PINN for the HJB equation (cake-eating); the DGM architecture for high-D PDEs",
            "PINN for the Black-Scholes PDE",
        ],
        "builds_on": ["Lecture 18 (PINN foundations)"],
        "leads_to": ["Lecture 20+ (continuous-time heterogeneous agents)"],
    },
    # --- Day 7 splits (Surrogates and GPs) ---
    "lectures/lecture_22_B21_deep_surrogate_models/slides/07_Deep_Surrogate_Models.tex": {
        "covers": [
            "Why surrogates: replacing expensive simulators with cheap, differentiable models",
            "Pseudo-states: the trick that lets one network serve many use cases",
            "Application sketches: structural estimation, UQ, optimal policy, the implied vol surface",
        ],
        "builds_on": ["Lectures 02-05 (NN basics)", "Lecture 12 (architecture / loss balancing)"],
        "leads_to": [
            "Lecture 23 (Gaussian processes as the Bayesian alternative)",
            "Lecture 26 (using a surrogate for SMM-based structural estimation)",
        ],
    },
    "lectures/lecture_23_B22_gp_bayesian_active_learning/slides/07_GP_Regression.tex": {
        "covers": [
            "Gaussian processes as a distribution over functions; squared-exponential and Mat\\'ern kernels",
            "Posterior predictions and confidence intervals; learning kernel hyperparameters",
            "Deep kernel learning: combining a neural feature extractor with a GP layer",
        ],
        "builds_on": ["Lecture 22 (deep surrogates)"],
        "leads_to": [
            "Lecture 24 (Bayesian active learning for sample design)",
            "Lecture 25 (GPs as value-function surrogates inside DP)",
        ],
    },
    "lectures/lecture_24_B23_scaling_gps_active_subspaces_deep_kernels/slides/07_Bayesian_Active_Learning.tex": {
        "covers": [
            "Where to sample? Bayesian active learning as a principled answer",
            "The BAL algorithm; progressive refinement of a GP surrogate",
            "BAL applied in economics; combining BAL with GPs for high-quality surrogates",
        ],
        "builds_on": ["Lecture 23 (GP regression)"],
        "leads_to": ["Lecture 25 (GPs for dynamic programming)"],
    },
    "lectures/lecture_25_B24_gps_for_dynamic_programming/slides/07_GPs_For_DP.tex": {
        "covers": [
            "Adaptive sparse GP value-function iteration (ASGP-VFI)",
            "Active subspaces (linear and deep) for high-dimensional state spaces",
            "Embarrassingly parallel VFI; head-to-head with DEQNs",
        ],
        "builds_on": ["Lecture 23 (GP regression)", "Lecture 24 (BAL)"],
        "leads_to": ["Lecture 26 (SMM with GP surrogates)", "Lectures 27-28 (climate IAMs)"],
    },
    # --- Day 8 splits (Climate) ---
    "lectures/lecture_27_B26_climate_economics_iams/slides/08_Climate_Economics_IAMs.tex": {
        "covers": [
            "Why integrated assessment models; the social cost of carbon",
            "DICE / CDICE: the carbon cycle, temperature dynamics, damage functions",
            "Equilibrium climate sensitivity as the dominant deep uncertainty",
        ],
        "builds_on": ["Lectures 06-09 (DEQN block)"],
        "leads_to": [
            "Lecture 28 (solving stochastic DICE with DEQNs and deep UQ)",
            "Lecture 29 (deep UQ + optimal policy)",
        ],
    },
    "lectures/lecture_28_B27_solving_dice_with_deqns/slides/08_DICE_With_DEQNs.tex": {
        "covers": [
            "Stochastic IAM with Epstein-Zin preferences; full constraint set and derivation",
            "Notebook 04 walk-through: 9-residual EZ loss, $\\gamma$-curriculum, stop-gradient trick",
            "Global UQ via Bayesian active learning with GP surrogates; SCC distributions",
        ],
        "builds_on": ["Lecture 27 (climate IAMs and DICE / CDICE)", "Lectures 22-25 (surrogates and GPs)"],
        "leads_to": ["Lecture 29 (deep UQ for optimal policy design)"],
    },
}


def make_intro_frame(title: str, c: dict[str, list[str]]) -> str:
    def block(label: str, items: list[str]) -> str:
        body = "\n".join(f"  \\item {x}" for x in items)
        return (
            "\\begin{block}{" + label + "}\n"
            "\\begin{itemize}\\itemsep2pt\n"
            f"{body}\n"
            "\\end{itemize}\n"
            "\\end{block}\n"
        )
    return (
        "% --- About-this-lecture orientation ---\n"
        "\\begin{frame}{About this lecture}\n"
        "\\small\n"
        + block("What this lecture covers", c["covers"])
        + block("Builds on", c["builds_on"])
        + block("Leads to", c["leads_to"])
        + "\\end{frame}\n\n"
    )


# Insertion point: after the closing `}` of the title-page wrapper,
# matched as `\titlepage\n\end{frame}\n}\n` (the format my splitter wrote).
INSERT_RE = re.compile(
    r"(\\titlepage\n\\end\{frame\}\n\}\n\n?)",
)


def main() -> int:
    n_inserted = 0
    n_already = 0
    n_unmatched = 0
    for rel, content in INTROS.items():
        path = ROOT / rel
        if not path.exists():
            print(f"MISSING {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        if "About this lecture" in text:
            n_already += 1
            print(f"SKIP (already has intro)  {rel}")
            continue
        new_frame = make_intro_frame("About this lecture", content)
        new_text, n = INSERT_RE.subn(lambda m: m.group(1) + new_frame, text, count=1)
        if n == 0:
            n_unmatched += 1
            print(f"NO INSERTION POINT  {rel}")
            continue
        path.write_text(new_text, encoding="utf-8")
        n_inserted += 1
        print(f"OK   {rel}")
    print(f"\ninserted {n_inserted}, skipped {n_already}, no-insertion-point {n_unmatched}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
