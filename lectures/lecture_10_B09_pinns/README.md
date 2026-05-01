# Lecture 10 (B09): Physics-informed neural networks

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance
> **Course author:** Simon Scheidegger
> **Compute tier:** `cpu-standard` &nbsp;·&nbsp; **Time budget:** `long`

## Learning goal

Build PINNs (physics-informed neural networks) that solve ODEs and economic PDEs by minimizing the PDE residual on collocation points. Distinguish soft and hard boundary-condition parametrizations, solve a 2-D Poisson PDE, then apply the same template to the cake-eating HJB and to Black-Scholes option pricing.

## Prerequisites

- [Lecture 06 (B05)](../lecture_06_B05_autodiff_for_deqns/README.md), Automatic differentiation for DEQNs

## External prerequisites

- Python 3.10+ environment (`requirements.txt` at repo root, or run on the course platform).
- Familiarity with the math listed under **Script reference** below.

## Script reference

- §7.1-7.4 (PINN foundations), §7.5-7.9 (Economic PDEs (HJB, Black-Scholes))
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md), full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf), companion script

## Slides

- [`06_PINNs.pdf`](slides/06_PINNs.pdf)

## Notebooks

### Core

- [`lecture_10_B09_01_ODE_PINN_ZeroBCs.ipynb`](notebooks/core/lecture_10_B09_01_ODE_PINN_ZeroBCs.ipynb)
- [`lecture_10_B09_02_ODE_PINN_SoftVsHardBCs.ipynb`](notebooks/core/lecture_10_B09_02_ODE_PINN_SoftVsHardBCs.ipynb)
- [`lecture_10_B09_03_PDE_PINN_Poisson2D.ipynb`](notebooks/core/lecture_10_B09_03_PDE_PINN_Poisson2D.ipynb)
- [`lecture_10_B09_04_Cake_Eating_HJB_PINN.ipynb`](notebooks/core/lecture_10_B09_04_Cake_Eating_HJB_PINN.ipynb)
- [`lecture_10_B09_05_Black_Scholes_PINN.ipynb`](notebooks/core/lecture_10_B09_05_Black_Scholes_PINN.ipynb)

### Exercises

_(none)_

### Solutions

_(none)_

### Extensions

_(none)_

## Checkpoint

> Solve a 2-D Poisson PDE with a PINN; price a European call via Black-Scholes PINN.

## Readings

- [`readings/links_by_lecture/lecture_10_B09.md`](../../readings/links_by_lecture/lecture_10_B09.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- Previous: [Lecture 09 (B08), Heterogeneous agents and Young's method](../lecture_09_B08_heterogeneous_agents_youngs_method/README.md)
- Next: [Lecture 11 (B10), Continuous-time heterogeneous agents, theory](../lecture_11_B10_continuous_time_ha_theory/README.md)
- [`COURSE_MAP.md`](../../COURSE_MAP.md)
- [`README.md`](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written and graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
