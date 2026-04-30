#!/usr/bin/env python3
"""check_american_english.

Flag a small set of British-English spellings that should not appear in
student-facing material per the course's American-English policy.

This is a heuristic guard, not a full spell checker. Words are matched
case-insensitively as whole words via `\\b...\\b`.

Input:    repository state (no args)
Exit codes:
  0 - no British spellings found
  1 - one or more found (per-file, per-line diagnostics on stderr)
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

BRITISH_TO_AMERICAN: dict[str, str] = {
    "behaviour": "behavior",
    "behaviours": "behaviors",
    "colour": "color",
    "colours": "colors",
    "favourable": "favorable",
    "favour": "favor",
    "favoured": "favored",
    "honour": "honor",
    "labour": "labor",
    "neighbour": "neighbor",
    "neighbourhood": "neighborhood",
    "centre": "center",
    "centres": "centers",
    "fibre": "fiber",
    "metre": "meter",
    "litre": "liter",
    "theatre": "theater",
    "analyse": "analyze",
    "analysed": "analyzed",
    "analyses": "analyzes",
    "analysing": "analyzing",
    "organise": "organize",
    "organised": "organized",
    "organisation": "organization",
    "optimise": "optimize",
    "optimised": "optimized",
    "optimisation": "optimization",
    "summarise": "summarize",
    "summarised": "summarized",
    "summarising": "summarizing",
    "synthesise": "synthesize",
    "synthesised": "synthesized",
    "normalise": "normalize",
    "normalised": "normalized",
    "normalising": "normalizing",
    "normalisation": "normalization",
    "minimise": "minimize",
    "minimised": "minimized",
    "minimising": "minimizing",
    "maximise": "maximize",
    "maximised": "maximized",
    "maximising": "maximizing",
    "realise": "realize",
    "realised": "realized",
    "recognise": "recognize",
    "recognised": "recognized",
    "specialise": "specialize",
    "specialised": "specialized",
    "characterise": "characterize",
    "characterised": "characterized",
    "categorise": "categorize",
    "categorised": "categorized",
    "modelling": "modeling",
    "modelled": "modeled",
    "labelled": "labeled",
    "travelling": "traveling",
    "travelled": "traveled",
    "cancelled": "canceled",
    "cancelling": "canceling",
    "fulfil": "fulfill",
    "fulfilment": "fulfillment",
    "enrolment": "enrollment",
    "instalment": "installment",
    "defence": "defense",
    "offence": "offense",
    "licence": "license",
    "practise": "practice",
    "programme": "program",
    "catalogue": "catalog",
    "dialogue": "dialog",
    "manoeuvre": "maneuver",
    "anaesthesia": "anesthesia",
    "haemoglobin": "hemoglobin",
    "paediatric": "pediatric",
    "aluminium": "aluminum",
    "judgement": "judgment",
    "ageing": "aging",
    "grey": "gray",
    "tyre": "tire",
    "draught": "draft",
    "sceptic": "skeptic",
    "sceptical": "skeptical",
    "whilst": "while",
    "amongst": "among",
    "towards": "toward",
}

INCLUDE_SUFFIXES = {".md", ".tex", ".py"}
SKIP_DIR_PARTS = {".git", "_dev", "ipynb_checkpoints", "__pycache__", "lecture_script", "legacy"}
SKIP_FILES = {
    "NOTICE.md",                 # may contain upstream British spellings preserved verbatim
    "MATERIALS_CROSSWALK.md",    # contains historical source filenames as identifiers
    "_render_reading_links.py",  # registry includes British venue names
    "check_american_english.py", # the dictionary itself
    "normalize_headers.py",      # borrowed source-repo utility
}


def build_pattern() -> re.Pattern[str]:
    alt = "|".join(re.escape(w) for w in sorted(BRITISH_TO_AMERICAN, key=len, reverse=True))
    return re.compile(rf"\b({alt})\b", re.IGNORECASE)


def main() -> int:
    pat = build_pattern()
    findings: list[tuple[str, int, str, str]] = []
    for path in REPO.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIR_PARTS for part in path.parts):
            continue
        if path.name in SKIP_FILES:
            continue
        if path.suffix not in INCLUDE_SUFFIXES:
            continue
        rel = str(path.relative_to(REPO))
        try:
            for lineno, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                for m in pat.finditer(line):
                    word = m.group(0)
                    suggested = BRITISH_TO_AMERICAN[word.lower()]
                    findings.append((rel, lineno, word, suggested))
        except Exception:
            continue

    if findings:
        print(f"check_american_english: FAIL ({len(findings)} occurrences)", file=sys.stderr)
        for rel, lineno, word, suggested in findings[:80]:
            print(f"  {rel}:{lineno}: '{word}' -> '{suggested}'", file=sys.stderr)
        if len(findings) > 80:
            print(f"  ... and {len(findings) - 80} more", file=sys.stderr)
        return 1
    print("check_american_english: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
