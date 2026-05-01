# Lecture 05 (B04): Architecture search and loss balancing

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance  \
> **Course author:** Simon Scheidegger  \
> **Compute tier:** `gpu-recommended` &nbsp;·&nbsp; **Time budget:** `long`

## What this lecture covers

Run neural-architecture search and loss balancing systematically. Implement random search and successive halving (Hyperband) from scratch in pure Python, and compare ReLoBRaLo, SoftAdapt, and GradNorm for multi-component loss balancing on a DEQN problem.

## Slides

- [`slides/04_Neural_Architecture_Search.pdf`](slides/04_Neural_Architecture_Search.pdf)
- [`slides/04_Neural_Architecture_Search.tex`](slides/04_Neural_Architecture_Search.tex)
- [`slides/05_Loss_Normalization.pdf`](slides/05_Loss_Normalization.pdf)
- [`slides/05_Loss_Normalization.tex`](slides/05_Loss_Normalization.tex)

## Code

- [`code/lecture_05_B04_02_NAS_Random_Search_10D.ipynb`](code/lecture_05_B04_02_NAS_Random_Search_10D.ipynb)
- [`code/lecture_05_B04_03_NAS_RandomSearch_Hyperband.ipynb`](code/lecture_05_B04_03_NAS_RandomSearch_Hyperband.ipynb)
- [`code/lecture_05_B04_04_Loss_Normalization.ipynb`](code/lecture_05_B04_04_Loss_Normalization.ipynb)
- [`code/lecture_05_B04_05_IRBC_Exercise.ipynb`](code/lecture_05_B04_05_IRBC_Exercise.ipynb)

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

## Prerequisites

- [Lecture 04 (B03)](../lecture_04_B03_irbc_with_deqns/README.md), IRBC with DEQNs

## Script reference

- §Chapter 4 (Neural architecture search and loss normalization)
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md), full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf), companion script

## Checkpoint

> Run random search on a 10-D NAS problem and compare ReLoBRaLo, SoftAdapt, and GradNorm.

## Readings

- [`readings/links_by_lecture/lecture_05_B04.md`](../../readings/links_by_lecture/lecture_05_B04.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- Previous: [Lecture 04 (B03), IRBC with DEQNs](../lecture_04_B03_irbc_with_deqns/README.md)
- Next: [Lecture 06 (B05), Automatic differentiation for DEQNs](../lecture_06_B05_autodiff_for_deqns/README.md)
- [`COURSE_MAP.md`](../../COURSE_MAP.md)
- [`README.md`](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written and graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
