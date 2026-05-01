# Contributing

Thanks for your interest in improving this course. Pull requests,
errata, and questions are all welcome.

## How to file an issue

Open an issue on
[GitHub](https://github.com/sischei/Deep_Learning_for_Solving_And_Estimating_Dynamic_Economic_Models/issues)
with:

- which lecture / notebook / slide deck it concerns (use the
  `Lecture XX (BYY)` form);
- what you expected and what you saw;
- if it is a code bug, the minimal reproducer (Python version, library
  versions, the smallest cell that fails).

## How to submit a pull request

1. Fork the repo and create a topic branch from `main`.
2. Make your changes. Keep PRs focused — one logical change per PR is
   easier to review.
3. **Run the validation suite** before pushing:
   ```bash
   python3 scripts/validate_headers.py
   python3 scripts/validate_no_private_paths.py
   python3 scripts/validate_landing_page_assets.py
   python3 scripts/check_american_english.py
   python3 scripts/validate_no_content_loss.py
   ```
   All five must pass.
4. Open the PR; describe what changed and why. Reference the lecture
   or block ID where applicable.

## House rules

- **Don't re-execute notebooks** as part of a structural edit
  (renaming, moving, or adding cells). Use `nbformat` to read/write
  programmatically. Existing cell outputs are part of the migration
  contract.
- **American English** in all student-facing materials. The
  `check_american_english.py` script flags common British spellings.
- **No live-class branding.** No "University of Geneva", "April
  2026", "Day 1/Day 2", etc. in student-facing files. Historical
  context lives only in `legacy/Geneva2026_TIMETABLE.md` and
  `MATERIALS_CROSSWALK.md`.
- **Borrowed material keeps its upstream notice verbatim.** See
  `NOTICE.md`.
- **Source code:** MIT. **Text / slides / figures:** CC0 1.0
  Universal. By contributing, you agree your contribution is licensed
  under the same terms.

## Reviewer checklist (suggested)

When you review a PR, run through these four perspectives:

- **Top editor:** notation consistent with the script; everything
  fits within page bounds; American English; no broken hyperlinks.
- **Mathematical economist:** equations and arguments are correct;
  no hand-waving where the script is rigorous.
- **Computational economist:** code runs in `RUN_MODE = "smoke"` on
  CPU; long-running paths are clearly documented; data dependencies
  are explicit.
- **Critical student:** prerequisites are honest; the learning goal
  is concrete and achievable from the materials provided.

## Where things live

See [`README.md`](README.md) for the user-facing repo tour and
[`COURSE_MAP.md`](COURSE_MAP.md) for the detailed map and learning
paths. The machine-readable course manifest is `course.yml`.
