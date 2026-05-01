#!/usr/bin/env python3
"""Regenerate per-lecture README.md from course.yml.

Per-lecture folders have a flat structure:
  - slides/    PDFs and .tex sources
  - code/      every .ipynb plus any auxiliary .py / data files
  - figures/   (optional) lecture-specific figure assets
  - README.md  this file

The README leads with a one-paragraph summary of the lecture, then a
single inline metadata line (compute, time, prerequisite), then the
materials. No blockquote header, no per-lecture course author or
license boilerplate (those live on the landing page).
"""
from __future__ import annotations
from pathlib import Path
import yaml

REPO = Path(__file__).resolve().parents[2]


# Per-lecture content summaries. Keyed by NEW block ID (B00..B16).
SUMMARIES: dict[str, str] = {
    "B00": "Get the local environment running, locate every part of the course (script, slides, code, toolkits, readings), understand the conventions used throughout (lecture and block IDs, the `RUN_MODE` switch, compute tiers), and reproduce a smoke-test run end-to-end.",
    "B01": "Build the working knowledge of deep learning that the rest of the course assumes: classical ML and the bias-variance trade-off; SGD and its variants; depth, width, and double descent; sequence models from MLPs through LSTMs to small Transformers, applied to economic time-series patterns. By the end you have built and trained models in both TensorFlow and PyTorch, and you can read the rest of the course's notebooks fluently.",
    "B02": "State the Deep Equilibrium Net (DEQN) idea precisely, train deterministic and stochastic Brock-Mirman DEQNs, and verify them against closed-form solutions. Handle constraints with Fischer-Burmeister complementarity, choose conditional-expectation quadrature deliberately, and compare six loss kernels (MSE, MAE, Huber, quantile, CVaR, log-cosh) on the same problem.",
    "B03": "Solve a multi-country International Real Business Cycle (IRBC) model with DEQNs. Recover the symmetric steady state, run a comparative-statics exercise (e.g. doubling depreciation), and report Euler-equation residuals across the simulated state distribution.",
    "B04": "Run neural-architecture search and loss balancing systematically. Implement random search and successive halving (Hyperband) from scratch, and compare ReLoBRaLo, SoftAdapt, and GradNorm for multi-component loss balancing on a DEQN problem.",
    "B05": "Master the autodiff machinery that DEQN training depends on. Derive a Lagrangian primitive analytically and recover its gradient with two `tf.GradientTape` (or equivalent) calls per Euler equation. Cross-check the autodiff residual against a hand-derived residual to machine precision.",
    "B06": "Train sequence-space DEQNs that use a long shock history (~80 steps) instead of the current-state vector as input. Reproduce the Brock-Mirman warm-up and the Krusell-Smith benchmark in sequence space, and understand why the sequence-space template generalizes to multi-equation systems with multiple shock channels.",
    "B07": "Solve OLG models with DEQNs at two scales: an analytic small OLG with a closed-form check, and the standard 56-period benchmark with borrowing constraints handled via Fischer-Burmeister complementarity. Read off lifecycle savings, aggregate dynamics, and equilibrium residuals across cohorts.",
    "B08": "Solve heterogeneous-agent models with two complementary methods: Young's (2010) histogram for the stationary distribution on Aiyagari, and a continuum-of-agents DEQN. Run both and diagnose when each is preferable. The Krusell-Smith deep-learning extension is provided as further reading.",
    "B09": "Build PINNs (physics-informed neural networks) that solve ODEs and economic PDEs by minimizing the PDE residual on collocation points. Distinguish soft and hard boundary-condition parametrizations, solve a 2-D Poisson PDE, then apply the same template to the cake-eating HJB and to Black-Scholes option pricing.",
    "B10": "State the continuous-time heterogeneous-agent system (HJB + Kolmogorov-forward) and connect each operator to its discrete-time analog. Understand the role of Ito calculus, ergodicity, and the master equation in the modern continuous-time HA literature.",
    "B11": "Solve continuous-time Aiyagari with two methods, a finite-difference scheme on a state grid and a PINN, then compare the resulting consumption policies and stationary distributions. Build a PINN for the coupled HJB + KFE system from scratch in the exercise notebook.",
    "B12": "Build deep surrogate models for expensive simulators, fit Gaussian-process regressors with Bayesian active learning, scale GPs to higher dimensions via active subspaces (linear and nonlinear) and deep kernels, and run GP value-function iteration. By the end you can pick a surrogate or a GP confidently for a new estimation, calibration, or policy-evaluation problem.",
    "B13": "Estimate structural parameters by simulated method of moments (SMM) on top of a deep surrogate. Run both single-parameter (rho) and joint (beta, rho) Brock-Mirman estimations, and report identification diagnostics.",
    "B14": "Simulate the DICE carbon cycle and temperature dynamics under business-as-usual and a mitigation scenario, then solve deterministic CDICE with a DEQN and verify against the production-code reference. Extend to stochastic CDICE with AR(1) productivity shocks using Gauss-Hermite quadrature for conditional expectations.",
    "B15": "Run a deep-uncertainty-quantification analysis on a stochastic IAM and use the UQ output to design constrained Pareto-improving carbon-tax policies, tax paths that, for every realisation of the deep uncertainty, leave no agent worse off than the business-as-usual baseline while strictly improving welfare for at least one. Articulate which parameters drive the policy recommendation.",
    "B16": "Synthesize the course: when is DEQN the right choice, when do you reach for PINNs, when does a surrogate-plus-GP combination win? Map each method to its sweet-spot problem class and articulate the trade-offs.",
}


def script_ref(entries: list[dict]) -> str:
    parts = [f"§{e['section']} ({e['title']})" for e in entries]
    return ", ".join(parts) if parts else "—"


def list_files(folder_abs: Path, kind: str) -> list[Path]:
    sub = folder_abs / kind
    if not sub.exists():
        return []
    return sorted(p for p in sub.rglob("*") if p.is_file())


def render_links(folder_abs: Path, files: list[Path]) -> str:
    if not files:
        return "_(none)_"
    out = []
    for f in files:
        rel = f.relative_to(folder_abs).as_posix()
        out.append(f"- [`{rel}`]({rel})")
    return "\n".join(out)


def render_lecture_readme(lec: dict, lec_index: dict[str, dict]) -> str:
    num = f"{lec['lecture']:02d}"
    block = lec["block"]
    title = lec["title"]
    folder = lec["folder"]
    folder_abs = REPO / folder

    slide_files = list_files(folder_abs, "slides")
    slides = [f for f in slide_files if f.suffix in {".pdf", ".tex"} and f.parent.name == "slides"]
    code_files = list_files(folder_abs, "code")
    figure_files = list_files(folder_abs, "figures")

    if lec["prereqs"]:
        prereq_md = ", ".join(
            f"[Lecture {lec_index[p]['lecture']:02d} ({p})](../{Path(lec_index[p]['folder']).name}/README.md)"
            for p in lec["prereqs"] if p in lec_index
        )
        meta_line = f"`{lec.get('compute', 'cpu-light')}` · `{lec.get('time', 'standard')}` · builds on {prereq_md}"
    else:
        meta_line = f"`{lec.get('compute', 'cpu-light')}` · `{lec.get('time', 'standard')}`"

    sorted_lecs = sorted(lec_index.values(), key=lambda x: x["lecture"])
    prev_link = next_link = None
    for i, l in enumerate(sorted_lecs):
        if l["block"] == block:
            if i > 0:
                pl = sorted_lecs[i - 1]
                prev_link = f"← [Previous: {pl['title']}](../{Path(pl['folder']).name}/README.md)"
            if i < len(sorted_lecs) - 1:
                nl = sorted_lecs[i + 1]
                next_link = f"→ [Next: {nl['title']}](../{Path(nl['folder']).name}/README.md)"
            break

    nav_parts = [p for p in (prev_link, next_link, "[Course map](../../COURSE_MAP.md)") if p]
    nav = " · ".join(nav_parts)

    summary = SUMMARIES.get(block, "_Summary pending._")
    script_md = script_ref(lec.get("script") or [])

    sections = [
        f"# Lecture {num} ({block}): {title}",
        "",
        summary,
        "",
        meta_line,
        "",
        "## Slides",
        "",
        render_links(folder_abs, slides),
        "",
        "## Code",
        "",
        render_links(folder_abs, code_files),
    ]

    if figure_files:
        sections += [
            "",
            "## Figures",
            "",
            render_links(folder_abs, figure_files),
        ]

    sections += [
        "",
        "## In the lecture script",
        "",
        f"{script_md}. The full chapter map is in [`script_to_lectures.md`](../../lecture_script/script_to_lectures.md).",
    ]

    if lec.get("checkpoint"):
        sections += [
            "",
            "## By the end you should",
            "",
            lec["checkpoint"],
        ]

    sections += [
        "",
        "## Readings",
        "",
        f"Curated bibliography for this lecture: [`lecture_{num}_{block}.md`](../../readings/links_by_lecture/lecture_{num}_{block}.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).",
        "",
        "---",
        "",
        nav,
        "",
    ]
    return "\n".join(sections)


def main() -> None:
    with open(REPO / "course.yml") as f:
        course = yaml.safe_load(f)

    lectures: list[dict] = course["lectures"]
    lec_index = {lec["block"]: lec for lec in lectures}

    for lec in lectures:
        out = render_lecture_readme(lec, lec_index)
        path = REPO / lec["folder"] / "README.md"
        path.write_text(out, encoding="utf-8")
        print(f"wrote {path.relative_to(REPO)}")

    print(f"\n{len(lectures)} lectures regenerated.")


if __name__ == "__main__":
    main()
