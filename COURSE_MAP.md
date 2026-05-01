# Course map

A walk-through of the 17-lecture sequence and the 3-toolkit track.

> For the public README portal, see [`README.md`](README.md). For the
> chapter-based companion text, see
> [`lecture_script/lecture_script.pdf`](lecture_script/lecture_script.pdf).

## Conventions

- **Lecture label** (`Lecture XX`): student-facing identifier, used everywhere outside the script.
- **Block ID** (`BYY`): canonical lecture identifier shared with the lecture script's lecture index. Block IDs are stable across renumbering.
- **Toolkit blocks** (`T1`, `T2`, `T3`): cross-cutting research-workflow modules. Not part of the lecture script. Strongly recommended even for readers on the Core DEQN path.
- **Compute tier**: `cpu-light` (laptop, minutes), `cpu-standard` (laptop, tens of minutes), `gpu-recommended` (a few minutes on GPU, longer on CPU; smoke mode runs on CPU), `gpu-required` (CPU does not finish in a reasonable time).
- **Time budget**: `short` (≤ 1 h with hands-on), `standard` (~ 2-3 h), `long` (half-day or more).

## Course-flow diagram

```mermaid
flowchart LR
  L01[L01 B00<br/>Orientation] --> L02
  L02[L02 B01<br/>Intro to DL] --> L03
  L02 --> L13
  L03[L03 B02<br/>DEQNs] --> L04
  L03 --> L06
  L04[L04 B03<br/>IRBC] --> L05
  L05[L05 B04<br/>NAS / Loss bal.] --> T1[T1<br/>Agentic loop]
  L06[L06 B05<br/>Autodiff] --> L07
  L06 --> L08
  L06 --> L10
  L06 --> L15
  L07[L07 B06<br/>Sequence-space] --> L17
  L08[L08 B07<br/>OLG] --> L09
  L09[L09 B08<br/>Heterog. agents / Young] --> L17
  L10[L10 B09<br/>PINNs] --> L11
  L11[L11 B10<br/>CT-HA theory] --> L12
  L12[L12 B11<br/>CT-HA numerics] --> T2[T2<br/>Project memory]
  T2 --> T3[T3<br/>Agentic exercises]
  L13[L13 B12<br/>Surrogates / GPs] --> L14
  L14[L14 B13<br/>SMM] --> L17
  L15[L15 B14<br/>Climate / IAMs] --> L16
  L16[L16 B15<br/>Deep UQ + Pareto policy] --> L17
  L17[L17 B16<br/>Wrap-up]

  style T1 fill:#fff3cd,stroke:#856404
  style T2 fill:#fff3cd,stroke:#856404
  style T3 fill:#fff3cd,stroke:#856404
```

## At-a-glance table

| # | Block | Title | Compute | Time | Prereqs |
|---:|---|---|---|---|---|
| 01 | B00 | Orientation, setup, reproducibility | cpu-light | short | — |
| 02 | B01 | Introduction to deep learning | cpu-standard | long | B00 |
| 03 | B02 | Deep Equilibrium Nets | cpu-standard | long | B01 |
| 04 | B03 | IRBC with DEQNs | gpu-recommended | long | B02 |
| 05 | B04 | Architecture search and loss balancing | gpu-recommended | long | B03 |
| **T1** | **T1** | **Toolkit, agentic research-coding loop** | **cpu-light** | **standard** | **B04** |
| 06 | B05 | Automatic differentiation for DEQNs | cpu-standard | standard | B02 |
| 07 | B06 | Sequence-space DEQNs | gpu-recommended | long | B05 |
| 08 | B07 | OLG models with DEQNs | gpu-recommended | long | B05 |
| 09 | B08 | Heterogeneous agents and Young's method | gpu-recommended | long | B07 |
| 10 | B09 | Physics-informed neural networks | cpu-standard | long | B05 |
| 11 | B10 | Continuous-time HA, theory | cpu-light | standard | B09 |
| 12 | B11 | Continuous-time HA, numerics | gpu-recommended | long | B10 |
| **T2** | **T2** | **Toolkit, project memory, agents, hooks** | **cpu-light** | **standard** | **B11** |
| **T3** | **T3** | **Toolkit, agentic-programming exercise handout** | **cpu-light** | **standard** | **T2** |
| 13 | B12 | Surrogates and Gaussian processes | gpu-recommended | long | B01 |
| 14 | B13 | Structural estimation via SMM | cpu-standard | long | B12 |
| 15 | B14 | Climate economics and IAMs | gpu-recommended | long | B05 |
| 16 | B15 | Deep UQ and Pareto-improving climate policy | gpu-recommended | long | B14 |
| 17 | B16 | Course wrap-up | cpu-light | short | B15 |

## Recommended learning paths

### Complete path (recommended for self-study)

Includes all three toolkit modules.

```
L01 → L02 → L03 → L04 → L05 → T1
   → L06 → L07 → L08 → L09 → L10 → L11 → L12 → T2 → T3
   → L13 → L14 → L15 → L16 → L17
```

### Core DEQN path

```
L01 → L02 → L03 → L04 → L05 → L06 → L07 → L08 → L09 → L17
```

### Continuous-time / PINN path

```
L01 → L02 → L03 → L06 → L10 → L11 → L12 → L17
```

### Surrogates, GPs, and estimation path

```
L01 → L02 → L13 → L14 → L17
```

### Climate and deep-UQ path

```
L01 → L02 → L03 → L06 → L13 → L15 → L16 → L17
```

### Toolkit-only path (research workflow training)

```
T1 → T2 → T3
```

## Decision guide for method choice

| Problem feature | Recommended method | Lectures |
|---|---|---|
| Recursive equilibrium with explicit Euler residuals | DEQN | L03-L09 |
| ODE/PDE in time or in a low-D state space | PINN | L10-L12 |
| Expensive simulator that must be queried often | Deep surrogate | L13, L14, L16 |
| Smooth low/medium-D function with uncertainty quantification | Gaussian process | L13 |
| Continuous-time heterogeneous agents (HJB + KFE) | PINN or finite difference | L11-L12 |
| Structural estimation with implicit moments | Surrogate-based SMM | L14 |
| Long-horizon climate-economy with deep uncertainty | DEQN + deep UQ + GP | L15, L16 |

## Compute and reproducibility notes

- Every notebook exposes `RUN_MODE = "smoke" | "teaching" | "production"` and `SEED = 0` at the top. Smoke mode bounds epochs, batch size, and sample size for low-spec laptops; teaching mode produces classroom-quality figures; production mode reproduces high-quality results and may require GPU.
- Reproduce the environment via `requirements.txt` or `environment.yml`.
- Notebook outputs are preserved as published; no re-execution is needed to read along.
