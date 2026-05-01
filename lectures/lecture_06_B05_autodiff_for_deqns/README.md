# Lecture 06 (B05): Automatic differentiation for DEQNs

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance
> **Course author:** Simon Scheidegger
> **Compute tier:** `cpu-standard` &nbsp;·&nbsp; **Time budget:** `standard`

## Learning goal

Master the autodiff machinery that DEQN training depends on. Derive a Lagrangian primitive analytically and recover its gradient with two `tf.GradientTape` (or equivalent) calls per Euler equation. Cross-check the autodiff residual against a hand-derived residual to machine precision.

## Prerequisites

- [Lecture 03 (B02)](../lecture_03_B02_deep_equilibrium_nets/README.md), Deep Equilibrium Nets

## External prerequisites

- Python 3.10+ environment (`requirements.txt` at repo root, or run on the course platform).
- Familiarity with the math listed under **Script reference** below.

## Script reference

- §2.7 (Automatic differentiation), §Appendix B (Matrix calculus)
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md), full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf), companion script

## Slides

- [`05b_AutoDiff_for_DEQN.pdf`](slides/05b_AutoDiff_for_DEQN.pdf)

## Notebooks

### Core

- [`lecture_06_B05_01_AutoDiff_Analytical_Examples.ipynb`](notebooks/core/lecture_06_B05_01_AutoDiff_Analytical_Examples.ipynb)
- [`lecture_06_B05_02_Brock_Mirman_AutoDiff_DEQN.ipynb`](notebooks/core/lecture_06_B05_02_Brock_Mirman_AutoDiff_DEQN.ipynb)
- [`lecture_06_B05_03_Brock_Mirman_Uncertainty_AutoDiff_DEQN.ipynb`](notebooks/core/lecture_06_B05_03_Brock_Mirman_Uncertainty_AutoDiff_DEQN.ipynb)

### Exercises

_(none)_

### Solutions

_(none)_

### Extensions

- [`lecture_06_B05_04_IRBC_AutoDiff_DEQN.ipynb`](notebooks/extensions/lecture_06_B05_04_IRBC_AutoDiff_DEQN.ipynb)

## Checkpoint

> Derive a Lagrangian primitive analytically and recover its gradient via two-tape autodiff.

## Readings

- [`readings/links_by_lecture/lecture_06_B05.md`](../../readings/links_by_lecture/lecture_06_B05.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- Previous: [Lecture 05 (B04), Architecture search and loss balancing](../lecture_05_B04_nas_loss_normalization/README.md)
- Next: [Lecture 07 (B06), Sequence-space DEQNs](../lecture_07_B06_sequence_space_deqns/README.md)
- [`COURSE_MAP.md`](../../COURSE_MAP.md)
- [`README.md`](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written and graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
