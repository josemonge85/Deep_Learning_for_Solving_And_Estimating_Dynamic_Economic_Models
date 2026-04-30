#!/usr/bin/env python3
"""Stamp every first-party notebook with the §1.6 lecture-header markdown
cell and a RUN_MODE/SEED code cell. Idempotent: re-running is a no-op
for already-stamped notebooks. Does NOT execute notebooks; cell outputs
are preserved verbatim.
"""
from __future__ import annotations
import re
from pathlib import Path
import nbformat
import yaml

REPO = Path(__file__).resolve().parents[1]

# Notebooks known to be long-running. For these, append a smoke-bound
# advisory markdown cell after the RUN_MODE cell. The actual hyper-parameter
# overrides live inside each notebook's first hyperparam cell — left to
# the May-7 follow-up agent (the per-notebook hyperparam variable names
# differ across notebooks and need careful detection).
LONG_RUNNING = {
    "lecture_11_B10_01_IRBC_DEQN.ipynb",
    "lecture_14_B13_08_OLG_Benchmark_DEQN.ipynb",
    "lecture_16_B15_12_KrusellSmith_DeepLearning.ipynb",
    "lecture_17_B16_KrusellSmith_Tutorial_CPU.ipynb",
    "lecture_10_B09_04_IRBC_AutoDiff_DEQN.ipynb",
    "lecture_17_B16_05_SequenceSpace_BrockMirman.ipynb",
    "lecture_17_B16_05b_SequenceSpace_IRBC.ipynb",
    "lecture_17_B16_06_SequenceSpace_KrusellSmith.ipynb",
    "lecture_21_B20_08_Aiyagari_Continuous_Time_FD_and_PINN_PyTorch.ipynb",
    "lecture_28_B27_02_DICE_DEQN_Library_Port.ipynb",
    "lecture_28_B27_03_Stochastic_DICE_DEQN.ipynb",
}

# Notebook with an upstream-borrowed origin (preserve its existing notice).
BORROWED = {
    "lecture_17_B16_KrusellSmith_Tutorial_CPU.ipynb",
}


def script_ref(entries: list[dict]) -> str:
    if not entries:
        return "—"
    return "; ".join(f"§{e['section']} ({e['title']})" for e in entries)


def role_from_path(path: Path) -> str:
    parts = path.parts
    for p in ("core", "exercises", "solutions", "extensions"):
        if p in parts:
            return {"exercises": "exercise", "solutions": "solution"}.get(p, p)
    if "python_refresher" in parts:
        return "pre-course"
    if "toolkit_01" in str(path) or "toolkit_02" in str(path):
        return "toolkit"
    return "core"


def find_lecture(nb_path: Path, course: dict) -> dict | None:
    rel = str(nb_path.relative_to(REPO))
    for lec in course["lectures"]:
        if rel.startswith(lec["folder"] + "/"):
            return lec
    for tk in course["toolkits"]:
        if rel.startswith(tk["folder"] + "/"):
            return {
                "lecture": tk["block"],
                "block": tk["block"],
                "title": tk["title"],
                "folder": tk["folder"],
                "script": [],
                "checkpoint": tk.get("checkpoint", ""),
            }
    return None


def header_text_lecture(lec: dict, source_path: str, role: str) -> str:
    if isinstance(lec["lecture"], int):
        num = f"{lec['lecture']:02d}"
        first_line = f"# Lecture {num} ({lec['block']}): {lec['title']}"
    else:
        first_line = f"# Toolkit {lec['block']}: {lec['title']}"
    return (
        f"{first_line}\n"
        f"\n"
        f"**Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance  \n"
        f"**Script reference:** {script_ref(lec.get('script') or [])}  \n"
        f"**Notebook role:** {role}  \n"
        f"**Original live-course source:** `{source_path}`  \n"
        f"**Course author:** Simon Scheidegger  \n"
        f"**License:** see repository `LICENSE` (MIT, code) and `LICENSE-content.md` (CC0 1.0, content)."
    )


def header_text_borrowed(source_path: str) -> str:
    return (
        "# Upstream material notice\n"
        "\n"
        "This notebook is adapted from an upstream Krusell-Smith JAX tutorial. "
        "The original upstream title, authorship, and license notice are "
        "preserved in the cell(s) immediately below this one — do not modify them.\n"
        "\n"
        "## Course placement\n"
        "\n"
        "**Used in:** Lecture 17 (B16): Sequence-Space DEQNs (extension)  \n"
        f"**Original live-course source:** `{source_path}`  \n"
        "**Course adaptation:** `TUTORIAL_MODE` switch added to bound runtime to ~7 min CPU.  \n"
        "**Course author of this adaptation:** Simon Scheidegger  \n"
        "**License:** see repository `LICENSE` and `LICENSE-content.md`; upstream license preserved verbatim below."
    )


def header_text_refresher(nb_path: Path) -> str:
    return (
        "# Lecture 01 (B00) — Pre-course Python refresher\n"
        "\n"
        "**Course:** Deep Learning for Solving and Estimating Dynamic Models in Economics and Finance  \n"
        "**Module role:** pre-course Python refresher (optional)  \n"
        f"**Notebook:** `{nb_path.name}`  \n"
        "**Course author:** Simon Scheidegger  \n"
        "**License:** see repository `LICENSE` and `LICENSE-content.md`."
    )


RUNMODE_CODE = (
    "# Run-mode switch (smoke = CPU-bounded for CI, teaching = laptop figures, production = full reproduction).\n"
    "RUN_MODE = \"smoke\"  # one of: \"smoke\", \"teaching\", \"production\"\n"
    "SEED = 0\n"
)

SMOKE_ADVISORY = (
    "> **Smoke mode.** This notebook is long-running at production settings. "
    "The cell above sets `RUN_MODE=\"smoke\"` so that the bound branch in the "
    "first hyperparameter cell below caps epochs / batch size / sample count "
    "to keep CPU runtime under ~3 minutes. To reproduce paper-quality results, "
    "switch to `\"teaching\"` or `\"production\"` (GPU recommended). See "
    "`COURSE_MAP.md` for the convention."
)


def already_stamped(nb: nbformat.NotebookNode) -> tuple[bool, bool]:
    """Return (has_header, has_runmode)."""
    has_header = False
    has_runmode = False
    for cell in nb.cells[:4]:
        src = "".join(cell.get("source", "")) if isinstance(cell.get("source"), list) else (cell.get("source") or "")
        if cell.cell_type == "markdown" and re.search(
            r"^#\s+(Lecture\s+\d{2}\s+\(B\d{2}\)|Toolkit\s+T\d|Lecture\s+01\s+\(B00\)\s+—\s+Pre-course|Upstream material notice)",
            src,
        ):
            has_header = True
        if cell.cell_type == "code" and "RUN_MODE" in src and "SEED" in src:
            has_runmode = True
    return has_header, has_runmode


def stamp(nb_path: Path, source_lookup: dict[str, str], course: dict) -> str:
    nb = nbformat.read(nb_path, as_version=4)
    has_header, has_runmode = already_stamped(nb)
    rel = str(nb_path.relative_to(REPO))
    if has_header and has_runmode:
        return "skip"

    is_refresher = "python_refresher" in rel
    is_borrowed = nb_path.name in BORROWED
    is_long = nb_path.name in LONG_RUNNING
    source_path = source_lookup.get(nb_path.name, "")

    new_cells = []

    if not has_header:
        if is_refresher:
            new_cells.append(nbformat.v4.new_markdown_cell(header_text_refresher(nb_path)))
        elif is_borrowed:
            new_cells.append(nbformat.v4.new_markdown_cell(header_text_borrowed(source_path)))
        else:
            lec = find_lecture(nb_path, course)
            if lec is None:
                return "no-meta"
            role = role_from_path(nb_path)
            new_cells.append(nbformat.v4.new_markdown_cell(header_text_lecture(lec, source_path, role)))

    if not has_runmode and not is_refresher:
        new_cells.append(nbformat.v4.new_code_cell(RUNMODE_CODE))
        if is_long:
            new_cells.append(nbformat.v4.new_markdown_cell(SMOKE_ADVISORY))

    nb.cells = new_cells + nb.cells
    nbformat.write(nb, nb_path)
    return "stamped"


def build_source_lookup() -> dict[str, str]:
    """Map destination basename -> source path, parsed from MATERIALS_CROSSWALK.md."""
    text = (REPO / "MATERIALS_CROSSWALK.md").read_text(encoding="utf-8")
    lookup = {}
    pat = re.compile(r"\|\s*`(lectures/day\d/[^`]+\.ipynb)`\s*\|\s*`(lectures/[^`]+\.ipynb)`")
    for m in pat.finditer(text):
        src, dst = m.group(1), m.group(2)
        lookup[Path(dst).name] = src
    # Toolkit
    pat2 = re.compile(r"\|\s*`(lectures/day5/[^`]+)`\s*\|\s*`(toolkit/[^`]+)`")
    for m in pat2.finditer(text):
        src, dst = m.group(1), m.group(2)
        lookup[Path(dst).name] = src
    return lookup


def main() -> None:
    course = yaml.safe_load((REPO / "course.yml").read_text())
    source_lookup = build_source_lookup()

    notebooks = (
        list((REPO / "lectures").rglob("*.ipynb"))
        + list((REPO / "toolkit").rglob("*.ipynb"))
    )
    notebooks.sort()

    counts = {"stamped": 0, "skip": 0, "no-meta": 0}
    for nb in notebooks:
        if "ipynb_checkpoints" in str(nb):
            continue
        result = stamp(nb, source_lookup, course)
        counts[result] += 1
        if result == "no-meta":
            print(f"  NO META: {nb.relative_to(REPO)}")

    print(f"\nStamped: {counts['stamped']}")
    print(f"Skipped (already stamped): {counts['skip']}")
    print(f"Missing metadata: {counts['no-meta']}")


if __name__ == "__main__":
    main()
