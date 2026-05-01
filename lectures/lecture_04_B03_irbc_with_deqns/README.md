# Lecture 04 (B03): IRBC with DEQNs

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance
> **Course author:** Simon Scheidegger
> **Compute tier:** `gpu-recommended` &nbsp;·&nbsp; **Time budget:** `long`

## Learning goal

Solve a multi-country International Real Business Cycle (IRBC) model with DEQNs. Recover the symmetric steady state, run a comparative-statics exercise (e.g. doubling depreciation), and report Euler-equation residuals across the simulated state distribution.

## Prerequisites

- [Lecture 03 (B02)](../lecture_03_B02_deep_equilibrium_nets/README.md), Deep Equilibrium Nets

## External prerequisites

- Python 3.10+ environment (`requirements.txt` at repo root, or run on the course platform).
- Familiarity with the math listed under **Script reference** below.

## Script reference

- §Chapter 3 (International real business cycle)
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md), full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf), companion script

## Slides

- [`03_IRBC.pdf`](slides/03_IRBC.pdf)

## Notebooks

### Core

- [`lecture_04_B03_01_IRBC_DEQN.ipynb`](notebooks/core/lecture_04_B03_01_IRBC_DEQN.ipynb)

### Exercises

_(none)_

### Solutions

_(none)_

### Extensions

_(none)_

## Checkpoint

> Train an N-country IRBC DEQN and reproduce the symmetric steady state.

## Readings

- [`readings/links_by_lecture/lecture_04_B03.md`](../../readings/links_by_lecture/lecture_04_B03.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- Previous: [Lecture 03 (B02), Deep Equilibrium Nets](../lecture_03_B02_deep_equilibrium_nets/README.md)
- Next: [Lecture 05 (B04), Architecture search and loss balancing](../lecture_05_B04_nas_loss_normalization/README.md)
- [`COURSE_MAP.md`](../../COURSE_MAP.md)
- [`README.md`](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written and graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
