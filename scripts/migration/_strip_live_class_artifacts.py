#!/usr/bin/env python3
"""Strip remaining live-class artifacts from slide .tex sources.

Removes / rewrites:

- "Cloud platform: nuvolos.cloud" lines (course platform is no longer assumed).
- "(NN min)" or "($\sim$NN min)" timing suffixes after frame titles, slot
  labels, and roadmap-bullet labels.
- "Slot A: 09:00--09:50" and similar slot-time prefixes.
- Time-slot text under "Next up:" closing slides ("10:45--12:00", "09:00--12:00").
- "Coffee break!" boxes.
- "morning's exercises", "this morning", "Thursday morning" → neutral phrasing.
- "Notebooks are on Nuvolos Cloud and the course GitHub repository." →
  "Notebooks are in the course repository."

The script edits .tex files in place. It does NOT recompile PDFs; run
`make build-slides` (or pdflatex per deck) to refresh PDFs after.
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Per-pattern (regex, replacement). Order matters where patterns overlap.
PATTERNS: list[tuple[re.Pattern[str], str]] = [
    # Drop "Cloud platform:" lines outright. These point to the live-class platform.
    (re.compile(r"^.*\\textbf\{(?:Cloud )?[Pp]latform:\}.*nuvolos\.cloud.*$\n?", re.MULTILINE), ""),
    # Remove "Slot A/B: HH:MM--HH:MM" prefix from roadmap bullets, keep the label.
    (re.compile(r"\\textbf\{Slot ([AB]): \d\d:\d\d--\d\d:\d\d\}~~\{\\small\(\d+ min\)\}"),
     r"\\textbf{Part \1}"),
    # "Equilibrium system + finger exercise (09:50--09:55)" → drop the timestamp.
    (re.compile(r" \(\d\d:\d\d--\d\d:\d\d\)"), ""),
    # "{\small 09:00--12:00}" / "{\small 10:45--12:00}" / "{\small Thursday morning, 09:00--12:00}"
    (re.compile(r"\{\\small (?:Thursday morning, )?\d\d:\d\d--\d\d:\d\d\}\n?"), ""),
    # "Back at 10:45 for ..." / "Coffee break!" boxes — drop entire colorbox/parbox block.
    (re.compile(
        r"\\begin\{center\}\s*\n\\colorbox\{[^}]+\}\{\\parbox\{[^}]+\}\{[^}]*Coffee break![^}]*\}\}\s*\n\\end\{center\}\n?",
        re.DOTALL), ""),
    # "(NN min)" or "($\sim$NN min)" or "(${\sim}NN$ min)" suffixes inside frame titles
    # and roadmap labels: "{Roadmap of This Lecture (75 min)}" → "{Roadmap of This Lecture}".
    (re.compile(r"~~\{\\small\(\$?\\?sim\$?\s*\d+\s*min\)\}"), ""),
    (re.compile(r"~~\{\\small\(\d+\s*min\)\}"), ""),
    (re.compile(r" \(\$\\sim\$\s*\d+\s*min\)"), ""),
    (re.compile(r" \(\$\{\\sim\}\d+\$\s*min\)"), ""),
    (re.compile(r" \(\$\\sim\$\d+\s*min\)"), ""),
    (re.compile(r" \(\d+\s*min\)"), ""),
    (re.compile(r" \(\${\\sim}\d+\$\s*min\)"), ""),
    # "Roadmap of This Lecture" — drop the trailing duration parens left after above
    (re.compile(r"\{Roadmap of This Lecture\s*\}"), "{Roadmap of This Lecture}"),
    (re.compile(r"\{Outline of This Lecture\s*\}"), "{Outline of This Lecture}"),
    (re.compile(r"\{This lecture\}\s*\(\$?\\?sim?\$?\s*\d+\s*min\)\s*:"), "{This lecture}:"),
    # "(this morning)", "(this afternoon)" parentheticals in body
    (re.compile(r"\s*\(this morning\)"), ""),
    (re.compile(r"\s*\(this afternoon\)"), ""),
    # "morning's exercises" → "exercises", "morning exercises" → "exercises"
    (re.compile(r"morning('s)? exercises"), "exercises"),
    (re.compile(r"morning's exercises"), "exercises"),
    # In-class banners / phrasing
    (re.compile(r"In-class notebooks \(this morning\)"), "Notebooks for this lecture"),
    (re.compile(r"In-class notebooks"), "Notebooks for this lecture"),
    # Cross-deck pointers: "From Deck 1 (this morning):" → "From Deck 1:"
    (re.compile(r"From Deck (\d+)\s*\(this morning\)"), r"From Deck \1"),
    # "Wrap-up: hands-on notebooks on Nuvolos Cloud." (L06 footnote)
    (re.compile(r"\\textbf\{hands-on notebooks\} on Nuvolos Cloud\."),
     r"\\textbf{hands-on notebooks} are in this repository."),
    (re.compile(r"on \\emphc\{Nuvolos Cloud\} and the course GitHub repository\."),
     "in the course repository."),
    (re.compile(r"on Nuvolos Cloud and the course GitHub repository\."),
     "in the course repository."),
    # "Thursday morning" anywhere
    (re.compile(r"\bThursday morning\b,?\s*"), ""),
    # Empty `(${\sim}NN$ min)` left dangling after a label
    (re.compile(r"\$\\sim\$\d+\s*min"), ""),
]


def process_file(path: Path) -> tuple[int, list[str]]:
    text = path.read_text(encoding="utf-8")
    original = text
    hits: list[str] = []
    for pat, repl in PATTERNS:
        new_text, n = pat.subn(repl, text)
        if n:
            hits.append(f"{n}× {pat.pattern[:60]}")
            text = new_text
    if text != original:
        path.write_text(text, encoding="utf-8")
    return (len(hits) > 0), hits


def main() -> int:
    decks = sorted((ROOT / "lectures").glob("lecture_*/slides/*.tex"))
    n_changed = 0
    for d in decks:
        changed, hits = process_file(d)
        if changed:
            n_changed += 1
            rel = d.relative_to(ROOT)
            print(f"== {rel}")
            for h in hits:
                print(f"   {h}")
    print(f"\n{n_changed}/{len(decks)} decks updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
