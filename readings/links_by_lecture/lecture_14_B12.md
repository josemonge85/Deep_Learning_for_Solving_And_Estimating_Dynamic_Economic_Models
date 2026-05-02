# Readings, Lecture 13 (B12): Surrogates and Gaussian processes

Default policy: link only. PDFs are not redistributed unless their license clearly permits it.

## Deep surrogate models

- **Chen, Didisheim, Scheidegger (2026), "Deep surrogates for finance: with an application to option pricing,"** *Journal of Financial Economics*, 177, 104222. [DOI](https://doi.org/10.1016/j.jfineco.2025.104222) · [publisher](https://www.sciencedirect.com/science/article/pii/S0304405X25002302). The reference for everything the lecture says about deep surrogates as a substitute for a costly model call: universal approximation, inference, parameter instability, and the option-pricing application that runs through the slides.
- **Scheidegger and Bilionis (2019), "Machine learning for high-dimensional dynamic stochastic economies,"** *Journal of Computational Science*, 33, 68–82. The earlier statement of the surrogate-of-an-economic-model idea, with a Bayesian active-learning loop.

## Gaussian processes and Bayesian active learning

- **Rasmussen and Williams (2006),** *Gaussian Processes for Machine Learning*, MIT Press. [Free PDF (publisher)](http://www.gaussianprocess.org/gpml/). Canonical textbook; Chapters 2 (regression) and 5 (model selection) cover the GP material in the lecture.
- **Brumm and Scheidegger (2017), "Using adaptive sparse grids to solve high-dimensional dynamic models,"** *Econometrica*, 85(5). The macro-economic backdrop for why active learning matters in dynamic-programming applications.

## Scaling GPs, active subspaces, and deep kernels

- **Constantine (2015),** *Active Subspaces: Emerging Ideas for Dimension Reduction in Parameter Studies*, SIAM. The book the active-subspaces section of the deck is based on.
- **Constantine, Dow, Wang (2014), "Active subspace methods in theory and practice: applications to kriging surfaces,"** *SIAM J. Sci. Comput.*, 36(4). The companion paper on combining active subspaces with GP regression.
- **Wilson, Hu, Salakhutdinov, Xing (2016), "Deep kernel learning,"** *AISTATS*. The foundational deep-kernel-learning paper used in the deep-kernel-learning notebook.
- **Gardner et al. (2018), "GPyTorch: blackbox matrix-matrix Gaussian process inference with GPU acceleration,"** *NeurIPS*. The GP library used in the notebooks.

## GPs for dynamic programming

- **Renner and Scheidegger (2018), "Machine learning for dynamic incentive problems,"** working paper. [SSRN](https://ssrn.com/abstract=3282487). The reference for the active-subspace-GP value-function-iteration (ASGP-VFI) approach in the slides.

## Companion lecture script

- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf), chapter-based reference text.
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md), full chapter-to-lecture map.

## Bibliography

All references for this course are collected in [`readings/bibliography.bib`](../bibliography.bib).
