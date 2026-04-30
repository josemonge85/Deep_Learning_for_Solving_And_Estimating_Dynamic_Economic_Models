#!/usr/bin/env bash
# Build the lecture script PDF.
set -euo pipefail
cd "$(dirname "$0")/../lecture_script"
pdflatex -interaction=nonstopmode lecture_script.tex
bibtex lecture_script || true
pdflatex -interaction=nonstopmode lecture_script.tex
pdflatex -interaction=nonstopmode lecture_script.tex
