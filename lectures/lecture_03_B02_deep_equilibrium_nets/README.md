# Lecture 03 (B02): Deep Equilibrium Nets

The central method of the course. **Deep Equilibrium Nets (DEQNs)** parameterize a recursive-equilibrium policy with a neural network and train it on equilibrium-residual losses, sidestepping the curse of dimensionality.

`cpu-standard` · `long` · builds on [Lecture 02 (B01)](../lecture_02_B01_intro_deep_learning/README.md)

> 📑 **Slides:** [02_DeepEquilibriumNets.pdf](slides/02_DeepEquilibriumNets.pdf)  
> 📓 **Notebooks:** [start here](code/lecture_03_B02_01_Brock_Mirman_1972_DEQN.ipynb) (5 in [`code/`](code/))  
> 📚 **Further reading:** [curated list](../../readings/links_by_lecture/lecture_03_B02.md)  
> 📖 **Script:** §2.1-2.4 (DEQN theory and motivation), §2.5 (Deterministic Brock-Mirman), §2.6 (Quadrature for conditional expectations), §2.4, 2.9 (Constraints and residual kernels)

## What this lecture covers

- **The DEQN principle.** Why minimizing the squared norm of equilibrium residuals on a simulated state distribution recovers the policy, and how this differs from projection, value-function iteration, and perturbation.
- **Deterministic Brock-Mirman.** A hand-built DEQN on the canonical growth model, with a closed-form check.
- **Stochastic Brock-Mirman.** Adding productivity shocks and using Gauss-Hermite quadrature for the conditional expectations in the Euler equation.
- **Constraints.** Borrowing and non-negativity constraints encoded in the loss via Fischer-Burmeister complementarity.
- **Loss design.** A side-by-side comparison of six loss kernels (MSE, MAE, Huber, quantile, CVaR, log-cosh) trained on the same setup so the trade-offs become concrete.

## Learning objectives

After this lecture you can:

- State the DEQN training principle and write the residual operator for a recursive equilibrium given to you.
- Train deterministic Brock-Mirman with a DEQN and verify the policy against the closed-form solution.
- Extend the Brock-Mirman DEQN to stochastic productivity with a quadrature rule of your choice.
- Encode borrowing and non-negativity constraints with Fischer-Burmeister complementarity.
- Pick a loss kernel deliberately given the residual distribution of a model.

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

## Readings

Curated bibliography for this lecture: [`lecture_03_B02.md`](../../readings/links_by_lecture/lecture_03_B02.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).

---

| ← Previous | Next → |
|---|---|
| [**Lecture 02: Introduction to deep learning**](../lecture_02_B01_intro_deep_learning/README.md)<br><sub>MLP, LSTM, Transformer on Edgeworth cycles, double descent, Genz approximations</sub> | [**Lecture 04: IRBC with DEQNs**](../lecture_04_B03_irbc_with_deqns/README.md)<br><sub>International real business cycle with DEQNs at scale</sub> |

[↑ Course map](../../COURSE_MAP.md)
