# Lecture 16 (B15): Deep uncertainty quantification and Pareto-improving climate policy

Stochastic IAMs depend on parameters whose true values are deeply uncertain. Plugging point estimates in, or averaging the uncertainty out, is misleading. This lecture builds a complete pipeline for taking that uncertainty seriously and turning it into a defensible policy menu.

`gpu-recommended` · `long` · builds on [Lecture 15 (B14)](../lecture_15_B14_climate_economics_iams/README.md)

## What this lecture covers

- **The deep-uncertainty problem.** Why equilibrium climate sensitivity, damage curvature, and intertemporal-substitution elasticity cannot be averaged out before optimization.
- **Stochastic CDICE-DEQN under Epstein-Zin.** A risk-sensitive recursive-utility solution that respects the tail.
- **GP surrogates for the policy outputs.** Bayesian active learning over the uncertain-parameter space.
- **Global sensitivity analysis.** Sobol indices and Shapley effects to localize where the policy is actually sensitive.
- **Constrained Pareto-improving carbon-tax policies.** Tax paths that, under every realization of the deep uncertainty (or every cohort, or every generation), leave no agent worse off than business-as-usual while strictly improving welfare for at least one. The endpoint is a defensible policy menu rather than a single number.

## Learning objectives

After this lecture you can:

- Run a deep-UQ analysis on a stochastic IAM with Epstein-Zin preferences.
- Build a GP surrogate for the policy outputs of a stochastic IAM with Bayesian active learning.
- Compute Sobol and Shapley sensitivity indices to localize the policy-relevant uncertainty.
- Design constrained Pareto-improving carbon-tax paths and articulate which parameters drive them.

## Slides

- [`slides/09_Deep_UQ_and_Optimal_Policies.pdf`](slides/09_Deep_UQ_and_Optimal_Policies.pdf)
- [`slides/09_Deep_UQ_and_Optimal_Policies.tex`](slides/09_Deep_UQ_and_Optimal_Policies.tex)

## Code

_(none)_

## In the lecture script

§11.4-11.6 (Deep UQ for IAMs and constrained Pareto-improving policy). The full chapter map is in [`script_to_lectures.md`](../../lecture_script/script_to_lectures.md).

## Readings

Curated bibliography for this lecture: [`lecture_16_B15.md`](../../readings/links_by_lecture/lecture_16_B15.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).

---

← [Previous: Climate economics and integrated assessment models](../lecture_15_B14_climate_economics_iams/README.md) · → [Next: Course wrap-up](../lecture_17_B16_course_wrap_up/README.md) · [Course map](../../COURSE_MAP.md)
