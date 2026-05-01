# Lecture 03 (B02): Deep Equilibrium Nets

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance  \
> **Course author:** Simon Scheidegger  \
> **Compute tier:** `cpu-standard` &nbsp;·&nbsp; **Time budget:** `long`

## What this lecture covers

State the Deep Equilibrium Net (DEQN) idea precisely, train deterministic and stochastic Brock-Mirman DEQNs, and verify them against closed-form solutions. Handle constraints with Fischer-Burmeister complementarity, choose conditional-expectation quadrature deliberately, and compare six loss kernels (MSE, MAE, Huber, quantile, CVaR, log-cosh) on the same problem.

## Slides

- [`slides/02_DeepEquilibriumNets.pdf`](slides/02_DeepEquilibriumNets.pdf)
- [`slides/02_DeepEquilibriumNets.tex`](slides/02_DeepEquilibriumNets.tex)

## Code

- [`code/lecture_03_B02_01_Brock_Mirman_1972_DEQN.ipynb`](code/lecture_03_B02_01_Brock_Mirman_1972_DEQN.ipynb)
- [`code/lecture_03_B02_02_Brock_Mirman_Uncertainty_DEQN.ipynb`](code/lecture_03_B02_02_Brock_Mirman_Uncertainty_DEQN.ipynb)
- [`code/lecture_03_B02_03_DEQN_Exercises_Blanks.ipynb`](code/lecture_03_B02_03_DEQN_Exercises_Blanks.ipynb)
- [`code/lecture_03_B02_04_DEQN_Exercises_Solutions.ipynb`](code/lecture_03_B02_04_DEQN_Exercises_Solutions.ipynb)
- [`code/lecture_03_B02_05_StochasticBM_LossComparison.ipynb`](code/lecture_03_B02_05_StochasticBM_LossComparison.ipynb)

## Prerequisites

- [Lecture 02 (B01)](../lecture_02_B01_intro_deep_learning/README.md), Introduction to deep learning

## Script reference

- §2.1-2.4 (DEQN theory and motivation), §2.5 (Deterministic Brock-Mirman), §2.6 (Quadrature for conditional expectations), §2.4, 2.9 (Constraints and residual kernels)
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md), full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf), companion script

## Checkpoint

> Train a stochastic Brock-Mirman DEQN with Fischer-Burmeister complementarity and verify against the closed-form policy.

## Readings

- [`readings/links_by_lecture/lecture_03_B02.md`](../../readings/links_by_lecture/lecture_03_B02.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- Previous: [Lecture 02 (B01), Introduction to deep learning](../lecture_02_B01_intro_deep_learning/README.md)
- Next: [Lecture 04 (B03), IRBC with DEQNs](../lecture_04_B03_irbc_with_deqns/README.md)
- [`COURSE_MAP.md`](../../COURSE_MAP.md)
- [`README.md`](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written and graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
