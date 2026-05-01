#!/usr/bin/env python3
"""Regenerate per-lecture README.md and the top-level at-a-glance table
from course.yml so every entry is a working Markdown hyperlink.
"""
from __future__ import annotations
from pathlib import Path
import re
import sys
import yaml

REPO = Path(__file__).resolve().parents[1]


# Per-lecture learning-goal paragraphs. Keyed by block ID (B00..B29, T1, T2).
LEARNING_GOALS: dict[str, str] = {
    "B00": "Get the local environment running, locate every part of the course (script, slides, notebooks, toolkits, readings), understand the conventions used throughout (lecture/block IDs, RUN_MODE switch, compute tiers), and reproduce a smoke-test run end-to-end.",
    "B01": "Articulate why neural networks are useful for solving and estimating dynamic stochastic models — what they buy you over projection, perturbation, value-function iteration, and other classical methods — and connect the bias-variance trade-off to function-approximation choices in economics.",
    "B02": "Understand how neural networks are trained: SGD and its variants, backpropagation, the role of depth and width, and how to monitor training in practice. By the end you can implement SGD by hand, build a small MLP in both TensorFlow and PyTorch, and instrument a training run with TensorBoard.",
    "B03": "Reason about generalization and inductive bias in neural networks: the double-descent phenomenon, the role of architecture in handling sequences, and the relative strengths of MLPs, LSTMs, and Transformers on time-series-like economic data (Edgeworth cycles).",
    "B04": "Choose function-approximation architectures and loss functions appropriate to a given economic problem. Use the Genz family of test integrands to compare loss choices on a controlled benchmark with known optima.",
    "B05": "State the Deep Equilibrium Net (DEQN) idea precisely: a policy network whose loss is the squared norm of equilibrium residuals, trained on simulated state distributions. Recognize when DEQNs are the right tool relative to projection, value-function iteration, and perturbation.",
    "B06": "Train a DEQN on the deterministic Brock-Mirman growth model and verify the trained policy against the closed-form solution. Diagnose convergence behavior and tune the basic ingredients (sampling distribution, residual normalization, training schedule).",
    "B07": "Extend the Brock-Mirman DEQN to stochastic productivity. Master the role of quadrature for conditional expectations: choose between Gauss-Hermite, Monte Carlo, and sparse alternatives, and compare their accuracy and per-step cost.",
    "B08": "Handle inequality constraints in DEQN training: penalty methods, Fischer-Burmeister complementarity, and residual-kernel weighting. Build intuition for which loss-balancing approach helps when training stalls because of constraint violations.",
    "B09": "Master the autodiff machinery that DEQN training depends on. Derive a Lagrangian primitive analytically and recover its gradient with two `tf.GradientTape` (or equivalent) calls per Euler equation. Cross-check the autodiff residual against a hand-derived residual to machine precision.",
    "B10": "Solve a multi-country International Real Business Cycle (IRBC) model with DEQNs. Recover the symmetric steady state, run a comparative-statics exercise (e.g. doubling depreciation), and report Euler-equation residuals across the simulated state distribution.",
    "B11": "Run neural-architecture search and loss balancing systematically. Implement random search and successive halving (Hyperband) from scratch in pure Python, and compare ReLoBRaLo, SoftAdapt, and GradNorm for multi-component loss balancing.",
    "B12": "Solve an analytic OLG (overlapping-generations) model with DEQNs and verify lifecycle savings against the closed form. Understand how cohort structure changes the residual operator and the training loss.",
    "B13": "Scale OLG-DEQN to the standard 56-period benchmark with borrowing constraints. Combine Fischer-Burmeister complementarity with cohort-stacked Lagrangians and read off the steady state.",
    "B14": "Implement Young's (2010) histogram method for stationary distributions in heterogeneous-agent models, iterate it on Aiyagari to convergence, and read the resulting wealth distribution and aggregates.",
    "B15": "Solve continuum-of-agents models with a DEQN and compare the result, side by side, with the Young-method solution from the previous lecture. Diagnose when each method is preferable.",
    "B16": "Train sequence-space DEQNs that use a long shock history (~80 steps) instead of the current-state vector as input. Reproduce the Brock-Mirman warm-up and the Krusell-Smith benchmark in sequence space, and understand why the sequence-space template generalizes to multi-equation systems with multiple shock channels.",
    "B17": "Build PINNs (physics-informed neural networks) that solve ODEs and PDEs by minimizing the PDE residual on collocation points. Distinguish soft and hard boundary-condition parametrizations and choose between them. Solve a 2-D Poisson PDE end-to-end.",
    "B18": "Apply PINNs to economic PDEs: solve the cake-eating HJB with a hard-BC trial solution, and price a European call option via a Black-Scholes PINN. Read off the value function, optimal consumption, and option delta from the trained network.",
    "B19": "State the continuous-time heterogeneous-agent system (HJB + Kolmogorov-forward) and connect each operator to its discrete-time analog. Understand the role of Ito calculus, ergodicity, and the master equation in the modern continuous-time HA literature.",
    "B20": "Solve continuous-time Aiyagari with two methods — a finite-difference scheme on a state grid and a PINN — and compare the resulting consumption policies and stationary distributions. Build a PINN for the coupled HJB + KFE system from scratch in the exercise notebook.",
    "B21": "Build a deep surrogate for an expensive simulator on a controlled test problem and validate it out-of-sample. Develop intuition for when surrogates pay for themselves over direct simulation.",
    "B22": "Fit Gaussian-process regressors and use Bayesian active learning (BAL) to choose new query points that reduce predictive uncertainty fastest. Quantify the resulting uncertainty reduction relative to passive sampling.",
    "B23": "Scale Gaussian processes to higher-dimensional inputs using active subspaces (linear and nonlinear) and deep kernels. Compare reconstruction error on a 10-D test function across linear AS, nonlinear AS, and deep-kernel parametrizations.",
    "B24": "Run Gaussian-process value-function iteration: combine GP function approximation with active learning inside the VFI loop. Diagnose stability and the trade-off between training-set size and per-iteration cost.",
    "B25": "Estimate structural parameters by simulated method of moments (SMM) on top of a deep surrogate. Run both single-parameter (rho) and joint (beta, rho) Brock-Mirman estimations and report identification diagnostics.",
    "B26": "Simulate the DICE carbon cycle and temperature dynamics under business-as-usual and a mitigation scenario. Read off the social cost of carbon and connect the IAM building blocks to the underlying climate science.",
    "B27": "Solve deterministic CDICE with a DEQN and verify against the production-code reference solution. Extend to stochastic CDICE with AR(1) productivity shocks using Gauss-Hermite quadrature for conditional expectations.",
    "B28": "Run a deep-uncertainty-quantification analysis on a stochastic IAM. Use the UQ output to identify constrained Pareto-improving carbon-tax policies and articulate which parameters drive the policy recommendation.",
    "B29": "Synthesize the course: when is DEQN the right choice, when do you reach for PINNs, when does a surrogate-plus-GP combination win? Map each method to its sweet-spot problem class and articulate the trade-offs.",
    "T1": "Develop a working agentic research-coding workflow: orient yourself in an unfamiliar codebase with an AI partner, structure prompts that produce useful (not generic) work, and complete the first set of workshop exercises end-to-end.",
    "T2": "Author the operational furniture that makes agentic research-coding sustainable for real projects: a project-memory `CLAUDE.md`, custom skills (e.g. an econometrics or backtest-validation skill), subagents for review and verification, and hooks that automate routine checks.",
}


def script_ref(entries: list[dict]) -> str:
    parts = [f"§{e['section']} ({e['title']})" for e in entries]
    return ", ".join(parts) if parts else "—"


def list_links(prefix: str, items: list[str]) -> str:
    if not items:
        return "_(none in this PR)_"
    out = []
    for rel in items:
        name = Path(rel).name
        out.append(f"- [`{name}`]({rel})")
    return "\n".join(out)


def compute_compute(lec: dict) -> str:
    return lec.get("compute", "cpu-light")


def compute_time(lec: dict) -> str:
    return lec.get("time", "standard")


def render_lecture_readme(lec: dict, prereq_titles: dict[str, str]) -> str:
    num = f"{lec['lecture']:02d}"
    block = lec["block"]
    title = lec["title"]
    folder = lec["folder"]

    slides = lec.get("slides") or []
    nb = lec.get("notebooks") or {}
    core = nb.get("core") or []
    exercises = nb.get("exercises") or []
    solutions = nb.get("solutions") or []
    extensions = nb.get("extensions") or []

    if lec["prereqs"]:
        prereq_md = ", ".join(
            f"[Lecture {prereq_titles[p][0]} ({p})](../{prereq_titles[p][1]}/README.md) — {prereq_titles[p][2]}"
            for p in lec["prereqs"]
            if p in prereq_titles
        )
    else:
        prereq_md = "_(none — start of course)_"

    script_md = script_ref(lec.get("script") or [])
    learning_goal = LEARNING_GOALS.get(block, "_Learning goal pending._")

    return f"""# Lecture {num} ({block}): {title}

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance
> **Course author:** Simon Scheidegger
> **Compute tier:** `{compute_compute(lec)}` &nbsp;·&nbsp; **Time budget:** `{compute_time(lec)}`

## Learning goal

{learning_goal}

## Prerequisites

- {prereq_md}

## External prerequisites

- Python 3.10+ environment (`requirements.txt` at repo root, or run on the course platform).
- Familiarity with the math listed under **Script reference** below.

## Script reference

- {script_md}
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md) — full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf) — companion script

## Slides

{list_links(folder, slides)}

## Notebooks

### Core

{list_links(folder, core)}

### Exercises

{list_links(folder, exercises)}

### Solutions

{list_links(folder, solutions)}

### Extensions

{list_links(folder, extensions)}

## Checkpoint

> {lec.get('checkpoint', '_To be filled in by the maintainer._')}

## Readings

- [`readings/links_by_lecture/lecture_{num}_{block}.md`](../../readings/links_by_lecture/lecture_{num}_{block}.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- [`COURSE_MAP.md`](../../COURSE_MAP.md)
- [`README.md`](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written / graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
"""


def render_at_a_glance(course: dict, lectures: list[dict], toolkits: list[dict]) -> str:
    """Markdown table fragment with linked lecture rows."""
    lines = [
        "| # | Block | Title | Compute | Time |",
        "|---:|---|---|---|---|",
    ]
    insert_after_T1 = "B04"
    insert_after_T2 = "B11"
    seen_T1 = False
    seen_T2 = False
    for lec in lectures:
        num = f"{lec['lecture']:02d}"
        block = lec["block"]
        title = lec["title"]
        folder = lec["folder"]
        compute = lec.get("compute", "")
        tt = lec.get("time", "")
        lines.append(
            f"| [{num}]({folder}/README.md) | {block} | [{title}]({folder}/README.md) | `{compute}` | `{tt}` |"
        )
        if block == insert_after_T1 and not seen_T1:
            tk = next(t for t in toolkits if t["block"] == "T1")
            lines.append(
                f"| **T1** | **T1** | **[Toolkit: {tk['title']}]({tk['folder']}/README.md)** | `{tk['compute']}` | `{tk['time']}` |"
            )
            seen_T1 = True
        if block == insert_after_T2 and not seen_T2:
            tk = next(t for t in toolkits if t["block"] == "T2")
            lines.append(
                f"| **T2** | **T2** | **[Toolkit: {tk['title']}]({tk['folder']}/README.md)** | `{tk['compute']}` | `{tk['time']}` |"
            )
            seen_T2 = True
    return "\n".join(lines)


def main() -> None:
    with open(REPO / "course.yml") as f:
        course = yaml.safe_load(f)

    lectures: list[dict] = course["lectures"]
    toolkits: list[dict] = course["toolkits"]

    # Build prereq_titles lookup: block -> (num_str, folder, title)
    prereq_titles = {
        lec["block"]: (f"{lec['lecture']:02d}", Path(lec["folder"]).name, lec["title"])
        for lec in lectures
    }

    # Per-lecture READMEs
    for lec in lectures:
        out = render_lecture_readme(lec, prereq_titles)
        path = REPO / lec["folder"] / "README.md"
        path.write_text(out, encoding="utf-8")
        print(f"  wrote {path.relative_to(REPO)}")

    # At-a-glance table for top-level README
    table_md = render_at_a_glance(course, lectures, toolkits)
    table_path = REPO / "_dev" / "_at_a_glance.md"
    table_path.write_text(table_md, encoding="utf-8")
    print(f"\nWrote at-a-glance table fragment to {table_path.relative_to(REPO)}")
    print(f"({len(lectures)} lectures + {len(toolkits)} toolkits)")


if __name__ == "__main__":
    main()
