# Lecture 08 (B07): OLG models with DEQNs

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance  \
> **Course author:** Simon Scheidegger  \
> **Compute tier:** `gpu-recommended` &nbsp;·&nbsp; **Time budget:** `long`

## What this lecture covers

Solve OLG models with DEQNs at two scales: an analytic small OLG with a closed-form check, and the standard 56-period benchmark with borrowing constraints handled via Fischer-Burmeister complementarity. Read off lifecycle savings, aggregate dynamics, and equilibrium residuals across cohorts.

## Slides

- [`slides/07_OLG_Models_DEQNs.pdf`](slides/07_OLG_Models_DEQNs.pdf)
- [`slides/07_OLG_Models_DEQNs.tex`](slides/07_OLG_Models_DEQNs.tex)

## Code

- [`code/lecture_08_B07_07_OLG_Analytic_DEQN.ipynb`](code/lecture_08_B07_07_OLG_Analytic_DEQN.ipynb)
- [`code/lecture_08_B07_08_OLG_Benchmark_DEQN.ipynb`](code/lecture_08_B07_08_OLG_Benchmark_DEQN.ipynb)
- [`code/lecture_08_B07_09_OLG_Exercise.ipynb`](code/lecture_08_B07_09_OLG_Exercise.ipynb)

## Prerequisites

- [Lecture 06 (B05)](../lecture_06_B05_autodiff_for_deqns/README.md), Automatic differentiation for DEQNs

## Script reference

- §5.1-5.5 (OLG with DEQNs), §5.6 (Large OLG benchmark)
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md), full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf), companion script

## Checkpoint

> Train an analytic OLG DEQN and reproduce the 56-period benchmark with borrowing constraints via Fischer-Burmeister.

## Readings

- [`readings/links_by_lecture/lecture_08_B07.md`](../../readings/links_by_lecture/lecture_08_B07.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- Previous: [Lecture 07 (B06), Sequence-space DEQNs](../lecture_07_B06_sequence_space_deqns/README.md)
- Next: [Lecture 09 (B08), Heterogeneous agents and Young's method](../lecture_09_B08_heterogeneous_agents_youngs_method/README.md)
- [`COURSE_MAP.md`](../../COURSE_MAP.md)
- [`README.md`](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written and graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
