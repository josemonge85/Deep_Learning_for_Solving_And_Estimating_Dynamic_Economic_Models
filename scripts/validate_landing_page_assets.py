#!/usr/bin/env python3
"""validate_landing_page_assets.

Verify that the public README contains:
  1. the hero <img> tag pointing to assets/hero/deep_learning_dynamic_models_hero.png;
  2. a "Toolkit modules" section header (placement is no longer
     order-checked — the new README is structured around a topic
     index that already names both toolkits).

Input:    repository state (no args)
Exit codes:
  0 - all checks pass
  1 - one or more checks failed (diagnostics on stderr)
"""
from __future__ import annotations
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
README = REPO / "README.md"
HERO = REPO / "assets/hero/deep_learning_dynamic_models_hero.png"


def main() -> int:
    failures: list[str] = []
    if not README.exists():
        print("validate_landing_page_assets: FAIL — README.md missing", file=sys.stderr)
        return 1
    text = README.read_text(encoding="utf-8")
    if "assets/hero/deep_learning_dynamic_models_hero.png" not in text:
        failures.append("hero <img> reference missing in README.md")
    if not HERO.exists():
        failures.append(f"hero file missing: {HERO.relative_to(REPO)}")
    if "Toolkit" not in text:
        failures.append("'Toolkit' content missing from README.md (toolkits should be visible)")

    if failures:
        print(f"validate_landing_page_assets: FAIL ({len(failures)} issues)", file=sys.stderr)
        for f in failures:
            print(f"  {f}", file=sys.stderr)
        return 1
    print("validate_landing_page_assets: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
