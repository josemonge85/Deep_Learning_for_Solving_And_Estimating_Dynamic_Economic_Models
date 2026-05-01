# Lecture 12 (B11): Continuous-time heterogeneous agents, numerics

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance
> **Course author:** Simon Scheidegger
> **Compute tier:** `gpu-recommended` &nbsp;·&nbsp; **Time budget:** `long`

## Learning goal

Solve continuous-time Aiyagari with two methods, a finite-difference scheme on a state grid and a PINN, then compare the resulting consumption policies and stationary distributions. Build a PINN for the coupled HJB + KFE system from scratch in the exercise notebook.

## Prerequisites

- [Lecture 11 (B10)](../lecture_11_B10_continuous_time_ha_theory/README.md), Continuous-time heterogeneous agents, theory

## External prerequisites

- Python 3.10+ environment (`requirements.txt` at repo root, or run on the course platform).
- Familiarity with the math listed under **Script reference** below.

## Script reference

- §8.7 (Numerical methods for CT-HA)
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md), full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf), companion script

## Slides

- [`08_CT_Heterogeneous_Agents_Numerical.pdf`](slides/08_CT_Heterogeneous_Agents_Numerical.pdf)

## Notebooks

### Core

- [`lecture_12_B11_06_PE_Discrete_HJB_PINN.ipynb`](notebooks/core/lecture_12_B11_06_PE_Discrete_HJB_PINN.ipynb)
- [`lecture_12_B11_07_PE_Diffusion_HJB_PINN.ipynb`](notebooks/core/lecture_12_B11_07_PE_Diffusion_HJB_PINN.ipynb)
- [`lecture_12_B11_08_Aiyagari_Continuous_Time_FD_and_PINN_PyTorch.ipynb`](notebooks/core/lecture_12_B11_08_Aiyagari_Continuous_Time_FD_and_PINN_PyTorch.ipynb)

### Exercises

- [`lecture_12_B11_09_PINN_Exercise.ipynb`](notebooks/exercises/lecture_12_B11_09_PINN_Exercise.ipynb)

### Solutions

_(none)_

### Extensions

_(none)_

## Checkpoint

> Solve continuous-time Aiyagari via finite differences and PINN, and compare distributions.

## Readings

- [`readings/links_by_lecture/lecture_12_B11.md`](../../readings/links_by_lecture/lecture_12_B11.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- Previous: [Lecture 11 (B10), Continuous-time heterogeneous agents, theory](../lecture_11_B10_continuous_time_ha_theory/README.md)
- Next: [Lecture 13 (B12), Surrogates and Gaussian processes](../lecture_13_B12_surrogates_and_gps/README.md)
- [`COURSE_MAP.md`](../../COURSE_MAP.md)
- [`README.md`](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written and graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
