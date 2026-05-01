# Lecture 18 (B17): PINNs I - residual learning for ODEs and PDEs

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance
> **Course author:** Simon Scheidegger
> **Compute tier:** `cpu-standard` &nbsp;·&nbsp; **Time budget:** `standard`

## Learning goal

Build PINNs (physics-informed neural networks) that solve ODEs and PDEs by minimizing the PDE residual on collocation points. Distinguish soft and hard boundary-condition parametrizations and choose between them. Solve a 2-D Poisson PDE end-to-end.

## Prerequisites

- [Lecture 10 (B09)](../lecture_10_B09_autodiff_for_deqns/README.md) — Automatic differentiation for DEQNs

## External prerequisites

- Python 3.10+ environment (`requirements.txt` at repo root, or run on the course platform).
- Familiarity with the math listed under **Script reference** below.

## Script reference

- §7.1-7.4 (PINN foundations)
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md) — full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf) — companion script

## Slides

- [`06_PINN_Foundations.pdf`](slides/06_PINN_Foundations.pdf) — DEQN vs PINN, automatic differentiation for PDEs, training pipeline, network architecture.

## Notebooks

### Core

- [`lecture_18_B17_01_ODE_PINN_ZeroBCs.ipynb`](notebooks/core/lecture_18_B17_01_ODE_PINN_ZeroBCs.ipynb)
- [`lecture_18_B17_02_ODE_PINN_SoftVsHardBCs.ipynb`](notebooks/core/lecture_18_B17_02_ODE_PINN_SoftVsHardBCs.ipynb)
- [`lecture_18_B17_03_PDE_PINN_Poisson2D.ipynb`](notebooks/core/lecture_18_B17_03_PDE_PINN_Poisson2D.ipynb)

### Exercises

_(none in this PR)_

### Solutions

_(none in this PR)_

### Extensions

_(none in this PR)_

## Checkpoint

> Solve a 2-D Poisson PDE with a PINN under both soft and hard boundary-condition parametrizations.

## Readings

- [`readings/links_by_lecture/lecture_18_B17.md`](../../readings/links_by_lecture/lecture_18_B17.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- [`COURSE_MAP.md`](../../COURSE_MAP.md)
- [`README.md`](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written / graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
