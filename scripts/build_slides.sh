#!/usr/bin/env bash
# Compile every lecture slide deck for which a .tex source exists.
set -euo pipefail
cd "$(dirname "$0")/.."
for tex in lectures/lecture_*/slides/*.tex toolkit/toolkit_*/slides/*.tex; do
  [[ -f "$tex" ]] || continue
  dir=$(dirname "$tex")
  base=$(basename "$tex" .tex)
  echo "Building $tex"
  (cd "$dir" && pdflatex -interaction=nonstopmode "$base.tex" >/dev/null) || echo "FAILED: $tex"
done
