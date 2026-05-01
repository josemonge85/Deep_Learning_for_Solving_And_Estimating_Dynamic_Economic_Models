# Lecture 09 (B08): Heterogeneous agents and Young's method

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance
> **Course author:** Simon Scheidegger
> **Compute tier:** `gpu-recommended` &nbsp;·&nbsp; **Time budget:** `long`

## Learning goal

Solve heterogeneous-agent models with two complementary methods: Young's (2010) histogram for the stationary distribution on Aiyagari, and a continuum-of-agents DEQN. Run both and diagnose when each is preferable. The Krusell-Smith deep-learning extension is provided as further reading.

## Prerequisites

- [Lecture 08 (B07)](../lecture_08_B07_olg_models_deqns/README.md), OLG models with DEQNs

## External prerequisites

- Python 3.10+ environment (`requirements.txt` at repo root, or run on the course platform).
- Familiarity with the math listed under **Script reference** below.

## Script reference

- §6.1-6.3 (Heterogeneous agents I), §6.4-6.6 (Heterogeneous agents II)
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md), full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf), companion script

## Slides

- [`08_Heterogeneous_Agents_Youngs_Method.pdf`](slides/08_Heterogeneous_Agents_Youngs_Method.pdf)

## Notebooks

### Core

- [`lecture_09_B08_10_Youngs_Method_Examples.ipynb`](notebooks/core/lecture_09_B08_10_Youngs_Method_Examples.ipynb)
- [`lecture_09_B08_11_Continuum_of_Agents_DEQN.ipynb`](notebooks/core/lecture_09_B08_11_Continuum_of_Agents_DEQN.ipynb)

### Exercises

_(none)_

### Solutions

_(none)_

### Extensions

- [`lecture_09_B08_12_KrusellSmith_DeepLearning.ipynb`](notebooks/extensions/lecture_09_B08_12_KrusellSmith_DeepLearning.ipynb)

## Checkpoint

> Run Young's histogram on Aiyagari and compare against a continuum-of-agents DEQN solution.

## Readings

- [`readings/links_by_lecture/lecture_09_B08.md`](../../readings/links_by_lecture/lecture_09_B08.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- Previous: [Lecture 08 (B07), OLG models with DEQNs](../lecture_08_B07_olg_models_deqns/README.md)
- Next: [Lecture 10 (B09), Physics-informed neural networks](../lecture_10_B09_pinns/README.md)
- [`COURSE_MAP.md`](../../COURSE_MAP.md)
- [`README.md`](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written and graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
