# Lecture 08 (B07): Brock-Mirman II - uncertainty and integration

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance
> **Course author:** Simon Scheidegger
> **Compute tier:** `cpu-standard` &nbsp;·&nbsp; **Time budget:** `standard`

## Learning goal

Extend the Brock-Mirman DEQN to stochastic productivity. Master the role of quadrature for conditional expectations: choose between Gauss-Hermite, Monte Carlo, and sparse alternatives, and compare their accuracy and per-step cost.

## Prerequisites

- [Lecture 07 (B06)](../lecture_07_B06_brock_mirman_deterministic_deqn/README.md) — Brock-Mirman I - deterministic DEQN

## External prerequisites

- Python 3.10+ environment (`requirements.txt` at repo root, or run on the course platform).
- Familiarity with the math listed under **Script reference** below.

## Script reference

- §2.6 (Quadrature for conditional expectations)
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md) — full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf) — companion script

## Slides

- [`02_BrockMirman_Uncertainty_Integration.pdf`](slides/02_BrockMirman_Uncertainty_Integration.pdf) — residuals, expectations, Gauss-Hermite and monomial quadrature, training diagnostics.

## Notebooks

### Core

- [`lecture_08_B07_02_Brock_Mirman_Uncertainty_DEQN.ipynb`](notebooks/core/lecture_08_B07_02_Brock_Mirman_Uncertainty_DEQN.ipynb)

### Exercises

_(none in this PR)_

### Solutions

_(none in this PR)_

### Extensions

_(none in this PR)_

## Checkpoint

> Train stochastic Brock-Mirman with two quadrature rules and compare accuracy and per-step cost.

## Readings

- [`readings/links_by_lecture/lecture_08_B07.md`](../../readings/links_by_lecture/lecture_08_B07.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- **Previous:** [Lecture 07 (B06): Brock-Mirman I - deterministic DEQN](../lecture_07_B06_brock_mirman_deterministic_deqn/README.md)
- **Next:** [Lecture 09 (B08): Constraints, residual kernels, and loss design](../lecture_09_B08_constraints_residual_kernels_loss_design/README.md)
- [Course map](../../COURSE_MAP.md)
- [Repository home](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written / graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
