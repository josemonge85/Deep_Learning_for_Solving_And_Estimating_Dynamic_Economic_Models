#!/usr/bin/env python3
"""Split lectures/lecture_02_B01_*/slides/01_Intro_to_DeepLearning.tex into 4 decks.

Source deck spans Lectures 02 (B01), 03 (B02), 04 (B03), 05 (B04).
Trims the L02 file in place; writes new .tex files for L03, L04, L05.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "lectures/lecture_02_B01_why_deep_learning/slides/01_Intro_to_DeepLearning.tex"
LINES = SRC.read_text(encoding="utf-8").splitlines(keepends=True)

PREAMBLE = "".join(LINES[:77])

QUESTIONS_FRAME = "".join(LINES[3036:3058])

def render_title(lec_id: str, block_id: str, title: str, subtitle: str) -> str:
    return (
        f"\\title[Lecture {lec_id} ({block_id})]{{Lecture {lec_id} ({block_id}): {title}}}\n"
        f"\\subtitle{{{subtitle}}}\n"
        "\\author{Simon Scheidegger}\n"
        "\\institute{HEC, University of Lausanne}\n"
        "\\date{}\n"
    )

TITLE_FRAME = (
    "\\begin{document}\n\n"
    "{\\setbeamercolor{background canvas}{bg=uzhgreylight}\n"
    "\\begin{frame}\n\\titlepage\n\\end{frame}\n}\n\n"
)

def slice_lines(start: int, end: int) -> str:
    return "".join(LINES[start - 1 : end])

L02_RANGES = [
    (87, 706),
]

L03_HEADER = "\\section{Artificial Neural Networks}\n\n"
L03_RANGES = [
    (715, 1348),
    (1357, 1362),
    (1496, 1995),
    (2019, 2077),
    (2942, 2964),
    (2967, 2993),
    (3016, 3035),
]

L04_RANGES = [
    (2086, 2408),
    (2417, 2925),
]

L05_RANGES = [
    (1254, 1271),
    (1357, 1362),
    (1365, 1493),
    (2996, 3013),
]


def build(out_path: Path, lec_id: str, block_id: str, title: str, subtitle: str, ranges, prepend_section: str = ""):
    body = "".join(slice_lines(s, e) for (s, e) in ranges)
    txt = (
        PREAMBLE
        + render_title(lec_id, block_id, title, subtitle)
        + TITLE_FRAME
        + prepend_section
        + body
        + "\n"
        + QUESTIONS_FRAME
        + "\n\\end{document}\n"
    )
    out_path.write_text(txt, encoding="utf-8")
    print(f"wrote {out_path.relative_to(ROOT)} ({len(txt.splitlines())} lines)")


def main():
    build(
        ROOT / "lectures/lecture_02_B01_why_deep_learning/slides/01_Intro_to_DeepLearning.tex",
        "02", "B01",
        "Why Deep Learning for Economics and Finance?",
        "Introduction to Machine Learning and Deep Learning",
        L02_RANGES,
    )
    build(
        ROOT / "lectures/lecture_03_B02_training_neural_networks/slides/02_Training_Neural_Networks.tex",
        "03", "B02",
        "Training Neural Networks",
        "Architecture, gradients, optimization, regularization-adjacent mechanics",
        L03_RANGES,
    )
    build(
        ROOT / "lectures/lecture_04_B03_generalization_sequence_models/slides/03_Generalization_Sequence_Models.tex",
        "04", "B03",
        "Generalization and Sequence Models",
        "Bias-variance, double descent, RNN / LSTM / Transformer",
        L04_RANGES,
    )
    build(
        ROOT / "lectures/lecture_05_B04_function_approximation_loss_design/slides/04_Function_Approximation_Loss_Design.tex",
        "05", "B04",
        "Function Approximation and Loss Design",
        "Universal approximation, robust losses, the curse of dimensionality",
        L05_RANGES,
    )


if __name__ == "__main__":
    main()
