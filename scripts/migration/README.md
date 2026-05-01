# Migration helpers

One-off scripts used to convert the live Geneva 2026 source repository
into the public 30-lecture + 2-toolkit structure. They are checked in
for reproducibility (so the splits can be re-derived) but are not part
of the daily-use tooling.

For day-to-day work use the validators and build helpers one level up:

- `scripts/validate_*.py` — five enforcing checks; run via `make validate`.
- `scripts/check_american_english.py` — spelling pass; also part of `make validate`.
- `scripts/build_script.sh`, `scripts/build_slides.sh` — LaTeX builds.
- `scripts/run_all_smoke_tests.py` — notebook smoke harness (stub; gated
  on the upcoming `RUN_MODE = "smoke"` switches).

## What lives here

- `_split_intro_deck.py`, `_split_remaining_decks.py` — frame-range
  splitters that carved the seven multi-lecture source decks into the
  20 per-lecture decks under `lectures/lecture_*/slides/`.
- `_patch_slide_headers.py` — removed `Day N` / `University of Geneva`
  branding from the 19 source `.tex` files.
- `_render_lecture_readmes.py` — generated the per-lecture `README.md`
  stubs from `course.yml` plus a learning-goals dictionary.
- `_render_reading_links.py` — generated `readings/links_by_lecture/`
  files from `bibliography.bib`.
- `_stamp_notebook_headers.py` — first-pass §1.6 lecture-header stamp
  on the 68 migrated notebooks. (The May 7 scheduled remote agent runs
  a thorough second pass that also adds `RUN_MODE`/`SEED` cells and
  smoke-mode bounds.)
- `normalize_headers.py`, `notebook_attribution.csv`,
  `notebook_chapter_map.csv` — utilities and reference tables carried
  over from `tools/` in the source repo.
