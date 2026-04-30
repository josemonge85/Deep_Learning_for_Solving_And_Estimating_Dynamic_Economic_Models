#!/usr/bin/env python3
"""Generate readings/links_by_lecture/lecture_XX_BYY.md files from a
small in-script registry. Default policy: link only — no PDFs are
redistributed. PDFs land in readings/allowed_pdfs/ only after license
clearance recorded in READINGS_AUDIT.csv (out of scope here).
"""
from __future__ import annotations
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "readings" / "links_by_lecture"

# Each entry: short_id -> dict with fields used in the markdown card.
READINGS = {
    "Fernandez-Villaverde-Nuno-Perla-2025-Taming": {
        "title": "Taming the Curse of Dimensionality: Quantitative Economics with Deep Learning",
        "authors": "Fernandez-Villaverde, J., Nuno, G., Perla, J.",
        "year": "2025",
        "venue": "NBER Working Paper / forthcoming",
        "url": "https://www.nber.org/papers/w33117",
        "note": "Survey of deep-learning methods for quantitative economic modelling. Read alongside Lectures 02 and 06.",
    },
    "Murphy-2022-PML": {
        "title": "Probabilistic Machine Learning: An Introduction",
        "authors": "Murphy, K. P.",
        "year": "2022",
        "venue": "MIT Press",
        "url": "https://probml.github.io/pml-book/book1.html",
        "note": "Free CC-BY-NC-ND draft from probml.github.io. Comprehensive textbook reference for the ML and deep-learning fundamentals.",
    },
    "James-Witten-Hastie-Tibshirani-2021-ISLR": {
        "title": "An Introduction to Statistical Learning, with Applications in R (2nd edition)",
        "authors": "James, G., Witten, D., Hastie, T., Tibshirani, R.",
        "year": "2021",
        "venue": "Springer",
        "url": "https://www.statlearning.com/",
        "note": "Free PDF available from statlearning.com. Accessible companion to ESL.",
    },
    "Azinovic-Gaegauf-Scheidegger-2022-DEQN": {
        "title": "Deep Equilibrium Nets",
        "authors": "Azinovic, M., Gaegauf, L., Scheidegger, S.",
        "year": "2022",
        "venue": "International Economic Review",
        "url": "https://onlinelibrary.wiley.com/doi/10.1111/iere.12575",
        "note": "Foundational DEQN paper. Working-paper version on author pages; SSRN/arXiv search will surface a freely available preprint.",
    },
    "Elsken-Metzen-Hutter-2019-NAS-Survey": {
        "title": "Neural Architecture Search: A Survey",
        "authors": "Elsken, T., Metzen, J. H., Hutter, F.",
        "year": "2019",
        "venue": "Journal of Machine Learning Research, 20(55):1-21",
        "url": "https://www.jmlr.org/papers/v20/18-598.html",
        "note": "Open-access survey covering search-space, search-strategy, and performance-estimation choices.",
    },
    "Young-2010-Histogram": {
        "title": "Solving the Incomplete Markets Model with Aggregate Uncertainty using the Krusell-Smith Algorithm and Non-Stochastic Simulations",
        "authors": "Young, E. R.",
        "year": "2010",
        "venue": "Journal of Economic Dynamics and Control, 34(1)",
        "url": "https://doi.org/10.1016/j.jedc.2008.11.010",
        "note": "Histogram method for stationary distributions in heterogeneous-agent models.",
    },
    "Maliar-Maliar-Winant-2021-DEQN-DSGE": {
        "title": "Deep Learning for Solving Dynamic Economic Models",
        "authors": "Maliar, L., Maliar, S., Winant, P.",
        "year": "2021",
        "venue": "Journal of Monetary Economics",
        "url": "https://doi.org/10.1016/j.jmoneco.2021.07.004",
        "note": "DEQN-style methods applied to representative-agent and heterogeneous-agent DSGE models.",
    },
    "Han-Yang-E-2023-DeepHAM": {
        "title": "DeepHAM: A Global Solution Method for Heterogeneous Agent Models with Aggregate Shocks",
        "authors": "Han, J., Yang, Y., E, W.",
        "year": "2023",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2112.14377",
        "note": "Krusell-Smith with deep learning, including aggregate-shock handling.",
    },
    "Auclert-Bardoczy-Rognlie-Straub-2021-SequenceSpace": {
        "title": "Using the Sequence-Space Jacobian to Solve and Estimate Heterogeneous-Agent Models",
        "authors": "Auclert, A., Bardóczy, B., Rognlie, M., Straub, L.",
        "year": "2021",
        "venue": "Econometrica, 89(5)",
        "url": "https://doi.org/10.3982/ECTA17434",
        "note": "Sequence-space methods that motivate sequence-space DEQNs in Lecture 17.",
    },
    "Azinovic-Yang-Zemlicka-2025-SequenceSpaceDEQN": {
        "title": "Deep Learning in the Sequence Space",
        "authors": "Azinovic, M., Yang, Y., Žemlička, J.",
        "year": "2025",
        "venue": "Working paper",
        "url": "https://scholar.google.com/scholar?q=Azinovic+Yang+Zemlicka+sequence+space+deep+learning",
        "note": "Sequence-space DEQNs. Working-paper version available on the authors' pages.",
    },
    "Folini-Friedl-Kuebler-Scheidegger-2024-CDICE": {
        "title": "The Climate in Climate Economics",
        "authors": "Folini, D., Friedl, A., Kuebler, F., Scheidegger, S.",
        "year": "2024",
        "venue": "Review of Economic Studies, 91(5)",
        "url": "https://doi.org/10.1093/restud/rdae011",
        "note": "Calibrated DICE-extended (CDICE) climate-economy model used in Lectures 27-28.",
    },
    "Friedl-Kuebler-Scheidegger-Usui-2023-DeepUQ": {
        "title": "Deep Uncertainty Quantification: With an Application to Integrated Assessment Models",
        "authors": "Friedl, A., Kuebler, F., Scheidegger, S., Usui, T.",
        "year": "2023",
        "venue": "Working paper",
        "url": "https://scholar.google.com/scholar?q=Deep+Uncertainty+Quantification+Integrated+Assessment+Models+Scheidegger",
        "note": "Deep-UQ framework applied to climate-economy models. Working-paper version on author pages.",
    },
    "Kuebler-Scheidegger-Surbek-2026-JPE-Macro": {
        "title": "Using Machine Learning to Compute Constrained Optimal Carbon Tax Rules",
        "authors": "Kuebler, F., Scheidegger, S., Surbek, O.",
        "year": "2026",
        "venue": "Journal of Political Economy: Macroeconomics (forthcoming)",
        "url": "https://scholar.google.com/scholar?q=Kuebler+Scheidegger+Surbek+constrained+optimal+carbon+tax",
        "note": "Constrained optimal carbon-tax design via deep surrogate models.",
    },
    "Cai-Lontzek-2019-StochasticDICE": {
        "title": "The Social Cost of Carbon with Economic and Climate Risks",
        "authors": "Cai, Y., Lontzek, T. S.",
        "year": "2019",
        "venue": "Journal of Political Economy, 127(6)",
        "url": "https://doi.org/10.1086/701890",
        "note": "Stochastic DICE with risks; reference for the Monte-Carlo SCC fan charts in Lecture 28.",
    },
    "Raissi-Perdikaris-Karniadakis-2019-PINN": {
        "title": "Physics-Informed Neural Networks: A Deep Learning Framework for Solving Forward and Inverse Problems Involving Nonlinear Partial Differential Equations",
        "authors": "Raissi, M., Perdikaris, P., Karniadakis, G. E.",
        "year": "2019",
        "venue": "Journal of Computational Physics, 378",
        "url": "https://doi.org/10.1016/j.jcp.2018.10.045",
        "note": "Foundational PINN paper.",
    },
    "Sirignano-Spiliopoulos-2018-DGM": {
        "title": "DGM: A Deep Learning Algorithm for Solving Partial Differential Equations",
        "authors": "Sirignano, J., Spiliopoulos, K.",
        "year": "2018",
        "venue": "Journal of Computational Physics, 375",
        "url": "https://doi.org/10.1016/j.jcp.2018.08.029",
        "note": "Deep Galerkin method for high-dimensional PDEs.",
    },
    "Achdou-Han-LasryLionsMoll-2022-CTHA": {
        "title": "Income and Wealth Distribution in Macroeconomics: A Continuous-Time Approach",
        "authors": "Achdou, Y., Han, J., Lasry, J.-M., Lions, P.-L., Moll, B.",
        "year": "2022",
        "venue": "Review of Economic Studies, 89(1)",
        "url": "https://doi.org/10.1093/restud/rdab002",
        "note": "Continuous-time heterogeneous agents (HJB + KFE). Reference for Lectures 20-21.",
    },
    "Black-Scholes-1973": {
        "title": "The Pricing of Options and Corporate Liabilities",
        "authors": "Black, F., Scholes, M.",
        "year": "1973",
        "venue": "Journal of Political Economy, 81(3)",
        "url": "https://doi.org/10.1086/260062",
        "note": "Original Black-Scholes paper, referenced in Lecture 19's PINN pricing notebook.",
    },
    "Schluntz-Zhang-2024-EffectiveAgents": {
        "title": "Building Effective Agents",
        "authors": "Schluntz, E., Zhang, B.",
        "year": "2024",
        "venue": "Anthropic engineering blog",
        "url": "https://www.anthropic.com/engineering/building-effective-agents",
        "note": "Practical patterns for agentic systems; background reading for Toolkit T1.",
    },
    "Korinek-2023-LLM-Economics": {
        "title": "Language Models and Cognitive Automation for Economic Research",
        "authors": "Korinek, A.",
        "year": "2023",
        "venue": "Journal of Economic Literature",
        "url": "https://www.aeaweb.org/articles?id=10.1257/jel.20231736",
        "note": "Survey of LLM use in economic research workflows.",
    },
}

# Per-lecture reading lists.
LECTURE_READINGS: dict[str, list[str]] = {
    "lecture_01_B00.md": [],
    "lecture_02_B01.md": [
        "Fernandez-Villaverde-Nuno-Perla-2025-Taming",
        "Murphy-2022-PML",
        "James-Witten-Hastie-Tibshirani-2021-ISLR",
    ],
    "lecture_03_B02.md": [
        "Murphy-2022-PML",
        "James-Witten-Hastie-Tibshirani-2021-ISLR",
    ],
    "lecture_04_B03.md": [
        "James-Witten-Hastie-Tibshirani-2021-ISLR",
    ],
    "lecture_05_B04.md": [],
    "lecture_06_B05.md": [
        "Azinovic-Gaegauf-Scheidegger-2022-DEQN",
        "Fernandez-Villaverde-Nuno-Perla-2025-Taming",
    ],
    "lecture_07_B06.md": [
        "Azinovic-Gaegauf-Scheidegger-2022-DEQN",
    ],
    "lecture_08_B07.md": [
        "Azinovic-Gaegauf-Scheidegger-2022-DEQN",
    ],
    "lecture_09_B08.md": [
        "Azinovic-Gaegauf-Scheidegger-2022-DEQN",
    ],
    "lecture_10_B09.md": [
        "Azinovic-Gaegauf-Scheidegger-2022-DEQN",
    ],
    "lecture_11_B10.md": [
        "Azinovic-Gaegauf-Scheidegger-2022-DEQN",
    ],
    "lecture_12_B11.md": [
        "Elsken-Metzen-Hutter-2019-NAS-Survey",
    ],
    "lecture_13_B12.md": [
        "Maliar-Maliar-Winant-2021-DEQN-DSGE",
    ],
    "lecture_14_B13.md": [
        "Maliar-Maliar-Winant-2021-DEQN-DSGE",
    ],
    "lecture_15_B14.md": [
        "Young-2010-Histogram",
    ],
    "lecture_16_B15.md": [
        "Maliar-Maliar-Winant-2021-DEQN-DSGE",
        "Han-Yang-E-2023-DeepHAM",
    ],
    "lecture_17_B16.md": [
        "Auclert-Bardoczy-Rognlie-Straub-2021-SequenceSpace",
        "Azinovic-Yang-Zemlicka-2025-SequenceSpaceDEQN",
    ],
    "lecture_18_B17.md": [
        "Raissi-Perdikaris-Karniadakis-2019-PINN",
        "Sirignano-Spiliopoulos-2018-DGM",
    ],
    "lecture_19_B18.md": [
        "Raissi-Perdikaris-Karniadakis-2019-PINN",
        "Black-Scholes-1973",
    ],
    "lecture_20_B19.md": [
        "Achdou-Han-LasryLionsMoll-2022-CTHA",
    ],
    "lecture_21_B20.md": [
        "Achdou-Han-LasryLionsMoll-2022-CTHA",
    ],
    "lecture_22_B21.md": [],
    "lecture_23_B22.md": [],
    "lecture_24_B23.md": [],
    "lecture_25_B24.md": [],
    "lecture_26_B25.md": [],
    "lecture_27_B26.md": [
        "Folini-Friedl-Kuebler-Scheidegger-2024-CDICE",
        "Cai-Lontzek-2019-StochasticDICE",
    ],
    "lecture_28_B27.md": [
        "Folini-Friedl-Kuebler-Scheidegger-2024-CDICE",
        "Cai-Lontzek-2019-StochasticDICE",
    ],
    "lecture_29_B28.md": [
        "Friedl-Kuebler-Scheidegger-Usui-2023-DeepUQ",
        "Kuebler-Scheidegger-Surbek-2026-JPE-Macro",
        "Folini-Friedl-Kuebler-Scheidegger-2024-CDICE",
    ],
    "lecture_30_B29.md": [],
}

# Lecture title lookup for headers
TITLES = {
    "lecture_01_B00": ("01", "B00", "Orientation, setup, and reproducibility"),
    "lecture_02_B01": ("02", "B01", "Why deep learning for economics and finance?"),
    "lecture_03_B02": ("03", "B02", "Training neural networks"),
    "lecture_04_B03": ("04", "B03", "Generalization and sequence models"),
    "lecture_05_B04": ("05", "B04", "Function approximation and loss design"),
    "lecture_06_B05": ("06", "B05", "Deep Equilibrium Nets — the central idea"),
    "lecture_07_B06": ("07", "B06", "Brock-Mirman I — deterministic DEQN"),
    "lecture_08_B07": ("08", "B07", "Brock-Mirman II — uncertainty and integration"),
    "lecture_09_B08": ("09", "B08", "Constraints, residual kernels, and loss design"),
    "lecture_10_B09": ("10", "B09", "Automatic differentiation for DEQNs"),
    "lecture_11_B10": ("11", "B10", "IRBC with DEQNs"),
    "lecture_12_B11": ("12", "B11", "Architecture search and loss balancing"),
    "lecture_13_B12": ("13", "B12", "OLG models with DEQNs"),
    "lecture_14_B13": ("14", "B13", "Large OLG benchmark"),
    "lecture_15_B14": ("15", "B14", "Krusell-Smith and Young's method"),
    "lecture_16_B15": ("16", "B15", "Continuum-of-agents DEQN and method comparison"),
    "lecture_17_B16": ("17", "B16", "Sequence-space DEQNs"),
    "lecture_18_B17": ("18", "B17", "PINNs I — residual learning for ODEs and PDEs"),
    "lecture_19_B18": ("19", "B18", "PINNs II — economic PDEs"),
    "lecture_20_B19": ("20", "B19", "Continuous-time HA theory"),
    "lecture_21_B20": ("21", "B20", "Continuous-time HA numerics"),
    "lecture_22_B21": ("22", "B21", "Deep surrogate models"),
    "lecture_23_B22": ("23", "B22", "Gaussian processes and Bayesian active learning"),
    "lecture_24_B23": ("24", "B23", "Scaling GPs — active subspaces and deep kernels"),
    "lecture_25_B24": ("25", "B24", "GPs for dynamic programming"),
    "lecture_26_B25": ("26", "B25", "Structural estimation via SMM"),
    "lecture_27_B26": ("27", "B26", "Climate economics and IAMs"),
    "lecture_28_B27": ("28", "B27", "Solving DICE with DEQNs"),
    "lecture_29_B28": ("29", "B28", "Deep uncertainty quantification and policy"),
    "lecture_30_B29": ("30", "B29", "Synthesis and method choice"),
}


def render(filename: str, ref_ids: list[str]) -> str:
    base = filename.rsplit(".", 1)[0]
    num, block, title = TITLES[base]
    body = [f"# Readings — Lecture {num} ({block}): {title}", ""]
    body.append("Default policy: link only. PDFs are not redistributed unless their license clearly permits it (see `READINGS_AUDIT.csv` once populated).")
    body.append("")
    if not ref_ids:
        body.append("> _No additional readings curated for this lecture beyond the companion lecture script. The script is the canonical reference; see [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf)._")
    else:
        body.append("## Selected references")
        body.append("")
        for rid in ref_ids:
            r = READINGS[rid]
            body.append(f"### {r['title']}")
            body.append("")
            body.append(f"- **Authors:** {r['authors']}")
            body.append(f"- **Year:** {r['year']}")
            body.append(f"- **Venue:** {r['venue']}")
            body.append(f"- **Link:** <{r['url']}>")
            body.append(f"- **Notes:** {r['note']}")
            body.append("")
    body.append("## Bibliography")
    body.append("")
    body.append("All references for this course are collected in [`readings/bibliography.bib`](../bibliography.bib).")
    body.append("")
    body.append("## Companion lecture script")
    body.append("")
    body.append(f"- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf) — chapter-based reference text")
    body.append(f"- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md) — full chapter-to-lecture map")
    return "\n".join(body) + "\n"


def main() -> None:
    for fname, refs in LECTURE_READINGS.items():
        path = OUT / fname
        path.write_text(render(fname, refs), encoding="utf-8")
    print(f"Wrote {len(LECTURE_READINGS)} reading-link files.")


if __name__ == "__main__":
    main()
