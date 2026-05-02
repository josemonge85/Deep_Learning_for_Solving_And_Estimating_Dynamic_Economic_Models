# Agentic AI for Coding & Research
## A Full-Day Intensive Lecture with Hands-On Exercises
### Best-of-Class Syllabus — v1.0

> **Audience:** PhD students and researchers in economics, finance, and computational social science.
> **Duration:** 3.5–4 hours (can be split across two half-day sessions).
> **Prerequisites:** Basic Python familiarity; no prior AI-tooling experience required.
> **Instructor note:** Every module includes a *Live Demo* block and a timed *Hands-On Exercise*. Participants should bring a laptop with internet access. Cloud fallback options are provided for every exercise.

---

## Learning Objectives

By the end of this lecture, participants will be able to:

1. Set up a production-grade agentic AI coding environment from scratch.
2. Understand the mental model of how LLMs and context windows work in practice.
3. Write high-quality prompts that produce reproducible, research-grade code and text.
4. Use `CLAUDE.md` and project memory patterns to maintain long-running research projects.
5. Build reusable skills and verifier-style subagents for repeatable workflows.
6. Automate the full research pipeline: data → analysis → figures → LaTeX → paper draft.
7. Use AI agents to replicate published papers and benchmark methods.
8. Know the failure modes, verification requirements, and ethical obligations of AI-assisted research.

---

## Schedule Overview

| # | Module | Time |
|---|--------|------|
| 0 | Orientation & Mental Models | 20 min |
| 1 | Production Environment Setup + **Exercise 1** | 30 min |
| 2 | The Core Interaction Loop + **Exercise 2** | 25 min |
| 3 | Prompt Engineering for Research + **Exercise 3** | 15 min |
| — | *Break* | 15 min |
| 4 | Project Memory & `CLAUDE.md` + **Exercise 4** | 20 min |
| 5 | Skills, Subagents & Workflows + **Exercise 5** | 20 min |
| 6 | From Raw Data to a Paper Section + **Exercise 6** | 25 min |
| 7 | AI Agents for Paper Replication + **Exercise 7** | 10 min |
| 8 | Verification, Failure Modes & Ethics | 15 min |
| — | Q&A & Discussion | 15 min |

**Total: ~3 hr 30 min**

---

## MODULE 0 — Orientation & Mental Models
### (20 minutes, lecture)

### 0.1 Why This Matters Now

The core argument: the bottleneck in computational research has shifted. It used to be *can you write the code?* It is now *can you correctly specify what you want?* This is a skill that rewards domain expertise — economists and social scientists have a natural advantage over pure software engineers, because what is hard is knowing what question to ask.

Two failure modes to avoid:
- **The hype trap:** "AI wrote a paper in 30 minutes!" — technically true, but the quality gap is real.
- **The dismissal trap:** "This is just autocomplete." — wrong; modern agents can autonomously plan, execute, debug, and iterate across a 2-hour session.

### 0.2 The Hierarchy of AI Coding Tools

```
Level 0–1  Browser chatbot + copy-paste
           (ChatGPT, Claude.ai, Gemini web)

Level 2    Agentic IDE
           (Cursor, GitHub Copilot in VS Code)
           → agent edits files as you watch

Level 3    Terminal agents — FULL ENVIRONMENT ACCESS
           (Claude Code, OpenAI Codex CLI, Gemini CLI)
           → reads/writes files, runs code, uses git

Level 4    Level 3 + external tools via MCP
           (databases, APIs, Zotero, Slack, HPC clusters)

Level 5    Autonomous containers — run for 1–2 hrs unattended
           ("go replicate this paper while I get coffee")
```

**Key insight:** All levels use the same underlying models. The difference is *scaffolding*, not raw intelligence. This lecture gets you to Level 3–4, with a taste of Level 5.

### 0.3 The Context Window — The Most Important Mental Model

An LLM has no persistent memory. Every message you send bundles the *entire conversation history* — your prompts, the model's responses, every file read, every code output — into one large document sent to the model each time. This is the **context window**.

```
Typical size: ~200,000 tokens ≈ ~150,000 words ≈ ~500 pages

What fills it:
  - System prompt         ~2,000 tokens
  - Your conversation     grows linearly
  - File contents         can be large (watch datasets!)
  - Code outputs          can be very large (watch logs!)
  - Tool call results     moderate
```

**The performance curve:** Quality degrades as context fills. A session at turn 5 is sharper than the same session at turn 35. This has concrete implications:

1. Break work into focused sessions with clear objectives.
2. Write state to disk — `progress.md`, `plan.md`, `decisions.md`.
3. Use `/compact` in Claude Code before context overflows.
4. Start a fresh session for each new sub-task; pass in the state files.

### 0.4 A Taxonomy of Tasks Where AI Excels vs. Struggles

| Task type | AI performance | Notes |
|-----------|---------------|-------|
| Data cleaning, reshaping | Excellent | Very fast ROI |
| Standard econometric code (OLS, GMM, VARs) | Excellent | Verify edge cases |
| Debugging cryptic errors | Excellent | Often faster than Stack Overflow |
| Writing boilerplate (LaTeX, README, slides) | Excellent | |
| Novel theory derivation | Poor | Do not trust without checking |
| New methods not in training data | Moderate–poor | Degrades gracefully |
| Verification / checking its own work | Poor | **Never skip human review** |
| Subtle statistical issues (identification) | Poor | Economist must lead |

---

## MODULE 1 — Production Environment Setup
### (30 minutes, live demo)

### 1.1 Core Stack

You need four things: a good terminal, Claude Code, a version-control discipline, and Python/R.

#### Step 1: Install a Modern Terminal

**macOS:**
```bash
brew install ghostty    # GPU-accelerated, renders large code outputs cleanly
brew install zellij     # Terminal multiplexer: split panes, tab management
brew install zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

**Linux (Ubuntu):**
```bash
# Zellij
bash <(curl -L https://zellij.dev/launch)

# Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

**Windows:** Install WSL2, then use Ubuntu instructions above.

**Zellij quick reference:**
```
Ctrl+p d     → split pane (vertical)
Ctrl+p n     → new tab
Alt+arrow    → navigate panes
Ctrl+p x     → close pane
```

Set up a default Zellij layout for research work (`~/.config/zellij/layouts/research.kdl`):
```kdl
layout {
    pane split_direction="vertical" {
        pane size="60%" name="claude"
        pane split_direction="horizontal" {
            pane size="50%" name="editor"
            pane name="output"
        }
    }
}
```
Launch with: `zellij --layout research`

#### Step 2: Install Claude Code

```bash
# Option A: via npm
npm install -g @anthropic-ai/claude-code

# Option B: via standalone installer
# Download from: https://docs.anthropic.com/en/docs/claude-code

# Verify
claude --version

# Launch in your project directory
cd ~/research/my-project
claude
```

**Subscription tiers** (as of 2026):

| Tier | Price | Use case |
|------|-------|----------|
| Pro | $20/month | Getting started; already included with Claude.ai Pro |
| Max | $100/month | Regular research use; recommended for daily workflows |
| Max 20x | $200/month | Power users running multi-hour autonomous sessions |
| API (pay-per-use) | ~$15–75/MTok | Cost-effective at low volume; expensive at high volume |

**Privacy:** Your files stay local. But any file Claude *reads* enters the context sent to Anthropic's API. **Do not point Claude at IRB-protected data, PII, or credentials.** Treat the risk profile as equivalent to Dropbox. For sensitive data: use a `.claudeignore` file (same syntax as `.gitignore`).

#### Step 3: Git Configuration (Non-Negotiable)

Every project must be a git repository. AI-generated changes that are not version-controlled cannot be rolled back. This is the single biggest protection against runaway agents.

```bash
# Create a new research project
mkdir ~/research/my-paper && cd ~/research/my-paper
git init
git branch -M main

# Create a .claudeignore (protects sensitive files)
cat > .claudeignore << 'EOF'
data/raw/           # Never let Claude read raw sensitive data
.env                # API keys
*.csv               # Often large; be selective
credentials/
EOF

# Create the initial structure
mkdir -p {data/{raw,processed},code,figures,paper,notes}
touch README.md

# Add a pre-task habit: commit before every Claude session
git add . && git commit -m "initial structure"
```

**Key discipline:** Before every Claude Code session, make a commit. After each session, review the diff (`git diff HEAD`) before committing. This takes 30 seconds and makes everything recoverable.

#### Step 4: Python Environment

```bash
# Install uv (fast Python package manager — 10–100x faster than pip)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create a project environment
uv init
uv add numpy pandas matplotlib scipy statsmodels jupyter

# Or for economics work:
uv add numpy pandas matplotlib scipy statsmodels \
       linearmodels pyhdfe econml pyfixest jupyter

# Activate
source .venv/bin/activate
```

**Why uv instead of conda?** Claude Code can install packages via uv without any confirmation dialogs, making autonomous workflows much smoother. Conda is better for complex C-extension dependencies (like TensorFlow/JAX).

#### Step 5: Configure Claude Code

```bash
# Launch Claude and run these setup commands
claude

# In the Claude Code session:
> /model claude-opus-4-5       # Use the most capable model
> /cost                        # Check your token spend
> /config                      # See all settings
```

Create a global settings file at `~/.claude/settings.json`:
```json
{
  "model": "claude-opus-4-5",
  "autoApprove": ["Read", "Write", "Edit"],
  "autoApprovePatterns": ["*.py", "*.R", "*.tex", "*.md"],
  "dangerouslyAllowWithoutApproval": false
}
```

### 1.2 Optional but Powerful: MCP Servers

MCPs (Model Context Protocol) connect Claude to external services. Install the ones relevant to you:

```bash
# Zotero (access your reference manager directly)
claude mcp add zotero

# GitHub (create branches, PRs, manage repos)
claude mcp add github

# Filesystem extended tools
claude mcp add filesystem

# Brave Search (let Claude search the web)
claude mcp add brave-search
```

Usage in a session:
```
> Search Zotero for papers on carbon taxation in OLG models
> Create a new GitHub branch called feature/robustness-checks
```

---

## EXERCISE 1 — Environment Bootstrap
### (15 minutes, hands-on)

**Goal:** Get a working Claude Code session running in a version-controlled project.

**Steps:**
1. Create a new directory `~/research/lecture-demo`
2. Initialize git
3. Create a `NOTES.md` with today's date and your name
4. Launch Claude Code: `claude`
5. Type: `> What files are in this directory? Summarize the structure.`
6. Type: `> Create a Python script that loads a CSV file and prints summary statistics. Use pathlib for file paths.`
7. Inspect the generated file. Run it.
8. `git add . && git commit -m "exercise 1: first claude session"`

**Success criterion:** You have a running Claude session, a git commit, and a Python file that Claude wrote.

**Troubleshooting:**
- `claude: command not found` → `npm install -g @anthropic-ai/claude-code` or restart terminal
- Authentication error → run `claude auth` and follow the browser prompt

---

## MODULE 2 — The Core Interaction Loop
### (25 minutes, lecture + live demo)

### 2.1 The Basic Vocabulary

Claude Code runs in your terminal and gives you a chat interface with superpowers. A few key commands:

```
/help                    → list all commands
/status                  → show current model, context usage
/compact                 → manually compress conversation history
/clear                   → start fresh (new context)
/cost                    → show token spend for this session
Ctrl+C                   → interrupt a running task
ESC                      → cancel current input / undo last turn
```

### 2.2 The Feedback Loop

The core pattern:
```
You: describe the task precisely
↓
Claude: reads files, plans, writes code
↓
Claude: executes code, shows output
↓
You: inspect output, give feedback
↓
repeat
```

**The most important skill is how to interrupt.** If Claude is going in the wrong direction:
- Press `Ctrl+C` immediately — stops execution
- Press `ESC` once — cancels the current message and lets you retype
- Press `ESC` twice — goes back one turn (undoes last action)

Do not let Claude finish a bad path and then try to course-correct. Interrupt early.

### 2.3 Prompt Quality Spectrum

**Level 0 — Vague (avoid):**
```
> Analyze this data
```

**Level 1 — Specific:**
```
> Load data/gdp_quarterly.csv. Compute YoY growth rates
  and print summary statistics.
```

**Level 2 — Specific + Context:**
```
> Load data/gdp_quarterly.csv. The column 'gdp_real' is
  in 2015 USD billions at quarterly frequency.
  Compute YoY growth rates, print a summary table
  (mean, sd, min, max, N), and flag any quarters
  where growth exceeds ±10% as potential outliers.
```

**Level 3 — Specific + Context + Constraints + Output spec:**
```
> Load data/gdp_quarterly.csv.
  - Column 'gdp_real': real GDP in 2015 USD billions, quarterly.
  - Compute year-over-year growth: g_t = (gdp_t / gdp_{t-4}) - 1
  - Print a summary table with: mean, sd, p5, p95, N
  - Flag quarters where |g_t| > 0.1 as outliers, print a list
  - Write the cleaned series (no outliers) to data/processed/gdp_growth.csv
  - Do NOT use pandas deprecated methods — use .iloc, not .ix
  Expected output format: Markdown table printed to stdout.
```

**Level 3 is always the goal.** Specificity is not nagging — it is the entire skill.

### 2.4 Patterns for Common Research Tasks

#### Pattern A: "Explain what this code does"
```
> Read code/estimate_var.py and explain:
  1. What it does, step by step
  2. Any assumptions it makes
  3. Any potential bugs or edge cases
  4. What inputs and outputs it expects
```

#### Pattern B: "Write new code matching an existing style"
```
> Read code/utils.py to understand the coding conventions
  (function naming, docstring style, error handling pattern).
  Then write a new function `compute_irfs()` that follows
  the same conventions and implements impulse response
  functions for the VAR model in code/estimate_var.py.
```

#### Pattern C: "Debug this error"
```
> I ran `python code/main.py` and got this error:
  [paste error]
  Read the relevant files and fix the bug.
  Do not change any function signatures or output formats.
```

#### Pattern D: "Refactor for reproducibility"
```
> Read all .py files in the code/ directory.
  Refactor them so that:
  1. All file paths use pathlib and are relative to the project root
  2. All random seeds are set at the top of main.py
  3. All hardcoded parameters are moved to a config dict in config.py
  4. Each script has a __main__ guard and a docstring
  Write a summary of all changes to notes/refactor_log.md
```

#### Pattern E: "Generate a LaTeX table"
```
> Read results/regression_output.json which contains OLS
  coefficient estimates, standard errors, and p-values
  for 3 specifications.
  Generate a LaTeX table in the style of the AER:
  - Three columns (one per specification)
  - Standard errors in parentheses below coefficients
  - Stars: * p<0.1, ** p<0.05, *** p<0.01
  - Fixed effects indicators at the bottom
  - Notes section
  Save to paper/tables/tab_main.tex.
  Do NOT use estout or any external packages — write raw LaTeX.
```

### 2.5 Context Management in Practice

**The progress file pattern** — use this for any session longer than 10 turns:
```
> Before we start: write a file called notes/session_state.md
  that summarizes:
  1. What we have done so far
  2. What is working
  3. What we need to do next
  4. Any design decisions we made and why
```

At the start of the next session:
```
> Read notes/session_state.md and continue from where we left off.
```

**The plan-first pattern** — for any multi-step task:
```
> Before writing any code:
  1. Read all relevant files
  2. Write a plan to notes/plan.md with numbered steps
  3. Ask me to confirm before executing
```

---

## EXERCISE 2 — First Real Task
### (15 minutes, hands-on)

**Goal:** Use the Level 3 prompt pattern on the shared synthetic panel.

**Dataset:** Use `data/synthetic_panel.csv` (from `generate_synthetic_data.py`).

**Task prompt to type:**
```
> I have a dataset at data/synthetic_panel.csv.
  Without loading it yet, first tell me how to inspect it
  (column names, shape, date range, missing values).
  Then:
  1. Load it and print the above diagnostics
  2. Compute annual average revenue by treatment group
  3. Generate a 2x2 panel of plots using matplotlib
     with a clean, publication-ready style (no gridlines,
     serif font, 6x5 inches)
  4. Save the figure to figures/panel_overview.pdf
  5. Write a 3-sentence description of what you see
     to notes/data_description.md
```

**Reflection questions:**
- Where did Claude do well? Where did it need correction?
- At what point would you have interrupted?

---

## MODULE 3 — Prompt Engineering for Research
### (30 minutes, lecture)

### 3.1 The Anatomy of a Research Prompt

Every good research prompt has up to six components:

```
[ROLE]       Who Claude is in this task
[CONTEXT]    What it needs to know to start
[TASK]       What you want done
[CONSTRAINTS] What it must/must not do
[OUTPUT]     What the deliverable looks like
[VERIFICATION] How to check it worked
```

Not every prompt needs all six — but omitting any one of them tends to produce a specific failure mode.

### 3.2 Role Prompts for Research

Set a role at the start of a project session, not on every message:

```
> You are a computational economist with deep expertise in
  time-series econometrics and Python. You write clean,
  well-documented code following PEP 8. You always:
  - Check for stationarity before estimating VARs
  - Report robust standard errors by default
  - Flag identification assumptions explicitly in comments
  - Never suppress warnings without explaining why
```

Or for a paper-writing session:
```
> You are a co-author helping me write the methods section
  of a paper in the style of the Review of Economic Studies.
  Your writing is precise, economical, and uses standard
  economic notation. You use LaTeX math mode correctly.
  When uncertain about notation, you ask before inventing.
```

### 3.3 The Constraint Vocabulary

Constraints are the difference between "AI wrote the code" and "AI wrote *my* code":

**Negative constraints (what NOT to do):**
```
Do NOT use statsmodels for this — use linearmodels.
Do NOT change any existing function signatures.
Do NOT use deprecated pandas syntax (.ix, .ix, inplace=True on chained ops).
Do NOT hardcode file paths — use pathlib relative to project root.
Do NOT print the full dataframe — print only the first 5 rows.
```

**Positive constraints (what to do):**
```
Always use type hints on function signatures.
Follow the AEA data and code policy: all results must be reproducible from a single script.
Use the exact notation from the paper draft (read paper/main.tex first).
Maintain backward compatibility with the existing test suite.
```

**Scope constraints:**
```
Only modify files in the code/ directory.
Do not touch paper/ or data/raw/.
Make only the minimum change needed to fix the bug.
Do one thing at a time; stop and report before moving to the next step.
```

### 3.4 The "Think Before You Code" Pattern

For complex or risky tasks, always force a planning step:

```
> I want you to restructure our estimation pipeline to
  support panel data with two-way fixed effects.

  BEFORE writing any code:
  1. Describe your plan in plain English
  2. List every file you plan to modify
  3. List any risks or potential breaking changes
  4. Estimate how many lines of code this involves

  Do not proceed until I say "go ahead."
```

This single pattern prevents ~80% of "Claude went off and rewrote everything" disasters.

### 3.5 Research-Specific Prompt Templates

#### Template 1: Replication Check
```
> Read code/estimate_model.py and paper/main.tex sections 3.2–3.4.
  Check whether the code matches the model description in the paper.
  Specifically:
  - Does the estimator match equation (5)?
  - Are the fixed effects specified as in footnote 8?
  - Are standard errors clustered as described in Section 3.3?
  Write a discrepancy report to notes/replication_check.md.
  Use this format:
    ✓ [item]: matches
    ✗ [item]: discrepancy — paper says X, code does Y
    ? [item]: unclear from paper
```

#### Template 2: Robustness Table
```
> I need to add three robustness checks to Table 2.
  The baseline specification is in code/estimate_baseline.py.

  New specifications to add:
  1. Add year fixed effects (on top of existing firm FE)
  2. Drop observations where leverage > 0.9
  3. Use winsorized outcome variable at 1%/99%

  For each:
  - Create a separate script that imports and calls estimate_baseline.py
    with modified arguments (do not copy-paste the baseline code)
  - Save results to results/robustness_{spec_name}.json
  - At the end, read all four result files and generate a LaTeX table
    with all four specifications side by side
    (baseline + 3 robustness), saved to paper/tables/tab_robustness.tex
```

#### Template 3: Literature-Aware Writing
```
> Read:
  - paper/main.tex, Section 2 (Related Literature)
  - notes/references_to_add.md (list of papers I want to cite)
  
  For each paper in references_to_add.md:
  1. Write 1–2 sentences situating it in our paper
  2. Indicate where in Section 2 it should be inserted
  3. Write the BibTeX entry
  
  Then produce a revised Section 2 draft with the new
  citations integrated. Flag any sentences you rewrote
  with a LaTeX comment % REVISED.
```

#### Template 4: Autonomous Long-Running Task
```
> I'm going to step away for 30 minutes.
  
  Your task: implement the full estimation pipeline as described
  in plan.md.
  
  Rules while I am away:
  - Commit to git after each major step (use descriptive messages)
  - If you encounter an error you cannot fix in 3 attempts, stop,
    write a clear error report to notes/blocked.md, and stop work
  - Do NOT modify any files in data/raw/ under any circumstances
  - Do NOT make any network requests
  - Write your progress every 10 steps to notes/progress.md
  
  When done (or blocked), write a summary to notes/session_end.md.
```

### 3.6 Common Failure Modes and Fixes

| Failure | Cause | Fix |
|---------|-------|-----|
| Claude "invents" results | Vague output spec | Add explicit verification step |
| Code works but is unreadable | No style constraint | Specify style in role prompt |
| Claude modifies wrong files | No scope constraint | Add explicit file scope |
| Long session degrades | Context overflow | Use `/compact`, break into sessions |
| Claude loops on same error | No retry limit | Specify "if 3 attempts fail, stop" |
| Wrong statistical method used | Insufficient domain spec | Add role prompt + method name |
| Output matches code, not paper | Disconnected context | Point Claude to paper section |

---

## EXERCISE 3 — Prompt Refactor
### (15 minutes, hands-on)

**Goal:** Take a bad prompt and improve it using the templates above.

**Starting prompt:**
```
> Analyze the data and run the regression and make a table.
```

**Task:**
1. Identify which components (Role, Context, Task, Constraints, Output, Verification) are missing.
2. Write a Level 3 version of this prompt for your own research context.
3. Share with a neighbor and critique each other's prompts.
4. Run your improved prompt and compare output quality to the original.

**Bonus:** Take a prompt you've used in the past that produced disappointing results. Apply the framework and rerun it.

---

## MODULE 4 — Project Memory & CLAUDE.md
### (20 minutes, lecture + demo)

### 4.1 What is CLAUDE.md?

`CLAUDE.md` is a file that Claude Code reads automatically at the start of every session in that directory. It is your project's persistent memory — the document that prevents you from re-explaining your project every session.

Think of it as a standing briefing memo for a very capable but amnesiac research assistant.

**Where to put it:**
- `~/CLAUDE.md` — global instructions (applies to all projects)
- `<project-root>/CLAUDE.md` — project-specific (applies when you cd here)
- `<subdir>/CLAUDE.md` — subdirectory-specific (advanced use)

### 4.2 CLAUDE.md Template for an Economics Research Project

```markdown
# CLAUDE.md — [Paper Title]

## Project Overview
- **Topic:** [one sentence]
- **Stage:** [draft | revision | final]
- **Target journal:** [e.g., Review of Economic Studies]
- **Co-authors:** [names and roles]
- **Last updated:** [date]

## Repository Structure
```
data/
  raw/          ← READ ONLY. Never modify.
  processed/    ← Your outputs go here
code/
  estimate.py   ← Main estimation script
  utils.py      ← Helper functions
  config.py     ← All parameters (do not hardcode elsewhere)
figures/        ← All figures (PDF format)
paper/
  main.tex      ← Main paper
  tables/       ← Generated LaTeX tables
  figures/      ← Symlinked from ../figures
notes/          ← Session logs, plans, decisions
```

## Coding Standards
- Python 3.11+; use type hints on all function signatures
- Use `pathlib.Path` for all file I/O (no os.path)
- All random seeds: set in config.py, passed explicitly
- Style: PEP 8, max line length 88 (black-compatible)
- Imports: standard library → third-party → local, alphabetical within groups
- No print() in functions — use logging

## Package Environment
- Environment: `uv` virtual env at `.venv/`
- Activate: `source .venv/bin/activate`
- Key packages: `linearmodels`, `pyfixest`, `pandas`, `numpy`, `matplotlib`
- Install new packages: `uv add <package>` (do not use pip directly)

## Statistical Conventions
- Standard errors: clustered at the [firm/county] level by default
- Fixed effects: two-way (firm + year) in baseline
- Outcome variable: [name and unit]
- Treatment variable: [name and coding]
- Sample: [description of sample restrictions]

## Notation (matches paper/main.tex)
- $i$ = firm, $t$ = year
- $Y_{it}$ = outcome variable
- $D_{it}$ = treatment indicator
- $\beta$ = coefficient of interest
- All variable names in code must match these names

## What I Am Working On Right Now
[Update this section at the start of each session]
- Current task: ...
- Last thing done: ...
- Next step: ...
- Blockers: ...

## Do Not Touch
- data/raw/ — any modification requires explicit confirmation
- paper/main.tex versions before today — check git history
- The main estimation function signature in estimate.py

## Known Issues
- [List any known bugs or data issues here]

## Decisions Made (and Why)
- Used OLS not IV because [reason] (see notes/identification.md)
- Dropped observations where X < 0 because [reason]
- [Add decisions as they arise]
```

### 4.3 The Progress File Pattern (Companion to CLAUDE.md)

For long sessions, maintain a rolling progress file:

```markdown
# notes/progress.md

## Session 2026-04-15

### Completed
- [x] Loaded and cleaned census data
- [x] Merged with patent data on firm FEIN
- [x] Estimated baseline OLS (Table 1)

### In Progress
- [ ] Robustness check: instrument with import competition
- [ ] Heterogeneity analysis by firm size

### Blocked
- IV first stage is weak (F = 4.2). Need to discuss with advisor.

### Decisions Made This Session
- Merged on FEIN not EIN because 23% of EINs are missing
- Dropped 2009 because of census break

### Next Session: Start Here
Read this file first. Then:
1. Fix the IV: try Bartik instrument instead (see paper/lit_review.md)
2. Continue with heterogeneity analysis
```

### 4.4 The Decisions Log

This is one of the most valuable habits:

```
> Write a file called notes/decisions.md if it does not
  exist, then append a new entry:
  
  ## [Today's date]
  **Decision:** [what we decided]
  **Reason:** [why]
  **Alternatives considered:** [what else we thought about]
  **Impact on results:** [expected effect on output]
```

After a month of consistent use, this file becomes invaluable when writing the paper's methodology section, responding to referee comments, or onboarding a new co-author.

---

## EXERCISE 4 — Write Your Own CLAUDE.md
### (10 minutes, hands-on)

**Goal:** Create a `CLAUDE.md` for a real or hypothetical project.

**Steps:**
1. Choose a project (real or the lecture demo).
2. Copy the template above into `CLAUDE.md` in your project root.
3. Fill in the relevant sections. The "What I Am Working On Right Now" and "Coding Standards" sections are the highest value — start there.
4. Launch a new Claude session (`/clear` if already open).
5. Type: `> Summarize this project's status and what I should work on next.`
6. Observe how Claude uses the CLAUDE.md to orient itself.

---

## MODULE 5 — Skills, Subagents & Workflows
### (20 minutes, lecture + demo)

### 5.1 Custom Skills: Reusable Workflows as Slash Commands

If you do something more than once a day, turn it into a skill. In Claude Code,
skills are reusable multi-step workflows stored as `SKILL.md` files under
`.claude/skills/`.

Example workshop skill:
- `example_skill/SKILL.md` → `/data-diagnostics`
- Purpose: inspect a CSV, report shape/dtypes/missingness/outliers, save a note

### 5.2 Subagents: Context Isolation and Verification

Subagents are specialized agents stored under `.claude/agents/`. They are most
useful when you want:

- independent verification
- isolated research in a separate context window
- a cheaper "skeptic" pass before accepting a result

Example workshop subagent:
- `example_subagent/verifier.md`
- Purpose: read-only verification of claims against files, logs, and outputs

### 5.3 Skills vs. Subagents

- Use a **skill** for a repeatable action with one clear workflow.
- Use a **subagent** when you want context separation, specialized review, or a
  skeptical second pass.

---

## EXERCISE 5 — Create a Skill & Use Subagents
### (10 minutes, hands-on)

**Goal:** Install one reusable skill and one verifier-style subagent.

**Steps:**
1. Copy `example_skill/SKILL.md` to `.claude/skills/data-diagnostics/SKILL.md`.
2. Copy `example_subagent/verifier.md` to `.claude/agents/verifier.md`.
3. Run `/data-diagnostics data/synthetic_panel.csv`.
4. Ask Claude to use the verifier subagent to review the diagnostics report.
5. Ask Claude to use subagents to research event-study implementation details for the synthetic panel.

---

## MODULE 6 — From Raw Data to a Paper Section
### (30 minutes, lecture + live demo)

### 6.1 The Full Research Pipeline

```
Raw data
  ↓ [clean.py]
Processed data
  ↓ [estimate.py]
Results (JSON/CSV)
  ↓ [figures.py + tables.py]
Figures (PDF) + Tables (LaTeX)
  ↓ [main.tex]
Paper section draft
```

Claude should be able to run and connect all of these steps given good setup. The goal is a pipeline where running `python main.py --all` reproduces the entire paper from scratch.

### 6.2 Building the Pipeline Step by Step

#### Step 1: Data Diagnostics
```
> Read data/raw/panel_data.csv.
  Do NOT modify it.
  Write a data diagnostic report to notes/data_report.md including:
  - Shape, column names, dtypes
  - Date range and panel dimensions (N firms, T years)
  - Missing value counts by column
  - Summary statistics for all numeric columns (mean, sd, p10, p50, p90)
  - Flag any obvious data issues (negative values where impossible,
    duplicate observations, outliers beyond 5 SD)
  Format as Markdown with a table for each section.
```

#### Step 2: Data Cleaning Script
```
> Based on the data report in notes/data_report.md,
  write code/clean.py that:
  1. Loads data/raw/panel_data.csv
  2. Applies the cleaning steps I describe below:
     [list steps]
  3. Saves to data/processed/panel_clean.parquet (use parquet for speed)
  4. Prints a before/after comparison table:
     - Number of observations dropped and why
     - Any variables transformed (log, winsorize, etc.)
  
  Requirements:
  - Use pathlib for all paths
  - All thresholds (e.g., winsorization cutoffs) must be in config.py
  - Add a docstring at the top of the file explaining what it does
  - At the end, run an assertion: assert len(df) > 10000, "Too few obs"
```

#### Step 3: Estimation
```
> Write code/estimate.py that:
  1. Loads data/processed/panel_clean.parquet
  2. Estimates the following specifications using pyfixest:
     - Spec 1 (baseline): Y ~ D | firm + year | cluster(firm)
     - Spec 2 (controls): Y ~ D + X1 + X2 | firm + year | cluster(firm)
     - Spec 3 (heterogeneity): Y ~ D + D:size_quartile | firm + year | cluster(firm)
  3. Saves results to results/estimates.json with keys:
     "baseline", "controls", "heterogeneity"
     Each value: dict with keys "coefs", "se", "pvalues", "nobs", "r2"
  4. Prints a clean summary table to stdout
  
  The variable names are defined in CLAUDE.md. Use them exactly.
```

#### Step 4: Figures
```
> Write code/figures.py that produces publication-ready figures.
  
  Figure 1: Event study plot
  - Load results/event_study.json
  - X-axis: event time (quarters relative to treatment)
  - Y-axis: estimated coefficient + 95% CI shaded
  - Add vertical line at t=-1, dashed
  - Add horizontal line at 0
  - Style: seaborn-white style, 7x4 inches, 300 DPI
  - Font: serif, size 11
  - Save to figures/fig_event_study.pdf AND figures/fig_event_study.png
  
  Figure 2: Heterogeneity by firm size (bar chart)
  [continue spec]
  
  At the end, print "Saved: [list of saved figures]"
```

#### Step 5: Tables → LaTeX
```
> Write code/tables.py that reads results/estimates.json
  and generates paper/tables/tab_main.tex.
  
  Requirements:
  - Use raw LaTeX string building (no external packages needed)
  - Three columns: Baseline, Controls, Heterogeneity
  - Row order: D (treatment), X1, X2, Constant, then separator, then
    Observations, R², Fixed effects indicators
  - Standard errors in parentheses on next row
  - Stars: * p<0.1, ** p<0.05, *** p<0.01
  - Bottom note: "Robust standard errors clustered at the firm level."
  - Table should compile with just \usepackage{booktabs}
  
  After generating, print the LaTeX to stdout for visual inspection.
```

#### Step 6: Paper Section Draft
```
> Read:
  - paper/main.tex, Section 3 (Data and Methodology)
  - notes/decisions.md
  - results/estimates.json
  - the notation defined in CLAUDE.md

  Write a first draft of Section 4 (Results), 400–600 words, that:
  1. Leads with the main result (coefficient magnitude + significance)
  2. Describes the economic magnitude in plain English using a
     back-of-envelope calculation
  3. Discusses the robustness checks in one paragraph
  4. Uses \citet{} and \citep{} for all references (BibTeX keys
     are in paper/references.bib)
  
  Write to paper/sections/results.tex.
  Add \input{paper/sections/results.tex} to main.tex in the correct place.
  Do NOT change anything else in main.tex.
```

### 6.3 The One-Script Runner

Once all pieces exist, have Claude wire them together:
```
> Write a script called run_all.py that runs the full pipeline:
  clean.py → estimate.py → figures.py → tables.py
  in that order, with clear progress messages.
  
  If any step fails, print the error and exit immediately.
  At the end, print a summary: "Pipeline complete. X figures, Y tables generated."
  
  Add a --dry-run flag that only checks that all input files exist
  without running anything.
```

---

## EXERCISE 6 — Data to Figures to LaTeX
### (25 minutes, hands-on)

**Goal:** Build a mini pipeline that produces a publication-ready figure and LaTeX table.

**Provided data:** `data/synthetic_panel.csv` (synthetic firm panel, 500 firms × 10 years)

**Steps:**
1. Run the data diagnostic prompt (Step 1 above, adapted).
2. Write an estimation script that runs a two-way FE regression.
3. Generate a coefficient plot.
4. Generate a LaTeX table.
5. Compile with `pdflatex` and inspect the output.

**Stretch goal:** Wire the three scripts into a `run_all.py` runner with the pattern above.

---

## MODULE 7 — AI Agents for Paper Replication
### (25 minutes, lecture)

### 7.1 Why Replication?

Replicating existing papers is the single best exercise for mastering AI-assisted research. It is:
- A bounded task with a clear success criterion (do the numbers match?)
- A forcing function for all the skills above (environment, prompts, pipelines)
- A genuine research contribution (many published replications are valued)
- The standard starting point for extending methods

### 7.2 The Replication Ladder

Different papers have different difficulty levels for AI replication:

| Type | Examples | AI success rate | Notes |
|------|----------|----------------|-------|
| Well-documented + code available | Most AER/RES papers post-2023 | High | AI mainly understands and adapts |
| Well-documented, no code | Standard econometrics (OLS, IV) | High | AI reimplements from spec |
| Sparse documentation, standard method | Older papers | Moderate | AI fills gaps; verify carefully |
| Novel method, first paper | Cutting-edge ML methods | Low–Moderate | AI needs guidance |
| Outside training distribution | Very new or unpublished | Low | AI will hallucinate details |

**Key insight from the Bilionis experiment:** AI succeeded on in-distribution papers (SINDy: widely implemented, textbook-level) and near-distribution papers (PIFT: one C++ implementation) but failed on a completely unseen method (BNN paper, unpublished at time of experiment).

Implication: **AI is a very fast second-year PhD student** — excellent at implementing known methods, mediocre at genuinely novel ones.

### 7.3 The Replication Prompt System

Adapt the Bilionis-style autonomous replication prompt:

```
> Role: You are a replication engineer tasked with reproducing
  computational results from a published paper.

  Paper: [title, authors, DOI]
  Paper source: paper/main.tex (LaTeX source)

  Mission: Replicate ALL quantitative results (figures + tables)
  from the paper.

  Hard rules (non-negotiable):
  1. You CANNOT use any code released by the authors.
     Implement from the LaTeX source only.
  2. You CANNOT embed paper figures as your own results.
     All figures must be generated by your implementation.
  3. You MUST track progress in notes/todo.md with checkboxes.
  4. You MUST commit to git after each major step.
  5. If stuck after 3 attempts, write to notes/blocked.md and stop.
  
  Stopping rule: ONLY stop when every targeted result has been
  reproduced OR you have documented why reproduction failed.
  "I ran the code" is not success — the numbers must match.
  
  Implementation requirements:
  - Python + NumPy/SciPy/JAX (as appropriate)
  - All figures saved to figures/replication/ as PDF
  - All tables saved to results/replication/ as JSON and LaTeX
  - A final comparison table: "Paper value vs. Our value"
  - Final report to notes/replication_report.md
  
  Start by reading the paper, then write a plan to notes/plan.md.
  Ask me to confirm before executing.
```

### 7.4 The Figure Reality Check

One of the most important sub-prompts:

```
> Before implementing anything:
  1. Compile paper/main.tex to get a PDF
  2. Extract every figure from the PDF
  3. For each figure, write per-figure notes to notes/figures_analysis.md:
     - Figure number and caption
     - X axis: variable name, range, scale (linear/log)
     - Y axis: variable name, range, scale (linear/log)
     - Number of lines/series
     - Any confidence intervals shown (what level?)
     - Any notable visual features (kinks, jumps, asymmetry)
  4. Also check the LaTeX source for any \includegraphics calls
     that reveal figure-generation parameters

  Only then should we start implementing.
  "I think it shows X" based on captions alone is not sufficient.
```

### 7.5 Handling Missing Details

Replication papers often omit details. The correct agentic approach:

```
> The paper does not specify the learning rate for the optimizer.
  Before guessing:
  1. Write down the three most common values used in this literature
  2. Design a quick sweep: train for 10 epochs with LR ∈ {1e-4, 1e-3, 1e-2}
  3. Run the sweep
  4. Pick the LR that best matches Figure 3's training curve
  5. Document the choice in notes/decisions.md with evidence
```

This pattern — **hypothesize → test → document** — is the hallmark of responsible replication.

### 7.6 Verification Checklist

After AI completes a replication, run this check:

```
> Compare your results against the paper.
  For each figure and table:
  - State the paper's value (read from LaTeX source)
  - State your value
  - Compute the relative error: (ours - paper) / |paper|
  - Classify: ✓ Match (<5% error), ~ Close (5–20%), ✗ Far (>20%)
  
  Write a summary table to notes/replication_check.md.
  For any ✗ result: hypothesize the most likely cause.
```

---

## EXERCISE 7 — Replicate a Method
### (10 minutes, hands-on)

**Goal:** Replicate a specific result from a well-known paper.

**Suggested targets (choose one):**

**Beginner:** Lasso on Macroeconomic Data (Stock & Watson 2012)
- Task: Replicate Figure 1 (forecasting RMSE vs. OLS across variable sets)
- All details are in the paper

**Intermediate:** SINDy (Brunton, Proctor, Kutz 2016)
- Task: Replicate Figure 3 (identified system for the Lorenz equations)
- Paper: https://arxiv.org/abs/1509.03580

**Advanced:** DEQN result from a paper of your choice
- Task: Replicate the first policy function figure

**Prompt to adapt:**
Use the replication prompt from Section 7.3, filling in the paper details. Start with the figure analysis step (7.4) before writing any implementation code.

**Debrief questions:**
- Where did AI succeed immediately? Where did it need help?
- What was the most important piece of context you had to provide?
- What would you verify before citing this replication in your own work?

---

## MODULE 8 — Optional Advanced Patterns: MCPs, Git, HPC
### (20 minutes, lecture)

### 8.1 Git as a Safety Net

Treat every AI session as working with a very fast but impulsive collaborator. Git is your undo button.

```bash
# Before any Claude session
git stash                    # or
git add . && git commit -m "pre-session checkpoint"

# After reviewing Claude's changes
git diff HEAD                # review everything
git add -p                   # selective staging
git commit -m "feat: [what Claude did]"

# If Claude went off the rails
git checkout .               # discard all unstaged changes
git reset --hard HEAD        # discard staged + unstaged
```

**In Claude:** You can ask Claude to use git discipline:
```
> After every completed step (not every file change, but every
  logical unit of work), commit to git with a descriptive message.
  Message format: "[action]: [what was done]"
  Examples: "feat: add IV estimation", "fix: correct SE clustering",
            "data: merge census and patent datasets"
```

### 8.2 MCP: GitHub Integration

With the GitHub MCP connected, Claude can manage your repository:

```
> Create a new branch called robustness-checks.
  Push the current state to that branch.
  Then open a pull request with the title "Add robustness checks"
  and a description summarizing what was done (read notes/progress.md).
```

```
> Look at the open issues on this repo.
  For each issue labeled "bug", suggest a fix in plain English before writing any code.
```

### 8.3 MCP: High-Performance Computing

For compute-intensive work (e.g., DEQN training, large Monte Carlo):

Set up SSH access and create a `cluster_skill.md` for Claude:

```markdown
# Cluster Skill

## Connection
- Cluster: gautschi.rcac.purdue.edu (or your institution's HPC)
- SSH command: ssh username@gautschi.rcac.purdue.edu
- Working dir: /scratch/username/my-paper/

## SLURM Template
```bash
#!/bin/bash
#SBATCH --job-name=deqn_train
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --gres=gpu:1
#SBATCH --time=02:00:00
#SBATCH --mem=32G

module load python/3.11 cuda/12.0
source ~/envs/research/bin/activate
python code/train.py --config config.yaml
```

## Monitoring
- Check status: `squeue -u username`
- Check logs: `tail -f slurm-JOBID.out`
- Kill job: `scancel JOBID`
```

Then prompt:
```
> Transfer code/ and config.yaml to the cluster.
  Submit a SLURM job using the template in cluster_skill.md.
  Monitor it every 5 minutes. When done, download results/ back.
```

### 8.4 The Parallel Agents Pattern

For large projects, run multiple Claude Code sessions in parallel:

```bash
# Terminal 1
cd ~/research/my-paper
claude
# Session: "I'm working on the data cleaning pipeline"

# Terminal 2
cd ~/research/my-paper
claude
# Session: "I'm drafting the literature review section"

# Terminal 3
cd ~/research/my-paper
claude
# Session: "I'm generating robustness tables"
```

Key: Each session should work in non-overlapping files. Set the scope explicitly:
```
> You are only allowed to modify files in the paper/ directory.
  Do not touch code/ or data/.
```

### 8.5 Zotero MCP for Literature

With the Zotero MCP connected:
```
> Search my Zotero library for papers on "carbon taxation OLG".
  Return the 5 most relevant papers with their BibTeX keys.
  For each, write a one-sentence description of its relevance
  to our paper.
```

```
> I want to add a literature review paragraph comparing our
  approach to three existing methods.
  Search Zotero for "deep equilibrium networks economics".
  Read the abstracts and suggest which three papers best
  contrast with our approach.
```

---

## MODULE 9 — Verification, Failure Modes & Ethics
### (15 minutes, lecture)

### 9.1 The Cardinal Rule: Never Skip Verification

AI-generated research code has a failure mode that is worse than a programming error: it produces *plausible but wrong* numbers. An RA who wrote buggy code that crashes is visible. An RA whose code runs cleanly but clusters SEs incorrectly is invisible.

**Mandatory verification steps:**

1. **Sanity checks on simulated data:** Before running on real data, run on synthetic data where you know the true answer.
   ```
   > Before we run on real data: generate a synthetic dataset where
     the true treatment effect is exactly 0.5 and run the estimator.
     The coefficient should be close to 0.5. If not, there is a bug.
   ```

2. **Reproduce a known result:** Run your code on a dataset where a published paper reports the result. Do the numbers match?

3. **Check the identification assumption in code:** Do not just read the code — run the first stage (if IV), print the FWL projection, plot the residuals.

4. **Regression against simple cases:** Does your complex estimator reduce to OLS when it should?

### 9.2 Five Things AI Gets Wrong in Econometrics

1. **Standard error clustering:** Claude often clusters at the wrong level or forgets to cluster at all. Always check: `print(model.summary())` and verify the SE formula in the docs.

2. **Fixed effects in nonlinear models:** Probit/logit with fixed effects — Claude may use the wrong incidental parameters correction. Specify explicitly: "use ppmlhdfe for Poisson FE" or "use logit with FE but flag the incidental parameters problem."

3. **Identification assumptions:** Claude will estimate any model you ask for, including misspecified ones. Domain knowledge is non-substitutable here.

4. **Panel structure:** Claude often forgets to sort by (id, time) before operations that require panel order. Add: "Assert the data is sorted by (firm, year) before any time-series operation."

5. **Merge logic:** Claude merges on the columns you specify, but may use inner/outer/left join incorrectly. Always specify: "Use a left join and check that no observations are lost. Assert len(merged) == len(left)."

### 9.3 Academic Integrity

**What you must disclose:** Most journals now have AI disclosure policies. The emerging standard (as of 2026) is:
- Disclose if AI generated substantial text that appears verbatim in the paper.
- You do not need to disclose AI-assisted code generation (just as you don't disclose using Matlab or Stata).
- You do not need to disclose using AI as an editor for your own prose.
- When in doubt, check the target journal's specific policy.

**What remains your responsibility:**
- All results, claims, and interpretations
- Reproducibility — if you used Claude to write the code, you own that code and must be able to explain and reproduce it
- All citations — AI hallucinating citations is a common failure mode; verify every reference

**Preventing hallucinated citations:**
```
> Do NOT invent any citations.
  Only cite papers that are already in paper/references.bib.
  If you want to cite a paper that is not in the bibliography,
  write it as: [CITE: author, year, topic — to be verified]
  and I will add it manually.
```

### 9.4 Data Privacy and Security

- **IRB-protected data:** Never let Claude read raw files containing PII. Process to aggregate form first.
- **API keys and credentials:** Use `.env` files and `.claudeignore` to wall these off. Never paste them in a prompt.
- **Proprietary datasets:** Check your data use agreement — some explicitly prohibit transmission to third-party AI services.
- **Unpublished work:** Be cautious about pasting unpublished theoretical results into prompts — the content enters Anthropic's API.

---

## Q&A AND DISCUSSION
### (15 minutes)

### Suggested Discussion Topics

1. **The "black box" problem:** If Claude wrote the code, do you truly understand your results?

2. **Competitive dynamics:** If AI dramatically reduces the cost of empirical execution, what changes in the market for research ideas?

3. **Refereeing AI-assisted work:** What signals should you look for as a referee to assess the robustness of AI-generated results?

4. **Graduate training implications:** Should PhD programs still require students to write estimation code by hand?

5. **Level 5 autonomy:** Under what conditions (if any) would you feel comfortable letting an agent run a full analysis unsupervised for two hours?

---

## REFERENCE: Essential Prompt Library

Copy, adapt, and save these prompts. They cover 90% of research workflow tasks.

### Session Management
```
/compact remember all design decisions and the current state of the estimation pipeline
```

```
> Write a session summary to notes/session_YYYY-MM-DD.md covering:
  what we did, what worked, what failed, and what to do next session.
```

### Code Quality
```
> Review all .py files in code/. For each function longer than 50 lines,
  suggest a refactor. For any function with no docstring, write one.
  Do not change behavior — only add documentation and refactor.
```

```
> Write a test suite in tests/test_estimation.py using pytest.
  Test each function in code/estimate.py with at least one test case.
  Use synthetic data where the true values are known.
```

### Data Work
```
> Load [file]. Do NOT modify it. Print:
  1. Shape, dtypes, date range
  2. % missing by column
  3. Summary stats (mean, sd, p10, p25, p50, p75, p90)
  4. Top 10 most common values for categorical columns
  Flag anything that looks unusual.
```

```
> Merge [A.csv] with [B.csv] on [key].
  Use a left join. Assert no rows from A are dropped.
  Print: N before merge, N after merge, N unmatched.
```

### Writing
```
> Read the attached paragraph. Improve it for clarity and concision.
  Rules: do not change meaning, do not change citations,
  do not add claims not in the original.
  Output: the revised paragraph only (no commentary).
```

```
> Read paper/main.tex. Are there any internal inconsistencies?
  Check: (a) notation consistency across sections,
  (b) cross-references to tables/figures that don't exist,
  (c) claims in the text that don't match the results tables.
```

### Debugging
```
> I got this error running code/main.py:
  [paste error + stack trace]
  
  Do not fix it yet. First, explain what caused it and why.
  Then propose two possible fixes. I will choose which one to apply.
```

### Literature
```
> I am writing a paper on [topic]. Here are 5 key papers I cite:
  [list]. What important papers am I likely missing?
  Do not invent references — only suggest papers you are confident exist.
  I will verify each one.
```

---

## APPENDIX A: Recommended Tools & Resources

### Essential Tools
| Tool | Purpose | Install |
|------|---------|---------|
| Claude Code | Primary agentic coding agent | `npm install -g @anthropic-ai/claude-code` |
| Cursor | IDE with agentic features | cursor.sh |
| Ghostty | Fast terminal | `brew install ghostty` |
| Zellij | Terminal multiplexer | `brew install zellij` |
| uv | Python package manager | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Git | Version control | Built-in on Linux/Mac |

### Python Packages for Economics Research
| Package | Purpose |
|---------|---------|
| `pyfixest` | Fast HDFE regression |
| `linearmodels` | Panel data, IV |
| `statsmodels` | General econometrics |
| `econml` | Causal ML (DML, Lasso IV) |
| `pyhdfe` | High-dimensional fixed effects |
| `arch` | Time series, GARCH |
| `scipy.optimize` | Numerical optimization |
| `jax` | Autodiff, GPU-accelerated numerics |

### Key Readings
- Goldsmith-Pinkham (2026): "Getting Started with Claude Code: A Researcher's Setup Guide" — paulgp.substack.com
- Bilionis et al. (2026): "We Asked an AI Agent to Replicate Three Research Papers" — ebilionis.substack.com
- Korinek & Balwit (2023): "Aligned AI as a Tool for Economists" — AEA Papers & Proceedings
- Anthropic Claude Code Docs: docs.anthropic.com/en/docs/claude-code

---

## APPENDIX B: Sample CLAUDE.md for a Computational Economics Paper

```markdown
# CLAUDE.md — Machine Learning for Dynamic Economic Models

## Project
Solving high-dimensional dynamic programs using deep equilibrium networks (DEQNs).
Target: Review of Economic Studies.
Stage: Revision.

## Repository Layout
code/
  deqn/           ← DEQN implementation (DO NOT modify without discussion)
  utils/          ← Helper functions
  experiments/    ← Experiment runners
  tests/          ← pytest test suite
data/
  calibration/    ← Parameter files (YAML)
  synthetic/      ← Synthetic benchmarks (reproducible from seed)
figures/
results/
  checkpoints/    ← Model checkpoints (gitignored, large)
  tables/         ← LaTeX table fragments
paper/
  main.tex
  sections/

## Tech Stack
- Python 3.11 + JAX 0.4.x
- Training: JAX JIT + vmap; all loops eliminated from inner loop
- GPU: CUDA 12; run via SLURM on cluster (see cluster_skill.md)
- Figures: matplotlib, seaborn-white style, PDF output
- Tables: raw LaTeX (no external packages except booktabs)

## Notation (paper/main.tex is authoritative)
- $V(s)$ = value function, $s$ ∈ state space
- $\pi(s)$ = policy function
- $\theta$ = neural network parameters
- $\beta$ = discount factor = 0.96
- All variable names in code: lowercase_snake_case matching paper notation

## Performance Targets
- 10-state model: solve in < 60 seconds on A100
- Policy function error vs. VFI benchmark: < 1e-4 in L∞ norm

## DO NOT
- Change the network architecture in deqn/model.py without creating
  a new file first and running tests
- Commit model checkpoints to git (they are gitignored)
- Use TF or PyTorch — this project is JAX-only
- Hardcode cluster-specific paths — use config.yaml

## Current Status
[Update each session]
```

---

## APPENDIX C: Quick Reference Card

Print and keep at your workstation.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AGENTIC AI RESEARCH — QUICK REFERENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BEFORE EVERY SESSION
□ git add . && git commit -m "pre-session checkpoint"
□ Update CLAUDE.md "What I Am Working On"

CONTEXT WINDOW HYGIENE  
□ Use /compact when session > 20 turns
□ Write state to notes/progress.md
□ Break big tasks into focused sub-sessions

PROMPT CHECKLIST (Level 3)
□ Role or context set?
□ Specific file names and paths given?
□ Constraints on what NOT to do?
□ Output format specified?
□ Verification step included?

SAFETY
□ Never point Claude at raw IRB/PII data
□ .claudeignore protects sensitive files
□ Review git diff before every commit
□ Interrupt early if Claude goes wrong direction

VERIFICATION
□ Run on synthetic data with known answer first
□ Check SE clustering formula explicitly
□ Verify merge: assert N before == N after
□ Never trust hallucinated citations

AFTER EVERY SESSION
□ git diff HEAD → review all changes
□ git add -p && git commit
□ Update notes/progress.md
□ Update CLAUDE.md "Current Status"

KEY COMMANDS
/compact           → compress context
/clear             → fresh context
/cost              → check token spend
Ctrl+C             → interrupt execution
ESC                → undo last turn
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

*Syllabus maintained at: [your course repository URL]*
*Feedback and corrections welcome.*
*Last revised: March 2026*
