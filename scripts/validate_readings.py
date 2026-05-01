#!/usr/bin/env python3
"""validate_readings.

Three checks against the readings/ subtree:

  (1) Every lecture in course.yml has a readings/links_by_lecture/<id>.md file.
  (2) No PDFs live anywhere under readings/ except readings/allowed_pdfs/
      and readings/private_DO_NOT_COMMIT/.
  (3) Every PDF in readings/allowed_pdfs/ has an `allowed_pdfs` row in
      READINGS_AUDIT.csv (matched on filename stem ↔ bib_key).

Input:    course.yml, readings/, READINGS_AUDIT.csv (optional)
Exit codes:
  0 - all checks pass
  1 - one or more checks failed; per-failure diagnostics on stderr
"""
from __future__ import annotations
import csv
import sys
from pathlib import Path

import yaml  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
READINGS = ROOT / "readings"
LINKS_DIR = READINGS / "links_by_lecture"
ALLOWED_DIR = READINGS / "allowed_pdfs"
PRIVATE_DIR = READINGS / "private_DO_NOT_COMMIT"
AUDIT_CSV = ROOT / "READINGS_AUDIT.csv"


def lecture_link_id(lec: dict) -> str:
    """Construct the lecture_XX_BYY identifier used as the link-file stem."""
    return f"lecture_{int(lec['lecture']):02d}_{lec['block']}"


def main() -> int:
    failures: list[str] = []

    # (1) per-lecture link files exist
    course = yaml.safe_load((ROOT / "course.yml").read_text(encoding="utf-8"))
    expected = [lecture_link_id(lec) for lec in course.get("lectures", [])]
    for stem in expected:
        if not (LINKS_DIR / f"{stem}.md").exists():
            failures.append(f"missing reading link file: readings/links_by_lecture/{stem}.md")

    # (2) no stray PDFs outside allowed_pdfs / private_DO_NOT_COMMIT
    for pdf in READINGS.rglob("*.pdf"):
        try:
            pdf.relative_to(ALLOWED_DIR)
            continue
        except ValueError:
            pass
        try:
            pdf.relative_to(PRIVATE_DIR)
            continue
        except ValueError:
            pass
        failures.append(f"stray PDF outside readings/allowed_pdfs/: {pdf.relative_to(ROOT)}")

    # (3) every PDF in allowed_pdfs is audited as such
    audited_keys: set[str] = set()
    if AUDIT_CSV.exists():
        with AUDIT_CSV.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(
                (line for line in f if not line.lstrip().startswith("#"))
            )
            for row in reader:
                if (row.get("redistribution_status") or "").strip() == "allowed_pdfs":
                    key = (row.get("bib_key") or "").strip()
                    if key:
                        audited_keys.add(key)
    if ALLOWED_DIR.exists():
        for pdf in ALLOWED_DIR.glob("*.pdf"):
            if pdf.stem not in audited_keys:
                failures.append(
                    f"{pdf.relative_to(ROOT)} is in readings/allowed_pdfs/ but not "
                    f"marked redistribution_status=allowed_pdfs in READINGS_AUDIT.csv"
                )

    if failures:
        for msg in failures:
            print(f"FAIL: {msg}", file=sys.stderr)
        return 1

    n_pdfs = len(list(ALLOWED_DIR.glob("*.pdf"))) if ALLOWED_DIR.exists() else 0
    print(f"validate_readings: OK ({len(expected)} lectures, {n_pdfs} allowed PDFs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
