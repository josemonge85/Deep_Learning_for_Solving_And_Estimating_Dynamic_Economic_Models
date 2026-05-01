# Lecture 10 (B09): Physics-informed neural networks

Build PINNs (physics-informed neural networks) that solve ODEs and economic PDEs by minimizing the PDE residual on collocation points. Distinguish soft and hard boundary-condition parametrizations, solve a 2-D Poisson PDE, then apply the same template to the cake-eating HJB and to Black-Scholes option pricing.

`cpu-standard` · `long` · builds on [Lecture 06 (B05)](../lecture_06_B05_autodiff_for_deqns/README.md)

## Slides

- [`slides/06_PINNs.pdf`](slides/06_PINNs.pdf)
- [`slides/06_PINNs.tex`](slides/06_PINNs.tex)

## Code

- [`code/lecture_10_B09_01_ODE_PINN_ZeroBCs.ipynb`](code/lecture_10_B09_01_ODE_PINN_ZeroBCs.ipynb)
- [`code/lecture_10_B09_02_ODE_PINN_SoftVsHardBCs.ipynb`](code/lecture_10_B09_02_ODE_PINN_SoftVsHardBCs.ipynb)
- [`code/lecture_10_B09_03_PDE_PINN_Poisson2D.ipynb`](code/lecture_10_B09_03_PDE_PINN_Poisson2D.ipynb)
- [`code/lecture_10_B09_04_Cake_Eating_HJB_PINN.ipynb`](code/lecture_10_B09_04_Cake_Eating_HJB_PINN.ipynb)
- [`code/lecture_10_B09_05_Black_Scholes_PINN.ipynb`](code/lecture_10_B09_05_Black_Scholes_PINN.ipynb)

## In the lecture script

§7.1-7.4 (PINN foundations), §7.5-7.9 (Economic PDEs (HJB, Black-Scholes)). The full chapter map is in [`script_to_lectures.md`](../../lecture_script/script_to_lectures.md).

## By the end you should

Solve a 2-D Poisson PDE with a PINN; price a European call via Black-Scholes PINN.

## Readings

Curated bibliography for this lecture: [`lecture_10_B09.md`](../../readings/links_by_lecture/lecture_10_B09.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).

---

← [Previous: Heterogeneous agents and Young's method](../lecture_09_B08_heterogeneous_agents_youngs_method/README.md) · → [Next: Continuous-time heterogeneous agents, theory](../lecture_11_B10_continuous_time_ha_theory/README.md) · [Course map](../../COURSE_MAP.md)
