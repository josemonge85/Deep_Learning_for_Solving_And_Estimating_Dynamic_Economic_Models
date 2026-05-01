# Toolkit 02 (T2): Project memory, agents, and hooks

A deeper module on operational practices for AI-assisted research:
CLAUDE.md project memory, custom skills (e.g. `econometrics-reviewer`,
`monte-carlo-designer`, `backtest-validator`), subagents, hooks, and
data-to-paper pipelines.

## Learning goal

Author the operational furniture that makes agentic research-coding sustainable for real projects: a project-memory `CLAUDE.md`, custom skills (e.g. an econometrics or backtest-validation skill), subagents for review and verification, and hooks that automate routine checks.

## When to do this

- **Recommended placement:** after Lecture 12, before the
  heterogeneous-agent block (Lectures 13+) where deeper project-memory
  practices pay off.
- **Standalone:** can also be done independently of the rest of the course.

## Materials

- `slides/05_Agentic_Programming_Exercises.pdf` — exercises handout.
- `templates/CLAUDE_md_template.md` — project-memory starter.
- `example_skill/SKILL.md`, `example_skill_strategic_revision/SKILL.md` —
  skill templates.
- `example_subagent/` — subagent templates (econometrics-reviewer,
  monte-carlo-designer, backtest-validator, code-reviewer, doc-generator,
  test-writer, verifier).
- `example_hooks/settings.json` — hooks configuration sample.

## Source

Migrated from `lectures/day5/` of the Geneva 2026 live course.
Course author: Simon Scheidegger.
