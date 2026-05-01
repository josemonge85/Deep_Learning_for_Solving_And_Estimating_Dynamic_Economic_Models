# Lecture 07 (B06): Brock-Mirman I - deterministic DEQN

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance
> **Course author:** Simon Scheidegger
> **Compute tier:** `cpu-standard` &nbsp;·&nbsp; **Time budget:** `standard`

## Learning goal

Train a DEQN on the deterministic Brock-Mirman growth model and verify the trained policy against the closed-form solution. Diagnose convergence behavior and tune the basic ingredients (sampling distribution, residual normalization, training schedule).

## Prerequisites

- [Lecture 06 (B05)](../lecture_06_B05_deqn_central_idea/README.md) — Deep Equilibrium Nets - the central idea

## External prerequisites

- Python 3.10+ environment (`requirements.txt` at repo root, or run on the course platform).
- Familiarity with the math listed under **Script reference** below.

## Script reference

- §2.5 (Deterministic Brock-Mirman)
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md) — full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf) — companion script

## Slides

- [`02_BrockMirman_Deterministic_DEQN.pdf`](slides/02_BrockMirman_Deterministic_DEQN.pdf) — neural network architecture, supervised vs unsupervised, deterministic Brock--Mirman.

## Notebooks

### Core

- [`lecture_07_B06_01_Brock_Mirman_1972_DEQN.ipynb`](notebooks/core/lecture_07_B06_01_Brock_Mirman_1972_DEQN.ipynb)

### Exercises

_(none in this PR)_

### Solutions

_(none in this PR)_

### Extensions

_(none in this PR)_

## Checkpoint

> Train a deterministic Brock-Mirman DEQN and verify against the closed-form policy.

## Readings

- [`readings/links_by_lecture/lecture_07_B06.md`](../../readings/links_by_lecture/lecture_07_B06.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- **Previous:** [Lecture 06 (B05): Deep Equilibrium Nets - the central idea](../lecture_06_B05_deqn_central_idea/README.md)
- **Next:** [Lecture 08 (B07): Brock-Mirman II - uncertainty and integration](../lecture_08_B07_brock_mirman_uncertainty_integration/README.md)
- [Course map](../../COURSE_MAP.md)
- [Repository home](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written / graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
