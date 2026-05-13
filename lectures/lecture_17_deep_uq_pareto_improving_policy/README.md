# Lecture 17: Deep uncertainty quantification and Pareto-improving climate policy

Stochastic IAMs depend on parameters whose true values are deeply uncertain. Plugging point estimates in, or averaging the uncertainty out, is misleading. This lecture builds a complete pipeline for taking that uncertainty seriously and turning it into a defensible policy menu.

`gpu-recommended` · `long` · builds on [Lecture 16](../lecture_16_climate_economics_iams/README.md)

> 📑 **Slides:** [lecture_17_deep_uq_pareto_policy.pdf](slides/lecture_17_deep_uq_pareto_policy.pdf)  
> 💻 **Code:** maintained in the external research repository [`sischei/JPE_Macro_Using_ML_to_compute_constrained_optimal_carbon_tax_rules`](https://github.com/sischei/JPE_Macro_Using_ML_to_compute_constrained_optimal_carbon_tax_rules)  
> 📚 **Further reading:** [curated list](../../readings/links_by_lecture/lecture_17.md)  
> 📖 **Script:** §11.9-11.12 (Bayesian learning, Epstein-Zin, deep UQ, constrained Pareto-improving carbon tax)

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

- [`slides/lecture_17_deep_uq_pareto_policy.pdf`](slides/lecture_17_deep_uq_pareto_policy.pdf)
- [`slides/lecture_17_deep_uq_pareto_policy.tex`](slides/lecture_17_deep_uq_pareto_policy.tex)

## Code

The code that supports this lecture, the full deep-UQ + Pareto-improving carbon-tax pipeline, lives in a separate research repository:

<https://github.com/sischei/JPE_Macro_Using_ML_to_compute_constrained_optimal_carbon_tax_rules>

That repository contains the stochastic CDICE-DEQN solver, the GP surrogate over the uncertain-parameter space with Bayesian active learning, the Sobol and Shapley sensitivity-analysis tooling, and the constrained Pareto-improving carbon-tax search. It is the artifact behind the corresponding paper and is maintained there to keep this teaching repository light.

## In the lecture script

§11.9-11.12 (Bayesian learning, Epstein-Zin, deep UQ, constrained Pareto-improving carbon tax). The full chapter map is in [`script_to_lectures.md`](../../lecture_script/script_to_lectures.md).

## Readings

Curated bibliography for this lecture: [`lecture_17.md`](../../readings/links_by_lecture/lecture_17.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).

---

| ← Previous | Next → |
|---|---|
| [**Lecture 16: Climate economics and IAMs**](../lecture_16_climate_economics_iams/README.md)<br><sub>DICE / CDICE simulation, deterministic and stochastic CDICE-DEQN</sub> | [**Lecture 18: Course wrap-up**](../lecture_18_course_wrap_up/README.md)<br><sub>Synthesis, decision guide, when to use which method</sub> |

[↑ Course map](../../COURSE_MAP.md)
