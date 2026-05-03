# Lecture 06 (B17): Agentic programming

A workshop on using AI coding agents (Claude Code) as research partners. Teaches the orientation, prompts, project memory, custom skills, subagents, and hooks that turn an LLM from a clever autocomplete into a real research collaborator, and pairs the slide material with twelve self-paced exercises.

`cpu-light` · `long` · builds on [Lecture 05 (B04)](../lecture_05_B04_nas_loss_normalization/README.md)

> 📑 **Slides:** [05_Agentic_Programming.pdf](slides/05_Agentic_Programming.pdf) and 1 more under [`slides/`](slides/)  
> 📚 **Further reading:** [curated list](../../readings/links_by_lecture/lecture_06_B17.md)  
> 📖 **Script:** —

## What this lecture covers

- **The agentic research-coding loop.** Mental models, environment setup, prompt engineering, and the day-to-day interaction loop on an empirical-economics example.
- **Project memory (`CLAUDE.md`).** Authoring a project-memory file that survives context rolls and makes the agent useful on a multi-month project.
- **Custom skills.** Two worked examples (`/data-diagnostics` and `/strategic-revision`); how to write your own.
- **Subagents.** Seven ready-made templates (verifier, code-reviewer, test-writer, doc-generator, econometrics-reviewer, monte-carlo-designer, backtest-validator).
- **Hooks.** Auto-pdflatex, audit logs, blocked paths, auto-commit on Stop; example `settings.json`.
- **The exercise handout.** Twelve workshop and self-study exercises (Hello Claude through autonomous Ralph loops).

## Learning objectives

After this lecture you can:

- Set up a working agentic research-coding environment.
- Write a project-memory `CLAUDE.md`, a custom skill, and a subagent suited to your own research.
- Configure hooks that automate routine checks.
- Complete the workshop exercises end-to-end and produce reusable templates.

## Slides

- [`slides/05_Agentic_Programming.pdf`](slides/05_Agentic_Programming.pdf)
- [`slides/05_Agentic_Programming.tex`](slides/05_Agentic_Programming.tex)
- [`slides/05_Agentic_Programming_Exercises.pdf`](slides/05_Agentic_Programming_Exercises.pdf)
- [`slides/05_Agentic_Programming_Exercises.tex`](slides/05_Agentic_Programming_Exercises.tex)

## Code

- [`code/CLAUDE_md_template.md`](code/CLAUDE_md_template.md)
- [`code/agentic_ai_lecture_syllabus.md`](code/agentic_ai_lecture_syllabus.md)
- [`code/data/synthetic_panel.csv`](code/data/synthetic_panel.csv)
- [`code/exercise_prompts.md`](code/exercise_prompts.md)
- [`code/exercise_solutions.md`](code/exercise_solutions.md)
- [`code/generate_synthetic_data.py`](code/generate_synthetic_data.py)
- [`code/hooks/settings.json`](code/hooks/settings.json)
- [`code/mincer_demo.py`](code/mincer_demo.py)
- [`code/outputs/mincer_figure.pdf`](code/outputs/mincer_figure.pdf)
- [`code/outputs/mincer_table.tex`](code/outputs/mincer_table.tex)
- [`code/skills/example_skill/SKILL.md`](code/skills/example_skill/SKILL.md)
- [`code/skills/strategic_revision/SKILL.md`](code/skills/strategic_revision/SKILL.md)
- [`code/subagents/backtest_validator.md`](code/subagents/backtest_validator.md)
- [`code/subagents/code_reviewer.md`](code/subagents/code_reviewer.md)
- [`code/subagents/doc_generator.md`](code/subagents/doc_generator.md)
- [`code/subagents/econometrics_reviewer.md`](code/subagents/econometrics_reviewer.md)
- [`code/subagents/monte_carlo_designer.md`](code/subagents/monte_carlo_designer.md)
- [`code/subagents/test_writer.md`](code/subagents/test_writer.md)
- [`code/subagents/verifier.md`](code/subagents/verifier.md)

## In the lecture script

—. The full chapter map is in [`script_to_lectures.md`](../../lecture_script/script_to_lectures.md).

## Readings

Curated bibliography for this lecture: [`lecture_06_B17.md`](../../readings/links_by_lecture/lecture_06_B17.md). The full BibTeX is in [`readings/bibliography.bib`](../../readings/bibliography.bib).

---

| ← Previous | Next → |
|---|---|
| [**Lecture 05: Architecture search and loss balancing**](../lecture_05_B04_nas_loss_normalization/README.md)<br><sub>Random search, Hyperband, ReLoBRaLo, SoftAdapt, GradNorm</sub> | [**Lecture 07: Automatic differentiation for DEQNs**](../lecture_07_B05_autodiff_for_deqns/README.md)<br><sub>Lagrangian primitives, two-tape gradients, IRBC autodiff</sub> |

[↑ Course map](../../COURSE_MAP.md)
