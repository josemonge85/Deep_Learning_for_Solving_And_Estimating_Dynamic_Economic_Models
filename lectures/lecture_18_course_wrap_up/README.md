# Lecture 18: Course wrap-up

Synthesis of the course: when to choose which method, and where the literature is moving.

`cpu-light` · `short` · builds on [Lecture 17](../lecture_17_deep_uq_pareto_improving_policy/README.md)

> 📑 **Slides:** [lecture_18_wrap_up.pdf](slides/lecture_18_wrap_up.pdf)  
> 📚 **Further reading:** [curated list](../../readings/links_by_lecture/lecture_18.md)  
> 📖 **Script:** §Chapter 12 (Synthesis and method choice), §Appendix A (Glossary), §Appendix D (Fixed points and Bellman)

## What this lecture covers

- **Method-choice matrix.** DEQN vs PINN vs surrogate-plus-GP vs deep UQ, indexed by state dimensionality, smoothness, presence of constraints, and need for uncertainty quantification.
- **The trade-offs.** Compute, sample efficiency, interpretability, and what each method gives up to scale.
- **Open frontiers.** Active subspaces in higher dimensions; sequence-space architectures for HA; deep-UQ at the frontier of climate-economic policy.
- **Where to go next.** Pointers into the script's bibliography for further self-study.

## Learning objectives

After this lecture you can:

- Articulate when to choose DEQN, PINN, GP, or surrogate methods for a new problem.
- Explain the trade-offs each method faces (compute, smoothness, dimensionality, uncertainty quantification).
- Identify research frontiers and open problems in computational and quantitative economics.

## Slides

- [`slides/lecture_18_wrap_up.pdf`](slides/lecture_18_wrap_up.pdf)
- [`slides/lecture_18_wrap_up.tex`](slides/lecture_18_wrap_up.tex)

## Code

_(none)_

## In the lecture script

§Chapter 12 (Synthesis and method choice), §Appendix A (Glossary), §Appendix D (Fixed points and Bellman). The full chapter map is in [`script_to_lectures.md`](../../lecture_script/script_to_lectures.md).

## Readings

Curated bibliography for this lecture: [`lecture_18.md`](../../readings/links_by_lecture/lecture_18.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).

---

| ← Previous | Next → |
|---|---|
| [**Lecture 17: Deep UQ and Pareto-improving carbon-tax design**](../lecture_17_deep_uq_pareto_improving_policy/README.md)<br><sub>GP surrogates, Bayesian active learning, Sobol / Shapley, constrained Pareto-improving rules</sub> | &nbsp; |

[↑ Course map](../../COURSE_MAP.md)
