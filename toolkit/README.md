# Day 5: Agentic Programming — Hands-on Workshop

Working materials for the Day 5 workshop on agentic programming with AI
coding agents. Structured so a student can also follow it as self-study.

**In-class schedule (Geneva 2026):** Monday May 4, 15:00–18:00 (3 h):
75 min Block I (orientation, environment setup, core loop, prompts;
Ex.\ 1–3) → 30 min coffee → 75 min Block II (CLAUDE.md, skills, subagents,
hooks, **autonomous Ralph loops**, data-to-paper, ethics; Ex.\ 4–7).
Run **Exercise 0 (Hello Claude, 10 min)** before class. The self-study
path below covers the same material at a more deliberate pace.

## Self-study path (no classroom needed)

1. Read `slides/05_Agentic_Programming.pdf` (~75 slides, ~4 hours).
2. Install Claude Code and run `generate_synthetic_data.py`.
3. Work through `exercise_prompts.md` in order:
   - **Exercise 0** (10 min) — Hello Claude. First contact, zero setup.
   - **Exercises 1–7** (3–4 h) — the full workshop flow.
   - **Exercises 8–11** (20–60 min each) — short, self-contained practice
     on subagents, hooks, skills, and the Mincer mini-demo.
   - **Exercise 12** (30–45 min) — autonomous Ralph loop on a tiny
     ridge-regression estimator with `pytest` as the verifier.
4. Cross-check against `exercise_solutions.md` after each exercise.

Each exercise tells you exactly which files to create, which prompts to paste,
and what artifacts to expect. Solutions are intentionally terse — the point
is to see the *shape* of a good answer, not to copy code.

## Files

| File | Purpose | How to run / use |
|------|---------|------------------|
| `README.md` | This file. | — |
| `generate_synthetic_data.py` | Generates the shared panel used in most exercises. | `python3 generate_synthetic_data.py` → creates `data/synthetic_panel.csv` (500 firms × 10 years). |
| `mincer_demo.py` | Warm-up demo: OLS Mincer wage regression on `wage1`. | `python3 mincer_demo.py` → prints summary + writes `outputs/mincer_table.tex` and `outputs/mincer_figure.pdf`. Requires `statsmodels`, `wooldridge`. |
| `exercise_prompts.md` | Copy-pasteable prompts for **Exercises 0–11**. | Read top-to-bottom; each exercise lists setup + prompts. |
| `exercise_solutions.md` | Solution sketches for every exercise. | Consult *after* attempting each exercise. |
| `CLAUDE_md_template.md` | Ready-to-customise `CLAUDE.md` template. | Used in Exercise 4. `cp CLAUDE_md_template.md <your-project>/CLAUDE.md`. |
| `example_skill/SKILL.md` | `/data-diagnostics` — data-quality check skill. | `cp -r example_skill ~/<project>/.claude/skills/data-diagnostics`, then `/data-diagnostics data/…csv`. |
| `example_skill_strategic_revision/SKILL.md` | `/strategic-revision` — parses referee reports into a revision plan. | `cp -r example_skill_strategic_revision ~/<project>/.claude/skills/strategic-revision`, then `/strategic-revision referee1.md referee2.md`. |
| `example_subagent/verifier.md` | Read-only skeptic (Haiku). | `cp example_subagent/verifier.md ~/<project>/.claude/agents/`, then `> Use the verifier subagent on …`. |
| `example_subagent/code_reviewer.md` | Generic code reviewer (Opus, read-only). | Same pattern. |
| `example_subagent/test_writer.md` | Unit-test author incl. synthetic recovery (Opus). | Same pattern. |
| `example_subagent/doc_generator.md` | Docstrings & README writer (Sonnet). | Same pattern. |
| `example_subagent/econometrics_reviewer.md` | Identification & inference auditor (Opus, read-only). | Same pattern. Reviews DiD/IV/RDD/ES code. |
| `example_subagent/monte_carlo_designer.md` | Designs & runs MC stress tests for estimators (Opus). | Same pattern. |
| `example_subagent/backtest_validator.md` | Look-ahead / survivorship / snooping auditor (Opus, read-only). | Same pattern. For finance backtests. |
| `example_hooks/settings.json` | Example Claude Code hooks (auto-pdflatex, audit log, block `data/raw/`, auto-commit on Stop). | `cp example_hooks/settings.json ~/<project>/.claude/settings.json`; requires `jq`. |
| `data/synthetic_panel.csv` | Balanced panel: 500 firms × 10 years with a 2015 treatment. | Regenerate with `generate_synthetic_data.py`. |

## Directory structure

```text
code/
  README.md
  generate_synthetic_data.py        <- regenerates data/synthetic_panel.csv
  mincer_demo.py                    <- warm-up OLS demo (run once)
  exercise_prompts.md               <- Exercises 0-11
  exercise_solutions.md             <- matching solutions
  CLAUDE_md_template.md             <- CLAUDE.md scaffold (Ex 4)
  outputs/                          <- created by mincer_demo.py
    mincer_table.tex
    mincer_figure.pdf
  data/
    synthetic_panel.csv             <- created by generate_synthetic_data.py
  example_skill/
    SKILL.md                        <- /data-diagnostics
  example_skill_strategic_revision/
    SKILL.md                        <- /strategic-revision
  example_subagent/                 <- 7 ready-made subagents
    verifier.md                     <- Haiku, read-only
    code_reviewer.md                <- Opus, read-only
    test_writer.md                  <- Opus, read+write
    doc_generator.md                <- Sonnet, read+write
    econometrics_reviewer.md        <- Opus, read-only
    monte_carlo_designer.md         <- Opus, read+write
    backtest_validator.md           <- Opus, read-only
  example_hooks/
    settings.json                   <- example PreToolUse/PostToolUse/Stop hooks
```

## One-time setup

```bash
cd lectures/day5/code

# 1. Materialise the synthetic panel
python3 generate_synthetic_data.py

# 2. (Optional) Run the Mincer warm-up once, so outputs/ is populated
pip install --user statsmodels wooldridge   # if missing
python3 mincer_demo.py

# 3. Create a scratch research project and copy the templates in
mkdir -p ~/research/lecture-demo/.claude/{skills,agents}
cp CLAUDE_md_template.md ~/research/lecture-demo/CLAUDE.md
cp -r example_skill             ~/research/lecture-demo/.claude/skills/data-diagnostics
cp -r example_skill_strategic_revision ~/research/lecture-demo/.claude/skills/strategic-revision
cp example_subagent/*.md        ~/research/lecture-demo/.claude/agents/
cp example_hooks/settings.json  ~/research/lecture-demo/.claude/settings.json
cd ~/research/lecture-demo && git init && git add . && git commit -m "init demo"
```

## Invoking the artifacts inside Claude Code

```
# Skills
> /data-diagnostics data/synthetic_panel.csv
> /strategic-revision referee1.md referee2.md

# Subagents (by name)
> Use the verifier subagent on results/did_results.json.
> Use the econometrics-reviewer subagent on code/estimate_did.py.
> Use the monte-carlo-designer subagent on code/new_estimator.py.
> Use the backtest-validator subagent on code/ff_momentum.py.
```

## Verifying everything works

```bash
# Subagent YAML frontmatter is well-formed
python3 -c "import re, yaml, pathlib
for p in sorted(pathlib.Path('example_subagent').glob('*.md')):
    m = re.match(r'^---\n(.*?)\n---\n', p.read_text(), re.DOTALL)
    d = yaml.safe_load(m.group(1))
    assert {'name','description','model','tools'} <= set(d)
    print(p.name, '->', d['name'], d['model'])"

# Hooks file is valid JSON
python3 -c "import json; json.load(open('example_hooks/settings.json')); print('ok')"

# Mincer demo produces expected artifacts
python3 mincer_demo.py && ls outputs/
```

All three checks pass in this repo as of 2026-04-14.

## Note

PINNs notebooks previously in this directory moved to `lectures/day6/code/`.
