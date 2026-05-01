# Toolkit 02 (T2): Project memory, agents, and hooks

A deeper module on operational practices for AI-assisted research:
CLAUDE.md project memory, custom skills (e.g. `econometrics-reviewer`,
`monte-carlo-designer`, `backtest-validator`), subagents, hooks, and
data-to-paper pipelines.

## Learning goal

Author the operational furniture that makes agentic research-coding sustainable for real projects: a project-memory `CLAUDE.md`, custom skills (e.g. an econometrics or backtest-validation skill), subagents for review and verification, and hooks that automate routine checks.

## When to do this

- **Recommended placement:** after Lecture 12, before the
  surrogate / GP block (Lecture 13+) where deeper project-memory
  practices pay off.
- **Standalone:** can also be done independently of the rest of the course.

## Materials

- `templates/CLAUDE_md_template.md`, project-memory starter.
- `example_skill/SKILL.md`, `example_skill_strategic_revision/SKILL.md`, skill templates.
- `example_subagent/`, subagent templates (econometrics-reviewer, monte-carlo-designer, backtest-validator, code-reviewer, doc-generator, test-writer, verifier).
- `example_hooks/settings.json`, hooks configuration sample.
- The exercise handout that covers both T1 and T2 lives in [`Toolkit T3`](../toolkit_03_T3_agentic_programming_exercises/README.md).

## Navigation

- **Suggested predecessor:** [Lecture 12 (B11): Continuous-time HA, numerics](../../lectures/lecture_12_B11_continuous_time_ha_numerics/README.md)
- **Suggested successor:** [Toolkit 03 (T3): Agentic programming, exercise handout](../toolkit_03_T3_agentic_programming_exercises/README.md)
- **Companion module:** [Toolkit 01 (T1): Agentic research-coding loop](../toolkit_01_T1_agentic_research_coding_loop/README.md)
- [Course map](../../COURSE_MAP.md)
- [Repository home](../../README.md)

## Copyright and attribution

- Course author: Simon Scheidegger (University of Lausanne).
- First-party material: code is MIT-licensed; written / graphical content is CC0 1.0 Universal.
