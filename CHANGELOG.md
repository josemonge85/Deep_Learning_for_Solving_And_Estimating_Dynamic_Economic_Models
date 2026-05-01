# Changelog

All notable changes to this course repository will be documented here.

This project follows a loose version scheme tied to course revisions:
**v0.x.y** while the structure and content are still being polished;
**v1.0.0** when the public release is ready to advertise.

## Unreleased

Initial public reorganization of the Geneva 2026 mini-course into a
self-paced, lecture-numbered, open-source course.

### Added

- **30 lecture folders** (`lectures/lecture_XX_BYY_*`) and **2 toolkit
  folders** (`toolkit/toolkit_0{1,2}_T{1,2}_*`). Each lecture folder
  has its own `README.md`, `slides/`, `notebooks/{core,exercises,solutions,extensions}/`,
  `code/`, `figures/`, and `notes/`.
- **Per-lecture READMEs** with concrete learning goals, prerequisites
  (linked back to predecessor lectures), script reference, slide and
  notebook links, checkpoint task, and readings.
- **Top-level [`README.md`](README.md)** as a welcoming course portal:
  what you'll learn, how to use the course, a topic index that maps
  every method block to its lecture range, and a setup section.
- **[`COURSE_MAP.md`](COURSE_MAP.md)** with at-a-glance table,
  Mermaid prerequisite-chain diagram, six learning paths, and a
  decision guide for method choice.
- **`course.yml`** — canonical machine-readable course manifest.
- **`MATERIALS_CROSSWALK.md`** — full source-to-destination mapping
  for every migrated artefact.
- **Companion lecture script** (`lecture_script/`) with a
  chapter-to-lecture map (`script_to_lectures.md`) and a glossary
  stub.
- **Per-lecture reading-link files** (`readings/links_by_lecture/`)
  with curated bibliography cards.
- **Validation suite** (`scripts/validate_*.py`,
  `scripts/check_american_english.py`): five real, enforcing checks.
- **Build helpers** (`scripts/build_script.sh`, `scripts/build_slides.sh`).
- **Reusable teaching package skeleton** (`src/dlef/`).
- **Licensing files**: MIT for code (`LICENSE`), CC0 1.0 Universal for
  written content (`LICENSE-content.md`); `AUTHORS.md`, `CITATION.cff`,
  `NOTICE.md`.
- **`CONTRIBUTING.md`**.

### Migrated from the live-course source

- **68 notebooks** (56 lecture notebooks + 12 python-refresher
  notebooks), each stamped with the §1.6 lecture-header markdown cell
  and a `RUN_MODE = "smoke"` / `SEED = 0` code cell. Long-running
  notebooks additionally got a smoke-mode advisory.
  Notebooks were **not re-executed** during migration; existing cell
  outputs are preserved verbatim.
- **122 slide PDFs** with 19 LaTeX sources patched: title now reads
  `Lecture XX (BYY): <topic>` (or `Toolkit T1/T2`); no Geneva
  branding, no live-course dates, no "Day N" pointers in deck bodies.
- **Lecture script PDF + LaTeX**, bibliography (`bib_econ.bib` →
  `readings/bibliography.bib`), hero figure, course-overview asset.
- **Day 5 toolkit material** (slides, exercises, solutions, prompt
  pack, example skills, subagents, hooks, templates) split into
  Toolkit T1 and T2.
- **Python refresher** moved under
  [`lectures/lecture_01_B00_*/python_refresher/`](lectures/lecture_01_B00_orientation_setup_reproducibility/python_refresher/).

### Excluded (per the source README inclusion rule)

- All Codex experiment notebooks (`*_codex.ipynb`) and supporting
  research scripts (`train_codex_surrogate_*.py`, `dice_2p_*.py`,
  `dice_deqn_codex_lib.py`).
- Day-N recap decks (`00_Recap_DayN.pdf`) — live-class only; the
  30-lecture structure does not need cross-day recaps.
- LaTeX build artefacts, `.claude/` agent state, alternative cover
  designs, private working notes (`suggestion.md`, `TODO_review.md`,
  `codex_results/`).
- Reading PDFs are linked rather than redistributed by default.

### Notes

- The course platform of record is **Nuvolos Cloud** for enrolled
  students (pre-configured environment); self-study readers can
  reproduce locally via `requirements.txt` or `environment.yml`.
- Course author: **Simon Scheidegger** (University of Lausanne).
  Paper co-authors of references are not course-material co-authors.
