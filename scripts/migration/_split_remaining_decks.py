#!/usr/bin/env python3
"""Split the remaining multi-lecture source decks into per-lecture decks.

Each entry below names a source .tex, the line at which to chop the preamble
(everything before \\title{...}), and the destination decks with their
content frame ranges (1-indexed, inclusive line numbers in the source file).
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def render_title(lec_id: str, block_id: str, title: str, subtitle: str) -> str:
    return (
        f"\\title[Lecture {lec_id} ({block_id})]{{Lecture {lec_id} ({block_id}): {title}}}\n"
        f"\\subtitle{{{subtitle}}}\n"
        "\\author{Simon Scheidegger}\n"
        "\\institute{HEC, University of Lausanne}\n"
        "\\date{}\n"
    )


TITLE_FRAME = (
    "\\begin{document}\n\n"
    "% Custom command used in some \"Finger Exercise\" frame titles.\n"
    "\\providecommand{\\exercisepause}{%\n"
    "  \\tikz[baseline=(X.base)]{\\node[fill=darkgreen!80!black, text=white,\n"
    "  rounded corners=2pt, inner sep=3pt, font=\\scriptsize\\bfseries](X){PAUSE};}}\n\n"
    "{\\setbeamercolor{background canvas}{bg=uzhgreylight}\n"
    "\\begin{frame}\n\\titlepage\n\\end{frame}\n}\n\n"
)


def split_one(source_rel: str, preamble_chop: int, splits: list):
    """Split one source deck into multiple destination decks.

    splits = [(dest_rel, lec_id, block_id, title, subtitle, ranges), ...]
    """
    src = ROOT / source_rel
    lines = src.read_text(encoding="utf-8").splitlines(keepends=True)
    preamble = "".join(lines[:preamble_chop])

    for dest_rel, lec_id, block_id, title, subtitle, ranges in splits:
        body = "".join("".join(lines[s - 1 : e]) for (s, e) in ranges)
        txt = (
            preamble
            + render_title(lec_id, block_id, title, subtitle)
            + TITLE_FRAME
            + body
            + "\n\\end{document}\n"
        )
        out_path = ROOT / dest_rel
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(txt, encoding="utf-8")
        print(f"wrote {dest_rel} ({len(txt.splitlines())} lines)")


def main():
    # Day 2: DEQN deck → L06 / L07 / L08 / L09
    split_one(
        "lectures/lecture_06_B05_deqn_central_idea/slides/02_DeepEquilibriumNets.tex",
        78,
        [
            (
                "lectures/lecture_06_B05_deqn_central_idea/slides/02_DeepEquilibriumNets.tex",
                "06", "B05",
                "Deep Equilibrium Nets --- The Central Idea",
                "Heterogeneity, high-dimensional state spaces, the DEQN solution",
                [(105, 477)],
            ),
            (
                "lectures/lecture_07_B06_brock_mirman_deterministic_deqn/slides/02_BrockMirman_Deterministic_DEQN.tex",
                "07", "B06",
                "Brock--Mirman with DEQNs --- Deterministic Case",
                "Neural network architecture, supervised vs unsupervised, deterministic Brock--Mirman",
                [(480, 1020)],
            ),
            (
                "lectures/lecture_08_B07_brock_mirman_uncertainty_integration/slides/02_BrockMirman_Uncertainty_Integration.tex",
                "08", "B07",
                "Brock--Mirman --- Uncertainty and Numerical Integration",
                "Residuals, expectations, Gauss--Hermite and monomial quadrature, training diagnostics",
                [(1070, 1315)],
            ),
            (
                "lectures/lecture_09_B08_constraints_residual_kernels_loss_design/slides/02_Constraints_Residual_Kernels.tex",
                "09", "B08",
                "Constraints, Residual Kernels, Loss Design",
                "Hard vs soft constraints, six loss kernels, data parallelism for DEQNs",
                [(1023, 1067), (1318, 1370), (1402, 1508), (1531, 1552), (1555, 1577)],
            ),
        ],
    )

    # Day 4: OLG deck → L13 / L14
    split_one(
        "lectures/lecture_13_B12_olg_models_deqns/slides/07_OLG_Models_DEQNs.tex",
        71,
        [
            (
                "lectures/lecture_13_B12_olg_models_deqns/slides/07_OLG_Models_DEQNs.tex",
                "13", "B12",
                "OLG Models with DEQNs --- Analytic 6-Cohort Case",
                "Why OLG, Krueger--Kuebler 2004, DEQN architecture and training",
                [(94, 706)],
            ),
            (
                "lectures/lecture_14_B13_large_olg_benchmark/slides/07_OLG_Large_Benchmark.tex",
                "14", "B13",
                "Large OLG Benchmark --- 56 Cohorts (AGS 2022)",
                "Bond market, lifecycle capital, training diagnostics",
                [(711, 1149)],
            ),
        ],
    )

    # Day 4: Krusell-Smith deck → L15 / L16
    split_one(
        "lectures/lecture_15_B14_krusell_smith_young_method/slides/08_Heterogeneous_Agents_Youngs_Method.tex",
        96,
        [
            (
                "lectures/lecture_15_B14_krusell_smith_young_method/slides/08_KrusellSmith_Young.tex",
                "15", "B14",
                "Krusell--Smith and Young's Method",
                "Heterogeneous agents, the KS insight, non-stochastic distribution updates",
                [(145, 1473)],
            ),
            (
                "lectures/lecture_16_B15_continuum_agents_deqn_method_comparison/slides/08_KrusellSmith_DEQN.tex",
                "16", "B15",
                "Continuum-Agent DEQNs --- Method Comparison",
                "DEQN with histogram encoding, DeepHAM, all-in-one DL, head-to-head",
                [(1485, 2329)],
            ),
        ],
    )

    # Day 6: PINN deck → L18 / L19
    split_one(
        "lectures/lecture_18_B17_pinn_foundations/slides/06_PINNs.tex",
        97,
        [
            (
                "lectures/lecture_18_B17_pinn_foundations/slides/06_PINN_Foundations.tex",
                "18", "B17",
                "Physics-Informed Neural Networks --- Foundations",
                "DEQN vs PINN, automatic differentiation for PDEs, training pipeline, architecture",
                [(132, 721)],
            ),
            (
                "lectures/lecture_19_B18_pinn_economic_pdes/slides/06_PINN_Economic_PDEs.tex",
                "19", "B18",
                "PINNs for Economic PDEs --- Boundary Conditions, HJB, Black--Scholes",
                "Soft vs hard BCs, HJB cake-eating, DGM architecture, Black--Scholes pricing",
                [(738, 1648)],
            ),
        ],
    )

    # Day 7: Surrogates and GPs deck → L22 / L23 / L24 / L25
    split_one(
        "lectures/lecture_22_B21_deep_surrogate_models/slides/07_Surrogates_and_GPs.tex",
        96,
        [
            (
                "lectures/lecture_22_B21_deep_surrogate_models/slides/07_Deep_Surrogate_Models.tex",
                "22", "B21",
                "Deep Surrogate Models",
                "Pseudo-states, structural estimation, UQ, optimal policy, implied vol surfaces",
                [(127, 627)],
            ),
            (
                "lectures/lecture_23_B22_gp_bayesian_active_learning/slides/07_GP_Regression.tex",
                "23", "B22",
                "Gaussian Process Regression",
                "Kernels, posterior, hyperparameter learning, deep kernel learning",
                [(628, 1536)],
            ),
            (
                "lectures/lecture_24_B23_scaling_gps_active_subspaces_deep_kernels/slides/07_Bayesian_Active_Learning.tex",
                "24", "B23",
                "Bayesian Active Learning",
                "Where to sample, BAL algorithm, BAL in economics, BAL + GPs for surrogates",
                [(1537, 1713)],
            ),
            (
                "lectures/lecture_25_B24_gps_for_dynamic_programming/slides/07_GPs_For_DP.tex",
                "25", "B24",
                "Gaussian Processes for Dynamic Programming",
                "ASGP value-function iteration, active subspaces, parallelization, GPs vs DEQNs",
                [(1714, 2454)],
            ),
        ],
    )

    # Day 8: Climate deck → L27 / L28
    split_one(
        "lectures/lecture_27_B26_climate_economics_iams/slides/08_Climate_Economics_IAMs.tex",
        74,
        [
            (
                "lectures/lecture_27_B26_climate_economics_iams/slides/08_Climate_Economics_IAMs.tex",
                "27", "B26",
                "Climate Economics and Integrated Assessment Models",
                "Why IAMs, social cost of carbon, DICE / CDICE baseline",
                [(106, 487)],
            ),
            (
                "lectures/lecture_28_B27_solving_dice_with_deqns/slides/08_DICE_With_DEQNs.tex",
                "28", "B27",
                "Solving DICE with DEQNs and Deep Uncertainty Quantification",
                "Stochastic IAM, Epstein--Zin loss, BAL + GP surrogates, SCC distributions",
                [(488, 1106)],
            ),
        ],
    )


if __name__ == "__main__":
    main()
