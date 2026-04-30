# Third-party notices

This repository contains first-party material (CC0 1.0 / MIT, see `LICENSE`
and `LICENSE-content.md`) and a small number of borrowed or adapted
artifacts. This file records the latter so attribution and licensing
remain auditable.

## Borrowed / adapted code

| File | Origin | Notes |
|---|---|---|
| `lectures/lecture_17_B16_sequence_space_deqns/notebooks/extensions/lecture_17_B16_KrusellSmith_Tutorial_CPU.ipynb` | Upstream Krusell-Smith JAX tutorial | Adapted with `TUTORIAL_MODE` switch. Upstream header retained verbatim in the notebook. |

Additional cases will be added here if PR 3 (notebook migration) discovers
further adapted material.

## External readings

Readings under `readings/` are linked or, where redistribution is cleared,
mirrored under `readings/allowed_pdfs/`. Each reading's license is
recorded in `READINGS_AUDIT.csv`. Uncleared readings are referenced via
DOI or publisher link only — they are not redistributed in this
repository.

## Externally-sourced figures

Figures or screenshots adapted from third-party publications are recorded
in `assets/attributions.yml` with their original source and license.

## Frameworks and libraries

This course uses the following open-source frameworks (see `requirements.txt`
for versions). Each retains its own license; consult the upstream project:

- NumPy, SciPy, pandas, Matplotlib, scikit-learn
- TensorFlow, TensorFlow Probability, Keras
- PyTorch
- JAX, jaxlib, Flax, Optax
- GPyTorch, BoTorch
- TensorBoard
