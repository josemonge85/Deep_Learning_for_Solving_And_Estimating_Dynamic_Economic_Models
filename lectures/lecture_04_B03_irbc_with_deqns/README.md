# Lecture 04 (B03): IRBC with DEQNs

Solve a multi-country International Real Business Cycle (IRBC) model with DEQNs. Recover the symmetric steady state, run a comparative-statics exercise (e.g. doubling depreciation), and report Euler-equation residuals across the simulated state distribution.

`gpu-recommended` · `long` · builds on [Lecture 03 (B02)](../lecture_03_B02_deep_equilibrium_nets/README.md)

## Slides

- [`slides/03_IRBC.pdf`](slides/03_IRBC.pdf)
- [`slides/03_IRBC.tex`](slides/03_IRBC.tex)

## Code

- [`code/lecture_04_B03_01_IRBC_DEQN.ipynb`](code/lecture_04_B03_01_IRBC_DEQN.ipynb)

## Figures

- [`figures/irbc_4approach_loss.pdf`](figures/irbc_4approach_loss.pdf)
- [`figures/irbc_4approach_loss.png`](figures/irbc_4approach_loss.png)
- [`figures/loss_norm_T_sensitivity.pdf`](figures/loss_norm_T_sensitivity.pdf)
- [`figures/loss_norm_T_sensitivity.png`](figures/loss_norm_T_sensitivity.png)
- [`figures/loss_norm_equal_errmap.pdf`](figures/loss_norm_equal_errmap.pdf)
- [`figures/loss_norm_equal_errmap.png`](figures/loss_norm_equal_errmap.png)
- [`figures/loss_norm_equal_weights.pdf`](figures/loss_norm_equal_weights.pdf)
- [`figures/loss_norm_equal_weights.png`](figures/loss_norm_equal_weights.png)
- [`figures/loss_norm_method_comparison.pdf`](figures/loss_norm_method_comparison.pdf)
- [`figures/loss_norm_method_comparison.png`](figures/loss_norm_method_comparison.png)
- [`figures/loss_norm_relobralo_errmap.pdf`](figures/loss_norm_relobralo_errmap.pdf)
- [`figures/loss_norm_relobralo_errmap.png`](figures/loss_norm_relobralo_errmap.png)
- [`figures/loss_norm_relobralo_weights.pdf`](figures/loss_norm_relobralo_weights.pdf)
- [`figures/loss_norm_relobralo_weights.png`](figures/loss_norm_relobralo_weights.png)
- [`figures/nas_best_surface.pdf`](figures/nas_best_surface.pdf)
- [`figures/nas_best_surface.png`](figures/nas_best_surface.png)
- [`figures/nas_random_search.pdf`](figures/nas_random_search.pdf)
- [`figures/nas_random_search.png`](figures/nas_random_search.png)
- [`figures/nas_search_results.pdf`](figures/nas_search_results.pdf)
- [`figures/nas_search_results.png`](figures/nas_search_results.png)

## In the lecture script

§Chapter 3 (International real business cycle). The full chapter map is in [`script_to_lectures.md`](../../lecture_script/script_to_lectures.md).

## By the end you should

Train an N-country IRBC DEQN and reproduce the symmetric steady state.

## Readings

Curated bibliography for this lecture: [`lecture_04_B03.md`](../../readings/links_by_lecture/lecture_04_B03.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).

---

← [Previous: Deep Equilibrium Nets](../lecture_03_B02_deep_equilibrium_nets/README.md) · → [Next: Architecture search and loss balancing](../lecture_05_B04_nas_loss_normalization/README.md) · [Course map](../../COURSE_MAP.md)
