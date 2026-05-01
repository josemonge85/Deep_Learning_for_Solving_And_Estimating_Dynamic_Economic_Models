# Lecture 09 (B08): Constraints, residual kernels, and loss design

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance
> **Course author:** Simon Scheidegger
> **Compute tier:** `cpu-standard` &nbsp;·&nbsp; **Time budget:** `standard`

## Learning goal

Handle inequality constraints in DEQN training: penalty methods, Fischer-Burmeister complementarity, and residual-kernel weighting. Build intuition for which loss-balancing approach helps when training stalls because of constraint violations.

## Prerequisites

- [Lecture 08 (B07)](../lecture_08_B07_brock_mirman_uncertainty_integration/README.md) — Brock-Mirman II - uncertainty and integration

## External prerequisites

- Python 3.10+ environment (`requirements.txt` at repo root, or run on the course platform).
- Familiarity with the math listed under **Script reference** below.

## Script reference

- §2.4 (Constraints), §2.9 (Residual kernels)
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md) — full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf) — companion script

## Slides

_(none in this PR)_

## Notebooks

### Core

- [`lecture_09_B08_05_StochasticBM_LossComparison.ipynb`](notebooks/core/lecture_09_B08_05_StochasticBM_LossComparison.ipynb)

### Exercises

- [`lecture_09_B08_03_DEQN_Exercises_Blanks.ipynb`](notebooks/exercises/lecture_09_B08_03_DEQN_Exercises_Blanks.ipynb)

### Solutions

- [`lecture_09_B08_04_DEQN_Exercises_Solutions.ipynb`](notebooks/solutions/lecture_09_B08_04_DEQN_Exercises_Solutions.ipynb)

### Extensions

_(none in this PR)_

## Checkpoint

> Implement Fischer-Burmeister complementarity in a DEQN loss and compare against penalty methods.

## Readings

- [`readings/links_by_lecture/lecture_09_B08.md`](../../readings/links_by_lecture/lecture_09_B08.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- [`COURSE_MAP.md`](../../COURSE_MAP.md)
- [`README.md`](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written / graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
