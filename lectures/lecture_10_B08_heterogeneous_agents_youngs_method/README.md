# Lecture 10 (B08): Heterogeneous agents and Young's method

Two complementary methods for stationary distributions in heterogeneous-agent models.

`gpu-recommended` · `long` · builds on [Lecture 09 (B07)](../lecture_09_B07_olg_models_deqns/README.md)

> 📑 **Slides:** [08_Heterogeneous_Agents_Youngs_Method.pdf](slides/08_Heterogeneous_Agents_Youngs_Method.pdf)  
> 📓 **Notebooks:** [start here](code/lecture_09_B08_10_Youngs_Method_Examples.ipynb) (3 in [`code/`](code/))  
> 📚 **Further reading:** [curated list](../../readings/links_by_lecture/lecture_10_B08.md)  
> 📖 **Script:** §6.1-6.3 (Heterogeneous agents I), §6.4-6.6 (Heterogeneous agents II)

## What this lecture covers

- **Young's (2010) histogram method.** Discretize the individual state, iterate a transition matrix to its fixed point; the workhorse of the discrete-time HA literature.
- **Continuum-of-agents DEQN.** Train the policy directly on a simulated cross-section, no histogram step required.
- **Aiyagari side-by-side.** Run both methods on the same model and read off the wealth distribution and aggregates.
- **When to choose which.** Computational cost, smoothness of the policy, and dimensionality of the individual state.
- **Krusell-Smith deep-learning extension.** Han-Yang-E (2023) is provided as further reading.

## Learning objectives

After this lecture you can:

- Iterate Young's histogram method to convergence on Aiyagari and read off the wealth distribution.
- Train a continuum-of-agents DEQN and compare its policy against the Young-method solution.
- Diagnose when each method is preferable.

## Slides

- [`slides/08_Heterogeneous_Agents_Youngs_Method.pdf`](slides/08_Heterogeneous_Agents_Youngs_Method.pdf)
- [`slides/08_Heterogeneous_Agents_Youngs_Method.tex`](slides/08_Heterogeneous_Agents_Youngs_Method.tex)

## Code

- [`code/lecture_09_B08_10_Youngs_Method_Examples.ipynb`](code/lecture_09_B08_10_Youngs_Method_Examples.ipynb)
- [`code/lecture_09_B08_11_Continuum_of_Agents_DEQN.ipynb`](code/lecture_09_B08_11_Continuum_of_Agents_DEQN.ipynb)
- [`code/lecture_09_B08_12_KrusellSmith_DeepLearning.ipynb`](code/lecture_09_B08_12_KrusellSmith_DeepLearning.ipynb)

## In the lecture script

§6.1-6.3 (Heterogeneous agents I), §6.4-6.6 (Heterogeneous agents II). The full chapter map is in [`script_to_lectures.md`](../../lecture_script/script_to_lectures.md).

## Readings

Curated bibliography for this lecture: [`lecture_10_B08.md`](../../readings/links_by_lecture/lecture_10_B08.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).

---

← [Previous: OLG models with DEQNs](../lecture_09_B07_olg_models_deqns/README.md) · → [Next: Physics-informed neural networks](../lecture_11_B09_pinns/README.md) · [Course map](../../COURSE_MAP.md)
