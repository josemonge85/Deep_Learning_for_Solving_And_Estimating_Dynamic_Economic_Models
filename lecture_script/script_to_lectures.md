# Script-to-lecture map

> **What this is.** A two-way crosswalk between the chapter-based companion text
> ([`Deep_Learning_for_Solving_And_Estimating_Dynamic_Economic_Models.pdf`](Deep_Learning_for_Solving_And_Estimating_Dynamic_Economic_Models.pdf))
> and the 18-lecture online course. The script is organized by topic; the
> course is organized by classroom session. Use this page to jump from a
> chapter you are reading to the lecture(s) that teach it, or from a lecture
> in your schedule to the chapter(s) that ground it.
>
> **How to read it.** Each row maps one script unit (preface, chapter, or
> appendix) to the public lecture(s) where it lands. Click a lecture to open
> its README, where you will find slides, notebooks, learning objectives, and
> readings. Click a chapter or appendix label to jump straight into the script.

## Quick links

- **Companion script PDF:** [`Deep_Learning_for_Solving_And_Estimating_Dynamic_Economic_Models.pdf`](Deep_Learning_for_Solving_And_Estimating_Dynamic_Economic_Models.pdf)
- **Course portal:** [`README.md`](../README.md)
- **Course-wide map:** [`COURSE_MAP.md`](../COURSE_MAP.md)
- **Glossary (Appendix A):** [`glossary.md`](glossary.md)

## Part I — Front matter and foundations

| Script unit | Public lecture(s) | Notes |
|---|---|---|
| Preface | [Lecture 01](../lectures/lecture_01_python_primer/README.md) | Public-repo URL and licensing language updated. |
| How to Read This Script | [Lecture 01](../lectures/lecture_01_python_primer/README.md) | Online course is lecture-numbered; the script is chapter-based. |
| Notation and Symbols | [Lecture 01](../lectures/lecture_01_python_primer/README.md); referenced from every lecture README | |
| Execution Map | [Lecture 01](../lectures/lecture_01_python_primer/README.md); all lectures | Maps script chapter order onto the 18 numbered lectures. |
| Ch. 1.1-1.4 | [Lecture 02](../lectures/lecture_02_intro_deep_learning/README.md) | Foundations and function approximation. |
| Ch. 1.4.1 | [Lecture 02](../lectures/lecture_02_intro_deep_learning/README.md) | Cross-referenced from Lectures [05](../lectures/lecture_05_nas_loss_normalization/README.md) and [14](../lectures/lecture_14_surrogates_and_gps/README.md). |
| Ch. 1.5-1.9 | [Lecture 02](../lectures/lecture_02_intro_deep_learning/README.md) | Optimization, depth, regularization. |
| Ch. 1.10-1.11 | [Lecture 02](../lectures/lecture_02_intro_deep_learning/README.md) | Generalization and sequence models. |

## Part II — Deep equilibrium networks (Ch. 2-4)

| Script unit | Public lecture(s) | Notes |
|---|---|---|
| Ch. 2.1-2.4 | [Lecture 03](../lectures/lecture_03_deep_equilibrium_nets/README.md) | DEQN theory and motivation; constraints sketched. |
| Ch. 2.5 | [Lecture 03](../lectures/lecture_03_deep_equilibrium_nets/README.md) | Deterministic Brock-Mirman. |
| Ch. 2.6 | [Lecture 03](../lectures/lecture_03_deep_equilibrium_nets/README.md) | Quadrature for conditional expectations. |
| Ch. 2.7 | [Lecture 07](../lectures/lecture_07_autodiff_for_deqns/README.md) | Automatic differentiation. |
| Ch. 2.8 | [Lecture 07](../lectures/lecture_07_autodiff_for_deqns/README.md) — extension | |
| Ch. 2.9 | [Lecture 03](../lectures/lecture_03_deep_equilibrium_nets/README.md) | Residual kernels and loss design. |
| Ch. 3 | [Lecture 04](../lectures/lecture_04_irbc_with_deqns/README.md) | International real business cycle. |
| Ch. 4 | [Lecture 05](../lectures/lecture_05_nas_loss_normalization/README.md) | Neural architecture search and loss normalization. |
| (no script chapter) | [Lecture 06](../lectures/lecture_06_agentic_programming/README.md) | Agentic programming workshop, slides plus exercises. |

## Part III — OLG, heterogeneous agents, sequence space (Ch. 5-6)

| Script unit | Public lecture(s) | Notes |
|---|---|---|
| Ch. 5.1-5.5 | [Lecture 08](../lectures/lecture_08_olg_models_deqns/README.md) | OLG with DEQNs. |
| Ch. 5.6 | [Lecture 08](../lectures/lecture_08_olg_models_deqns/README.md) | Large OLG benchmark with borrowing constraints. |
| Ch. 6.1-6.3 | [Lecture 09](../lectures/lecture_09_heterogeneous_agents_youngs_method/README.md) | Heterogeneous agents I, Young's method. |
| Ch. 6.4-6.6 | [Lecture 09](../lectures/lecture_09_heterogeneous_agents_youngs_method/README.md) | Heterogeneous agents II, continuum-of-agents DEQN. |
| Ch. 6.7 | [Lecture 10](../lectures/lecture_10_sequence_space_deqns/README.md) | Sequence-space DEQNs. |

## Part IV — PINNs and continuous-time methods (Ch. 7-8)

| Script unit | Public lecture(s) | Notes |
|---|---|---|
| Ch. 7.1-7.4 | [Lecture 11](../lectures/lecture_11_pinns/README.md) | PINN foundations. |
| Ch. 7.5-7.9 | [Lecture 11](../lectures/lecture_11_pinns/README.md) | Economic PDEs (HJB, Black-Scholes); Ch. 7.7 previews Ch. 8. |
| Ch. 8.1-8.5 | [Lecture 12](../lectures/lecture_12_continuous_time_ha_theory/README.md) | Why continuous time, Ito calculus, the Kolmogorov forward equation, the HJB equation, Huggett/Aiyagari competitive equilibrium. |
| Ch. 8.6 | [Lecture 13](../lectures/lecture_13_continuous_time_ha_numerics/README.md) | The PINN solver for the stationary HJB-KFE Aiyagari system. Lecture 13 ships one companion notebook — the upwind-finite-difference + PINN Aiyagari solver (`lecture_13_08_...`); the single-PDE HJB warm-ups that used to accompany it are PINN exercises and belong with [Lecture 11](../lectures/lecture_11_pinns/README.md). |
| Ch. 8.7-8.8 | [Lecture 12](../lectures/lecture_12_continuous_time_ha_theory/README.md); [Lecture 13](../lectures/lecture_13_continuous_time_ha_numerics/README.md) | The master equation (derived in Lecture 12) and EMINNs (the deep-learning master-equation solver, in Lecture 13). |

## Part V — Surrogates, estimation, applications (Ch. 9-11)

| Script unit | Public lecture(s) | Notes |
|---|---|---|
| Ch. 9.1-9.2 | [Lecture 14](../lectures/lecture_14_surrogates_and_gps/README.md) | Deep surrogates. |
| Ch. 9.3-9.6 | [Lecture 14](../lectures/lecture_14_surrogates_and_gps/README.md) | GPs and Bayesian active learning. |
| Ch. 9.7 | [Lecture 14](../lectures/lecture_14_surrogates_and_gps/README.md) | Active subspaces. |
| Ch. 9.8 | [Lecture 14](../lectures/lecture_14_surrogates_and_gps/README.md) | GP value-function iteration. |
| Ch. 9.9 | [Lecture 14](../lectures/lecture_14_surrogates_and_gps/README.md) | Deep kernels. |
| Ch. 9.10 | [Lecture 14](../lectures/lecture_14_surrogates_and_gps/README.md) | GPs among Bayesian cousins. |
| Ch. 10 | [Lecture 15](../lectures/lecture_15_structural_estimation_smm/README.md) | Structural estimation via SMM. |
| Ch. 11.1-11.2 | [Lecture 16](../lectures/lecture_16_climate_economics_iams/README.md) | IAMs and DICE. |
| Ch. 11.3-11.8 | [Lecture 16](../lectures/lecture_16_climate_economics_iams/README.md) | CDICE-DEQN: non-stationary setup, deterministic solver, AR(1) productivity extension. |
| Ch. 11.9-11.12 | [Lecture 17](../lectures/lecture_17_deep_uq_pareto_improving_policy/README.md) | Bayesian learning, Epstein-Zin, deep UQ surrogates, constrained Pareto-improving carbon tax. |

## Part VI — Wrap-up and appendices (Ch. 12, App. A-E)

| Script unit | Public lecture(s) | Notes |
|---|---|---|
| Ch. 12 | [Lecture 18](../lectures/lecture_18_course_wrap_up/README.md) | Course wrap-up and method choice. |
| Appendix A — Glossary | [Lecture 18](../lectures/lecture_18_course_wrap_up/README.md); referenced everywhere | Mirror at [`glossary.md`](glossary.md). |
| Appendix B — Matrix calculus | [Lecture 07](../lectures/lecture_07_autodiff_for_deqns/README.md) | |
| Appendix C — Ito calculus | [Lecture 12](../lectures/lecture_12_continuous_time_ha_theory/README.md) | |
| Appendix D — Fixed points and Bellman | [Lecture 18](../lectures/lecture_18_course_wrap_up/README.md); cross-referenced from [Lecture 03](../lectures/lecture_03_deep_equilibrium_nets/README.md) | |
| Appendix E — Reproducibility info | [Lecture 01](../lectures/lecture_01_python_primer/README.md) | |
