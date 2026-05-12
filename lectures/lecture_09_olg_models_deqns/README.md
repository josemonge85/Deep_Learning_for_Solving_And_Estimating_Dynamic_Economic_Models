# Lecture 09: OLG models with DEQNs

Overlapping-generations (OLG) models with DEQNs, at two scales.

`gpu-recommended` · `long` · builds on [Lecture 07](../lecture_07_autodiff_for_deqns/README.md)

> 📑 **Slides:** [lecture_09_olg_models_deqns.pdf](slides/lecture_09_olg_models_deqns.pdf)  
> 📓 **Notebooks:** [start here](code/lecture_09_08_OLG_Analytic_DEQN_persistent.ipynb) (5 in [`code/`](code/))  
> 📚 **Further reading:** [curated list](../../readings/links_by_lecture/lecture_09.md)  
> 📖 **Script:** §5.1-5.5 (OLG with DEQNs), §5.6 (Large OLG benchmark)

## What this lecture covers

- **Cohort structure.** One Euler equation per cohort, stacked into a single Lagrangian primitive; the DEQN training principle does not change.
- **Analytic small OLG.** A closed-form lifecycle savings model used as a sanity check on the DEQN solution.
- **The 56-period benchmark.** The standard production-scale OLG model with borrowing constraints.
- **Borrowing constraints.** Product-form KKT complementarity used cohort-by-cohort to handle the inequalities (softplus heads for non-negativity, squared product residuals `(λ·k')²` in the loss).
- **Diagnostics.** Lifecycle profiles, aggregate dynamics, and equilibrium residuals across cohorts.

## Learning objectives

After this lecture you can:

- Write the cohort-stacked Lagrangian for an OLG DEQN.
- Train an analytic small-OLG DEQN and verify lifecycle savings against the closed form.
- Reproduce the 56-period OLG benchmark with borrowing and collateral constraints via product-form KKT residuals.
- Read off lifecycle profiles, aggregate dynamics, and equilibrium residuals across cohorts.

## Slides

- [`slides/lecture_09_olg_models_deqns.pdf`](slides/lecture_09_olg_models_deqns.pdf)
- [`slides/lecture_09_olg_models_deqns.tex`](slides/lecture_09_olg_models_deqns.tex)

## Code

**Analytic 6-agent OLG** — closed-form validation target.
- [`code/lecture_09_08_OLG_Analytic_DEQN_persistent.ipynb`](code/lecture_09_08_OLG_Analytic_DEQN_persistent.ipynb) — primary classroom variant: persistent-simulation training, validation against the Krueger–Kübler closed-form savings rates.
- [`code/lecture_09_07_OLG_Analytic_DEQN_exogenous.ipynb`](code/lecture_09_07_OLG_Analytic_DEQN_exogenous.ipynb) — feedback-free ablation: training cloud drawn from broad exogenous boxes.

**Benchmark 56-agent OLG** — Azinovic–Gaegauf–Scheidegger (2022) production scale.
- [`code/lecture_09_10_OLG_Benchmark_DEQN_persistent.ipynb`](code/lecture_09_10_OLG_Benchmark_DEQN_persistent.ipynb) — primary classroom variant: persistent-simulation training on the model's ergodic set.
- [`code/lecture_09_09_OLG_Benchmark_DEQN_exogenous.ipynb`](code/lecture_09_09_OLG_Benchmark_DEQN_exogenous.ipynb) — feedback-free ablation: training cloud drawn from broad exogenous boxes.

**Student exercise.**
- [`code/lecture_09_11_OLG_Exercise.ipynb`](code/lecture_09_11_OLG_Exercise.ipynb)

## In the lecture script

§5.1-5.5 (OLG with DEQNs), §5.6 (Large OLG benchmark). The full chapter map is in [`script_to_lectures.md`](../../lecture_script/script_to_lectures.md).

## Readings

Curated bibliography for this lecture: [`lecture_09.md`](../../readings/links_by_lecture/lecture_09.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).

---

| ← Previous | Next → |
|---|---|
| [**Lecture 08: Sequence-space DEQNs**](../lecture_08_sequence_space_deqns/README.md)<br><sub>Brock-Mirman, IRBC, Krusell-Smith with shock-history inputs</sub> | [**Lecture 10: Heterogeneous agents and Young's method**](../lecture_10_heterogeneous_agents_youngs_method/README.md)<br><sub>Young's histogram, Krusell-Smith, continuum-of-agents DEQN</sub> |

[↑ Course map](../../COURSE_MAP.md)
