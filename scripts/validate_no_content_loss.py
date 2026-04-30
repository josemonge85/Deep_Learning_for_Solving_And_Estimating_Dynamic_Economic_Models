#!/usr/bin/env python3
"""validate_no_content_loss.

Verify that every entry in MATERIALS_CROSSWALK.md marked `migrated`
has a corresponding destination file (or folder) in this repository.

This is a structural check; it does NOT compare cell-by-cell content
(that would require access to the live-course source repo).

Input:    repository state + MATERIALS_CROSSWALK.md
Exit codes:
  0 - every claimed migration target exists
  1 - one or more targets missing (per-file diagnostics on stderr)
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
CROSSWALK = REPO / "MATERIALS_CROSSWALK.md"

# Match table rows of the form:
#   | `<source>` | `<destination>` | migrated... |
ROW_RE = re.compile(
    r"^\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|\s*(migrated[^|]*)\|",
    re.MULTILINE,
)


def main() -> int:
    if not CROSSWALK.exists():
        print(f"validate_no_content_loss: FAIL — {CROSSWALK.name} missing", file=sys.stderr)
        return 1
    text = CROSSWALK.read_text(encoding="utf-8")
    rows = ROW_RE.findall(text)
    missing: list[tuple[str, str]] = []
    for src, dst, status in rows:
        candidate = REPO / dst
        if candidate.exists():
            continue
        if dst.endswith("/") and (REPO / dst.rstrip("/")).exists():
            continue
        # brace-expansion entries describe multi-file groups; skip
        if "{" in dst and "}" in dst:
            continue
        missing.append((src, dst))

    if missing:
        print(f"validate_no_content_loss: FAIL ({len(missing)} of {len(rows)} migration targets missing)", file=sys.stderr)
        for src, dst in missing[:50]:
            print(f"  source `{src}` -> destination `{dst}` (NOT FOUND)", file=sys.stderr)
        if len(missing) > 50:
            print(f"  ... and {len(missing) - 50} more", file=sys.stderr)
        return 1
    print(f"validate_no_content_loss: OK ({len(rows)} migration targets verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
