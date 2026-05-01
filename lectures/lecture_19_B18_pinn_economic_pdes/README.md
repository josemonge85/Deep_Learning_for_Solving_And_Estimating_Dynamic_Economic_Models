# Lecture 19 (B18): PINNs II - economic PDEs

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance
> **Course author:** Simon Scheidegger
> **Compute tier:** `cpu-standard` &nbsp;·&nbsp; **Time budget:** `standard`

## Learning goal

Apply PINNs to economic PDEs: solve the cake-eating HJB with a hard-BC trial solution, and price a European call option via a Black-Scholes PINN. Read off the value function, optimal consumption, and option delta from the trained network.

## Prerequisites

- [Lecture 18 (B17)](../lecture_18_B17_pinn_foundations/README.md) — PINNs I - residual learning for ODEs and PDEs

## External prerequisites

- Python 3.10+ environment (`requirements.txt` at repo root, or run on the course platform).
- Familiarity with the math listed under **Script reference** below.

## Script reference

- §7.5-7.9 (Economic PDEs (HJB, Black-Scholes))
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md) — full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf) — companion script

## Slides

_(none in this PR)_

## Notebooks

### Core

- [`lecture_19_B18_04_Cake_Eating_HJB_PINN.ipynb`](notebooks/core/lecture_19_B18_04_Cake_Eating_HJB_PINN.ipynb)
- [`lecture_19_B18_05_Black_Scholes_PINN.ipynb`](notebooks/core/lecture_19_B18_05_Black_Scholes_PINN.ipynb)

### Exercises

_(none in this PR)_

### Solutions

_(none in this PR)_

### Extensions

_(none in this PR)_

## Checkpoint

> Solve the cake-eating HJB with a hard-BC trial solution; price a European call via Black-Scholes PINN.

## Readings

- [`readings/links_by_lecture/lecture_19_B18.md`](../../readings/links_by_lecture/lecture_19_B18.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- [`COURSE_MAP.md`](../../COURSE_MAP.md)
- [`README.md`](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written / graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
