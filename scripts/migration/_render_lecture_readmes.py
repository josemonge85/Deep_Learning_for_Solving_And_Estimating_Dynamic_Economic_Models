#!/usr/bin/env python3
"""Regenerate per-lecture README.md from course.yml after the
30-lecture-to-17-lecture re-coarsening."""
from __future__ import annotations
from pathlib import Path
import yaml

REPO = Path(__file__).resolve().parents[2]


# Per-lecture learning-goal paragraphs. Keyed by NEW block ID (B00..B16, T1..T3).
LEARNING_GOALS: dict[str, str] = {
    "B00": "Get the local environment running, locate every part of the course (script, slides, notebooks, toolkits, readings), understand the conventions used throughout (lecture/block IDs, RUN_MODE switch, compute tiers), and reproduce a smoke-test run end-to-end.",
    "B01": "Build the working knowledge of deep learning that the rest of the course assumes: classical ML and the bias-variance trade-off; SGD and its variants; depth, width, and double descent; sequence models from MLPs through LSTMs to small Transformers, applied to economic time-series patterns. By the end you have built and trained models in both TensorFlow and PyTorch, and you can read the rest of the course's notebooks fluently.",
    "B02": "State the Deep Equilibrium Net (DEQN) idea precisely, train deterministic and stochastic Brock-Mirman DEQNs, and verify them against closed-form solutions. Handle constraints with Fischer-Burmeister complementarity, choose conditional-expectation quadrature deliberately, and compare six loss kernels (MSE, MAE, Huber, quantile, CVaR, log-cosh) on the same problem.",
    "B03": "Solve a multi-country International Real Business Cycle (IRBC) model with DEQNs. Recover the symmetric steady state, run a comparative-statics exercise (e.g. doubling depreciation), and report Euler-equation residuals across the simulated state distribution.",
    "B04": "Run neural-architecture search and loss balancing systematically. Implement random search and successive halving (Hyperband) from scratch in pure Python, and compare ReLoBRaLo, SoftAdapt, and GradNorm for multi-component loss balancing on a DEQN problem.",
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
    "T1": "Develop a working agentic research-coding workflow: orient yourself in an unfamiliar codebase with an AI partner, structure prompts that produce useful (not generic) work, and complete the first set of workshop exercises end-to-end.",
    "T2": "Author the operational furniture that makes agentic research-coding sustainable for real projects: a project-memory `CLAUDE.md`, custom skills (e.g. an econometrics or backtest-validation skill), subagents for review and verification, and hooks that automate routine checks.",
    "T3": "Work through the agentic-programming exercise handout that accompanies T1 and T2, both the workshop set and the self-study extensions, and consolidate the techniques into a personal research-coding playbook.",
}


def script_ref(entries: list[dict]) -> str:
    parts = [f"§{e['section']} ({e['title']})" for e in entries]
    return ", ".join(parts) if parts else "—"


def list_links(items: list[str]) -> str:
    if not items:
        return "_(none)_"
    return "\n".join(f"- [`{Path(rel).name}`]({rel})" for rel in items)


def render_lecture_readme(lec: dict, lec_index: dict[str, dict]) -> str:
    num = f"{lec['lecture']:02d}"
    block = lec["block"]
    title = lec["title"]

    slides = lec.get("slides") or []
    nb = lec.get("notebooks") or {}
    core = nb.get("core") or []
    exercises = nb.get("exercises") or []
    solutions = nb.get("solutions") or []
    extensions = nb.get("extensions") or []

    if lec["prereqs"]:
        prereq_md = ", ".join(
            f"[Lecture {lec_index[p]['lecture']:02d} ({p})](../{Path(lec_index[p]['folder']).name}/README.md), {lec_index[p]['title']}"
            for p in lec["prereqs"] if p in lec_index
        )
    else:
        prereq_md = "_(none, start of course)_"

    # Prev / next nav: walk lectures in `lecture` order
    sorted_lecs = sorted(lec_index.values(), key=lambda x: x["lecture"])
    prev_md = "_(this is the first lecture)_"
    next_md = "_(this is the last lecture)_"
    for i, l in enumerate(sorted_lecs):
        if l["block"] == block:
            if i > 0:
                pl = sorted_lecs[i - 1]
                prev_md = f"[Lecture {pl['lecture']:02d} ({pl['block']}), {pl['title']}](../{Path(pl['folder']).name}/README.md)"
            if i < len(sorted_lecs) - 1:
                nl = sorted_lecs[i + 1]
                next_md = f"[Lecture {nl['lecture']:02d} ({nl['block']}), {nl['title']}](../{Path(nl['folder']).name}/README.md)"
            break

    script_md = script_ref(lec.get("script") or [])
    learning_goal = LEARNING_GOALS.get(block, "_Learning goal pending._")

    return f"""# Lecture {num} ({block}): {title}

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance
> **Course author:** Simon Scheidegger
> **Compute tier:** `{lec.get('compute', 'cpu-light')}` &nbsp;·&nbsp; **Time budget:** `{lec.get('time', 'standard')}`

## Learning goal

{learning_goal}

## Prerequisites

- {prereq_md}

## External prerequisites

- Python 3.10+ environment (`requirements.txt` at repo root, or run on the course platform).
- Familiarity with the math listed under **Script reference** below.

## Script reference

- {script_md}
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md), full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf), companion script

## Slides

{list_links(slides)}

## Notebooks

### Core

{list_links(core)}

### Exercises

{list_links(exercises)}

### Solutions

{list_links(solutions)}

### Extensions

{list_links(extensions)}

## Checkpoint

> {lec.get('checkpoint', '_To be filled in by the maintainer._')}

## Readings

- [`readings/links_by_lecture/lecture_{num}_{block}.md`](../../readings/links_by_lecture/lecture_{num}_{block}.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- Previous: {prev_md}
- Next: {next_md}
- [`COURSE_MAP.md`](../../COURSE_MAP.md)
- [`README.md`](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written and graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
"""


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
