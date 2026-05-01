# Migration helpers

One-off scripts used to convert the live Geneva 2026 source repository
into the public 17-lecture plus 3-toolkit structure. They are checked
in for reproducibility, but are not part of the daily-use tooling.

For day-to-day work use the validators and build helpers one level up:

- `scripts/validate_*.py`, six enforcing checks; run via `make validate`.
- `scripts/check_american_english.py`, spelling pass; also part of `make validate`.
- `scripts/build_script.sh`, `scripts/build_slides.sh`, LaTeX builds.
- `scripts/run_all_smoke_tests.py`, notebook smoke harness (stub; gated on the `RUN_MODE = "smoke"` switches).

## What lives here

- `_consolidate_lectures.py`, the consolidation script that re-coarsened the destination tree from 30 lecture folders to 17, relocating notebooks and deleting fragment folders. Single-shot; not idempotent.
- `_strip_about_lecture_frame.py`, removes the splitter-inserted "About this lecture" frame from each consolidated `.tex` deck.
- `_retitle_slides.py`, rewrites the `\title[...]{...}` and `\subtitle{...}` lines of every consolidated deck to the new lecture number, block, and title.
- `_render_lecture_readmes.py`, regenerates per-lecture `README.md` from `course.yml` plus a learning-goals dictionary keyed on the new block IDs.
- `_render_reading_links.py`, generated `readings/links_by_lecture/` files from `bibliography.bib`.
- `_refresh_notebook_headers.py`, refreshes the §1.6 lecture-header markdown cell of every first-party notebook so it matches the new lecture number, block, title, and script reference. Idempotent; does not execute notebooks.
- `_patch_slide_headers.py`, removed `Day N` / `University of Geneva` branding from the source `.tex` files.
- `_strip_live_class_artifacts.py`, removed Nuvolos refs, slot-time prefixes, and "this morning" phrasing from the destination decks.
- `_stamp_notebook_headers.py`, first-pass §1.6 lecture-header stamp on the 68 migrated notebooks (predecessor of `_refresh_notebook_headers.py`).
- `normalize_headers.py`, `notebook_attribution.csv`, `notebook_chapter_map.csv`, utilities and reference tables carried over from `tools/` in the source repo.
