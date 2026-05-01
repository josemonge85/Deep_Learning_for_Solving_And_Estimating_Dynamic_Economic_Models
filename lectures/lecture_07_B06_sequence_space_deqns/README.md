# Lecture 07 (B06): Sequence-space DEQNs

Train sequence-space DEQNs that use a long shock history (~80 steps) instead of the current-state vector as input. Reproduce the Brock-Mirman warm-up and the Krusell-Smith benchmark in sequence space, and understand why the sequence-space template generalizes to multi-equation systems with multiple shock channels.

`gpu-recommended` · `long` · builds on [Lecture 06 (B05)](../lecture_06_B05_autodiff_for_deqns/README.md)

## Slides

- [`slides/06_SequenceSpace_DEQNs.pdf`](slides/06_SequenceSpace_DEQNs.pdf)
- [`slides/06_SequenceSpace_DEQNs.tex`](slides/06_SequenceSpace_DEQNs.tex)

## Code

- [`code/lecture_07_B06_05_SequenceSpace_BrockMirman.ipynb`](code/lecture_07_B06_05_SequenceSpace_BrockMirman.ipynb)
- [`code/lecture_07_B06_05b_SequenceSpace_IRBC.ipynb`](code/lecture_07_B06_05b_SequenceSpace_IRBC.ipynb)
- [`code/lecture_07_B06_06_SequenceSpace_KrusellSmith.ipynb`](code/lecture_07_B06_06_SequenceSpace_KrusellSmith.ipynb)
- [`code/lecture_07_B06_KrusellSmith_Tutorial_CPU.ipynb`](code/lecture_07_B06_KrusellSmith_Tutorial_CPU.ipynb)

## In the lecture script

§6.7 (Sequence-space DEQNs). The full chapter map is in [`script_to_lectures.md`](../../lecture_script/script_to_lectures.md).

## By the end you should

Train a sequence-space DEQN on Brock-Mirman with an 80-step shock history.

## Readings

Curated bibliography for this lecture: [`lecture_07_B06.md`](../../readings/links_by_lecture/lecture_07_B06.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).

---

← [Previous: Automatic differentiation for DEQNs](../lecture_06_B05_autodiff_for_deqns/README.md) · → [Next: OLG models with DEQNs](../lecture_08_B07_olg_models_deqns/README.md) · [Course map](../../COURSE_MAP.md)
