# Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance

<p align="center">
  <img src="assets/hero/deep_learning_dynamic_models_hero.png" width="95%" alt="Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance">
</p>

<br/>

**Hi, and welcome.** If you work on the kind of dynamic stochastic
models that show up in macro, asset pricing, or climate economics, and
you want to actually *use* modern deep learning on them rather than
read another survey about it, this course is for you. It is free,
self-paced, and built to be worked through with your own laptop open.

Everything you need is right here in this repository:

- a textbook-length [companion script](lecture_script/lecture_script.pdf) you can read end-to-end,
- **18 paired lectures** with slides, runnable Jupyter notebooks, and exercises,
- a workshop on using AI coding agents as research partners (Lecture 06),
- and a curated bibliography linking out to the underlying papers.

Pick the lecture you actually need, run the notebooks, work the
exercises. There is no enrollment, no cohort, no deadline. Just dig in.

> 🚀 **Start here →** [Lecture 02, intro to deep learning](lectures/lecture_02_B01_intro_deep_learning/README.md)
> &nbsp;·&nbsp; new to Python? begin with the [Python primer](lectures/lecture_01_B00_python_primer/README.md)
> &nbsp;·&nbsp; want the panoramic view? open [`COURSE_MAP.md`](COURSE_MAP.md)

## What you will learn

This course teaches a coherent set of deep-learning methods for the
recursive, stochastic, often high-dimensional models that show up in
modern macroeconomics, asset pricing, and climate-economic policy work.
Five capabilities, each motivated below.

### 1. Solving recursive equilibrium models with neural networks

Most quantitative macro models reduce to functional equations (Euler
equations, Bellman equations, market-clearing conditions) that
classical methods (projection, value-function iteration, perturbation)
struggle with once the state space gets large or the policy is
nonsmooth. **Deep Equilibrium Nets (DEQNs)** parameterize the policy
or value function with a neural network and minimize the
equilibrium-equation residuals directly via stochastic gradient descent,
sidestepping a curse-of-dimensionality grid. The companion **Physics-Informed
Neural Networks (PINNs)** do the same for continuous-time models: the
loss is the residual of a Hamilton–Jacobi–Bellman equation, automatic
differentiation supplies the derivatives, and there is no mesh.
You will build both end-to-end on benchmarks where the answer is known
(Brock–Mirman, cake-eating, Black–Scholes) and then on models where it
is not (IRBC, OLG with 56 cohorts, Krusell–Smith with a continuum of
agents, continuous-time heterogeneous agents).

### 2. Surrogates, Gaussian processes, and Bayesian active learning

Many calibration, estimation, and policy-evaluation tasks call the
underlying model thousands or millions of times. A **deep surrogate
model** replaces that expensive call with a cheap, differentiable
neural network trained on a few hundred or thousand simulator outputs.
A **Gaussian process (GP)** does the same with built-in uncertainty
quantification, which lets **Bayesian active learning (BAL)** pick the
next training point optimally instead of throwing samples at a
hypercube. We then push GPs to high dimension via **active subspaces**
and **deep kernel learning**, and use them inside value-function
iteration (ASGP-VFI) as a competitor to DEQNs.

### 3. Structural estimation via simulated method of moments

Once a deep surrogate is in place, **simulated method of moments
(SMM)** estimation becomes a small optimization over the surrogate
rather than a brutal repeated re-solve of the structural model. You
will run single- and joint-parameter SMM on a deep surrogate of
Brock–Mirman and see how the estimator behaves under realistic noise
and identification challenges.

### 4. Deep UQ and Pareto-improving climate policy

Integrated assessment models (DICE, CDICE) carry parameters whose
true values are deeply uncertain, equilibrium climate sensitivity
being the textbook example. Plugging point estimates in and reading
off a single social cost of carbon is misleading; averaging the
uncertainty out before optimization is worse, because the policy you
would choose under expected damages is generally not the policy you
would choose if you took the tail risk seriously.

The course teaches a complete pipeline that addresses this directly.
We solve a stochastic IAM with DEQNs under Epstein–Zin preferences,
build GP surrogates for the quantities of interest with Bayesian
active learning, and run global sensitivity analysis (Sobol, Shapley
effects) to localize where the policy is actually sensitive to which
parameters. On top of that surrogate we then **design constrained
Pareto-improving carbon-tax policies**: tax paths that, for every
realization of the deep uncertainty (or every cohort, or every
generation), leave no agent worse off than the business-as-usual
baseline while strictly improving welfare for at least one. This turns
"what should the carbon tax be?" from a single number computed under a
single calibration into a defensible policy menu that respects who
bears the risk and who benefits, *without* averaging the uncertainty
away.

### 5. An AI-assisted research-coding workflow

Modern empirical and computational economics benefits enormously from
using AI coding agents (Claude Code) as research partners, but only
when the workflow is set up deliberately. **Lecture 06** is a
hands-on workshop that teaches the orientation, prompt patterns,
project memory (`CLAUDE.md`), custom skills, subagents, and hooks
that turn an LLM from a clever autocomplete into a real research
collaborator, paired with twelve self-paced exercises so you walk
out with reusable templates rather than slideware.

## How to use this course

Different readers come in with different goals, so pick the entry point
that fits yours:

- 🚀 **I want a guided start.** Open the
  [Python primer (Lecture 01)](lectures/lecture_01_B00_python_primer/README.md)
  if you need it, then follow the **Complete path** in
  [`COURSE_MAP.md`](COURSE_MAP.md). It walks through all 18 lectures
  in their natural order.
- 🎯 **I have a specific topic in mind.** Jump straight to the
  **topic index** below.
- 🧪 **I want the research-workflow training first.** Jump to
  [Lecture 06, agentic programming](lectures/lecture_06_B17_agentic_programming/README.md),
  then come back to the rest of the sequence.
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

Every long-running notebook exposes a `RUN_MODE = "smoke" | "full"` switch
at the top so you can run it on a CPU laptop in minutes (smoke mode, for a sanity
check) or take it all the way for the published-figure quality result.

## Topic index, find what you want

| If you want to learn… | Read | Notebooks |
|---|---|---|
| **Deep-learning fundamentals** (training, generalization, sequence models) | [Lecture 02](lectures/lecture_02_B01_intro_deep_learning/README.md) | MLP, LSTM, Transformer on Edgeworth cycles, double descent, Genz approximations |
| **Deep Equilibrium Nets (DEQNs)**, the central method | [Lecture 03](lectures/lecture_03_B02_deep_equilibrium_nets/README.md) | Brock-Mirman (deterministic, stochastic), Fischer-Burmeister constraints, six loss kernels |
| **Large-scale nonlinear DSGE** (IRBC) | [Lecture 04](lectures/lecture_04_B03_irbc_with_deqns/README.md) | International real business cycle with DEQNs |
| **Architecture search and loss balancing** (NAS, ReLoBRaLo) | [Lecture 05](lectures/lecture_05_B04_nas_loss_normalization/README.md) | Random search, Hyperband, ReLoBRaLo, SoftAdapt, GradNorm |
| **Agentic programming** (AI coding agents as research partners) | [Lecture 06](lectures/lecture_06_B17_agentic_programming/README.md) | Claude Code workflow, prompts, project memory, custom skills, subagents, hooks, plus a 12-exercise workshop |
| **Automatic differentiation for DEQNs** | [Lecture 07](lectures/lecture_07_B05_autodiff_for_deqns/README.md) | Lagrangian primitives, two-tape gradients, IRBC autodiff |
| **Sequence-space DEQNs** | [Lecture 08](lectures/lecture_08_B06_sequence_space_deqns/README.md) | Brock-Mirman, IRBC, Krusell-Smith with shock-history inputs |
| **OLG with DEQNs** | [Lecture 09](lectures/lecture_09_B07_olg_models_deqns/README.md) | Analytic OLG, 56-cohort benchmark, Fischer-Burmeister borrowing constraints |
| **Heterogeneous agents and Young's method** | [Lecture 10](lectures/lecture_10_B08_heterogeneous_agents_youngs_method/README.md) | Young's histogram, Krusell-Smith, continuum-of-agents DEQN |
| **PINNs and continuous-time HA** | [Lectures 11-13](lectures/lecture_11_B09_pinns/README.md) | ODE / PDE PINNs, hard vs soft BCs, cake-eating HJB, Black-Scholes PINN, continuous-time Aiyagari |
| **Surrogates, Gaussian processes, deep kernels** | [Lecture 14](lectures/lecture_14_B12_surrogates_and_gps/README.md) | Surrogate primer, GP regression, BAL, active subspaces, deep kernel learning, GP-VFI |
| **Structural estimation via SMM** | [Lecture 15](lectures/lecture_15_B13_structural_estimation_smm/README.md) | Brock-Mirman SMM (single- and joint-parameter) on a deep surrogate |
| **Climate economics, IAMs, and deep UQ** | [Lectures 16-17](lectures/lecture_16_B14_climate_economics_iams/README.md) | DICE / CDICE simulation, deterministic and stochastic CDICE-DEQN, deep UQ, constrained Pareto-improving carbon-tax design |
| **Synthesis, when to use which method** | [Lecture 18](lectures/lecture_18_B16_course_wrap_up/README.md) | Decision guide and outlook |

For the full table including compute and time budgets, prerequisites,
and the visual prerequisite diagram, see
[`COURSE_MAP.md`](COURSE_MAP.md).

## Setup

Notebooks run on **Python 3.10+**. Two reproducible setups:

```bash
# pip
pip install -r requirements.txt

# conda
conda env create -f environment.yml
conda activate dlef
```

Main dependencies: NumPy, SciPy, pandas, Matplotlib, scikit-learn,
TensorFlow ≥ 2.15, PyTorch ≥ 2.0, JAX (selected notebooks), GPyTorch
and BoTorch (Lecture 13).

## Repository at a glance

```
.
├── README.md             ← you are here
├── COURSE_MAP.md         ← detailed map, learning paths, prerequisite diagram
├── lectures/             ← 18 lecture folders (lecture_XX_BYY_*)
│   └── lecture_*/
│       ├── README.md         summary, slides, code, prerequisites, readings
│       ├── slides/           PDFs and .tex sources
│       ├── code/             notebooks, supporting .py modules, data files
│       └── figures/          (optional) lecture-specific figure assets
├── lecture_script/       ← textbook-length companion script
├── readings/             ← per-lecture link guides + bibliography.bib
└── assets/               ← hero figure, generated figures, attributions
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
