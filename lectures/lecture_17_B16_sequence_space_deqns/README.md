# Lecture 17 (B16): Sequence-space DEQNs

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance
> **Course author:** Simon Scheidegger
> **Compute tier:** `gpu-recommended` &nbsp;·&nbsp; **Time budget:** `long`

## Learning goal

Train sequence-space DEQNs that use a long shock history (~80 steps) instead of the current-state vector as input. Reproduce the Brock-Mirman warm-up and the Krusell-Smith benchmark in sequence space, and understand why the sequence-space template generalizes to multi-equation systems with multiple shock channels.

## Prerequisites

- [Lecture 16 (B15)](../lecture_16_B15_continuum_agents_deqn_method_comparison/README.md) — Continuum-of-agents DEQN and method comparison

## External prerequisites

- Python 3.10+ environment (`requirements.txt` at repo root, or run on the course platform).
- Familiarity with the math listed under **Script reference** below.

## Script reference

- §6.7 (Sequence-space DEQNs)
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md) — full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf) — companion script

## Slides

- [`06_SequenceSpace_DEQNs.pdf`](slides/06_SequenceSpace_DEQNs.pdf)

## Notebooks

### Core

- [`lecture_17_B16_05_SequenceSpace_BrockMirman.ipynb`](notebooks/core/lecture_17_B16_05_SequenceSpace_BrockMirman.ipynb)
- [`lecture_17_B16_06_SequenceSpace_KrusellSmith.ipynb`](notebooks/core/lecture_17_B16_06_SequenceSpace_KrusellSmith.ipynb)

### Exercises

_(none in this PR)_

### Solutions

_(none in this PR)_

### Extensions

- [`lecture_17_B16_05b_SequenceSpace_IRBC.ipynb`](notebooks/extensions/lecture_17_B16_05b_SequenceSpace_IRBC.ipynb)
- [`lecture_17_B16_KrusellSmith_Tutorial_CPU.ipynb`](notebooks/extensions/lecture_17_B16_KrusellSmith_Tutorial_CPU.ipynb)

## Checkpoint

> Train a sequence-space DEQN on Brock-Mirman with an 80-step shock history.

## Readings

- [`readings/links_by_lecture/lecture_17_B16.md`](../../readings/links_by_lecture/lecture_17_B16.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- **Previous:** [Lecture 16 (B15): Continuum-of-agents DEQN and method comparison](../lecture_16_B15_continuum_agents_deqn_method_comparison/README.md)
- **Next:** [Lecture 18 (B17): PINNs I - residual learning for ODEs and PDEs](../lecture_18_B17_pinn_foundations/README.md)
- [Course map](../../COURSE_MAP.md)
- [Repository home](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written / graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
