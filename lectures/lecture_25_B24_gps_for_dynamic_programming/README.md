# Lecture 25 (B24): GPs for dynamic programming

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance
> **Course author:** Simon Scheidegger
> **Compute tier:** `cpu-standard` &nbsp;·&nbsp; **Time budget:** `long`

## Learning goal

Run Gaussian-process value-function iteration: combine GP function approximation with active learning inside the VFI loop. Diagnose stability and the trade-off between training-set size and per-iteration cost.

## Prerequisites

- [Lecture 24 (B23)](../lecture_24_B23_scaling_gps_active_subspaces_deep_kernels/README.md) — Scaling GPs - active subspaces and deep kernels

## External prerequisites

- Python 3.10+ environment (`requirements.txt` at repo root, or run on the course platform).
- Familiarity with the math listed under **Script reference** below.

## Script reference

- §9.8 (GP-VFI), §9.10 (GPs among Bayesian cousins)
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md) — full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf) — companion script

## Slides

_(none in this PR)_

## Notebooks

### Core

- [`lecture_25_B24_04_GP_Value_Function_Iteration.ipynb`](notebooks/core/lecture_25_B24_04_GP_Value_Function_Iteration.ipynb)

### Exercises

_(none in this PR)_

### Solutions

_(none in this PR)_

### Extensions

_(none in this PR)_

## Checkpoint

> Run GP-VFI on a 2-D test economy and reach a stable value function.

## Readings

- [`readings/links_by_lecture/lecture_25_B24.md`](../../readings/links_by_lecture/lecture_25_B24.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- [`COURSE_MAP.md`](../../COURSE_MAP.md)
- [`README.md`](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written / graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
