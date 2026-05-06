# Lecture 17: Deep uncertainty quantification and Pareto-improving climate policy

Stochastic IAMs depend on parameters whose true values are deeply uncertain. Plugging point estimates in, or averaging the uncertainty out, is misleading. This lecture builds a complete pipeline for taking that uncertainty seriously and turning it into a defensible policy menu.

`gpu-recommended` · `long` · builds on [Lecture 16](../lecture_16_climate_economics_iams/README.md)

> 📑 **Slides:** [09_Deep_UQ_and_Optimal_Policies.pdf](slides/09_Deep_UQ_and_Optimal_Policies.pdf)  
> 📓 **Notebooks:** [`code/lecture_17_09_DICE_2P_UQ_Analysis.ipynb`](code/lecture_17_09_DICE_2P_UQ_Analysis.ipynb)  
> 📚 **Further reading:** [curated list](../../readings/links_by_lecture/lecture_17.md)  
> 📖 **Script:** §11.4-11.6 (Deep UQ for IAMs and constrained Pareto-improving policy)

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

- [`code/lecture_17_09_DICE_2P_UQ_Analysis.ipynb`](code/lecture_17_09_DICE_2P_UQ_Analysis.ipynb) -- Sobol indices and univariate effects on $(\rho, \pi_2)$ from 25 reference DICE solutions cached under [`code/_pt_solutions/2p/`](code/_pt_solutions/2p/). Runs end-to-end on CPU in about a minute.
- Supporting pipeline: [`dice_2p_surrogate_lib.py`](code/dice_2p_surrogate_lib.py), [`train_dice_2p_pointsolutions.py`](code/train_dice_2p_pointsolutions.py), [`train_dice_2p_surrogate.py`](code/train_dice_2p_surrogate.py), [`compute_dice_2p_gp_anchors.py`](code/compute_dice_2p_gp_anchors.py), [`run_dice_2p_pipeline.sh`](code/run_dice_2p_pipeline.sh).

## In the lecture script

§11.4-11.6 (Deep UQ for IAMs and constrained Pareto-improving policy). The full chapter map is in [`script_to_lectures.md`](../../lecture_script/script_to_lectures.md).

## Readings

Curated bibliography for this lecture: [`lecture_17.md`](../../readings/links_by_lecture/lecture_17.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).

---

| ← Previous | Next → |
|---|---|
| [**Lecture 16: Climate economics and IAMs**](../lecture_16_climate_economics_iams/README.md)<br><sub>DICE / CDICE simulation, deterministic and stochastic CDICE-DEQN</sub> | [**Lecture 18: Course wrap-up**](../lecture_18_course_wrap_up/README.md)<br><sub>Synthesis, decision guide, when to use which method</sub> |

[↑ Course map](../../COURSE_MAP.md)
