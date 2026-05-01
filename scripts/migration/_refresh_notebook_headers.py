#!/usr/bin/env python3
"""Refresh the §1.6 lecture-header markdown cell in every first-party
notebook to reflect the new (post-consolidation) lecture number, block,
title, and script reference. Reads canonical metadata from course.yml.
Idempotent. Does NOT execute notebooks; only the first markdown cell is
rewritten, all other cells (including outputs) are preserved verbatim.
"""
from __future__ import annotations
import re
from pathlib import Path

import nbformat
import yaml

REPO = Path(__file__).resolve().parents[2]
HEADER_RE = re.compile(r"^#\s+Lecture\s+\d+\s+\(B\d+\)", re.MULTILINE)
TOOLKIT_HEADER_RE = re.compile(r"^#\s+Toolkit\s+T\d", re.MULTILINE)


def script_ref(entries: list[dict] | None) -> str:
    if not entries:
        return "—"
    return ", ".join(f"§{e['section']} ({e['title']})" for e in entries)


def header_for_lecture(lec: dict, role: str, source_path: str) -> str:
    nn = f"{lec['lecture']:02d}"
    block = lec["block"]
    title = lec["title"]
    return (
        f"# Lecture {nn} ({block}): {title}\n\n"
        f"**Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance  \n"
        f"**Script reference:** {script_ref(lec.get('script'))}  \n"
        f"**Notebook role:** {role}  \n"
        f"**Original live-course source:** `{source_path}`  \n"
        f"**Course author:** Simon Scheidegger  \n"
        f"**License:** see repository `LICENSE` (MIT, code) and `LICENSE-content.md` (CC0 1.0, content).\n"
    )


def header_for_toolkit(tk: dict, source_path: str) -> str:
    code = tk["block"]
    title = tk["title"]
    return (
        f"# Toolkit {code}: {title}\n\n"
        f"**Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance  \n"
        f"**Notebook role:** toolkit  \n"
        f"**Original live-course source:** `{source_path}`  \n"
        f"**Course author:** Simon Scheidegger  \n"
        f"**License:** see repository `LICENSE` (MIT, code) and `LICENSE-content.md` (CC0 1.0, content).\n"
    )


def existing_source_path(cell_src: str) -> str | None:
    m = re.search(r"\*\*Original live-course source:\*\*\s+`([^`]+)`", cell_src)
    return m.group(1) if m else None


def role_from_path(notebook: Path) -> str:
    parts = notebook.parts
    if "core" in parts:
        return "core"
    if "exercises" in parts:
        return "exercise"
    if "solutions" in parts:
        return "solution"
    if "extensions" in parts:
        return "extension"
    return "core"


def main() -> int:
    course = yaml.safe_load((REPO / "course.yml").read_text(encoding="utf-8"))
    lec_by_folder = {Path(l["folder"]).name: l for l in course["lectures"]}
    tk_by_folder = {Path(t["folder"]).name: t for t in course["toolkits"]}

    refreshed = 0
    for nb_path in REPO.rglob("*.ipynb"):
        if any(p in {".ipynb_checkpoints", "_dev", "legacy"} for p in nb_path.parts):
            continue
        # Skip Python-refresher notebooks (no lecture header expected)
        if "python_refresher" in nb_path.parts:
            continue
        # Locate the lecture or toolkit folder
        rel = nb_path.relative_to(REPO)
        folder_name = None
        for part in rel.parts:
            if part.startswith("lecture_") or part.startswith("toolkit_"):
                folder_name = part
                break
        if folder_name is None:
            continue

        nb = nbformat.read(nb_path, as_version=4)
        if not nb.cells:
            continue
        first = nb.cells[0]
        if first.cell_type != "markdown":
            continue
        if not (HEADER_RE.search(first.source) or TOOLKIT_HEADER_RE.search(first.source)):
            continue

        # Special case: borrowed/adapted Krusell-Smith tutorial keeps its
        # upstream notice intact; we do not rewrite its first cell.
        if "KrusellSmith_Tutorial_CPU" in nb_path.name:
            continue

        old_source_path = existing_source_path(first.source) or "(unknown source)"

        if folder_name in lec_by_folder:
            lec = lec_by_folder[folder_name]
            new_src = header_for_lecture(lec, role_from_path(nb_path), old_source_path)
        elif folder_name in tk_by_folder:
            tk = tk_by_folder[folder_name]
            new_src = header_for_toolkit(tk, old_source_path)
        else:
            continue

        if first.source.strip() == new_src.strip():
            continue

        first.source = new_src
        nbformat.write(nb, nb_path)
        refreshed += 1
        print(f"refreshed: {rel}")

    print(f"\nRefreshed {refreshed} notebook headers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
