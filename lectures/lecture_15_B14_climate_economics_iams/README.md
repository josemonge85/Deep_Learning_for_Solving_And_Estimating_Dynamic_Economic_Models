# Lecture 15 (B14): Climate economics and integrated assessment models

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance
> **Course author:** Simon Scheidegger
> **Compute tier:** `gpu-recommended` &nbsp;·&nbsp; **Time budget:** `long`

## Learning goal

Simulate the DICE carbon cycle and temperature dynamics under business-as-usual and a mitigation scenario, then solve deterministic CDICE with a DEQN and verify against the production-code reference. Extend to stochastic CDICE with AR(1) productivity shocks using Gauss-Hermite quadrature for conditional expectations.

## Prerequisites

- [Lecture 06 (B05)](../lecture_06_B05_autodiff_for_deqns/README.md), Automatic differentiation for DEQNs

## External prerequisites

- Python 3.10+ environment (`requirements.txt` at repo root, or run on the course platform).
- Familiarity with the math listed under **Script reference** below.

## Script reference

- §11.1-11.2 (IAMs and DICE), §11.3 (DICE with DEQNs)
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md), full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf), companion script

## Slides

- [`08_Climate_Economics_IAMs.pdf`](slides/08_Climate_Economics_IAMs.pdf)

## Notebooks

### Core

- [`lecture_15_B14_02_DICE_DEQN_Library_Port.ipynb`](notebooks/core/lecture_15_B14_02_DICE_DEQN_Library_Port.ipynb)

### Exercises

- [`lecture_15_B14_01_Climate_Exercise.ipynb`](notebooks/exercises/lecture_15_B14_01_Climate_Exercise.ipynb)

### Solutions

_(none)_

### Extensions

- [`lecture_15_B14_03_Stochastic_DICE_DEQN.ipynb`](notebooks/extensions/lecture_15_B14_03_Stochastic_DICE_DEQN.ipynb)

## Checkpoint

> Simulate the DICE carbon cycle and temperature dynamics, then solve deterministic CDICE with a DEQN.

## Readings

- [`readings/links_by_lecture/lecture_15_B14.md`](../../readings/links_by_lecture/lecture_15_B14.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- Previous: [Lecture 14 (B13), Structural estimation via SMM](../lecture_14_B13_structural_estimation_smm/README.md)
- Next: [Lecture 16 (B15), Deep uncertainty quantification and Pareto-improving climate policy](../lecture_16_B15_deep_uq_pareto_improving_policy/README.md)
- [`COURSE_MAP.md`](../../COURSE_MAP.md)
- [`README.md`](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written and graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
