# Lecture 14 (B13): Structural estimation via SMM

Structural estimation by simulated method of moments (SMM), made tractable by replacing the inner-loop model solve with a deep surrogate.

`cpu-standard` · `long` · builds on [Lecture 13 (B12)](../lecture_13_B12_surrogates_and_gps/README.md)

## What this lecture covers

- **SMM in one slide.** The moment-matching condition, the asymptotic distribution of the estimator, and the role of the weighting matrix.
- **Surrogate-based estimation.** Why the surrogate makes a brutal repeated re-solve into a cheap optimization.
- **Single-parameter Brock-Mirman.** Estimating the productivity persistence rho on a deep surrogate of the model.
- **Joint estimation.** Estimating (beta, rho) together; identification diagnostics, Jacobian rank, and asymptotic standard errors.
- **Sensitivity to the surrogate.** What happens to the estimator when the surrogate is wrong; switching to a GP for comparison.

## Learning objectives

After this lecture you can:

- State the SMM moment condition and the asymptotic distribution of the estimator.
- Run a single-parameter SMM (rho) on a deep surrogate of Brock-Mirman.
- Run a joint (beta, rho) SMM and read off identification diagnostics.
- Replace the surrogate with a GP and compare estimation behavior.

## Slides

- [`slides/08_Exercise_Structural_Estimation.pdf`](slides/08_Exercise_Structural_Estimation.pdf)
- [`slides/08_Exercise_Structural_Estimation.tex`](slides/08_Exercise_Structural_Estimation.tex)

## Code

- [`code/lecture_14_B13_03_Structural_Estimation_BM.ipynb`](code/lecture_14_B13_03_Structural_Estimation_BM.ipynb)
- [`code/lecture_14_B13_03b_Structural_Estimation_BM_Joint.ipynb`](code/lecture_14_B13_03b_Structural_Estimation_BM_Joint.ipynb)

## In the lecture script

§Chapter 10 (Structural estimation via SMM). The full chapter map is in [`script_to_lectures.md`](../../lecture_script/script_to_lectures.md).

## Readings

Curated bibliography for this lecture: [`lecture_14_B13.md`](../../readings/links_by_lecture/lecture_14_B13.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).

---

← [Previous: Surrogates and Gaussian processes](../lecture_13_B12_surrogates_and_gps/README.md) · → [Next: Climate economics and integrated assessment models](../lecture_15_B14_climate_economics_iams/README.md) · [Course map](../../COURSE_MAP.md)
