# Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance

<p align="center">
  <img src="assets/hero/deep_learning_dynamic_models_hero.png" width="95%" alt="Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance">
</p>

> **Welcome.** This is a free, self-paced graduate course for PhD
> students and researchers in **computational and quantitative
> economics and finance** who want to use modern deep learning to
> solve and estimate the kinds of dynamic stochastic models that
> appear in macro, finance, and climate economics.
>
> Everything you need is in this repository: a textbook-length
> [lecture script](lecture_script/lecture_script.pdf), 30 paired
> lectures (slides + runnable Jupyter notebooks + exercises), a
> 2-module toolkit on using AI coding agents as research partners,
> and a curated bibliography. Work through it in your own order, at
> your own pace.

## What you will learn

By the end of the course you will be able to:

- **Solve recursive equilibrium models** (representative-agent and
  heterogeneous-agent, discrete- and continuous-time) with neural
  networks, using **Deep Equilibrium Nets (DEQNs)** and
  **Physics-Informed Neural Networks (PINNs)**.
- **Build deep surrogate models and Gaussian processes** for
  expensive simulators, including **Bayesian active learning**, scaling
  to high-dimensional settings via **active subspaces** and
  **deep kernels**.
- **Estimate** structural models with **simulated method of moments
  (SMM)** on top of deep surrogates.
- **Quantify deep uncertainty** in integrated-assessment models of
  climate economics, and design **constrained Pareto-improving
  carbon-tax policies**.
- Run an **AI-assisted research-coding workflow** end-to-end.

## How to use this course

Pick whichever entry point fits your goal:

- 🚀 **I want a guided start.** Open
  [Lecture 01](lectures/lecture_01_B00_orientation_setup_reproducibility/README.md)
  and follow the **Complete path** in [`COURSE_MAP.md`](COURSE_MAP.md).
  This walks through all 30 lectures and weaves in both toolkits at
  their natural insertion points.
- 🎯 **I have a specific topic in mind.** Use the **topic index**
  below to jump straight to the relevant block.
- 🧪 **I want the research-workflow training first.** Start with the
  [agentic-programming toolkit](toolkit/toolkit_01_T1_agentic_research_coding_loop/README.md),
  then return to the lecture sequence.
- 📖 **I want a textbook.** Read the chapter-based
  [companion script](lecture_script/lecture_script.pdf); each chapter
  links to one or more lectures via
  [`script_to_lectures.md`](lecture_script/script_to_lectures.md).

For each lecture, the workflow is the same:

1. read the relevant chapter or section of the script;
2. step through the lecture's slide deck (under `slides/`);
3. run the **core** notebooks (under `notebooks/core/`);
4. attempt the **exercise** notebooks, then check the **solutions**;
5. optionally explore the **extensions** for advanced material.

Every long-running notebook exposes a `RUN_MODE = "smoke" | "teaching" | "production"` switch
at the top so you can run it on a CPU laptop in minutes, on a workstation for classroom-quality
figures, or on a GPU for full reproductions.

## Topic index — find what you want

| If you want to learn… | Read | Notebooks |
|---|---|---|
| **Deep-learning fundamentals** (training, generalization, sequence models) | [Lectures 02–05](lectures/lecture_02_B01_why_deep_learning/README.md) | MLP / LSTM / Transformer on Edgeworth cycles, double descent, Genz approximations |
| **Deep Equilibrium Nets (DEQNs)** — the central method | [Lectures 06–10](lectures/lecture_06_B05_deqn_central_idea/README.md) | Brock-Mirman (deterministic, stochastic), Fischer-Burmeister constraints, autodiff |
| **Large-scale nonlinear DSGE** (IRBC) | [Lecture 11](lectures/lecture_11_B10_irbc_with_deqns/README.md) | International real business cycle with DEQNs |
| **Architecture search & loss balancing** (NAS, ReLoBRaLo) | [Lecture 12](lectures/lecture_12_B11_architecture_search_loss_balancing/README.md) | Random search, Hyperband, ReLoBRaLo / SoftAdapt / GradNorm |
| **OLG and heterogeneous agents** (discrete time) | [Lectures 13–17](lectures/lecture_13_B12_olg_models_deqns/README.md) | OLG, Krusell-Smith, Young's method, continuum-of-agents DEQN, sequence-space DEQNs |
| **PINNs and continuous-time HA** | [Lectures 18–21](lectures/lecture_18_B17_pinn_foundations/README.md) | ODE / PDE PINNs, hard vs soft BCs, cake-eating HJB, Black-Scholes PINN, continuous-time Aiyagari |
| **Surrogates, Gaussian processes, deep kernels** | [Lectures 22–25](lectures/lecture_22_B21_deep_surrogate_models/README.md) | Surrogate primer, GP regression + BAL, active subspaces, deep kernel learning, GP-VFI |
| **Structural estimation via SMM** | [Lecture 26](lectures/lecture_26_B25_structural_estimation_smm/README.md) | Brock-Mirman SMM (single- and joint-parameter) on a deep surrogate |
| **Climate economics, IAMs, and deep UQ** | [Lectures 27–29](lectures/lecture_27_B26_climate_economics_iams/README.md) | DICE / CDICE simulation, deterministic and stochastic CDICE-DEQN, deep UQ, optimal carbon-tax design |
| **Synthesis — when to use which method** | [Lecture 30](lectures/lecture_30_B29_synthesis_method_choice/README.md) | Decision guide and outlook |
| **Agentic research-coding workflow** | [Toolkit T1](toolkit/toolkit_01_T1_agentic_research_coding_loop/README.md) | AI-coding mental models, prompt engineering, the core interaction loop |
| **Project memory, custom skills, subagents, hooks** | [Toolkit T2](toolkit/toolkit_02_T2_project_memory_agents_hooks/README.md) | CLAUDE.md, skills, subagents, hooks, data-to-paper pipelines |

For the full table including compute and time budgets, prerequisites,
and the visual prerequisite diagram, see
[`COURSE_MAP.md`](COURSE_MAP.md).

## Toolkit modules — first-class, not optional

The two toolkits live alongside the lectures and teach the
**research workflow** that makes the rest of the course tractable for
real projects. Both can be done as standalone modules.

| Toolkit | Folder | Recommended placement |
|---|---|---|
| **T1 — Agentic research-coding loop** | [`toolkit/toolkit_01_T1_*/`](toolkit/toolkit_01_T1_agentic_research_coding_loop/README.md) | After Lecture 05, before starting DEQN work |
| **T2 — Project memory, agents, and hooks** | [`toolkit/toolkit_02_T2_*/`](toolkit/toolkit_02_T2_project_memory_agents_hooks/README.md) | After Lecture 12, before the heterogeneous-agent block |

## Setup

Notebooks run on **Python 3.10+**. Two reproducible setups:

```bash
# pip
pip install -r requirements.txt

# conda
conda env create -f environment.yml
conda activate dlef
```

Main dependencies: NumPy / SciPy / pandas / Matplotlib / scikit-learn,
TensorFlow ≥ 2.15, PyTorch ≥ 2.0, JAX (selected notebooks), GPyTorch /
BoTorch (Lectures 23–25). The full course platform of record (Nuvolos
Cloud) ships these pre-installed, so you can also run everything in
the cloud.

## Repository at a glance

```
.
├── README.md             ← you are here
├── COURSE_MAP.md         ← detailed map, learning paths, prerequisite diagram
├── course.yml            ← machine-readable course manifest
├── lectures/             ← 30 lecture folders (lecture_XX_BYY_*)
│   └── lecture_*/
│       ├── README.md         lecture index
│       ├── slides/           PDFs (and .tex sources)
│       ├── notebooks/
│       │   ├── core/         walkthroughs
│       │   ├── exercises/    blanks
│       │   ├── solutions/    filled-in
│       │   └── extensions/   advanced
│       ├── code/             auxiliary modules
│       ├── figures/          generated and static figures
│       └── notes/            short lecture-specific notes
├── toolkit/              ← Toolkit T1 and T2
├── lecture_script/       ← textbook-length companion script
├── readings/             ← per-lecture link guides + bibliography.bib
├── src/dlef/             ← reusable teaching package
├── assets/               ← hero figure, generated figures, attributions
├── data/                 ← generated datasets
├── scripts/              ← validation, build, and smoke-test scripts
└── legacy/               ← historical (live-course) timetable
```

## Glossary

The script's Appendix A is the canonical glossary. A grep-able copy
lives at [`lecture_script/glossary.md`](lecture_script/glossary.md).

## Readings and copyright

Most readings are journal articles, working papers, or copyrighted
books. The public repository **links** to publishers, DOIs, arXiv, or
author pages rather than redistributing PDFs. Per-lecture link guides
live under
[`readings/links_by_lecture/`](readings/links_by_lecture/);
the full bibliography is in
[`readings/bibliography.bib`](readings/bibliography.bib).

## License and citation

- **Code:** [MIT](LICENSE)
- **Text, slides, script, figures:** [CC0 1.0 Universal](LICENSE-content.md)
- **Third-party material:** see [`NOTICE.md`](NOTICE.md) and
  [`assets/attributions.yml`](assets/attributions.yml)
- **Citation:** [`CITATION.cff`](CITATION.cff)

Course author: **Simon Scheidegger** (University of Lausanne).

## Errata, contributions, and contact

Questions, corrections, and pull requests are welcome on
[GitHub](https://github.com/sischei/Deep_Learning_for_Solving_And_Estimating_Dynamic_Economic_Models).
By contributing you agree that your contribution is licensed under the
same terms as this repository.
