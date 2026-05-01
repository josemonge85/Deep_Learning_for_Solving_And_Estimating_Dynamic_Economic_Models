#!/usr/bin/env python3
"""Remove the splitter-inserted ``\\begin{frame}{About this lecture}...\\end{frame}``
block (and the preceding blank line, if any) from each .tex file passed on
the command line. Idempotent: prints `unchanged` when no such frame exists.
"""
from __future__ import annotations
import sys
import re
from pathlib import Path

PATTERN = re.compile(
    r"\n*\\begin\{frame\}\{About this lecture\}.*?\\end\{frame\}\n",
    re.DOTALL,
)


def strip(path: Path) -> bool:
    txt = path.read_text(encoding="utf-8")
    new = PATTERN.sub("\n", txt, count=1)
    if new == txt:
        return False
    path.write_text(new, encoding="utf-8")
    return True


def main() -> int:
    for arg in sys.argv[1:]:
        p = Path(arg)
        if not p.exists():
            print(f"missing: {p}")
            continue
        if strip(p):
            print(f"stripped: {p}")
        else:
            print(f"unchanged: {p}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
