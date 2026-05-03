# Lecture 09 (B07): OLG models with DEQNs

Overlapping-generations (OLG) models with DEQNs, at two scales.

`gpu-recommended` · `long` · builds on [Lecture 07 (B05)](../lecture_07_B05_autodiff_for_deqns/README.md)

> 📑 **Slides:** [07_OLG_Models_DEQNs.pdf](slides/07_OLG_Models_DEQNs.pdf)  
> 📓 **Notebooks:** [start here](code/lecture_09_B07_07_OLG_Analytic_DEQN.ipynb) (3 in [`code/`](code/))  
> 📚 **Further reading:** [curated list](../../readings/links_by_lecture/lecture_09_B07.md)  
> 📖 **Script:** §5.1-5.5 (OLG with DEQNs), §5.6 (Large OLG benchmark)

## What this lecture covers

- **Cohort structure.** One Euler equation per cohort, stacked into a single Lagrangian primitive; the DEQN training principle does not change.
- **Analytic small OLG.** A closed-form lifecycle savings model used as a sanity check on the DEQN solution.
- **The 56-period benchmark.** The standard production-scale OLG model with borrowing constraints.
- **Borrowing constraints.** Fischer-Burmeister complementarity used cohort-by-cohort to handle the inequality.
- **Diagnostics.** Lifecycle profiles, aggregate dynamics, and equilibrium residuals across cohorts.

## Learning objectives

After this lecture you can:

- Write the cohort-stacked Lagrangian for an OLG DEQN.
- Train an analytic small-OLG DEQN and verify lifecycle savings against the closed form.
- Reproduce the 56-period OLG benchmark with borrowing constraints via Fischer-Burmeister.
- Read off lifecycle profiles, aggregate dynamics, and equilibrium residuals across cohorts.

## Slides

- [`slides/07_OLG_Models_DEQNs.pdf`](slides/07_OLG_Models_DEQNs.pdf)
- [`slides/07_OLG_Models_DEQNs.tex`](slides/07_OLG_Models_DEQNs.tex)

## Code

- [`code/lecture_09_B07_07_OLG_Analytic_DEQN.ipynb`](code/lecture_09_B07_07_OLG_Analytic_DEQN.ipynb)
- [`code/lecture_09_B07_08_OLG_Benchmark_DEQN.ipynb`](code/lecture_09_B07_08_OLG_Benchmark_DEQN.ipynb)
- [`code/lecture_09_B07_09_OLG_Exercise.ipynb`](code/lecture_09_B07_09_OLG_Exercise.ipynb)

## In the lecture script

§5.1-5.5 (OLG with DEQNs), §5.6 (Large OLG benchmark). The full chapter map is in [`script_to_lectures.md`](../../lecture_script/script_to_lectures.md).

## Readings

Curated bibliography for this lecture: [`lecture_09_B07.md`](../../readings/links_by_lecture/lecture_09_B07.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).

---

| ← Previous | Next → |
|---|---|
| [**Lecture 08: Sequence-space DEQNs**](../lecture_08_B06_sequence_space_deqns/README.md)<br><sub>Brock-Mirman, IRBC, Krusell-Smith with shock-history inputs</sub> | [**Lecture 10: Heterogeneous agents and Young's method**](../lecture_10_B08_heterogeneous_agents_youngs_method/README.md)<br><sub>Young's histogram, Krusell-Smith, continuum-of-agents DEQN</sub> |

[↑ Course map](../../COURSE_MAP.md)
