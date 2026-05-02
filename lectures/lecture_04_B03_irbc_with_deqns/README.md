# Lecture 04 (B03): IRBC with DEQNs

The first large-scale nonlinear DSGE application of DEQNs.

`gpu-recommended` · `long` · builds on [Lecture 03 (B02)](../lecture_03_B02_deep_equilibrium_nets/README.md)

> 📑 **Slides:** [03_IRBC.pdf](slides/03_IRBC.pdf)  
> 📓 **Notebooks:** [start here](code/lecture_04_B03_01_IRBC_DEQN.ipynb)  
> 📚 **Further reading:** [curated list](../../readings/links_by_lecture/lecture_04_B03.md)  
> 📖 **Script:** §Chapter 3 (International real business cycle)

## What this lecture covers

- **The IRBC model.** N symmetric countries with capital, country-specific productivity shocks, and risk-sharing through a complete bond market; equilibrium is N Euler equations plus a world resource constraint.
- **Why DEQNs scale here.** The state space is 2N-dimensional; classical methods scale poorly with N, DEQNs do not.
- **Solution and validation.** Train the DEQN, recover the symmetric steady state, and validate the policy via Euler-equation residuals along a simulated path.
- **Comparative statics.** Read off the effect of a parameter change (e.g. doubling depreciation) directly from the trained policy.

## Learning objectives

After this lecture you can:

- Set up the IRBC residual loss on a simulated state distribution.
- Train an N-country IRBC DEQN and recover the symmetric steady state.
- Run a comparative-statics exercise and read the result from the trained policy.
- Report Euler-equation residuals as a diagnostic across the simulated state distribution.

## Slides

- [`slides/03_IRBC.pdf`](slides/03_IRBC.pdf)
- [`slides/03_IRBC.tex`](slides/03_IRBC.tex)

## Code

- [`code/lecture_04_B03_01_IRBC_DEQN.ipynb`](code/lecture_04_B03_01_IRBC_DEQN.ipynb)

## Figures

- [`figures/irbc_4approach_loss.pdf`](figures/irbc_4approach_loss.pdf)
- [`figures/irbc_4approach_loss.png`](figures/irbc_4approach_loss.png)

## In the lecture script

§Chapter 3 (International real business cycle). The full chapter map is in [`script_to_lectures.md`](../../lecture_script/script_to_lectures.md).

## Readings

Curated bibliography for this lecture: [`lecture_04_B03.md`](../../readings/links_by_lecture/lecture_04_B03.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).

---

← [Previous: Deep Equilibrium Nets](../lecture_03_B02_deep_equilibrium_nets/README.md) · → [Next: Architecture search and loss balancing](../lecture_05_B04_nas_loss_normalization/README.md) · [Course map](../../COURSE_MAP.md)
