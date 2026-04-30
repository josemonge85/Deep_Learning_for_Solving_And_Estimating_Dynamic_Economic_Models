#!/usr/bin/env python3
"""run_all_smoke_tests.

Stub. Real implementation will execute every notebook in `course.yml`
that does not have `smoke_disabled: true`, in smoke mode, on CPU,
within its compute budget, and report failures.

Input:    course.yml (canonical manifest)
Exit codes:
  0 - all smoke tests passed (currently always returns 0; real checks pending)
  1 - one or more notebooks failed; per-notebook diagnostics on stderr
"""
import sys
print("[run_all_smoke_tests] stub: real smoke harness not yet implemented; exiting 0.")
sys.exit(0)
