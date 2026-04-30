#!/usr/bin/env python3
"""Regenerate per-lecture README.md and the top-level at-a-glance table
from course.yml so every entry is a working Markdown hyperlink.
"""
from __future__ import annotations
from pathlib import Path
import re
import sys
import yaml

REPO = Path(__file__).resolve().parents[1]


def script_ref(entries: list[dict]) -> str:
    parts = [f"§{e['section']} ({e['title']})" for e in entries]
    return ", ".join(parts) if parts else "—"


def list_links(prefix: str, items: list[str]) -> str:
    if not items:
        return "_(none in this PR)_"
    out = []
    for rel in items:
        name = Path(rel).name
        out.append(f"- [`{name}`]({rel})")
    return "\n".join(out)


def compute_compute(lec: dict) -> str:
    return lec.get("compute", "cpu-light")


def compute_time(lec: dict) -> str:
    return lec.get("time", "standard")


def render_lecture_readme(lec: dict, prereq_titles: dict[str, str]) -> str:
    num = f"{lec['lecture']:02d}"
    block = lec["block"]
    title = lec["title"]
    folder = lec["folder"]

    slides = lec.get("slides") or []
    nb = lec.get("notebooks") or {}
    core = nb.get("core") or []
    exercises = nb.get("exercises") or []
    solutions = nb.get("solutions") or []
    extensions = nb.get("extensions") or []

    if lec["prereqs"]:
        prereq_md = ", ".join(
            f"[Lecture {prereq_titles[p][0]} ({p})](../{prereq_titles[p][1]}/README.md) — {prereq_titles[p][2]}"
            for p in lec["prereqs"]
            if p in prereq_titles
        )
    else:
        prereq_md = "_(none — start of course)_"

    script_md = script_ref(lec.get("script") or [])

    return f"""# Lecture {num} ({block}): {title}

> **Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance
> **Course author:** Simon Scheidegger
> **Compute tier:** `{compute_compute(lec)}` &nbsp;·&nbsp; **Time budget:** `{compute_time(lec)}`

## Learning goal

> _Concrete one-paragraph statement to be filled in by the maintainer; the script reference below is the canonical source of truth in the meantime._

## Prerequisites

- {prereq_md}

## External prerequisites

- Python 3.10+ environment (`requirements.txt` at repo root, or run on the course platform).
- Familiarity with the math listed under **Script reference** below.

## Script reference

- {script_md}
- [`lecture_script/script_to_lectures.md`](../../lecture_script/script_to_lectures.md) — full chapter-to-lecture map
- [`lecture_script/lecture_script.pdf`](../../lecture_script/lecture_script.pdf) — companion script

## Slides

{list_links(folder, slides)}

## Notebooks

### Core

{list_links(folder, core)}

### Exercises

{list_links(folder, exercises)}

### Solutions

{list_links(folder, solutions)}

### Extensions

{list_links(folder, extensions)}

## Checkpoint

> {lec.get('checkpoint', '_To be filled in by the maintainer._')}

## Readings

- [`readings/links_by_lecture/lecture_{num}_{block}.md`](../../readings/links_by_lecture/lecture_{num}_{block}.md)
- [`readings/bibliography.bib`](../../readings/bibliography.bib)

## Navigation

- [`COURSE_MAP.md`](../../COURSE_MAP.md)
- [`README.md`](../../README.md)

## Copyright and attribution

- First-party material: course author Simon Scheidegger. Code is MIT-licensed; written / graphical content is CC0 1.0 Universal.
- Borrowed or adapted material (where present) preserves its upstream notice in the file header. See [`NOTICE.md`](../../NOTICE.md).
"""


def render_at_a_glance(course: dict, lectures: list[dict], toolkits: list[dict]) -> str:
    """Markdown table fragment with linked lecture rows."""
    lines = [
        "| # | Block | Title | Compute | Time |",
        "|---:|---|---|---|---|",
    ]
    insert_after_T1 = "B04"
    insert_after_T2 = "B11"
    seen_T1 = False
    seen_T2 = False
    for lec in lectures:
        num = f"{lec['lecture']:02d}"
        block = lec["block"]
        title = lec["title"]
        folder = lec["folder"]
        compute = lec.get("compute", "")
        tt = lec.get("time", "")
        lines.append(
            f"| [{num}]({folder}/README.md) | {block} | [{title}]({folder}/README.md) | `{compute}` | `{tt}` |"
        )
        if block == insert_after_T1 and not seen_T1:
            tk = next(t for t in toolkits if t["block"] == "T1")
            lines.append(
                f"| **T1** | **T1** | **[Toolkit: {tk['title']}]({tk['folder']}/README.md)** | `{tk['compute']}` | `{tk['time']}` |"
            )
            seen_T1 = True
        if block == insert_after_T2 and not seen_T2:
            tk = next(t for t in toolkits if t["block"] == "T2")
            lines.append(
                f"| **T2** | **T2** | **[Toolkit: {tk['title']}]({tk['folder']}/README.md)** | `{tk['compute']}` | `{tk['time']}` |"
            )
            seen_T2 = True
    return "\n".join(lines)


def main() -> None:
    with open(REPO / "course.yml") as f:
        course = yaml.safe_load(f)

    lectures: list[dict] = course["lectures"]
    toolkits: list[dict] = course["toolkits"]

    # Build prereq_titles lookup: block -> (num_str, folder, title)
    prereq_titles = {
        lec["block"]: (f"{lec['lecture']:02d}", Path(lec["folder"]).name, lec["title"])
        for lec in lectures
    }

    # Per-lecture READMEs
    for lec in lectures:
        out = render_lecture_readme(lec, prereq_titles)
        path = REPO / lec["folder"] / "README.md"
        path.write_text(out, encoding="utf-8")
        print(f"  wrote {path.relative_to(REPO)}")

    # At-a-glance table for top-level README
    table_md = render_at_a_glance(course, lectures, toolkits)
    table_path = REPO / "_dev" / "_at_a_glance.md"
    table_path.write_text(table_md, encoding="utf-8")
    print(f"\nWrote at-a-glance table fragment to {table_path.relative_to(REPO)}")
    print(f"({len(lectures)} lectures + {len(toolkits)} toolkits)")


if __name__ == "__main__":
    main()
