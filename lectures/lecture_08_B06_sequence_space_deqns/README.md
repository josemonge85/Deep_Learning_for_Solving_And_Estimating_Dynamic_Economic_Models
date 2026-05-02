# Lecture 08 (B06): Sequence-space DEQNs

A modern DEQN variant where the policy reads a long shock history instead of a current-state vector. Following Azinovic-Yang-Žemlička (2025).

`gpu-recommended` · `long` · builds on [Lecture 07 (B05)](../lecture_07_B05_autodiff_for_deqns/README.md)

> 📑 **Slides:** [06_SequenceSpace_DEQNs.pdf](slides/06_SequenceSpace_DEQNs.pdf)  
> 📓 **Notebooks:** [start here](code/lecture_07_B06_05_SequenceSpace_BrockMirman.ipynb) (4 in [`code/`](code/))  
> 📚 **Further reading:** [curated list](../../readings/links_by_lecture/lecture_08_B06.md)  
> 📖 **Script:** §6.7 (Sequence-space DEQNs)

## What this lecture covers

- **The sequence-space idea.** Replace the high-dimensional state with the last ~80 shock realizations; the network learns the residual map directly.
- **Why it generalizes.** The same template handles multi-equation systems with multiple shock channels without re-engineering the input.
- **Brock-Mirman warm-up.** Sequence-space DEQN with an 80-step shock history; verify the policy.
- **Krusell-Smith benchmark.** The same template on the canonical heterogeneous-agent benchmark.
- **Self-study extensions.** Multi-country IRBC and a borrowed JAX tutorial port (`KrusellSmith_Tutorial_CPU.ipynb`).

## Learning objectives

After this lecture you can:

- Build the shock-history input pipeline for a sequence-space DEQN.
- Train a sequence-space DEQN on Brock-Mirman with an 80-step shock history and verify the policy.
- Extend the same template to Krusell-Smith.
- Explain why sequence-space DEQNs handle multi-shock systems gracefully.

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

## Readings

Curated bibliography for this lecture: [`lecture_08_B06.md`](../../readings/links_by_lecture/lecture_08_B06.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).

---

← [Previous: Automatic differentiation for DEQNs](../lecture_07_B05_autodiff_for_deqns/README.md) · → [Next: OLG models with DEQNs](../lecture_09_B07_olg_models_deqns/README.md) · [Course map](../../COURSE_MAP.md)
