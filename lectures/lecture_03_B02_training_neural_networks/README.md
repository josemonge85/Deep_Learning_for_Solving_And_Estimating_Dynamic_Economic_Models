# Lecture 03 (B02): Training neural networks

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance
> **Course author:** Simon Scheidegger
> **Compute tier:** `cpu-standard` &nbsp;·&nbsp; **Time budget:** `standard`

## Learning goal

Understand how neural networks are trained: SGD and its variants, backpropagation, the role of depth and width, and how to monitor training in practice. By the end you can implement SGD by hand, build a small MLP in both TensorFlow and PyTorch, and instrument a training run with TensorBoard.

## Prerequisites

- [Lecture 02 (B01)](../lecture_02_B01_why_deep_learning/README.md) — Why deep learning for economics and finance?

## External prerequisites

- Python 3.10+ environment (`requirements.txt` at repo root, or run on the course platform).
- Familiarity with the math listed under **Script reference** below.

## Script reference

- §1.5-1.9 (Optimization, depth, regularization)
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md) — full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf) — companion script

## Slides

- [`02_Training_Neural_Networks.pdf`](slides/02_Training_Neural_Networks.pdf) — perceptron, multilayer networks, gradient descent / SGD, backprop, optimizers, batch normalization, software ecosystem.

## Notebooks

### Core

- [`lecture_03_B02_02_GradientDescent_and_StochasticGradientDescent.ipynb`](notebooks/core/lecture_03_B02_02_GradientDescent_and_StochasticGradientDescent.ipynb)
- [`lecture_03_B02_04_Gentle_DNN.ipynb`](notebooks/core/lecture_03_B02_04_Gentle_DNN.ipynb)
- [`lecture_03_B02_06_PyTorch_intro.ipynb`](notebooks/core/lecture_03_B02_06_PyTorch_intro.ipynb)

### Exercises

_(none in this PR)_

### Solutions

_(none in this PR)_

### Extensions

- [`lecture_03_B02_05_Tensorboard.ipynb`](notebooks/extensions/lecture_03_B02_05_Tensorboard.ipynb)

## Checkpoint

> Implement SGD by hand and reproduce the loss-curve behavior of an MLP on a simple regression task.

## Readings

- [`readings/links_by_lecture/lecture_03_B02.md`](../../readings/links_by_lecture/lecture_03_B02.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- [`COURSE_MAP.md`](../../COURSE_MAP.md)
- [`README.md`](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written / graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
