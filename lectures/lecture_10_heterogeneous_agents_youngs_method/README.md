# Lecture 10: Heterogeneous agents and Young's method

Two complementary methods for stationary distributions in heterogeneous-agent models.

`gpu-recommended` · `long` · builds on [Lecture 09](../lecture_09_olg_models_deqns/README.md)

> 📑 **Slides:** [lecture_10_heterogeneous_agents_youngs.pdf](slides/lecture_10_heterogeneous_agents_youngs.pdf)  
> 📓 **Notebooks:** [start here](code/lecture_10_10_Youngs_Method_Examples.ipynb) (3 in [`code/`](code/))  
> 📚 **Further reading:** [curated list](../../readings/links_by_lecture/lecture_10.md)  
> 📖 **Script:** §6.1-6.3 (Heterogeneous agents I), §6.4-6.6 (Heterogeneous agents II)

## What this lecture covers

The deck is intentionally encyclopedic, in five parts. Treat them as your reading map; budget ~30–45 min per part, and feel free to stop after Part IV on a first pass.

- **Part I — Motivation.** Why the aggregate state becomes infinite-dimensional once agents are heterogeneous, and why the cross-sectional distribution has to be tracked at all.
- **Part II — Young's (2010) non-stochastic simulation.** The mean-preserving lottery, the two-stage capital/shock cascade, grid design, and the O(1) bracketing trick. Notebook 10 isolates this operator on toy examples (including the script's hand-worked 4-point update).
- **Part III — The Krusell–Smith logic.** The traditional nested fixed point, bounded rationality, and approximate aggregation (R² > 0.9999 on mean dynamics, with the caveats). No notebook of its own; this is the benchmark the DEQN methods are measured against.
- **Part IV — DEQN teaching implementation.** Young's histogram embedded in a DEQN training loop, on the Appendix-A.5 **Bewley endowment** economy of Azinovic, Gaegauf & Scheidegger (2022): no capital and no firm, a single bond in unit net supply, Epstein–Zin preferences, a six-state aggregate shock, and two idiosyncratic productivity types. Notebook 11 is this implementation.
- **Part V — Alternative deep-learning routes to Krusell–Smith.** All-in-one DL (Maliar–Maliar–Winant 2021), DeepHAM's learned generalized moments (Han–Yang–E 2024), DeepSAM, and structural RL, with a "which method, when?" chooser. Notebook 12 is a classroom-scale all-in-one DL solver on the canonical KS economy. (The sequence-space alternative to histogram encoding is developed in the Sequence-Space DEQNs lecture and in §6.7 of the script, not here.)

Notebook → part map:
- Notebook 10 (`lecture_10_10_Youngs_Method_Examples.ipynb`) → Part II
- Notebook 11 (`lecture_10_11_Continuum_of_Agents_DEQN.ipynb`) → Part IV
- Notebook 12 (`lecture_10_12_KrusellSmith_DeepLearning.ipynb`) → Part V (extension)

## Learning objectives

After this lecture you can:

- Run Young's (2010) histogram update by hand and in code, and explain why it preserves the mean exactly while only approximating higher moments.
- Embed the histogram update inside a DEQN training loop on the Appendix-A.5 Bewley endowment economy, with the distribution co-evolving with the policy and price networks.
- Compare the deep-learning routes to Krusell–Smith (all-in-one DL, DeepHAM) and judge which one fits a given heterogeneous-agent model.

## Slides

- [`slides/lecture_10_heterogeneous_agents_youngs.pdf`](slides/lecture_10_heterogeneous_agents_youngs.pdf)
- [`slides/lecture_10_heterogeneous_agents_youngs.tex`](slides/lecture_10_heterogeneous_agents_youngs.tex)

## Code

- [`code/lecture_10_10_Youngs_Method_Examples.ipynb`](code/lecture_10_10_Youngs_Method_Examples.ipynb)
- [`code/lecture_10_11_Continuum_of_Agents_DEQN.ipynb`](code/lecture_10_11_Continuum_of_Agents_DEQN.ipynb)
- [`code/lecture_10_12_KrusellSmith_DeepLearning.ipynb`](code/lecture_10_12_KrusellSmith_DeepLearning.ipynb)

## In the lecture script

§6.1-6.3 (Heterogeneous agents I), §6.4-6.6 (Heterogeneous agents II). The full chapter map is in [`script_to_lectures.md`](../../lecture_script/script_to_lectures.md).

## Readings

Curated bibliography for this lecture: [`lecture_10.md`](../../readings/links_by_lecture/lecture_10.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).

---

| ← Previous | Next → |
|---|---|
| [**Lecture 09: OLG models with DEQNs**](../lecture_09_olg_models_deqns/README.md)<br><sub>Analytic OLG, 56-cohort benchmark, Fischer-Burmeister borrowing constraints</sub> | [**Lecture 11: Physics-informed neural networks (PINNs)**](../lecture_11_pinns/README.md)<br><sub>ODE / PDE PINNs, soft vs hard BCs, cake-eating HJB, Black-Scholes</sub> |

[↑ Course map](../../COURSE_MAP.md)
