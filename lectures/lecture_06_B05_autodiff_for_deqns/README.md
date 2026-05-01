# Lecture 06 (B05): Automatic differentiation for DEQNs

Master the autodiff machinery that DEQN training depends on. Derive a Lagrangian primitive analytically and recover its gradient with two `tf.GradientTape` (or equivalent) calls per Euler equation. Cross-check the autodiff residual against a hand-derived residual to machine precision.

`cpu-standard` · `standard` · builds on [Lecture 03 (B02)](../lecture_03_B02_deep_equilibrium_nets/README.md)

## Slides

- [`slides/05b_AutoDiff_for_DEQN.pdf`](slides/05b_AutoDiff_for_DEQN.pdf)
- [`slides/05b_AutoDiff_for_DEQN.tex`](slides/05b_AutoDiff_for_DEQN.tex)

## Code

- [`code/lecture_06_B05_01_AutoDiff_Analytical_Examples.ipynb`](code/lecture_06_B05_01_AutoDiff_Analytical_Examples.ipynb)
- [`code/lecture_06_B05_02_Brock_Mirman_AutoDiff_DEQN.ipynb`](code/lecture_06_B05_02_Brock_Mirman_AutoDiff_DEQN.ipynb)
- [`code/lecture_06_B05_03_Brock_Mirman_Uncertainty_AutoDiff_DEQN.ipynb`](code/lecture_06_B05_03_Brock_Mirman_Uncertainty_AutoDiff_DEQN.ipynb)
- [`code/lecture_06_B05_04_IRBC_AutoDiff_DEQN.ipynb`](code/lecture_06_B05_04_IRBC_AutoDiff_DEQN.ipynb)

## In the lecture script

§2.7 (Automatic differentiation), §Appendix B (Matrix calculus). The full chapter map is in [`script_to_lectures.md`](../../lecture_script/script_to_lectures.md).

## By the end you should

Derive a Lagrangian primitive analytically and recover its gradient via two-tape autodiff.

## Readings

Curated bibliography for this lecture: [`lecture_06_B05.md`](../../readings/links_by_lecture/lecture_06_B05.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).

---

← [Previous: Architecture search and loss balancing](../lecture_05_B04_nas_loss_normalization/README.md) · → [Next: Sequence-space DEQNs](../lecture_07_B06_sequence_space_deqns/README.md) · [Course map](../../COURSE_MAP.md)
