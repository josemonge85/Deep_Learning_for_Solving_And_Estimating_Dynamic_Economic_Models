# Course map

A walk-through of the 18-lecture sequence.

> For the public README portal, see [`README.md`](README.md). For the chapter-based companion text, see [`lecture_script/Deep_Learning_for_Solving_And_Estimating_Dynamic_Economic_Models.pdf`](lecture_script/Deep_Learning_for_Solving_And_Estimating_Dynamic_Economic_Models.pdf).

## Conventions

- **Lecture label** (`Lecture XX`): student-facing identifier; matches the folder name `lectures/lecture_XX_*/`.
- **Compute tier**: `cpu-light` (laptop, minutes), `cpu-standard` (laptop, tens of minutes), `gpu-recommended` (a few minutes on GPU, longer on CPU; smoke mode runs on CPU), `gpu-required` (CPU does not finish in a reasonable time).
- **Time budget**: `short` (≤ 1 h with hands-on), `standard` (~ 2-3 h), `long` (half-day or more).

## Course-flow diagram

```mermaid
flowchart LR
  L01[L01<br/>Python primer] --> L02
  L02[L02<br/>Intro to DL] --> L03
  L02 --> L14
  L03[L03<br/>DEQNs] --> L04
  L03 --> L07
  L04[L04<br/>IRBC] --> L05
  L05[L05<br/>NAS / Loss bal.] --> L06
  L06[L06<br/>Agentic programming] --> L07
  L07[L07<br/>Autodiff] --> L08
  L07 --> L09
  L07 --> L11
  L07 --> L16
  L08[L08<br/>Sequence-space] --> L18
  L09[L09<br/>OLG] --> L10
  L10[L10<br/>Heterog. agents / Young] --> L18
  L11[L11<br/>PINNs] --> L12
  L12[L12<br/>CT-HA theory] --> L13
  L13[L13<br/>CT-HA numerics] --> L14
  L14[L14<br/>Surrogates / GPs] --> L15
  L15[L15<br/>SMM] --> L18
  L16[L16<br/>Climate / IAMs] --> L17
  L17[L17<br/>Deep UQ + Pareto policy] --> L18
  L18[L18<br/>Wrap-up]

  style L06 fill:#fff3cd,stroke:#856404
```

## At-a-glance table

| # | Title | Compute | Time | Prereqs |
|---:|---|---|---|---|
| 01 | Python primer | cpu-light | short | — |
| 02 | Introduction to deep learning | cpu-standard | long | L01 |
| 03 | Deep Equilibrium Nets | cpu-standard | long | L02 |
| 04 | IRBC with DEQNs | gpu-recommended | long | L03 |
| 05 | Architecture search and loss balancing | gpu-recommended | long | L04 |
| **06** | **Agentic programming** | **cpu-light** | **long** | **L05** |
| 07 | Automatic differentiation for DEQNs | cpu-standard | standard | L03 |
| 08 | Sequence-space DEQNs | gpu-recommended | long | L07 |
| 09 | OLG models with DEQNs | gpu-recommended | long | L07 |
| 10 | Heterogeneous agents and Young's method | gpu-recommended | long | L09 |
| 11 | Physics-informed neural networks | cpu-standard | long | L07 |
| 12 | Continuous-time HA, theory | cpu-light | standard | L11 |
| 13 | Continuous-time HA, numerics | gpu-recommended | long | L12 |
| 14 | Surrogates and Gaussian processes | gpu-recommended | long | L02 |
| 15 | Structural estimation via SMM | cpu-standard | long | L14 |
| 16 | Climate economics and IAMs | gpu-recommended | long | L07 |
| 17 | Deep UQ and Pareto-improving climate policy | gpu-recommended | long | L16 |
| 18 | Course wrap-up | cpu-light | short | L17 |

## Recommended learning paths

### Complete path (self-study)

```
L01 → L02 → L03 → L04 → L05 → L06 (agentic programming)
   → L07 → L08 → L09 → L10 → L11 → L12 → L13
   → L14 → L15 → L16 → L17 → L18
```

### Core DEQN path

```
L01 → L02 → L03 → L04 → L05 → L07 → L08 → L09 → L10 → L18
```

### Continuous-time / PINN path

```
L01 → L02 → L03 → L07 → L11 → L12 → L13 → L18
```

### Surrogates, GPs, and estimation path

```
L01 → L02 → L14 → L15 → L18
```

### Climate and deep-UQ path

```
L01 → L02 → L03 → L07 → L14 → L16 → L17 → L18
```

## Decision guide for method choice

| Problem feature | Recommended method | Lectures |
|---|---|---|
| Recursive equilibrium with explicit Euler residuals | DEQN | L03–L10 |
| ODE/PDE in time or in a low-D state space | PINN | L11–L13 |
| Expensive simulator that must be queried often | Deep surrogate | L14, L15, L17 |
| Smooth low/medium-D function with uncertainty quantification | Gaussian process | L14 |
| Continuous-time heterogeneous agents (HJB + KFE) | PINN or finite difference | L12–L13 |
| Structural estimation with implicit moments | Surrogate-based SMM | L15 |
| Long-horizon climate-economy with deep uncertainty | DEQN + deep UQ + GP | L16, L17 |

## Compute and reproducibility notes

- Every notebook exposes `RUN_MODE = "smoke" | "teaching" | "production"` and `SEED = 0` at the top. Smoke mode bounds epochs, batch size, and sample size for low-spec laptops; teaching mode produces classroom-quality figures; production mode reproduces high-quality results and may require GPU.
- Reproduce the environment via `requirements.txt` or `environment.yml`.
- Notebook outputs are preserved as published; no re-execution is needed to read along.
