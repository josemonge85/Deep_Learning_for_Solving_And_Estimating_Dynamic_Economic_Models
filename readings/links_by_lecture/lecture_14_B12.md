# Readings, Lecture 14 (B12): Surrogates and Gaussian processes

Default policy: link only.

## Deep surrogate models

- **Chen, Didisheim, Scheidegger (2026), "Deep surrogates for finance: with an application to option pricing,"** *Journal of Financial Economics*, 177, 104222. [DOI](https://doi.org/10.1016/j.jfineco.2025.104222) · [publisher](https://www.sciencedirect.com/science/article/pii/S0304405X25002302). The reference for everything the lecture says about deep surrogates as a substitute for a costly model call: universal approximation, inference, parameter instability, and the option-pricing application that runs through the slides.
- **Scheidegger, Bilionis (2019), "Machine learning for high-dimensional dynamic stochastic economies,"** *Journal of Computational Science*, 33, 68–82. The earlier statement of the surrogate-of-an-economic-model idea, with a Bayesian active-learning loop.

## Gaussian processes and Bayesian active learning

- **Rasmussen, Williams (2006),** *Gaussian Processes for Machine Learning*, MIT Press. [Free PDF](http://www.gaussianprocess.org/gpml/). Canonical textbook; Chapters 2 and 5.
- **Brumm, Scheidegger (2017), "Using adaptive sparse grids to solve high-dimensional dynamic models,"** *Econometrica*, 85(5). The macro-economic backdrop for active learning in dynamic programming.

## Scaling GPs, active subspaces, and deep kernels

- **Constantine (2015),** *Active Subspaces*, SIAM. The book the active-subspaces section is based on.
- **Constantine, Dow, Wang (2014), "Active subspace methods in theory and practice,"** *SIAM J. Sci. Comput.*, 36(4). Active subspaces with GP regression.
- **Wilson, Hu, Salakhutdinov, Xing (2016), "Deep kernel learning,"** *AISTATS*. The foundational deep-kernel-learning paper used in the deep-kernel notebook.
- **Gardner et al. (2018), "GPyTorch,"** *NeurIPS*. The GP library used in the notebooks.

## GPs for dynamic programming

- **Renner, Scheidegger (2018), "Machine learning for dynamic incentive problems,"** working paper. [SSRN](https://ssrn.com/abstract=3282487). The reference for the active-subspace-GP value-function-iteration (ASGP-VFI) approach in the slides.

## Companion lecture script

- [`lecture_script/Deep_Learning_for_Solving_And_Estimating_Dynamic_Economic_Models.pdf`](../../lecture_script/Deep_Learning_for_Solving_And_Estimating_Dynamic_Economic_Models.pdf), chapter-based reference text.
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md), full chapter-to-lecture map.

## Bibliography

All references for this course are collected in [`readings/bibliography.bib`](../bibliography.bib).
