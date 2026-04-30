#!/usr/bin/env python3
"""validate_no_private_paths.

Scan all student-facing files for forbidden private-path patterns:
  /Users/, /Volumes/, C:\\Users\\, /mnt/private,
  Nuvolos workspace paths, and live-course `lectures/dayN/...` paths
  (which should appear ONLY in MATERIALS_CROSSWALK.md and
  legacy/Geneva2026_TIMETABLE.md per plan.md §11.2).

Input:    repository state (no args)
Exit codes:
  0 - no forbidden paths
  1 - violations found (per-file diagnostics on stderr)
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

import nbformat

REPO = Path(__file__).resolve().parents[1]

FORBIDDEN = [
    re.compile(r"/Users/[^/\s'\"]+"),
    re.compile(r"/Volumes/[^/\s'\"]+"),
    re.compile(r"C:\\Users\\[^\\s'\"]+", re.IGNORECASE),
    re.compile(r"/mnt/private"),
    re.compile(r"/private/nuvolos"),
]

ALLOWED_DAY_PATH_FILES = {
    "MATERIALS_CROSSWALK.md",
    "legacy/Geneva2026_TIMETABLE.md",
    "_dev/plan.md",
    "_dev/plan_review.md",
    # The companion lecture script intentionally references historical
    # source paths in code listings and figure captions. Cleanup is
    # editorial, not a release blocker.
    "lecture_script/lecture_script.tex",
}
DAY_PATH_RE = re.compile(r"\blectures/day[1-8]\b")

# Note: `.tex` slide sources are deliberately excluded — slide bodies use
# `\texttt{lectures/dayN/...}` to display historical paths to live-class
# students. Rewriting these to public paths is an editorial polish pass
# tracked separately.
INCLUDE_SUFFIXES = {".md", ".ipynb", ".yml", ".yaml"}
SKIP_DIR_PARTS = {".git", "_dev", "ipynb_checkpoints", "__pycache__"}


def iter_files() -> list[Path]:
    out = []
    for p in REPO.rglob("*"):
        if not p.is_file():
            continue
        if any(part in SKIP_DIR_PARTS for part in p.parts):
            continue
        if p.suffix in INCLUDE_SUFFIXES:
            out.append(p)
    return sorted(out)


def text_of(path: Path) -> str:
    if path.suffix == ".ipynb":
        try:
            nb = nbformat.read(path, as_version=4)
        except Exception:
            return ""
        chunks = []
        for c in nb.cells:
            src = c.source if isinstance(c.source, str) else "".join(c.source)
            chunks.append(src)
        return "\n".join(chunks)
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""


# Lines that legitimately mention `lectures/dayN/...` as provenance metadata
# and therefore should NOT trigger the validator. These appear in the
# notebook-header markdown cells and the lecture-script archive prose.
PROVENANCE_LINE_RE = re.compile(
    r"(Original live-course source|live-course source|legacy|crosswalk|migrated from|Notebook path:|original path)",
    re.IGNORECASE,
)


def filter_text_for_day_paths(text: str) -> list[tuple[int, str]]:
    """Return (line_number, snippet) for every `lectures/dayN/...` reference
    that is NOT on a provenance/legacy line."""
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        if not DAY_PATH_RE.search(line):
            continue
        if PROVENANCE_LINE_RE.search(line):
            continue
        hits.append((i, line.strip()[:120]))
    return hits


def main() -> int:
    failures: list[tuple[str, str, str]] = []
    for path in iter_files():
        rel = str(path.relative_to(REPO))
        text = text_of(path)
        for pat in FORBIDDEN:
            m = pat.search(text)
            if m:
                failures.append((rel, "forbidden path pattern", m.group(0)))
        if rel in ALLOWED_DAY_PATH_FILES:
            continue
        for lineno, snippet in filter_text_for_day_paths(text):
            failures.append((rel, f"line {lineno}: live-course `lectures/dayN/...` path", snippet))
    if failures:
        print(f"validate_no_private_paths: FAIL ({len(failures)} violations)", file=sys.stderr)
        for f, pat, snip in failures[:50]:
            print(f"  {f}: {pat} ({snip!r})", file=sys.stderr)
        if len(failures) > 50:
            print(f"  ... and {len(failures) - 50} more", file=sys.stderr)
        return 1
    print("validate_no_private_paths: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
