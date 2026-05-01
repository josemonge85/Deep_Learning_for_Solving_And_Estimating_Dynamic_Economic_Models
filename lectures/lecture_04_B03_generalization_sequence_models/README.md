# Lecture 04 (B03): Generalization and sequence models

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance
> **Course author:** Simon Scheidegger
> **Compute tier:** `cpu-standard` &nbsp;·&nbsp; **Time budget:** `standard`

## Learning goal

Reason about generalization and inductive bias in neural networks: the double-descent phenomenon, the role of architecture in handling sequences, and the relative strengths of MLPs, LSTMs, and Transformers on time-series-like economic data (Edgeworth cycles).

## Prerequisites

- [Lecture 03 (B02)](../lecture_03_B02_training_neural_networks/README.md) — Training neural networks

## External prerequisites

- Python 3.10+ environment (`requirements.txt` at repo root, or run on the course platform).
- Familiarity with the math listed under **Script reference** below.

## Script reference

- §1.10-1.11 (Generalization, sequence models)
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md) — full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf) — companion script

## Slides

- [`03_Generalization_Sequence_Models.pdf`](slides/03_Generalization_Sequence_Models.pdf) — overfitting, regularization, double descent, RNN / LSTM / Transformer.

## Notebooks

### Core

- [`lecture_04_B03_03_Double_Descent.ipynb`](notebooks/core/lecture_04_B03_03_Double_Descent.ipynb)
- [`lecture_04_B03_08_MLP_LSTM_Transformer_Edgeworth_Cycles.ipynb`](notebooks/core/lecture_04_B03_08_MLP_LSTM_Transformer_Edgeworth_Cycles.ipynb)

### Exercises

_(none in this PR)_

### Solutions

_(none in this PR)_

### Extensions

- [`lecture_04_B03_09_Transformer_InContext_AR1.ipynb`](notebooks/extensions/lecture_04_B03_09_Transformer_InContext_AR1.ipynb)

## Checkpoint

> Reproduce double descent on a small synthetic dataset and compare MLP/LSTM/Transformer on Edgeworth cycles.

## Readings

- [`readings/links_by_lecture/lecture_04_B03.md`](../../readings/links_by_lecture/lecture_04_B03.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- **Previous:** [Lecture 03 (B02): Training neural networks](../lecture_03_B02_training_neural_networks/README.md)
- **Next:** [Lecture 05 (B04): Function approximation and loss design](../lecture_05_B04_function_approximation_loss_design/README.md)
- [Course map](../../COURSE_MAP.md)
- [Repository home](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written / graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
