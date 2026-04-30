# Geneva 2026 — original live-course timetable

> **Note.** This file is **historical context only**. The public course
> in this repository is organized as a 30-lecture self-study sequence
> (see [`README.md`](../README.md) and [`COURSE_MAP.md`](../COURSE_MAP.md)),
> not as a day-by-day live schedule. The day numbering below refers to
> the live mini-course held at the University of Geneva in
> April-May 2026.
>
> Path mappings inside this file (`lectures/dayN/...`) refer to the
> *source* repository
> `Deep_Learning_Econ_Finance_Geneva_2026`, **not** to this public
> repository. For the day-to-lecture mapping, see
> [`COURSE_MAP.md`](../COURSE_MAP.md) and the lecture-prefixed file
> names under `lectures/lecture_XX_BYY_*/`.

# Deep Learning for Economics and Finance — Live course at the University of Geneva (April 20-23 & May 4-7, 2026)

This mini-course introduced **Deep Learning for Economics and Finance** for
Ph.D. students in economics and related disciplines. The course was held
over two sessions of four days each on Nuvolos Cloud.

## Detailed Timetable

### Session 1: April 20-23 — Discrete Time: From DNNs to Heterogeneous Agents

#### Day 1 — Monday, April 20th (afternoon, 3h)
**Introduction to Machine Learning, Deep Learning, and Sequence Models**

| Time | Topic | Materials |
|------|-------|-----------|
| 15:00-16:15 | Introduction to Machine Learning, Deep Learning, and Sequence Models | Slides: `lectures/day1/slides/01_Intro_to_DeepLearning.pdf` |
| 16:15-16:45 | Coffee Break | - |
| 16:45-18:00 | Hands-on: Basic ML, Gradient Descent & SGD, Double Descent, Deep Neural Networks, TensorBoard, PyTorch, Genz Approximation & Loss Functions, MLP vs LSTM vs Transformer on Edgeworth cycles, tiny in-context Transformer (advanced) | Notebooks 01-09 in `lectures/day1/code/` |

#### Day 2 — Tuesday, April 21st (morning, 3h)
**Deep Equilibrium Nets: Theory and First Applications**

| Time | Topic | Materials |
|------|-------|-----------|
| 09:00-10:15 | Introduction to Deep Equilibrium Nets | Slides: `02_DeepEquilibriumNets.pdf`; Notebooks: `01_Brock_Mirman_1972_DEQN`, `02_Brock_Mirman_Uncertainty_DEQN` |
| 10:15-10:45 | Coffee Break | - |
| 10:45-12:00 | Exercises: Solving dynamic stochastic models with DEQNs | Notebooks: `03_DEQN_Exercises_Blanks`, `04_DEQN_Exercises_Solutions` |

#### Day 3 — Wednesday, April 22nd (morning, 3h)
**Advanced DEQNs: Nonlinear Models, NAS, and Loss Normalization**

| Time | Topic | Materials |
|------|-------|-----------|
| 09:00-09:50 | Solving nonlinear dynamic stochastic models with DEQNs: the IRBC model | Slides: `03_IRBC.pdf`; Notebook: `01_IRBC_DEQN` |
| 09:50-09:55 | Finger Exercise: IRBC Euler equations (effect of doubling δ) | In slides |
| 10:00-10:30 | Coffee Break | - |
| 10:30-11:10 | Neural Architecture Search and Loss Normalization | Slides: `04_Neural_Architecture_Search.pdf`, `05_Loss_Normalization.pdf`; Notebooks: `02_NAS_Random_Search_10D`, `03_NAS_RandomSearch_Hyperband`, `04_Loss_Normalization` |
| 11:10-11:15 | Finger Exercise: ReLoBRaLo loss balancing | In slides |
| 11:15-12:00 | Introduction to the production-code DEQN library: solving a stochastic OLG model | Slides: `03_IRBC.pdf` (Part IV) |

#### Day 4 — Thursday, April 23rd (morning, 3h)
**Automatic Differentiation, Sequence-Space DEQNs, and OLG Models**

| Time | Topic | Materials |
|------|-------|-----------|
| 09:00-09:50 | Automatic Differentiation primer | Slides: `05b_AutoDiff_for_DEQN.pdf`; Notebooks: `01_AutoDiff_Analytical_Examples`, `02_Brock_Mirman_AutoDiff_DEQN`, `03_Brock_Mirman_Uncertainty_AutoDiff_DEQN` |
| 09:50-10:35 | Deep Learning in the Sequence Space | Slides: `06_SequenceSpace_DEQNs.pdf`; in-class: `05_SequenceSpace_BrockMirman`; demo/self-study: `06_SequenceSpace_KrusellSmith`, `KrusellSmith_Tutorial_CPU` |
| 10:35-11:00 | Coffee Break | - |
| 11:00-11:55 | OLG models with DEQNs | Slides: `07_OLG_Models_DEQNs.pdf`; Notebooks: `07_OLG_Analytic_DEQN`, `08_OLG_Benchmark_DEQN`; finger exercise on OLG savings (in slides) |
| 11:55-12:00 | Wrap-up | - |

> **Day 4 self-study extension on heterogeneous agents.** Deck `08_Heterogeneous_Agents_Youngs_Method.pdf` and notebooks `10_Youngs_Method_Examples`, `11_Continuum_of_Agents_DEQN`, `12_KrusellSmith_DeepLearning` cover Young's (2010) method, Krusell-Smith, and a DEQN teaching implementation. (See public Lectures 15-16.)

### Session 2: May 4-7 — Continuous Time, Surrogates, and Applications

#### Day 5 — Monday, May 4th (afternoon, 3h)
**Agentic Programming: Using AI Agents for Research**

| Time | Topic | Materials |
|------|-------|-----------|
| 15:00-16:15 | Orientation, mental models, environment setup, prompt engineering | Slides: `05_Agentic_Programming.pdf`; handout: `05_Agentic_Programming_Exercises.pdf` |
| 16:15-16:45 | Coffee Break | - |
| 16:45-18:00 | CLAUDE.md, project memory, skills & subagents, hooks, data-to-paper pipeline, replication, verification & ethics | Exercises 4-7; prompt pack `exercise_prompts.md`; self-study Exercises 0 and 8-11 |

(Public-course mapping: this material became `toolkit/toolkit_01_T1_*` and `toolkit/toolkit_02_T2_*`.)

#### Day 6 — Tuesday, May 5th (morning, 3h)
**PINNs and Continuous-Time Heterogeneous Agent Models**

| Time | Topic | Materials |
|------|-------|-----------|
| 09:00-09:35 | PINNs: foundations, PDE residuals, collocation | Slides: `06_PINNs.pdf`; Notebooks: `01_ODE_PINN_ZeroBCs`, `03_PDE_PINN_Poisson2D` |
| 09:35-09:40 | Finger Exercise: PINN loss for u''+u=0 | In slides |
| 09:40-10:05 | PINNs: boundary conditions; Adam → L-BFGS / FP64 | In-class: `02_ODE_PINN_SoftVsHardBCs`, `04_Cake_Eating_HJB_PINN`; self-study: `05_Black_Scholes_PINN` |
| 10:05-10:10 | Finger Exercise: hard-BC trial solution | In slides |
| 10:15-10:45 | Coffee Break | - |
| 10:45-11:30 | Continuous-time HA models: HJB + KFE + Aiyagari | Slides: `07_CT_Heterogeneous_Agents_Theory.pdf`, `08_CT_Heterogeneous_Agents_Numerical.pdf` |
| 11:30-11:35 | Finger Exercise: HJB equation | In slides |
| 11:35-12:00 | Numerical methods and PINN implementation for HA models | In-class: `08_Aiyagari_Continuous_Time_FD_and_PINN_PyTorch`, `09_PINN_Exercise`; self-study stepping stones: `06_PE_Discrete_HJB_PINN`, `07_PE_Diffusion_HJB_PINN` |

#### Day 7 — Wednesday, May 6th (morning, 3h)
**Surrogate Models, Gaussian Processes, and Deep Kernels**

| Time | Topic | Materials |
|------|-------|-----------|
| 09:00-09:45 | Deep Surrogate Models, GPR, BAL, Deep Kernel Learning | Slides: `07_Surrogates_and_GPs.pdf` (Parts I-III, V); in-class: `01_Surrogate_Primer`, `02_GP_and_BAL`; demo/self-study: `08_Deep_Kernel_Learning` |
| 09:45-10:15 | GPs for Dynamic Programming: VFI with active subspaces; deep active subspaces | Slides: `07_Surrogates_and_GPs.pdf` (Part IV); in-class: `04_GP_Value_Function_Iteration`; demo/self-study: notebooks 05, 06, 07, 09, 10 |
| 10:15-10:45 | Coffee Break | - |
| 10:45-12:00 | Exercise: surrogate-based structural estimation via SMM in the Brock-Mirman model | Slides: `08_Exercise_Structural_Estimation.pdf`; single-parameter (ρ): `03_Structural_Estimation_BM`; joint (β, ρ): `03b_Structural_Estimation_BM_Joint` |

#### Day 8 — Thursday, May 7th (morning, 3h)
**Climate Economics, Integrated Assessment Models, and Deep UQ**

| Time | Topic | Materials |
|------|-------|-----------|
| 09:00-09:50 | Climate change macroeconomics, IAMs, the DICE carbon cycle and temperature dynamics | Slides: `08_Climate_Economics_IAMs.pdf`; warm-up: `01_Climate_Exercise`; deterministic CDICE-DEQN: `02_DICE_DEQN_Library_Port`; stochastic CDICE-DEQN: `03_Stochastic_DICE_DEQN` |
| 09:50-09:55 | Finger Exercise: one-step carbon cycle | In slides |
| 10:00-10:30 | Coffee Break | - |
| 10:30-11:15 | Deep UQ for stochastic IAMs; constrained Pareto-improving policies via deep surrogates | Slides: `09_Deep_UQ_and_Optimal_Policies.pdf` |
| 11:15-11:20 | Finger Exercise: interpreting the social cost of carbon | In slides |
| 11:20-12:00 | Course wrap-up, key takeaways, and outlook | Slides: `10_Wrap_Up.pdf` |

## Why this file is here

The public, lecture-numbered course is the canonical organisation. This
timetable is preserved for two reasons:

1. transparency about the course's origin as a live mini-course; and
2. so that a student who first encountered the live course can find the
   day-to-lecture mapping in one place.

The day-to-lecture mapping is recorded in
[`MATERIALS_CROSSWALK.md`](../MATERIALS_CROSSWALK.md). Source `lectures/dayN/` paths
appear *only* in this file and in the crosswalk; they do **not** appear
in student-facing lecture READMEs.
