#!/usr/bin/env python3
"""Normalize the introductory markdown cell of every course notebook.

The unified header layout, beneath the existing H1, is:

    *Companion notebook to **Day N — <day name>** (Chapter X of the lecture script).*

    *Author: Simon Scheidegger (HEC Lausanne) — [course repository](https://github.com/sischei/Deep_Learning_for_Solving_And_Estimating_Dynamic_Economic_Models).*

    [*Adapted from earlier work by …; gratefully acknowledged.*]   ← only when applicable

The H1 title and the rest of the notebook (other markdown cells, code, outputs,
metadata) are preserved verbatim. Any pre-existing metadata block immediately
under the H1 is detected and replaced rather than duplicated.

Usage:
    python tools/normalize_headers.py            # dry run, prints unified diffs
    python tools/normalize_headers.py --apply    # rewrite notebooks in place
    python tools/normalize_headers.py --notebook lectures/day1/code/01_BasicML_intro.ipynb

The two CSV inputs (chapter and attribution maps) sit next to this script.
"""

from __future__ import annotations

import argparse
import csv
import difflib
import glob
import os
import re
import sys
from pathlib import Path

import nbformat

REPO_ROOT = Path(__file__).resolve().parent.parent
CHAPTER_MAP_CSV = REPO_ROOT / "tools" / "notebook_chapter_map.csv"
ATTRIB_CSV = REPO_ROOT / "tools" / "notebook_attribution.csv"

REPO_URL = "https://github.com/sischei/Deep_Learning_for_Solving_And_Estimating_Dynamic_Economic_Models"

# Pre-existing metadata patterns (case-insensitive). A line matching any of
# these is treated as old metadata to drop, provided it sits in the run of
# lines immediately after the H1 (separated only by blanks or horizontal rules).
OLD_META_PATTERNS = [
    re.compile(r"^\*\*Course\b", re.I),
    re.compile(r"^\*\*Author\b", re.I),
    re.compile(r"^\*\*Day\b", re.I),
    re.compile(r"^\*\*Reference\b", re.I),
    re.compile(r"^\*\*Instructor\b", re.I),
    re.compile(r"^Notebook by ", re.I),
    re.compile(r"^By \[?Simon", re.I),
    re.compile(r"^\*Companion notebook", re.I),
    re.compile(r"^\*Author:", re.I),
    re.compile(r"^Deep Learning in Economics and Finance", re.I),
    re.compile(r"^---\s*$"),
    re.compile(r"^### A self-contained port", re.I),  # Day 8 nb 02 sub-title used as metadata anchor
]
# A line that is NOT old metadata (and not blank) ends the metadata run.


def load_chapter_map() -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    with CHAPTER_MAP_CSV.open() as f:
        for row in csv.DictReader(f):
            out[row["day_dir"]] = {
                "day_name": row["day_name"],
                "chapter_label": row["chapter_label"],
            }
    return out


def load_attrib_map() -> dict[str, str]:
    out: dict[str, str] = {}
    if not ATTRIB_CSV.exists():
        return out
    with ATTRIB_CSV.open() as f:
        for row in csv.DictReader(f):
            # Normalise to relative-to-repo POSIX paths.
            out[row["notebook_path"].strip()] = row["adapted_from_line"].strip()
    return out


def day_n_from_path(nb_path: Path) -> tuple[int, str]:
    """Return (day_number, day_dir) for a notebook path under lectures/dayN/code/."""
    for part in nb_path.parts:
        m = re.match(r"day(\d+)$", part)
        if m:
            return int(m.group(1)), part
    raise ValueError(f"cannot infer day from {nb_path}")


def split_first_md_cell(source: str) -> tuple[str, str, str]:
    """Split a markdown cell source into (preamble, h1_line, body).

    preamble is everything before the first H1 (usually empty).
    h1_line is the H1 line itself, including the leading "# ".
    body is everything after the H1 line, with one leading newline stripped.

    If no H1 is found, h1_line is empty and body equals source.
    """
    lines = source.splitlines()
    h1_idx = next(
        (i for i, ln in enumerate(lines) if ln.lstrip().startswith("# ")), None
    )
    if h1_idx is None:
        return source, "", ""
    preamble = "\n".join(lines[:h1_idx])
    h1_line = lines[h1_idx]
    body = "\n".join(lines[h1_idx + 1 :])
    if body.startswith("\n"):
        body = body[1:]
    return preamble, h1_line, body


GLOBAL_DROP_PATTERNS = [
    # Legacy single-line author attributions that recur across the course.
    re.compile(r"^Notebook by .*", re.I),
    re.compile(r"^By \[?Simon Scheidegger\]?.*", re.I),
    re.compile(r"^\*\*Author\*\*:.*", re.I),
    re.compile(r"^\*\*Course\*\*:.*", re.I),
    re.compile(r"^\*\*Instructor\*\*:.*", re.I),
    re.compile(r"^\*\*Day\b.*", re.I),
    re.compile(r"^\*\*Reference\*\*:.*", re.I),
    # Standalone course-attribution banners that reference Geneva
    re.compile(r"^\*\*Deep Learning .*Geneva.*\*\*\s*$", re.I),
    re.compile(r"^\*Deep Learning .*Geneva.*\*\s*$", re.I),
    re.compile(r"^\*\*Deep Learning .*Geneva.*$", re.I),
    re.compile(r"^Deep Learning .*Geneva.*$", re.I),
    re.compile(r"^\(University of Geneva.*\)\.?\s*$", re.I),
]

# Embedded "University of Geneva" parentheticals or trailing fragments removed
# from any markdown cell text (not just standalone lines).
GENEVA_INLINE_SUBS = [
    (re.compile(r",?\s*University of Geneva,\s*April/May\s*2026", re.I), ""),
    (re.compile(r"\s*\(University of Geneva,\s*\d{4}\)", re.I), ""),
    (re.compile(r",\s*University of Geneva,\s*\d{4}", re.I), ""),
    (re.compile(r"\s+—\s*University of Geneva,\s*\d{4}", re.I), ""),
    (re.compile(r"\s+--\s*University of Geneva,\s*\d{4}", re.I), ""),
]


def strip_old_metadata(body: str) -> str:
    """Drop pre-existing metadata lines.

    Step 1: walk lines from the top of the body, skipping blanks; drop lines
    that match OLD_META_PATTERNS, stop at the first non-matching non-blank
    line, and trim the leading blanks that remain.

    Step 2: anywhere in the rest of the body, drop standalone lines matching
    GLOBAL_DROP_PATTERNS (legacy author/course/instructor lines that may
    survive after a subheading).
    """
    lines = body.splitlines()
    # Step 1: top-of-body strip.
    i = 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1
            continue
        if any(p.match(ln) for p in OLD_META_PATTERNS):
            i += 1
            continue
        break
    while i < len(lines) and not lines[i].strip():
        i += 1
    rest = lines[i:]

    # Step 2: global single-line drop of legacy attributions.
    cleaned: list[str] = []
    for ln in rest:
        if any(p.match(ln) for p in GLOBAL_DROP_PATTERNS):
            continue
        cleaned.append(ln)

    # Collapse runs of >=2 blank lines that the global drop may have created.
    out: list[str] = []
    blank_run = 0
    for ln in cleaned:
        if ln.strip():
            blank_run = 0
            out.append(ln)
        else:
            blank_run += 1
            if blank_run < 2:
                out.append(ln)
    while out and not out[0].strip():
        out.pop(0)
    while out and not out[-1].strip():
        out.pop()
    return "\n".join(out)


def build_header(
    nb_rel_path: str,
    h1_line: str,
    cleaned_body: str,
    chapter_map: dict[str, dict[str, str]],
    attrib_map: dict[str, str],
) -> str:
    nb_path = Path(nb_rel_path)
    day_n, day_dir = day_n_from_path(nb_path)
    info = chapter_map[day_dir]
    day_name = info["day_name"]
    chapter_label = info["chapter_label"]

    pieces = [h1_line, ""]
    pieces.append(
        f"*Companion notebook to **Day {day_n} — {day_name}** "
        f"({chapter_label} of the lecture script).*"
    )
    pieces.append("")
    pieces.append(
        f"*Author: Simon Scheidegger (HEC Lausanne and Grantham Institute, LSE) — "
        f"[course repository]({REPO_URL}).*"
    )
    if nb_rel_path in attrib_map:
        pieces.append("")
        pieces.append(f"*{attrib_map[nb_rel_path]}*")
    if cleaned_body:
        pieces.append("")
        pieces.append(cleaned_body)
    return "\n".join(pieces).rstrip() + "\n"


def find_first_md_index(nb) -> int | None:
    for i, c in enumerate(nb.cells):
        if c.cell_type == "markdown":
            return i
    return None


def scrub_geneva_from_markdown(source: str) -> str:
    """Remove standalone Geneva attribution lines and trim embedded mentions."""
    lines = source.splitlines()
    out: list[str] = []
    for ln in lines:
        # Standalone Geneva-banner line: drop entirely.
        if any(p.match(ln) for p in GLOBAL_DROP_PATTERNS) and "Geneva" in ln:
            continue
        new_ln = ln
        for rx, repl in GENEVA_INLINE_SUBS:
            new_ln = rx.sub(repl, new_ln)
        out.append(new_ln)
    # Collapse runs of >=2 blank lines.
    collapsed: list[str] = []
    blank_run = 0
    for ln in out:
        if ln.strip():
            blank_run = 0
            collapsed.append(ln)
        else:
            blank_run += 1
            if blank_run < 2:
                collapsed.append(ln)
    return "\n".join(collapsed)


def process_notebook(
    nb_path: Path,
    chapter_map: dict[str, dict[str, str]],
    attrib_map: dict[str, str],
    apply: bool,
) -> tuple[str, str, str]:
    """Return (status, old_first_cell, new_first_cell).

    status is one of: 'rewrite', 'no-change', 'no-h1'.
    """
    rel = str(nb_path.relative_to(REPO_ROOT))
    nb = nbformat.read(str(nb_path), as_version=4)
    idx = find_first_md_index(nb)
    if idx is None:
        return "no-h1", "", ""
    original = nb.cells[idx].source
    _, h1_line, body = split_first_md_cell(original)
    if not h1_line:
        # No H1 to anchor the unified header; only do the Geneva sweep.
        geneva_changed = False
        for c in nb.cells:
            if c.cell_type != "markdown":
                continue
            scrubbed = scrub_geneva_from_markdown(c.source)
            if scrubbed != c.source:
                c.source = scrubbed
                geneva_changed = True
        if geneva_changed and apply:
            nbformat.write(nb, str(nb_path), version=nbformat.NO_CONVERT)
        return ("rewrite" if geneva_changed else "no-h1"), original, nb.cells[idx].source
    cleaned = strip_old_metadata(body)
    new = build_header(rel, h1_line, cleaned, chapter_map, attrib_map)
    if new.rstrip() == original.rstrip():
        return "no-change", original, new
    # Geneva sweep across ALL markdown cells (including the first, post-header).
    nb.cells[idx].source = new
    geneva_changed = False
    for c in nb.cells:
        if c.cell_type != "markdown":
            continue
        scrubbed = scrub_geneva_from_markdown(c.source)
        if scrubbed != c.source:
            c.source = scrubbed
            geneva_changed = True
    new_first = nb.cells[idx].source

    if apply:
        nbformat.write(nb, str(nb_path), version=nbformat.NO_CONVERT)
    if new_first.rstrip() == original.rstrip() and not geneva_changed:
        return "no-change", original, new_first
    return "rewrite", original, new_first


def discover_notebooks(repo_root: Path, override: str | None) -> list[Path]:
    if override:
        p = repo_root / override if not Path(override).is_absolute() else Path(override)
        return [p]
    pattern = str(repo_root / "lectures" / "day*" / "code" / "*.ipynb")
    found = sorted(Path(p) for p in glob.glob(pattern))
    return [
        p
        for p in found
        if "archive" not in p.parts and not p.name.endswith("_codex.ipynb")
    ]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument(
        "--apply",
        action="store_true",
        help="Rewrite notebooks in place (default: dry-run, prints diffs).",
    )
    ap.add_argument(
        "--notebook",
        help="Process a single notebook by path (relative to repo root or absolute).",
    )
    ap.add_argument(
        "--no-diff",
        action="store_true",
        help="Suppress per-notebook diffs in dry-run; just print the summary.",
    )
    args = ap.parse_args()

    chapter_map = load_chapter_map()
    attrib_map = load_attrib_map()

    targets = discover_notebooks(REPO_ROOT, args.notebook)

    rewrites: list[Path] = []
    no_change: list[Path] = []
    no_h1: list[Path] = []

    for nb_path in targets:
        try:
            status, old, new = process_notebook(
                nb_path, chapter_map, attrib_map, apply=args.apply
            )
        except Exception as exc:
            print(f"ERROR processing {nb_path}: {exc}", file=sys.stderr)
            continue
        if status == "rewrite":
            rewrites.append(nb_path)
            if not args.apply and not args.no_diff:
                rel = nb_path.relative_to(REPO_ROOT)
                diff = difflib.unified_diff(
                    old.splitlines(keepends=True),
                    new.splitlines(keepends=True),
                    fromfile=f"a/{rel} (first md cell, before)",
                    tofile=f"b/{rel} (first md cell, after)",
                )
                sys.stdout.write("".join(diff))
                sys.stdout.write("\n")
        elif status == "no-change":
            no_change.append(nb_path)
        elif status == "no-h1":
            no_h1.append(nb_path)

    print("\n=== Summary ===")
    verb = "rewritten" if args.apply else "would be rewritten"
    print(f"{len(rewrites):3d} notebooks {verb}.")
    print(f"{len(no_change):3d} notebooks already match the canonical header.")
    print(f"{len(no_h1):3d} notebooks skipped (no H1 found):")
    for p in no_h1:
        print(f"    - {p.relative_to(REPO_ROOT)}")
    n_attrib = sum(1 for p in rewrites if str(p.relative_to(REPO_ROOT)) in attrib_map)
    print(f"{n_attrib:3d} notebooks carry an 'Adapted from …' line.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
