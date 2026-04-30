#!/usr/bin/env python3
"""One-shot script: rewrite the title/date/comment block of every migrated
slide deck so the title reads `Lecture XX (BYY): <title>` and all
references to "University of Geneva", the live-course dates, and
\"Geneva 2026\" are removed.

The deck-specific subtitle (the actual topic) is preserved.
"""
from __future__ import annotations
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

# (folder_name_substring) -> (lecture_number_str, block_id, public_lecture_title)
LECTURE_TITLES: dict[str, tuple[str, str, str]] = {
    "lecture_02_B01": ("02", "B01", "Why Deep Learning for Economics and Finance?"),
    "lecture_06_B05": ("06", "B05", "Deep Equilibrium Nets --- The Central Idea"),
    "lecture_10_B09": ("10", "B09", "Automatic Differentiation for DEQNs"),
    "lecture_11_B10": ("11", "B10", "IRBC with DEQNs"),
    "lecture_12_B11": ("12", "B11", "Architecture Search and Loss Balancing"),
    "lecture_13_B12": ("13", "B12", "OLG Models with DEQNs"),
    "lecture_15_B14": ("15", "B14", "Krusell--Smith and Young's Method"),
    "lecture_17_B16": ("17", "B16", "Sequence-Space DEQNs"),
    "lecture_18_B17": ("18", "B17", "PINNs I --- Residual Learning for ODEs and PDEs"),
    "lecture_20_B19": ("20", "B19", "Continuous-Time Heterogeneous Agents --- Theory"),
    "lecture_21_B20": ("21", "B20", "Continuous-Time Heterogeneous Agents --- Numerics"),
    "lecture_22_B21": ("22", "B21", "Deep Surrogate Models"),
    "lecture_26_B25": ("26", "B25", "Structural Estimation via SMM"),
    "lecture_27_B26": ("27", "B26", "Climate Economics and Integrated Assessment Models"),
    "lecture_29_B28": ("29", "B28", "Deep Uncertainty Quantification and Policy"),
    "lecture_30_B29": ("30", "B29", "Synthesis and Method Choice"),
    "toolkit_01_T1": ("T1", "T1", "Agentic Research-Coding Loop"),
    "toolkit_02_T2": ("T2", "T2", "Project Memory, Agents, and Hooks"),
}


def find_meta(path: Path) -> tuple[str, str, str] | None:
    for key, val in LECTURE_TITLES.items():
        if key in str(path):
            return val
    return None


def patch_text(src: str, num: str, block: str, title: str) -> str:
    out = src

    # ---- Header comment block ------------------------------------------------
    # Drop comment lines that name University of Geneva / Day N / specific dates.
    out = re.sub(
        r"^%[^\n]*University of Geneva[^\n]*\n",
        "",
        out,
        flags=re.MULTILINE,
    )
    out = re.sub(
        r"^%[^\n]*April[^\n]*2026[^\n]*\n",
        "",
        out,
        flags=re.MULTILINE,
    )
    out = re.sub(
        r"^%[^\n]*May[^\n]*2026[^\n]*\n",
        "",
        out,
        flags=re.MULTILINE,
    )
    out = re.sub(
        r"^%[^\n]*Day\s+\d[^\n]*\n",
        "",
        out,
        flags=re.MULTILINE,
    )
    out = re.sub(
        r"^%[^\n]*Geneva[^\n]*\n",
        "",
        out,
        flags=re.MULTILINE,
    )
    out = re.sub(
        r"^%[^\n]*Duration:[^\n]*\n",
        "",
        out,
        flags=re.MULTILINE,
    )

    # Add a single replacement comment header at the very top.
    if num.startswith("T"):
        header_comment = (
            "% ============================================================================\n"
            f"% Toolkit {num}: {title}\n"
            "% Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance\n"
            "% Course author: Simon Scheidegger\n"
            "% ============================================================================\n"
        )
    else:
        header_comment = (
            "% ============================================================================\n"
            f"% Lecture {num} ({block}): {title}\n"
            "% Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance\n"
            "% Course author: Simon Scheidegger\n"
            "% ============================================================================\n"
        )
    # Replace any existing top comment block before \documentclass.
    out = re.sub(
        r"\A(?:%[^\n]*\n|\s*\n)*",
        header_comment + "\n",
        out,
        count=1,
    )

    # ---- \title[...]% multi-line form ---------------------------------------
    if num.startswith("T"):
        new_title_line = (
            f"\\title[Toolkit {num}]{{Toolkit {num}: {title}}}"
        )
    else:
        new_title_line = (
            f"\\title[Lecture {num} ({block})]{{Lecture {num} ({block}): {title}}}"
        )

    # NOTE: pass replacements as lambdas to bypass re.sub's processing of
    # backslash-escapes (otherwise `\t` in `\title` becomes a TAB).

    # Pattern A: \title[...]%\n{...}     (split form)
    out = re.sub(
        r"\\title\[[^\]]*\]\s*%[^\n]*\n\s*\{[^}]*\}",
        lambda m: new_title_line,
        out,
        count=1,
    )
    # Pattern B: \title[...]{...}        (single-line form)
    out = re.sub(
        r"\\title\[[^\]]*\]\{[^}]*\}",
        lambda m: new_title_line,
        out,
        count=1,
    )
    # Pattern C: \title{...}             (no short form)
    out = re.sub(
        r"\\title\{[^}]*\}",
        lambda m: new_title_line,
        out,
        count=1,
    )

    # ---- \subtitle: drop any leading "Lecture NN:" or "Day N:" prefix --------
    def clean_subtitle(m: re.Match) -> str:
        body = m.group(1)
        body = re.sub(r"^\s*Lecture\s+\d+\s*[:.\-]\s*", "", body)
        body = re.sub(r"^\s*Day\s+\d+\s*[:.\-]\s*", "", body)
        return f"\\subtitle{{{body}}}"

    out = re.sub(
        r"\\subtitle\{([^}]*)\}",
        clean_subtitle,
        out,
        count=1,
    )

    # ---- \institute: simplify ------------------------------------------------
    out = re.sub(
        r"\\institute\[[^\]]*\]\{[^}]*\}",
        lambda m: "\\institute{HEC, University of Lausanne}",
        out,
        count=1,
    )

    # ---- \date: blank out Geneva/April/May references ------------------------
    out = re.sub(
        r"\\date\{[^}]*(?:University of Geneva|April[^}]*2026|May[^}]*2026|Geneva)[^}]*\}",
        lambda m: "\\date{}",
        out,
        count=1,
    )

    return out


def main() -> None:
    tex_files = list((REPO / "lectures").rglob("slides/*.tex")) + list(
        (REPO / "toolkit").rglob("slides/*.tex")
    )
    tex_files.sort()
    changed = 0
    for path in tex_files:
        meta = find_meta(path)
        if meta is None:
            print(f"  SKIP (no metadata): {path.relative_to(REPO)}")
            continue
        num, block, title = meta
        src = path.read_text(encoding="utf-8")
        out = patch_text(src, num, block, title)
        if out != src:
            path.write_text(out, encoding="utf-8")
            changed += 1
            print(f"  patched: {path.relative_to(REPO)} -> Lecture {num} ({block})")
        else:
            print(f"  no change: {path.relative_to(REPO)}")
    print(f"\n{changed} of {len(tex_files)} files patched.")


if __name__ == "__main__":
    main()
