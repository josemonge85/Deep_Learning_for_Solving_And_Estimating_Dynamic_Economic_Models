# Exercise Prompts -- Day 5: Agentic Programming

Copy-pasteable prompts for **twelve** exercises (0 and 1--11). Use this file
alongside `exercise_solutions.md`. Adapt file paths and project names to your
own setup.

- **Exercise 0** (10 min) -- Hello Claude. Zero setup, smallest possible first contact.
- **Exercises 1--7** (~3 h total) -- The canonical workshop flow.
- **Exercises 8--11** (~20 min each) -- Short, self-contained practice on
  specialist subagents, hooks, the strategic-revision skill, and the Mincer
  warm-up demo. Designed for self-study.

---

## Exercise 0: Hello Claude (10 min)

**Goal:** Confirm Claude Code is installed and your shell sees it. No research
content yet.

### Step 1 -- Install (if needed)
```bash
# Primary route (cross-platform):
npm install -g @anthropic-ai/claude-code
# Verify:
claude --version
```

### Step 2 -- Make a scratch folder and launch Claude
```bash
mkdir -p ~/research/hello-claude && cd ~/research/hello-claude
echo "Just testing." > notes.txt
claude
```

### Step 3 -- Paste this into Claude Code
```text
What files are in this directory? Then read notes.txt and
rewrite it in the style of a one-sentence haiku. Save to haiku.md.
```

### Step 4 -- Verify
```bash
cat haiku.md           # should contain a short haiku
ls                     # should now include haiku.md
```

**Success criteria**
- `claude --version` prints a version
- `haiku.md` exists and contains exactly what you asked for
- You understand that Claude read your file and wrote a new file

**Stretch:** Type `/cost` inside Claude and note how much that cost in tokens.

---

## Exercise 1: Environment Bootstrap (15 min)

**Goal:** Get a working Claude Code session in a version-controlled project.

### Step 1 -- Create a demo project and local data copy (run in your terminal)
```bash
mkdir ~/research/lecture-demo && cd ~/research/lecture-demo
cp /path/to/Deep_Learning_Econ_Finance_Geneva_2026/lectures/day5/code/generate_synthetic_data.py .
python generate_synthetic_data.py
git init && git branch -M main
echo "# Lecture Demo - $(date +%Y-%m-%d) - [Your Name]" > NOTES.md
git add NOTES.md generate_synthetic_data.py data/synthetic_panel.csv
git commit -m "init: lecture demo project"
```

### Step 2 -- Launch Claude Code
```bash
claude
```

### Step 3 -- First prompt (paste into Claude Code)
```text
What files are in this directory? Summarize the structure.
```

### Step 4 -- Generate code (paste into Claude Code)
```text
Create a Python script called explore_data.py that:
1. Accepts a CSV file path as a command-line argument
2. Loads the CSV with pandas
3. Prints: shape, column names, dtypes, first 5 rows
4. Prints summary statistics (mean, std, min, max) for numeric columns
5. Reports the percentage of missing values per column
Use pathlib for all file paths. Add an if __name__ == "__main__" guard.
```

### Step 5 -- Run and commit (in your terminal)
```bash
python explore_data.py data/synthetic_panel.csv
git add . && git commit -m "exercise 1: first claude session"
```

**Stretch goal:** Add a `## Read-only paths` section to `CLAUDE.md` listing
`data/raw/` and `.env`, then sketch a `PreToolUse` hook (Exercise 10) that
hard-blocks any `Edit`/`Write` to those paths.

---

## Exercise 2: First Real Task (15 min)

**Goal:** Use a Level 3 prompt + Plan Mode to analyze the shared synthetic panel.

### Step 1 -- Enter Plan Mode (Shift+Tab inside Claude Code)
Press **`Shift+Tab`** until the prompt indicator shows `[plan]`. In plan
mode Claude proposes a plan first and waits for your approval *before*
touching any file. This is the right starting move for any non-trivial
task.

### Step 2 -- The prompt (paste into Claude Code while in plan mode)
```text
I have a dataset at data/synthetic_panel.csv.
Without loading it yet, first tell me how to inspect it
(column names, shape, date range, missing values).
Then:
1. Load it and print the above diagnostics
2. Compute annual average revenue by treatment group
3. Generate a 2x2 panel of plots using matplotlib:
   - Top-left: mean revenue over time, treated vs control
   - Top-right: histogram of log(revenue), pre vs post
   - Bottom-left: mean employees over time, treated vs control
   - Bottom-right: scatter of log(revenue) vs log(employees)
   Style: no gridlines, serif font, 6x5 inches, 300 DPI.
4. Save the figure to figures/panel_overview.pdf
5. Write a 3-sentence description of what you see
   to notes/data_description.md
```

### Step 3 -- Read the plan, then approve
Claude returns a numbered plan (no edits yet). Read it. If you spot a
missing constraint, *type a correction first*, then approve. Press
**`Shift+Tab`** again to exit plan mode and let Claude execute.

**Reflection questions after completing**

- Where did Claude do well?
- Where did it need correction?
- At what point would you have interrupted?
- What constraint would have prevented any issues?

---

## Exercise 3: Prompt Refactor (15 min)

**Goal:** Take a bad prompt and improve it using the 6-component framework.

### The bad prompt (Level 0)
```text
Analyze the data and run the regression and make a table.
```

### Your task

1. **Diagnose:** Which of the 6 components are missing?
   - [ ] Role
   - [ ] Context
   - [ ] Task
   - [ ] Constraints
   - [ ] Output specification
   - [ ] Verification
2. **Rewrite** it as a Level 3 prompt. Here is a model answer to compare against:

### Model answer (Level 3 rewrite)
```text
[ROLE] You are a computational economist working on panel data analysis.
[CONTEXT] I have a firm-level panel dataset at data/synthetic_panel.csv.
Variables: revenue (USD millions), employees (count), treated (0/1 indicator),
firm_id (integer), year (2010-2019). Treatment starts in 2015.
[TASK] Estimate a difference-in-differences regression:
  log(revenue) ~ treated * post + firm_FE + year_FE
  with standard errors clustered at the firm level.
[CONSTRAINTS] Use pyfixest. Do not modify the data file.
  Do not use deprecated pandas methods.
[OUTPUT] Save regression results to results/did_estimates.json.
  Generate a LaTeX table with booktabs to paper/tables/tab_did.tex.
  Three columns: (1) no FE, (2) firm FE, (3) two-way FE.
  Standard errors in parentheses. Stars: * p<0.1, ** p<0.05, *** p<0.01.
[VERIFY] Also run on a synthetic dataset where true effect = 0.05.
  The estimated coefficient should be within 0.01 of the true value.
```

3. **Test both** in Claude Code and compare the output quality.

---

## Exercise 4: Write Your Own CLAUDE.md (10 min)

**Goal:** Create a `CLAUDE.md` for a real or hypothetical project.

### Step 1 -- Copy the template
Copy `CLAUDE_md_template.md` to your project root and rename it to
`CLAUDE.md`:
```bash
cp /path/to/Deep_Learning_Econ_Finance_Geneva_2026/lectures/day5/code/CLAUDE_md_template.md \
   ~/research/lecture-demo/CLAUDE.md
```

### Step 2 -- Fill in the three highest-value sections
Edit `CLAUDE.md` and customize:

- **Repository Structure** (which directories are read-only?)
- **Coding Standards** (what rules should Claude follow?)
- **Current Status** (what are you working on right now?)

> **Note:** the template assumes `uv` for venv management and a `pyproject.toml`
> layout. If your project uses plain `pip`/`venv`, conda, or poetry, delete the
> `## Package Environment` section (or rewrite it for your setup) -- a stale
> section is worse than a missing one.

### Step 3 -- Test it (paste into Claude Code after `/clear`)
```text
Summarize this project's status and what I should work on next.
```

### Step 4 -- Verify constraints (paste into Claude Code)
```text
Write a function to compute the treatment effect.
Follow the coding standards and notation defined in this project.
```

**Check:** Does Claude respect `pathlib`, type hints, NumPy docstrings, and
your naming conventions?

### Step 5 -- Test the guardrails (paste into Claude Code)
```text
Delete data/raw/original_download.csv and replace it with a cleaned version.
```

**Expected:** Claude should refuse because `CLAUDE.md` marks `data/raw/` as
read-only.

---

## Exercise 5: Create a Skill and Use Subagents (10 min)

**Goal:** Create one reusable skill and one verifier-style subagent. We use
two routes for the subagent: the **`/agents` UI** (interactive, recommended
for first-timers) and the **copy-the-file** route (scriptable, for CI / repo
templates).

### Step 1 -- Copy the example skill (run in your terminal)
```bash
cd ~/research/lecture-demo
mkdir -p .claude/skills/data-diagnostics
cp /path/to/Deep_Learning_Econ_Finance_Geneva_2026/lectures/day5/code/example_skill/SKILL.md \
   .claude/skills/data-diagnostics/SKILL.md
```

### Step 2 -- Create the verifier subagent via the `/agents` UI
Inside Claude Code:
```text
/agents
```
A picker opens. Choose **Create new agent** -> **Project**. Set:
- **name:** `verifier`
- **model:** `haiku` (cheap; verifiers don't need Opus)
- **tools:** `Read, Grep, Glob` (read-only)
- **system prompt:** "You are a sceptical verifier. Read the artifact
  the user names, list the two biggest risks, cite the evidence line
  by line. Do not modify any file."

Confirm. The UI writes `.claude/agents/verifier.md` for you. (Equivalent
shell-only route: `cp .../example_subagent/verifier.md
.claude/agents/verifier.md` -- use this in repo templates / CI.)

### Step 3 -- Run the skill (paste into Claude Code)
```text
/data-diagnostics data/synthetic_panel.csv
```

### Step 4 -- Use the verifier subagent (paste into Claude Code)
```text
Use the verifier subagent to review the diagnostics report.
List the two biggest risks before I estimate anything,
and tell me what evidence you used for each claim.
```

### Step 4 -- Use subagents for scoped research (paste into Claude Code)
```text
Use subagents to research how DiD event studies are typically implemented
in Python, then outline an implementation plan for our synthetic data.
Keep the final answer to one page and cite only what you actually inspected.
```

---

## Exercise 6: Data -> Figures -> LaTeX Pipeline (25 min)

**Goal:** Build a complete mini research pipeline from the shared synthetic
panel.

If you are not already in a project with local data, first run:

```bash
python generate_synthetic_data.py
```

### Prompt 1 -- Diagnostics
```text
Run /data-diagnostics on data/synthetic_panel.csv.
Then summarize the two most important data-quality conclusions
in notes/pipeline_diagnostics.md before writing any code.
```

### Prompt 2 -- Estimate
```text
Write code/estimate_did.py:
Load data/synthetic_panel.csv.
Use the existing "post" column (1 if year >= 2015, else 0;
already present in the synthetic panel -- do not recreate it).
Run three OLS regressions of log(revenue) on treated*post:
  (1) No fixed effects
  (2) Firm fixed effects (use dummies or demeaning)
  (3) Firm + year fixed effects
Use numpy and scipy only (no statsmodels/pyfixest).
Cluster standard errors at the firm level.
Save all coefficients, SEs, p-values, N, and R-squared
to results/did_results.json.
Print a summary table to stdout.
```

### Prompt 3 -- Generate figure
```text
Write code/plot_did.py:
Load data/synthetic_panel.csv.
Create an event study plot:
- For each year 2010-2019, estimate the coefficient on
  treated * I(year == t), with 2014 as the omitted reference year.
- X-axis: year, Y-axis: coefficient (relative to 2014)
- Add 95% confidence intervals as a shaded band
- Vertical dashed line at 2014 (treatment onset)
- Style: serif font, 7x4 inches, 300 DPI, no gridlines
Save to figures/event_study.pdf AND figures/event_study.png.
```

### Prompt 4 -- Generate LaTeX table
```text
Write code/make_table.py:
Read results/did_results.json.
Generate a LaTeX table to paper/tables/tab_did.tex.
Format:
- Three columns: (1) No FE, (2) Firm FE, (3) Two-way FE
- Coefficient of treated*post in the first row
- Standard errors in parentheses below
- Stars: * p<0.1, ** p<0.05, *** p<0.01
- Rows for: N observations, R-squared, Firm FE (Yes/No), Year FE (Yes/No)
- Use booktabs (toprule, midrule, bottomrule) only
Print the LaTeX to stdout as well.
```

### Prompt 5 -- Verify
```text
The true treatment effect is 0.05.
Load results/did_results.json and check:
1. Is the two-way FE coefficient within [0.03, 0.07]?
2. Is it statistically significant at the 5% level?
3. Are the pre-trend coefficients (2010-2014) close to zero?
Print PASS or FAIL for each check with the actual values.
```

**Stretch goal:** Write `run_all.py` that chains steps 1-4 with error handling.

---

## Exercise 7: Replicate a Method (10 min)

**Goal:** Use an AI agent to replicate a published result from scratch.

### Choose your difficulty

| Level | Paper | Target |
|-------|-------|--------|
| Beginner | Stock & Watson (2012), Lasso forecasting | Figure 1: RMSE vs OLS |
| Intermediate | Brunton, Proctor & Kutz (2016), SINDy (arXiv:1509.03580) | Figure 3: Lorenz system |
| Advanced | Any DEQN paper from Days 1-4 | First policy function figure |

### The replication prompt (adapt for your chosen paper)
```text
Role: You are a replication engineer.

Paper: [title, authors, year]
Mission: Replicate [specific figure or table number].

Hard rules:
1. You CANNOT use any code released by the authors.
2. Track progress in notes/todo.md with checkboxes.
3. Commit to git after each major step.
4. If stuck after 3 attempts, write to notes/blocked.md and STOP.

Before implementing:
1. Read the paper description (I will provide relevant details)
2. For the target figure: identify x-axis, y-axis, ranges,
   number of series, any confidence intervals
3. Write a plan to notes/plan.md
4. Ask me to confirm before executing

Implementation:
- Python + NumPy/SciPy only (no sklearn for the beginner track)
- Save figure to figures/replication/
- Save code to code/replicate_[paper].py

Final check: compare your result to the paper's figure
and write a brief assessment to notes/replication_assessment.md.
```

### Debrief questions

1. Where did AI succeed immediately?
2. What context did you have to provide that was not in the prompt?
3. What would you verify before citing this replication in your own paper?

---

## Exercise 8: Mincer Warm-Up Demo (15 min)

**Goal:** Reproduce the Mincer wage demo from the slides by driving Claude
Code, then compare against the reference script.

### Step 1 -- Install the data package
```bash
pip install --user statsmodels wooldridge
```

### Step 2 -- Run the reference script once so you know the target
```bash
cd /path/to/lectures/day5/code
python3 mincer_demo.py
ls outputs/                 # should list mincer_table.tex, mincer_figure.pdf
```

### Step 3 -- Start a fresh scratch project and launch Claude
```bash
mkdir -p ~/research/mincer-demo && cd ~/research/mincer-demo
git init && git branch -M main
claude
```

### Step 4 -- Paste this Level 3 prompt
```text
Role: applied labour economist.
Data: wage1 from the `wooldridge` package.
Model:  log(wage) = b0 + b1*educ + b2*exper + b3*exper^2 + b4*female + u

Outputs:
1) outputs/mincer_table.tex -- booktabs regression table,
   standard errors in parentheses, stars at .01/.05/.10.
2) outputs/mincer_figure.pdf -- scatter of educ vs log(wage)
   + fitted partial line, holding exper and female at means;
   serif font, 6x4 inches.

Constraints: do NOT modify the raw dataset.
Verify: print the regression summary and assert 0.07 < b1 < 0.10.
```

### Step 5 -- Diff your output against the reference
```bash
diff outputs/mincer_table.tex /path/to/lectures/day5/code/outputs/mincer_table.tex || true
```
The coefficients should match to 4 decimals. The figure need not be byte-identical.

**Reflection:** How many of the 6 prompt components are present? Which did
Claude fill in from context rather than from your prompt?

---

## Exercise 9: Use a Specialist Subagent (20 min)

**Goal:** Feel the difference between a generic reviewer and a domain
specialist.

### Step 1 -- Copy the two reviewers into your scratch project
```bash
cd ~/research/lecture-demo      # or whichever demo project from Ex 1
mkdir -p .claude/agents
cp /path/to/lectures/day5/code/example_subagent/code_reviewer.md          .claude/agents/
cp /path/to/lectures/day5/code/example_subagent/econometrics_reviewer.md  .claude/agents/
```

### Step 2 -- Write a deliberately imperfect DiD script
Paste into Claude:
```text
Create code/toy_did.py that:
- loads data/synthetic_panel.csv
- builds a "post" column = 1{year >= 2015}
- runs an OLS of log(revenue) on treated*post WITHOUT firm or year FE
- uses robust HC1 standard errors (NOT clustered)
- prints the coefficient and SE

Keep it under 30 lines. Use numpy and statsmodels.
```

### Step 3 -- First audit with the generic reviewer
```text
> Use the code-reviewer subagent on code/toy_did.py.
```
Note what it finds (mostly style, correctness).

### Step 4 -- Second audit with the specialist
```text
> Use the econometrics-reviewer subagent on code/toy_did.py.
  Treatment is firm-level, staggered adoption from 2015.
```
Note the *new* issues it surfaces: missing FE, clustering at wrong level,
no pre-trend check, no heterogeneous-effects consideration.

### Step 5 -- Fix one issue and re-audit
Pick the highest-priority flag and ask Claude to fix it. Then re-run
`> Use the econometrics-reviewer subagent on code/toy_did.py.`

**Reflection:** Make a two-column list -- what the generic reviewer flagged
vs. what the specialist flagged. Which list would a referee care about?

---

## Exercise 10: Install a Hook and a Real Skill (20 min)

**Goal:** Automate the two actions you most often repeat by hand.

### Part A -- Audit-log hook (10 min)

1. Install the example hooks file (requires `jq`):
   ```bash
   cd ~/research/lecture-demo
   mkdir -p .claude
   cp /path/to/lectures/day5/code/example_hooks/settings.json .claude/settings.json
   ```

2. Open it and read the three hooks defined (`PostToolUse`, `PreToolUse`, `Stop`).

3. Launch Claude and ask it to edit some file, then:
   ```bash
   cat .claude/audit.log
   ```
   You should see one line per edit.

4. Now ask Claude to modify `data/raw/original_download.csv` (create a dummy
   file first if needed). The `PreToolUse` hook should block the edit.

### Part B -- Strategic-revision skill (10 min)

1. Copy the skill:
   ```bash
   cp -r /path/to/lectures/day5/code/example_skill_strategic_revision \
         .claude/skills/strategic-revision
   ```

2. Create two fake referee reports as plain markdown (3-5 comments each) at
   `referee1.md` and `referee2.md`. Add one deliberately conflicting request
   between the two (e.g., R1 wants more theory, R2 wants less).

3. Inside Claude:
   ```text
   /strategic-revision referee1.md referee2.md
   ```

4. Inspect `notes/revision_plan.md`:
   - Are comments parsed into discrete tasks?
   - Is the conflict flagged in its own section?
   - Are dependencies mapped between tasks?

**Reflection:** What would it have taken to produce this plan by hand? How
many times a year do you get a stack of referee reports?

---

## Exercise 11: Design a Monte Carlo Study (30 min)

**Goal:** Use the `monte-carlo-designer` subagent to stress-test a toy estimator.

### Step 1 -- Install the subagent
```bash
cp /path/to/lectures/day5/code/example_subagent/monte_carlo_designer.md \
   .claude/agents/
```

### Step 2 -- Write a minimal target estimator
Paste into Claude:
```text
Create code/ols_plus.py that exposes one function:

    def estimate(y, X) -> (beta_hat, se_hat):
        # OLS + HC1 standard errors
        ...

Write it with numpy only. Add a 3-line docstring.
```

### Step 3 -- Ask the designer to plan first
```text
> Use the monte-carlo-designer subagent to propose an MC plan
  for code/ols_plus.py. Estimand: the coefficient on x1.
  DGPs: (i) homoskedastic baseline, (ii) heteroskedastic with
  Var(e) = (1 + x1^2). Grid: N in {200, 1000, 5000}. 1000 reps.
  Target runtime < 5 minutes on this laptop.

  Save the plan to notes/mc_plan.md and WAIT for my approval.
```

Read `notes/mc_plan.md`. Edit the plan if needed.

### Step 4 -- Approve and execute
```text
Plan approved. Please run the Monte Carlo now and save results
under simulations/results/ in parquet form.
```

### Step 5 -- Inspect the output
```bash
ls simulations/ outputs/tables/ outputs/figures/
cat notes/mc_memo.md
```

Expected artefacts:
- `simulations/mc_ols_plus.py`
- `simulations/results/*.parquet`
- `outputs/tables/mc_ols_plus.tex`
- `outputs/figures/mc_ols_plus.pdf`
- `notes/mc_memo.md`

**Reflection:** The HC1 SE should be near-correct in the baseline and
under-cover in the heteroskedastic DGP. Do your size tables confirm this? If
not, is the estimator wrong or the MC wrong? (This is the moment an MC study
is supposed to create.)

---

## Exercise 12: Run an Autonomous Ralph Loop (30--45 min)

**Goal.** Drive a closed-loop, autonomous iteration with the
Anthropic-verified `/ralph-loop` plugin. By the end, Claude will have
implemented a tiny estimator, written its tests, and committed -- with you
only specifying what "done" looks like.

**Background.** See Day 5 Part VII slides. Two flavours:
- `/ralph-loop` plugin (single prompt, stop-hook re-injection).
- `snarktank/ralph` (PRD-driven, fresh AI each iteration; advanced).

We do the simpler `/ralph-loop` here; the snarktank flow is left as a
stretch.

### Step 1 -- Install the plugin (inside Claude Code)
```
/plugin marketplace add ralph-loop
/plugin install ralph-loop
```

### Step 2 -- Prepare the workspace (in your terminal)
```bash
mkdir -p ~/research/ralph-demo/{code,tests,results}
cd ~/research/ralph-demo
git init && git branch -M main
git commit --allow-empty -m "init"

# Seed an empty estimator and an empty test
cat > code/estimator.py <<'EOF'
"""Tiny ridge-regression estimator. To be implemented by Ralph."""
import numpy as np

def fit_ridge(X: np.ndarray, y: np.ndarray, lam: float) -> np.ndarray:
    """Return the coefficient vector beta_hat solving
       (X'X + lam I) beta = X'y."""
    raise NotImplementedError
EOF

cat > tests/test_estimator.py <<'EOF'
"""Three machine-checkable acceptance tests for the Ralph loop."""
import numpy as np
from code.estimator import fit_ridge

def test_recovers_known_beta():
    rng = np.random.default_rng(0)
    n, p = 200, 5
    X = rng.standard_normal((n, p))
    beta_true = np.array([1.0, -0.5, 0.0, 2.0, -1.5])
    y = X @ beta_true + 0.1 * rng.standard_normal(n)
    beta_hat = fit_ridge(X, y, lam=1e-6)
    assert np.allclose(beta_hat, beta_true, atol=0.05)

def test_ridge_shrinks_with_large_lambda():
    rng = np.random.default_rng(0)
    X = rng.standard_normal((100, 3))
    y = X @ np.array([3.0, -2.0, 1.0]) + rng.standard_normal(100)
    beta_small = fit_ridge(X, y, lam=1e-6)
    beta_large = fit_ridge(X, y, lam=1e3)
    assert np.linalg.norm(beta_large) < np.linalg.norm(beta_small)

def test_returns_correct_shape():
    rng = np.random.default_rng(0)
    X = rng.standard_normal((50, 7))
    y = rng.standard_normal(50)
    beta = fit_ridge(X, y, lam=1.0)
    assert beta.shape == (7,)
EOF

git add . && git commit -m "seed: estimator stub + acceptance tests"
```

### Step 3 -- Launch the loop (inside Claude Code in this dir)
```
/ralph-loop "Implement code/estimator.py so that
   `pytest -q tests/test_estimator.py` passes with all three tests green.
   After each implementation attempt, run pytest, read the output, and
   refine. When all tests pass, write the literal string
   ALL_TESTS_PASS as the final line of your response."
   --max-iterations 6
   --completion-promise "ALL_TESTS_PASS"
```

### Step 4 -- Watch and verify
- Each iteration: Claude edits `code/estimator.py`, runs `pytest`, reads
  the failures, edits again. The plugin re-injects the prompt on every
  `Stop` until it sees `ALL_TESTS_PASS` or the iteration cap is hit.
- Use `/cost` between iterations to track spend.
- If it spins, type `/cancel-ralph`.

**Success criterion.** All three tests green; `git log --oneline` shows one
or more commits made inside the loop; `/cost` < $1 on Sonnet.

### Reflection
1. What did the loop do that you would have done differently?
2. How would you tighten the prompt to converge in fewer iterations?
3. What is the smallest *machine-checkable* spec for which you would trust
   a 20-iteration Ralph loop to run unsupervised?

### Stretch (Ex 12b): the PRD-driven `snarktank/ralph`
For a multi-story project, install:
```
/plugin marketplace add snarktank/ralph
/plugin install ralph-skills@ralph-marketplace
```
Then ask Claude inside a fresh project:
```
> Load the prd skill and create a PRD for: "DiD estimator on
  data/synthetic_panel.csv, with cluster-robust SE, an event-study
  plot, a LaTeX table, and pytest acceptance tests on synthetic data
  with known true effect = 0.05."

> Load the ralph skill and convert tasks/prd-did.md to prd.json.
```
Inspect `prd.json`, then run `./scripts/ralph/ralph.sh --tool claude 15`.
Watch `progress.txt` grow and `prd.json` update one story at a time.

**Hard rules for any Ralph loop in research:**
- Always run on a feature branch you can throw away.
- Hooks on (especially the `data/raw/` `PreToolUse` guard).
- Set `--max-iterations` *and* a per-iteration timeout
  (`timeout 600` in front of the script).
- Treat the resulting commits as a junior contributor's PR -- review
  before merging to `main`.


