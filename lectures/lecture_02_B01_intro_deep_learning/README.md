# Lecture 02 (B01): Introduction to deep learning

The working knowledge of deep learning that the rest of the course assumes, with economics-flavoured worked examples throughout.

`cpu-standard` · `long` · builds on [Lecture 01 (B00)](../lecture_01_B00_python_primer/README.md)

> 📑 **Slides:** [01_Intro_to_DeepLearning.pdf](slides/01_Intro_to_DeepLearning.pdf)  
> 📓 **Notebooks:** [start here](code/lecture_02_B01_01_BasicML_intro.ipynb) (9 in [`code/`](code/))  
> 📚 **Further reading:** [curated list](../../readings/links_by_lecture/lecture_02_B01.md)  
> 📖 **Script:** §1.1-1.4 (Foundations and function approximation), §1.5-1.9 (Optimization, depth, and regularization), §1.10-1.11 (Generalization, sequence models)

## What this lecture covers

- **Classical ML and the bias-variance trade-off.** Linear regression, classification, and unsupervised learning as a foundation for everything that follows.
- **Stochastic gradient descent.** SGD, mini-batches, momentum, and adaptive variants (Adam, RMSProp); when each one is the right default.
- **Deep neural networks.** Depth, width, activation choices, and the **double-descent** phenomenon on a controlled synthetic example.
- **Sequence models.** MLPs, LSTMs, and small Transformers compared on Edgeworth-cycle data, exposing the **memory ladder** of architectures.
- **Tooling.** TensorFlow and PyTorch side by side, plus TensorBoard for instrumenting a training run.

## Learning objectives

After this lecture you can:

- Implement SGD by hand and explain mini-batch, momentum, and adaptive variants.
- Train an MLP and a deep neural network end-to-end in TensorFlow and in PyTorch.
- Reproduce double descent on a controlled synthetic problem.
- Compare MLP, LSTM, and small-Transformer architectures on Edgeworth-cycle data and read off the memory ladder.
- Use TensorBoard to instrument a training run.

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

## In the lecture script

§1.1-1.4 (Foundations and function approximation), §1.5-1.9 (Optimization, depth, and regularization), §1.10-1.11 (Generalization, sequence models). The full chapter map is in [`script_to_lectures.md`](../../lecture_script/script_to_lectures.md).

## Readings

Curated bibliography for this lecture: [`lecture_02_B01.md`](../../readings/links_by_lecture/lecture_02_B01.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).

---

| ← Previous | Next → |
|---|---|
| [**Lecture 01: Python primer**](../lecture_01_B00_python_primer/README.md)<br><sub>Jupyter, basic data structures, NumPy, plotting, classes</sub> | [**Lecture 03: Deep Equilibrium Nets**](../lecture_03_B02_deep_equilibrium_nets/README.md)<br><sub>Brock-Mirman (deterministic, stochastic), Fischer-Burmeister constraints, six loss kernels</sub> |

[↑ Course map](../../COURSE_MAP.md)
