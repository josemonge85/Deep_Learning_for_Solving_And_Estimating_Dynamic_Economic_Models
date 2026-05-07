# Lecture 12: Continuous-time heterogeneous agents, theory

The continuous-time heterogeneous-agent system, paired with the master equation that closes it in general equilibrium.

`cpu-light` · `standard` · builds on [Lecture 11](../lecture_11_pinns/README.md)

> 📑 **Slides:** [lecture_12_continuous_time_ha_theory.pdf](slides/lecture_12_continuous_time_ha_theory.pdf)  
> 📚 **Further reading:** [curated list](../../readings/links_by_lecture/lecture_12.md)  
> 📖 **Script:** §8.1-8.6 (HJB, KFE, master equation), §Appendix C (Ito calculus)

## What this lecture covers

- **The HJB equation.** The individual's value function as a viscosity solution; drift, diffusion, and idiosyncratic shock terms.
- **The Kolmogorov forward equation.** Cross-sectional distribution dynamics and the stationary distribution.
- **Aiyagari in continuous time.** The canonical example, mapped to its discrete-time analog operator by operator.
- **Ito calculus essentials.** What you need from stochastic differential equations to read the rest of the lecture.
- **The master equation.** Closing the system in general equilibrium and connecting to the modern continuous-time HA literature.

## Learning objectives

After this lecture you can:

- Write the HJB-KFE system for the Aiyagari model.
- Identify each operator's role (drift, diffusion, idiosyncratic shock, distribution update).
- State the master equation and its place in the modern HA literature.

## Slides

- [`slides/lecture_12_continuous_time_ha_theory.pdf`](slides/lecture_12_continuous_time_ha_theory.pdf)
- [`slides/lecture_12_continuous_time_ha_theory.tex`](slides/lecture_12_continuous_time_ha_theory.tex)

## Code

_(none)_

## In the lecture script

§8.1-8.6 (HJB, KFE, master equation), §Appendix C (Ito calculus). The full chapter map is in [`script_to_lectures.md`](../../lecture_script/script_to_lectures.md).

## Readings

Curated bibliography for this lecture: [`lecture_12.md`](../../readings/links_by_lecture/lecture_12.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).

---

| ← Previous | Next → |
|---|---|
| [**Lecture 11: Physics-informed neural networks (PINNs)**](../lecture_11_pinns/README.md)<br><sub>ODE / PDE PINNs, soft vs hard BCs, cake-eating HJB, Black-Scholes</sub> | [**Lecture 13: Continuous-time HA, numerics**](../lecture_13_continuous_time_ha_numerics/README.md)<br><sub>Achdou-Han-Lasry-Lions-Moll finite-difference scheme, PINN for HJB-KFE, continuous-time Aiyagari</sub> |

[↑ Course map](../../COURSE_MAP.md)
