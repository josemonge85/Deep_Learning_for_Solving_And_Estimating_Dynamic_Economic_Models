# Lecture 10 (B08): Heterogeneous agents and Young's method

Two complementary methods for stationary distributions in heterogeneous-agent models.

`gpu-recommended` · `long` · builds on [Lecture 09 (B07)](../lecture_09_B07_olg_models_deqns/README.md)

> 📑 **Slides:** [08_Heterogeneous_Agents_Youngs_Method.pdf](slides/08_Heterogeneous_Agents_Youngs_Method.pdf)  
> 📓 **Notebooks:** [start here](code/lecture_10_B08_10_Youngs_Method_Examples.ipynb) (3 in [`code/`](code/))  
> 📚 **Further reading:** [curated list](../../readings/links_by_lecture/lecture_10_B08.md)  
> 📖 **Script:** §6.1-6.3 (Heterogeneous agents I), §6.4-6.6 (Heterogeneous agents II)

## What this lecture covers

The deck is intentionally encyclopedic. Treat the three Parts below as your reading map; budget ~60 min per Part, and feel free to stop at the end of Part II on a first pass.

- **Part I: Methods.** Young's (2010) histogram method, traditional Krusell-Smith with bounded rationality, and three deep-learning approaches to the same problem (continuum-of-agents DEQN, all-in-one DL after Maliar-Maliar-Winant, DeepHAM). Read first; this is the conceptual core.
- **Part II: Aiyagari teaching model.** Run Young and the DEQN side-by-side on the same calibration; read off the wealth distribution and aggregates. Notebooks 10 and 11 belong here.
- **Part III: State-of-the-art.** Krusell-Smith with the deep-learning machinery; comparison against Young's method on a model with aggregate risk. Notebook 12 belongs here. Skip on a first pass if time-pressed.

The notebooks map to the Parts:
- Notebook 10 (`10_Youngs_Method_Examples.ipynb`) -> Parts I-II
- Notebook 11 (`11_Continuum_of_Agents_DEQN.ipynb`) -> Part II
- Notebook 12 (`12_KrusellSmith_DeepLearning.ipynb`) -> Part III (extension)

## Learning objectives

After this lecture you can:

- Iterate Young's histogram method to convergence on Aiyagari and read off the wealth distribution.
- Train a continuum-of-agents DEQN and compare its policy against the Young-method solution.
- Diagnose when each method is preferable.

## Slides

- [`slides/08_Heterogeneous_Agents_Youngs_Method.pdf`](slides/08_Heterogeneous_Agents_Youngs_Method.pdf)
- [`slides/08_Heterogeneous_Agents_Youngs_Method.tex`](slides/08_Heterogeneous_Agents_Youngs_Method.tex)

## Code

- [`code/lecture_10_B08_10_Youngs_Method_Examples.ipynb`](code/lecture_10_B08_10_Youngs_Method_Examples.ipynb)
- [`code/lecture_10_B08_11_Continuum_of_Agents_DEQN.ipynb`](code/lecture_10_B08_11_Continuum_of_Agents_DEQN.ipynb)
- [`code/lecture_10_B08_12_KrusellSmith_DeepLearning.ipynb`](code/lecture_10_B08_12_KrusellSmith_DeepLearning.ipynb)

## In the lecture script

§6.1-6.3 (Heterogeneous agents I), §6.4-6.6 (Heterogeneous agents II). The full chapter map is in [`script_to_lectures.md`](../../lecture_script/script_to_lectures.md).

## Readings

Curated bibliography for this lecture: [`lecture_10_B08.md`](../../readings/links_by_lecture/lecture_10_B08.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).

---

| ← Previous | Next → |
|---|---|
| [**Lecture 09: OLG models with DEQNs**](../lecture_09_B07_olg_models_deqns/README.md)<br><sub>Analytic OLG, 56-cohort benchmark, Fischer-Burmeister borrowing constraints</sub> | [**Lecture 11: Physics-informed neural networks (PINNs)**](../lecture_11_B09_pinns/README.md)<br><sub>ODE / PDE PINNs, soft vs hard BCs, cake-eating HJB, Black-Scholes</sub> |

[↑ Course map](../../COURSE_MAP.md)
