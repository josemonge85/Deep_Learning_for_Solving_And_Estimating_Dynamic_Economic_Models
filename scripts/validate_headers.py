#!/usr/bin/env python3
"""validate_headers.

Verify that every first-party Jupyter notebook under lectures/ and
toolkit/ has a Lecture XX (BYY) markdown header as cell 0 (or the
borrowed-material variant for the upstream-adapted notebook).

Input:    repository state (no args)
Exit codes:
  0 - all notebooks have a valid header
  1 - one or more notebooks lack a valid header (per-file diagnostics on stderr)

Usage: python scripts/validate_headers.py
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

import nbformat

REPO = Path(__file__).resolve().parents[1]
HEADER_RE = re.compile(
    r"^#\s+(?:Lecture\s+\d{2}\s+\(B\d{2}\)|Toolkit\s+T\d|Lecture\s+01\s+\(B00\)\s+—\s+Pre-course|Upstream material notice)"
)


def has_valid_header(nb_path: Path) -> tuple[bool, str]:
    nb = nbformat.read(nb_path, as_version=4)
    if not nb.cells:
        return False, "notebook has no cells"
    first = nb.cells[0]
    if first.cell_type != "markdown":
        return False, f"cell 0 is {first.cell_type}, expected markdown"
    src = first.source if isinstance(first.source, str) else "".join(first.source)
    if not HEADER_RE.search(src):
        first_line = src.split("\n", 1)[0][:80]
        return False, f"cell 0 missing Lecture/Toolkit header (first line: {first_line!r})"
    return True, ""


def main() -> int:
    notebooks = (
        list((REPO / "lectures").rglob("*.ipynb"))
        + list((REPO / "toolkit").rglob("*.ipynb"))
    )
    failures: list[tuple[Path, str]] = []
    for nb in sorted(notebooks):
        if "ipynb_checkpoints" in str(nb):
            continue
        ok, msg = has_valid_header(nb)
        if not ok:
            failures.append((nb, msg))

    if failures:
        print(f"validate_headers: FAIL ({len(failures)} of {len(notebooks)} notebooks)", file=sys.stderr)
        for nb, msg in failures:
            print(f"  {nb.relative_to(REPO)}: {msg}", file=sys.stderr)
        return 1
    print(f"validate_headers: OK ({len(notebooks)} notebooks)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
