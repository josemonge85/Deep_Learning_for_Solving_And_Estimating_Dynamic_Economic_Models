# Lecture 03 (B02): Deep Equilibrium Nets

State the Deep Equilibrium Net (DEQN) idea precisely, train deterministic and stochastic Brock-Mirman DEQNs, and verify them against closed-form solutions. Handle constraints with Fischer-Burmeister complementarity, choose conditional-expectation quadrature deliberately, and compare six loss kernels (MSE, MAE, Huber, quantile, CVaR, log-cosh) on the same problem.

`cpu-standard` · `long` · builds on [Lecture 02 (B01)](../lecture_02_B01_intro_deep_learning/README.md)

## Slides

- [`slides/02_DeepEquilibriumNets.pdf`](slides/02_DeepEquilibriumNets.pdf)
- [`slides/02_DeepEquilibriumNets.tex`](slides/02_DeepEquilibriumNets.tex)

## Code

- [`code/lecture_03_B02_01_Brock_Mirman_1972_DEQN.ipynb`](code/lecture_03_B02_01_Brock_Mirman_1972_DEQN.ipynb)
- [`code/lecture_03_B02_02_Brock_Mirman_Uncertainty_DEQN.ipynb`](code/lecture_03_B02_02_Brock_Mirman_Uncertainty_DEQN.ipynb)
- [`code/lecture_03_B02_03_DEQN_Exercises_Blanks.ipynb`](code/lecture_03_B02_03_DEQN_Exercises_Blanks.ipynb)
- [`code/lecture_03_B02_04_DEQN_Exercises_Solutions.ipynb`](code/lecture_03_B02_04_DEQN_Exercises_Solutions.ipynb)
- [`code/lecture_03_B02_05_StochasticBM_LossComparison.ipynb`](code/lecture_03_B02_05_StochasticBM_LossComparison.ipynb)

## In the lecture script

§2.1-2.4 (DEQN theory and motivation), §2.5 (Deterministic Brock-Mirman), §2.6 (Quadrature for conditional expectations), §2.4, 2.9 (Constraints and residual kernels). The full chapter map is in [`script_to_lectures.md`](../../lecture_script/script_to_lectures.md).

## By the end you should

Train a stochastic Brock-Mirman DEQN with Fischer-Burmeister complementarity and verify against the closed-form policy.

## Readings

Curated bibliography for this lecture: [`lecture_03_B02.md`](../../readings/links_by_lecture/lecture_03_B02.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).

---

← [Previous: Introduction to deep learning](../lecture_02_B01_intro_deep_learning/README.md) · → [Next: IRBC with DEQNs](../lecture_04_B03_irbc_with_deqns/README.md) · [Course map](../../COURSE_MAP.md)
