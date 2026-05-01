# Lecture 13 (B12): Surrogates and Gaussian processes

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance
> **Course author:** Simon Scheidegger
> **Compute tier:** `gpu-recommended` &nbsp;·&nbsp; **Time budget:** `long`

## Learning goal

Build deep surrogate models for expensive simulators, fit Gaussian-process regressors with Bayesian active learning, scale GPs to higher dimensions via active subspaces (linear and nonlinear) and deep kernels, and run GP value-function iteration. By the end you can pick a surrogate or a GP confidently for a new estimation, calibration, or policy-evaluation problem.

## Prerequisites

- [Lecture 02 (B01)](../lecture_02_B01_intro_deep_learning/README.md), Introduction to deep learning

## External prerequisites

- Python 3.10+ environment (`requirements.txt` at repo root, or run on the course platform).
- Familiarity with the math listed under **Script reference** below.

## Script reference

- §9.1-9.2 (Deep surrogates), §9.3-9.6 (GPs and Bayesian active learning), §9.7 (Active subspaces), §9.8 (GP value-function iteration), §9.9 (Deep kernels), §9.10 (GPs among Bayesian cousins)
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md), full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf), companion script

## Slides

- [`07_Surrogates_and_GPs.pdf`](slides/07_Surrogates_and_GPs.pdf)
- [`gp_active_learning.pdf`](slides/gp_active_learning.pdf)

## Notebooks

### Core

- [`lecture_13_B12_01_Surrogate_Primer.ipynb`](notebooks/core/lecture_13_B12_01_Surrogate_Primer.ipynb)
- [`lecture_13_B12_02_GP_and_BAL.ipynb`](notebooks/core/lecture_13_B12_02_GP_and_BAL.ipynb)
- [`lecture_13_B12_04_GP_Value_Function_Iteration.ipynb`](notebooks/core/lecture_13_B12_04_GP_Value_Function_Iteration.ipynb)
- [`lecture_13_B12_05_Active_Subspace_2D.ipynb`](notebooks/core/lecture_13_B12_05_Active_Subspace_2D.ipynb)
- [`lecture_13_B12_06_Active_Subspace_10D.ipynb`](notebooks/core/lecture_13_B12_06_Active_Subspace_10D.ipynb)
- [`lecture_13_B12_08_Deep_Kernel_Learning.ipynb`](notebooks/core/lecture_13_B12_08_Deep_Kernel_Learning.ipynb)

### Exercises

_(none)_

### Solutions

_(none)_

### Extensions

- [`lecture_13_B12_07_Active_Subspace_Nonlinear.ipynb`](notebooks/extensions/lecture_13_B12_07_Active_Subspace_Nonlinear.ipynb)
- [`lecture_13_B12_09_Deep_Active_Subspace_Ridge.ipynb`](notebooks/extensions/lecture_13_B12_09_Deep_Active_Subspace_Ridge.ipynb)
- [`lecture_13_B12_10_Deep_AS_vs_Linear_AS_Borehole.ipynb`](notebooks/extensions/lecture_13_B12_10_Deep_AS_vs_Linear_AS_Borehole.ipynb)

## Checkpoint

> Build a deep surrogate, fit a GP with Bayesian active learning, and apply linear/deep active subspaces to a 10-D test function.

## Readings

- [`readings/links_by_lecture/lecture_13_B12.md`](../../readings/links_by_lecture/lecture_13_B12.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- Previous: [Lecture 12 (B11), Continuous-time heterogeneous agents, numerics](../lecture_12_B11_continuous_time_ha_numerics/README.md)
- Next: [Lecture 14 (B13), Structural estimation via SMM](../lecture_14_B13_structural_estimation_smm/README.md)
- [`COURSE_MAP.md`](../../COURSE_MAP.md)
- [`README.md`](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written and graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
