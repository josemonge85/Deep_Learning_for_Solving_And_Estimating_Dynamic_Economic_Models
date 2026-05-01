# Lecture 05 (B04): Architecture search and loss balancing

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance
> **Course author:** Simon Scheidegger
> **Compute tier:** `gpu-recommended` &nbsp;·&nbsp; **Time budget:** `long`

## Learning goal

Run neural-architecture search and loss balancing systematically. Implement random search and successive halving (Hyperband) from scratch in pure Python, and compare ReLoBRaLo, SoftAdapt, and GradNorm for multi-component loss balancing on a DEQN problem.

## Prerequisites

- [Lecture 04 (B03)](../lecture_04_B03_irbc_with_deqns/README.md), IRBC with DEQNs

## External prerequisites

- Python 3.10+ environment (`requirements.txt` at repo root, or run on the course platform).
- Familiarity with the math listed under **Script reference** below.

## Script reference

- §Chapter 4 (Neural architecture search and loss normalization)
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md), full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf), companion script

## Slides

- [`04_Neural_Architecture_Search.pdf`](slides/04_Neural_Architecture_Search.pdf)
- [`05_Loss_Normalization.pdf`](slides/05_Loss_Normalization.pdf)

## Notebooks

### Core

- [`lecture_05_B04_02_NAS_Random_Search_10D.ipynb`](notebooks/core/lecture_05_B04_02_NAS_Random_Search_10D.ipynb)
- [`lecture_05_B04_03_NAS_RandomSearch_Hyperband.ipynb`](notebooks/core/lecture_05_B04_03_NAS_RandomSearch_Hyperband.ipynb)
- [`lecture_05_B04_04_Loss_Normalization.ipynb`](notebooks/core/lecture_05_B04_04_Loss_Normalization.ipynb)

### Exercises

- [`lecture_05_B04_05_IRBC_Exercise.ipynb`](notebooks/exercises/lecture_05_B04_05_IRBC_Exercise.ipynb)

### Solutions

_(none)_

### Extensions

_(none)_

## Checkpoint

> Run random search on a 10-D NAS problem and compare ReLoBRaLo, SoftAdapt, and GradNorm.

## Readings

- [`readings/links_by_lecture/lecture_05_B04.md`](../../readings/links_by_lecture/lecture_05_B04.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- Previous: [Lecture 04 (B03), IRBC with DEQNs](../lecture_04_B03_irbc_with_deqns/README.md)
- Next: [Lecture 06 (B05), Automatic differentiation for DEQNs](../lecture_06_B05_autodiff_for_deqns/README.md)
- [`COURSE_MAP.md`](../../COURSE_MAP.md)
- [`README.md`](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written and graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
