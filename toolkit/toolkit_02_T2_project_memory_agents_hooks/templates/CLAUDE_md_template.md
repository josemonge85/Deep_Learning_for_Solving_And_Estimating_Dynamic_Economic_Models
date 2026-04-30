# CLAUDE.md -- Fiscal Multipliers in a Heterogeneous-Agent Framework

## Project Overview
- **Topic:** Estimating state-dependent fiscal multipliers using a heterogeneous-agent New Keynesian (HANK) model calibrated to U.S. quarterly data (1966Q1--2019Q4).
- **Stage:** Revision (R&R at Review of Economic Studies)
- **Target journal:** Review of Economic Studies
- **Co-authors:** Jane Doe (MIT), John Smith (LSE)
- **Last updated:** 2026-03-31

## Repository Structure
```
data/
  raw/            <- READ ONLY. Never modify. BLS/FRED downloads.
  processed/      <- Cleaned panels, merged datasets
  simulated/      <- Model-generated data (overwritten by code)
code/
  calibrate.py    <- Calibration targets and steady-state solver
  estimate.py     <- Main estimation (SMM + neural surrogate)
  simulate.py     <- Impulse responses and counterfactuals
  utils.py        <- Shared helpers (IO, plotting defaults)
  config.py       <- All hyperparameters and file paths
figures/          <- Publication-quality figures (PDF only)
paper/
  main.tex        <- Main manuscript
  appendix.tex    <- Online appendix
  tables/         <- Generated LaTeX tables (do not hand-edit)
  bib/            <- BibTeX files
results/          <- JSON/pickle outputs from estimation
notes/            <- Session logs, TODOs, referee memos
tests/            <- pytest test suite
```

## Coding Standards
- Python 3.11+; type hints on all function signatures
- `pathlib.Path` for all file I/O -- never use string concatenation for paths
- Random seeds: always set via `config.SEED` (currently 42)
- Style: PEP 8, max line length 88 (Black formatter)
- No `print()` inside library functions -- use `logging` module
- Docstrings: NumPy style for all public functions
- Imports: standard library, then third-party, then local (isort order)
- Never use `from module import *`

## Package Environment
- Virtual environment managed by `uv` at `.venv/`
- Activate: `source .venv/bin/activate`
- Key packages: numpy, scipy, pandas, matplotlib, jax, jaxlib, pyfixest, linearmodels
- Install new packages: `uv add <package>` (updates pyproject.toml automatically)
- Lock file: `uv.lock` -- commit after any dependency change

## Statistical Conventions
- Standard errors: clustered at the state level (51 clusters) in all micro regressions
- Fixed effects: two-way (state + quarter) in baseline specification
- Confidence intervals: 90% for impulse responses, 95% for regression coefficients
- Outcome variable: real GDP growth (annualized, log difference x 400)
- Treatment: government spending shock identified via Blanchard-Perotti (2002) timing
- Bootstrap: block bootstrap with block length = 8 quarters, 1000 replications

## Notation (matches paper/main.tex)
- i = state, t = quarter
- Y_{it} = real GDP growth, G_{it} = government spending-to-GDP ratio
- beta_1 = fiscal multiplier (coefficient of interest)
- Phi(x) = neural network surrogate for the policy function
- theta = structural parameters (calibrated or estimated)

## Current Status
**UPDATE THIS EVERY SESSION**
- Current task: Revising Table 3 per referee comment #7 (add pre-trend test)
- Last thing done: Re-estimated baseline with updated BLS data through 2019Q4
- Next step: Run placebo test (randomize treatment timing) and add to appendix
- Blockers: Waiting on co-author to confirm new calibration targets

## Do Not Touch
- `data/raw/` -- original downloads; re-downloading changes checksums
- `estimate.py` main() function signature -- called by HPC batch scripts
- `paper/bib/references.bib` -- managed by Zotero export; edit in Zotero only
- `.github/workflows/` -- CI pipeline; discuss changes with all co-authors first

## Decisions Made (and Why)
- 2026-01-15: Switched from TensorFlow to JAX for 3x speedup on GPU cluster
- 2026-02-03: Dropped pre-1966 data (structural break in fiscal reporting)
- 2026-02-20: Changed clustering from county to state (too few obs per county)
- 2026-03-10: Added neural surrogate for policy function (referee suggestion #4)
- 2026-03-25: Fixed off-by-one in quarter indexing (shifted IRFs by one period)
