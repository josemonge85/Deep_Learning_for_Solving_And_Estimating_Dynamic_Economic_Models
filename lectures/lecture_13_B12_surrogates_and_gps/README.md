# Lecture 13 (B12): Surrogates and Gaussian processes

A toolkit of cheap, differentiable approximations for expensive simulators: deep surrogates, Gaussian processes, active subspaces, and GP value-function iteration.

`gpu-recommended` · `long` · builds on [Lecture 02 (B01)](../lecture_02_B01_intro_deep_learning/README.md)

## What this lecture covers

- **Deep surrogate models.** A neural network trained on simulator input-output pairs; when the surrogate pays for itself over direct simulation.
- **Gaussian processes.** GP regression with built-in uncertainty quantification; the basis for Bayesian active learning.
- **Bayesian active learning (BAL).** Choose the next training point to maximize information gain rather than throwing samples at a hypercube.
- **Active subspaces.** Linear and nonlinear dimension reduction so GPs scale to higher input dimensions.
- **Deep kernel learning.** Combining a neural feature map with a GP kernel for the same scaling goal.
- **GP value-function iteration.** GPs inside the VFI loop as a competitor to DEQN-VFI.

## Learning objectives

After this lecture you can:

- Train a deep surrogate on a controlled test problem and validate it out-of-sample.
- Fit a GP regressor and run a Bayesian active-learning loop.
- Apply linear and nonlinear active subspaces to a 10-D test function.
- Run GP-VFI on a 2-D test economy and reach a stable value function.
- Pick a surrogate vs GP vs deep-kernel approach for a new problem.

## Slides

- [`slides/07_Surrogates_and_GPs.pdf`](slides/07_Surrogates_and_GPs.pdf)
- [`slides/07_Surrogates_and_GPs.tex`](slides/07_Surrogates_and_GPs.tex)
- [`slides/gp_active_learning.pdf`](slides/gp_active_learning.pdf)

## Code

- [`code/lecture_13_B12_01_Surrogate_Primer.ipynb`](code/lecture_13_B12_01_Surrogate_Primer.ipynb)
- [`code/lecture_13_B12_02_GP_and_BAL.ipynb`](code/lecture_13_B12_02_GP_and_BAL.ipynb)
- [`code/lecture_13_B12_04_GP_Value_Function_Iteration.ipynb`](code/lecture_13_B12_04_GP_Value_Function_Iteration.ipynb)
- [`code/lecture_13_B12_05_Active_Subspace_2D.ipynb`](code/lecture_13_B12_05_Active_Subspace_2D.ipynb)
- [`code/lecture_13_B12_06_Active_Subspace_10D.ipynb`](code/lecture_13_B12_06_Active_Subspace_10D.ipynb)
- [`code/lecture_13_B12_07_Active_Subspace_Nonlinear.ipynb`](code/lecture_13_B12_07_Active_Subspace_Nonlinear.ipynb)
- [`code/lecture_13_B12_08_Deep_Kernel_Learning.ipynb`](code/lecture_13_B12_08_Deep_Kernel_Learning.ipynb)
- [`code/lecture_13_B12_09_Deep_Active_Subspace_Ridge.ipynb`](code/lecture_13_B12_09_Deep_Active_Subspace_Ridge.ipynb)
- [`code/lecture_13_B12_10_Deep_AS_vs_Linear_AS_Borehole.ipynb`](code/lecture_13_B12_10_Deep_AS_vs_Linear_AS_Borehole.ipynb)

## In the lecture script

§9.1-9.2 (Deep surrogates), §9.3-9.6 (GPs and Bayesian active learning), §9.7 (Active subspaces), §9.8 (GP value-function iteration), §9.9 (Deep kernels), §9.10 (GPs among Bayesian cousins). The full chapter map is in [`script_to_lectures.md`](../../lecture_script/script_to_lectures.md).

## Readings

Curated bibliography for this lecture: [`lecture_13_B12.md`](../../readings/links_by_lecture/lecture_13_B12.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).

---

← [Previous: Continuous-time heterogeneous agents, numerics](../lecture_12_B11_continuous_time_ha_numerics/README.md) · → [Next: Structural estimation via SMM](../lecture_14_B13_structural_estimation_smm/README.md) · [Course map](../../COURSE_MAP.md)
