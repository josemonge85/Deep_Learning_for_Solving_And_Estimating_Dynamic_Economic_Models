# Lecture 21 (B20): Continuous-time HA numerics

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance
> **Course author:** Simon Scheidegger
> **Compute tier:** `gpu-recommended` &nbsp;·&nbsp; **Time budget:** `long`

## Learning goal

Solve continuous-time Aiyagari with two methods — a finite-difference scheme on a state grid and a PINN — and compare the resulting consumption policies and stationary distributions. Build a PINN for the coupled HJB + KFE system from scratch in the exercise notebook.

## Prerequisites

- [Lecture 20 (B19)](../lecture_20_B19_continuous_time_ha_theory/README.md) — Continuous-time HA theory

## External prerequisites

- Python 3.10+ environment (`requirements.txt` at repo root, or run on the course platform).
- Familiarity with the math listed under **Script reference** below.

## Script reference

- §8.7 (Numerical methods for CT-HA)
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md) — full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf) — companion script

## Slides

- [`08_CT_Heterogeneous_Agents_Numerical.pdf`](slides/08_CT_Heterogeneous_Agents_Numerical.pdf)

## Notebooks

### Core

- [`lecture_21_B20_06_PE_Discrete_HJB_PINN.ipynb`](notebooks/core/lecture_21_B20_06_PE_Discrete_HJB_PINN.ipynb)
- [`lecture_21_B20_07_PE_Diffusion_HJB_PINN.ipynb`](notebooks/core/lecture_21_B20_07_PE_Diffusion_HJB_PINN.ipynb)
- [`lecture_21_B20_08_Aiyagari_Continuous_Time_FD_and_PINN_PyTorch.ipynb`](notebooks/core/lecture_21_B20_08_Aiyagari_Continuous_Time_FD_and_PINN_PyTorch.ipynb)

### Exercises

- [`lecture_21_B20_09_PINN_Exercise.ipynb`](notebooks/exercises/lecture_21_B20_09_PINN_Exercise.ipynb)

### Solutions

_(none in this PR)_

### Extensions

_(none in this PR)_

## Checkpoint

> Solve continuous-time Aiyagari via finite differences and PINN; compare distributions.

## Readings

- [`readings/links_by_lecture/lecture_21_B20.md`](../../readings/links_by_lecture/lecture_21_B20.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- **Previous:** [Lecture 20 (B19): Continuous-time HA theory](../lecture_20_B19_continuous_time_ha_theory/README.md)
- **Next:** [Lecture 22 (B21): Deep surrogate models](../lecture_22_B21_deep_surrogate_models/README.md)
- [Course map](../../COURSE_MAP.md)
- [Repository home](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written / graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
