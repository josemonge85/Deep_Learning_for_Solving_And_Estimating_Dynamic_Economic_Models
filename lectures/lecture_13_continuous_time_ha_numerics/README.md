# Lecture 13: Continuous-time heterogeneous agents, numerics

Two methods to solve the HJB-KFE system numerically: a finite-difference scheme on a grid, and a PINN.

`gpu-recommended` · `long` · builds on [Lecture 12](../lecture_12_continuous_time_ha_theory/README.md)

> 📑 **Slides:** [lecture_13_continuous_time_ha_numerics.pdf](slides/lecture_13_continuous_time_ha_numerics.pdf)  
> 📓 **Notebooks:** [start here](code/lecture_13_06_PE_Discrete_HJB_PINN.ipynb) (4 in [`code/`](code/))  
> 📚 **Further reading:** [curated list](../../readings/links_by_lecture/lecture_13.md)  
> 📖 **Script:** §8.7 (Numerical methods for CT-HA)

## What this lecture covers

- **Upwind finite-difference.** The Achdou-Han-Lasry-Lions-Moll scheme for HJB on a state grid, paired with the KFE solver on the same grid.
- **Continuous-time Aiyagari.** The running example for both methods.
- **A PINN for the coupled system.** Built from scratch; both equations as residual losses on shared collocation points.
- **Side-by-side comparison.** Consumption policies and stationary distributions across the two methods.
- **Method choice.** When to reach for finite-difference vs PINN as state dimensionality grows.

## Learning objectives

After this lecture you can:

- Implement an upwind finite-difference solver for the Aiyagari HJB-KFE system.
- Build a PINN for the coupled HJB-KFE system from scratch.
- Compare consumption policies and stationary distributions across the two methods.
- Diagnose convergence on each method and choose between them for a new problem.

## Slides

- [`slides/lecture_13_continuous_time_ha_numerics.pdf`](slides/lecture_13_continuous_time_ha_numerics.pdf)
- [`slides/lecture_13_continuous_time_ha_numerics.tex`](slides/lecture_13_continuous_time_ha_numerics.tex)

## Code

- [`code/lecture_13_06_PE_Discrete_HJB_PINN.ipynb`](code/lecture_13_06_PE_Discrete_HJB_PINN.ipynb)
- [`code/lecture_13_07_PE_Diffusion_HJB_PINN.ipynb`](code/lecture_13_07_PE_Diffusion_HJB_PINN.ipynb)
- [`code/lecture_13_08_Aiyagari_Continuous_Time_FD_and_PINN_PyTorch.ipynb`](code/lecture_13_08_Aiyagari_Continuous_Time_FD_and_PINN_PyTorch.ipynb)
- [`code/lecture_13_09_PINN_Exercise.ipynb`](code/lecture_13_09_PINN_Exercise.ipynb)

## In the lecture script

§8.7 (Numerical methods for CT-HA). The full chapter map is in [`script_to_lectures.md`](../../lecture_script/script_to_lectures.md).

## Readings

Curated bibliography for this lecture: [`lecture_13.md`](../../readings/links_by_lecture/lecture_13.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).

---

| ← Previous | Next → |
|---|---|
| [**Lecture 12: Continuous-time HA, theory**](../lecture_12_continuous_time_ha_theory/README.md)<br><sub>HJB, Kolmogorov-forward, master equation, Ito calculus</sub> | [**Lecture 14: Surrogates and Gaussian processes**](../lecture_14_surrogates_and_gps/README.md)<br><sub>Surrogate primer, GP regression, Bayesian active learning, active subspaces, deep kernel learning, GP-VFI</sub> |

[↑ Course map](../../COURSE_MAP.md)
