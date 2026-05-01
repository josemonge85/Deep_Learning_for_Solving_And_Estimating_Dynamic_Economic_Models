# Lecture 22 (B21): Deep surrogate models

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance
> **Course author:** Simon Scheidegger
> **Compute tier:** `cpu-standard` &nbsp;·&nbsp; **Time budget:** `standard`

## Learning goal

Build a deep surrogate for an expensive simulator on a controlled test problem and validate it out-of-sample. Develop intuition for when surrogates pay for themselves over direct simulation.

## Prerequisites

- [Lecture 05 (B04)](../lecture_05_B04_function_approximation_loss_design/README.md) — Function approximation and loss design

## External prerequisites

- Python 3.10+ environment (`requirements.txt` at repo root, or run on the course platform).
- Familiarity with the math listed under **Script reference** below.

## Script reference

- §9.1-9.2 (Surrogates)
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md) — full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf) — companion script

## Slides

- [`07_Deep_Surrogate_Models.pdf`](slides/07_Deep_Surrogate_Models.pdf) — pseudo-states, structural estimation, UQ, optimal policy, implied vol surfaces.

## Notebooks

### Core

- [`lecture_22_B21_01_Surrogate_Primer.ipynb`](notebooks/core/lecture_22_B21_01_Surrogate_Primer.ipynb)

### Exercises

_(none in this PR)_

### Solutions

_(none in this PR)_

### Extensions

_(none in this PR)_

## Checkpoint

> Build a deep surrogate for an expensive simulator and validate out-of-sample.

## Readings

- [`readings/links_by_lecture/lecture_22_B21.md`](../../readings/links_by_lecture/lecture_22_B21.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- **Previous:** [Lecture 21 (B20): Continuous-time HA numerics](../lecture_21_B20_continuous_time_ha_numerics/README.md)
- **Next:** [Lecture 23 (B22): Gaussian processes and Bayesian active learning](../lecture_23_B22_gp_bayesian_active_learning/README.md)
- [Course map](../../COURSE_MAP.md)
- [Repository home](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written / graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
