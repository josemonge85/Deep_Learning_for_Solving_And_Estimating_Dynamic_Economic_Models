# Lecture 24 (B23): Scaling GPs - active subspaces and deep kernels

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance
> **Course author:** Simon Scheidegger
> **Compute tier:** `gpu-recommended` &nbsp;·&nbsp; **Time budget:** `long`

## Learning goal

Scale Gaussian processes to higher-dimensional inputs using active subspaces (linear and nonlinear) and deep kernels. Compare reconstruction error on a 10-D test function across linear AS, nonlinear AS, and deep-kernel parametrizations.

## Prerequisites

- [Lecture 23 (B22)](../lecture_23_B22_gp_bayesian_active_learning/README.md) — Gaussian processes and Bayesian active learning

## External prerequisites

- Python 3.10+ environment (`requirements.txt` at repo root, or run on the course platform).
- Familiarity with the math listed under **Script reference** below.

## Script reference

- §9.7 (Active subspaces), §9.9 (Deep kernels)
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md) — full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf) — companion script

## Slides

- [`07_Bayesian_Active_Learning.pdf`](slides/07_Bayesian_Active_Learning.pdf) — where to sample, BAL algorithm, BAL in economics, BAL + GPs for surrogates.

## Notebooks

### Core

- [`lecture_24_B23_05_Active_Subspace_2D.ipynb`](notebooks/core/lecture_24_B23_05_Active_Subspace_2D.ipynb)
- [`lecture_24_B23_06_Active_Subspace_10D.ipynb`](notebooks/core/lecture_24_B23_06_Active_Subspace_10D.ipynb)
- [`lecture_24_B23_08_Deep_Kernel_Learning.ipynb`](notebooks/core/lecture_24_B23_08_Deep_Kernel_Learning.ipynb)

### Exercises

_(none in this PR)_

### Solutions

_(none in this PR)_

### Extensions

- [`lecture_24_B23_07_Active_Subspace_Nonlinear.ipynb`](notebooks/extensions/lecture_24_B23_07_Active_Subspace_Nonlinear.ipynb)
- [`lecture_24_B23_09_Deep_Active_Subspace_Ridge.ipynb`](notebooks/extensions/lecture_24_B23_09_Deep_Active_Subspace_Ridge.ipynb)
- [`lecture_24_B23_10_Deep_AS_vs_Linear_AS_Borehole.ipynb`](notebooks/extensions/lecture_24_B23_10_Deep_AS_vs_Linear_AS_Borehole.ipynb)

## Checkpoint

> Apply linear and deep active subspaces to a 10-D test function; compare reconstruction error.

## Readings

- [`readings/links_by_lecture/lecture_24_B23.md`](../../readings/links_by_lecture/lecture_24_B23.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- **Previous:** [Lecture 23 (B22): Gaussian processes and Bayesian active learning](../lecture_23_B22_gp_bayesian_active_learning/README.md)
- **Next:** [Lecture 25 (B24): GPs for dynamic programming](../lecture_25_B24_gps_for_dynamic_programming/README.md)
- [Course map](../../COURSE_MAP.md)
- [Repository home](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written / graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
