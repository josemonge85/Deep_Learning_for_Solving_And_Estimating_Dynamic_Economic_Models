# Lecture 02 (B01): Introduction to deep learning

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance  \
> **Course author:** Simon Scheidegger  \
> **Compute tier:** `cpu-standard` &nbsp;·&nbsp; **Time budget:** `long`

## What this lecture covers

Build the working knowledge of deep learning that the rest of the course assumes: classical ML and the bias-variance trade-off; SGD and its variants; depth, width, and double descent; sequence models from MLPs through LSTMs to small Transformers, applied to economic time-series patterns. By the end you have built and trained models in both TensorFlow and PyTorch, and you can read the rest of the course's notebooks fluently.

## Slides

- [`slides/01_Intro_to_DeepLearning.pdf`](slides/01_Intro_to_DeepLearning.pdf)
- [`slides/01_Intro_to_DeepLearning.tex`](slides/01_Intro_to_DeepLearning.tex)

## Code

- [`code/SGD_data.txt`](code/SGD_data.txt)
- [`code/lecture_02_B01_01_BasicML_intro.ipynb`](code/lecture_02_B01_01_BasicML_intro.ipynb)
- [`code/lecture_02_B01_02_GradientDescent_and_StochasticGradientDescent.ipynb`](code/lecture_02_B01_02_GradientDescent_and_StochasticGradientDescent.ipynb)
- [`code/lecture_02_B01_03_Double_Descent.ipynb`](code/lecture_02_B01_03_Double_Descent.ipynb)
- [`code/lecture_02_B01_04_Gentle_DNN.ipynb`](code/lecture_02_B01_04_Gentle_DNN.ipynb)
- [`code/lecture_02_B01_05_Tensorboard.ipynb`](code/lecture_02_B01_05_Tensorboard.ipynb)
- [`code/lecture_02_B01_06_PyTorch_intro.ipynb`](code/lecture_02_B01_06_PyTorch_intro.ipynb)
- [`code/lecture_02_B01_07_Genz_Approximation_and_Loss_Functions.ipynb`](code/lecture_02_B01_07_Genz_Approximation_and_Loss_Functions.ipynb)
- [`code/lecture_02_B01_08_MLP_LSTM_Transformer_Edgeworth_Cycles.ipynb`](code/lecture_02_B01_08_MLP_LSTM_Transformer_Edgeworth_Cycles.ipynb)
- [`code/lecture_02_B01_09_Transformer_InContext_AR1.ipynb`](code/lecture_02_B01_09_Transformer_InContext_AR1.ipynb)

## Prerequisites

- [Lecture 01 (B00)](../lecture_01_B00_orientation_setup_reproducibility/README.md), Orientation, setup, and reproducibility

## Script reference

- §1.1-1.4 (Foundations and function approximation), §1.5-1.9 (Optimization, depth, and regularization), §1.10-1.11 (Generalization, sequence models)
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md), full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf), companion script

## Checkpoint

> Train an MLP, an LSTM, and a small Transformer on Edgeworth cycles, and read off the memory ladder.

## Readings

- [`readings/links_by_lecture/lecture_02_B01.md`](../../readings/links_by_lecture/lecture_02_B01.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- Previous: [Lecture 01 (B00), Orientation, setup, and reproducibility](../lecture_01_B00_orientation_setup_reproducibility/README.md)
- Next: [Lecture 03 (B02), Deep Equilibrium Nets](../lecture_03_B02_deep_equilibrium_nets/README.md)
- [`COURSE_MAP.md`](../../COURSE_MAP.md)
- [`README.md`](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written and graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
