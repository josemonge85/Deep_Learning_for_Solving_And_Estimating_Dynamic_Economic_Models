# Lecture 12 (B11): Continuous-time heterogeneous agents, numerics

Solve continuous-time Aiyagari with two methods, a finite-difference scheme on a state grid and a PINN, then compare the resulting consumption policies and stationary distributions. Build a PINN for the coupled HJB + KFE system from scratch in the exercise notebook.

`gpu-recommended` · `long` · builds on [Lecture 11 (B10)](../lecture_11_B10_continuous_time_ha_theory/README.md)

## Slides

- [`slides/08_CT_Heterogeneous_Agents_Numerical.pdf`](slides/08_CT_Heterogeneous_Agents_Numerical.pdf)
- [`slides/08_CT_Heterogeneous_Agents_Numerical.tex`](slides/08_CT_Heterogeneous_Agents_Numerical.tex)

## Code

- [`code/lecture_12_B11_06_PE_Discrete_HJB_PINN.ipynb`](code/lecture_12_B11_06_PE_Discrete_HJB_PINN.ipynb)
- [`code/lecture_12_B11_07_PE_Diffusion_HJB_PINN.ipynb`](code/lecture_12_B11_07_PE_Diffusion_HJB_PINN.ipynb)
- [`code/lecture_12_B11_08_Aiyagari_Continuous_Time_FD_and_PINN_PyTorch.ipynb`](code/lecture_12_B11_08_Aiyagari_Continuous_Time_FD_and_PINN_PyTorch.ipynb)
- [`code/lecture_12_B11_09_PINN_Exercise.ipynb`](code/lecture_12_B11_09_PINN_Exercise.ipynb)

## In the lecture script

§8.7 (Numerical methods for CT-HA). The full chapter map is in [`script_to_lectures.md`](../../lecture_script/script_to_lectures.md).

## By the end you should

Solve continuous-time Aiyagari via finite differences and PINN, and compare distributions.

## Readings

Curated bibliography for this lecture: [`lecture_12_B11.md`](../../readings/links_by_lecture/lecture_12_B11.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).

---

← [Previous: Continuous-time heterogeneous agents, theory](../lecture_11_B10_continuous_time_ha_theory/README.md) · → [Next: Surrogates and Gaussian processes](../lecture_13_B12_surrogates_and_gps/README.md) · [Course map](../../COURSE_MAP.md)
