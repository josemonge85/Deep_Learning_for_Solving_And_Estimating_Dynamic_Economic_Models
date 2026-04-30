# Exercise Solutions -- Day 5: Agentic Programming

These are **reference solution sketches**, not the only acceptable answers.
The point of the workshop is to learn how to drive the agent well, so the
"solution" is defined by the workflow, artifacts, and checks more than by one
exact code listing.

## Exercise 0: Hello Claude

**Reference workflow**

1. Install Claude Code and confirm `claude --version` works.
2. Create a scratch folder, drop one small file into it, launch `claude`.
3. Ask Claude to read the file and write a derivative artefact.

**Expected artifacts**

- `haiku.md` containing a short three-line haiku referencing `notes.txt`.

**Typical mistakes**

- Running `claude` outside any project folder (Claude will happily work in
  `~`; don't). Always `cd` into a specific project first.
- Forgetting that Claude's output is invisible until it writes a file or
  prints to stdout -- read both.
- Running out of the free-tier budget before you start real work; consider a
  `$20/mo` plan from day one.

## Exercise 1: Environment Bootstrap

**Reference workflow**

1. Create a clean git repository.
2. Copy `generate_synthetic_data.py` into the demo project and run it so
   `data/synthetic_panel.csv` exists locally.
3. Launch Claude Code and run `/init`.
4. Ask for `explore_data.py` with `pathlib` and a standard CLI entry point.
5. Run the script, inspect the output, and commit the result.

**Expected artifacts**

- `CLAUDE.md`
- `data/synthetic_panel.csv`
- `explore_data.py`
- One git commit

**What to check**

- The script accepts a CSV path argument.
- The script prints shape, columns, dtypes, head, summary stats, and missingness.
- The file uses `pathlib.Path` rather than `os.path`.

## Exercise 2: First Real Task

**Reference workflow**

1. Press `Shift+Tab` *before* sending the prompt; the indicator should
   read `[plan]`.
2. Send the Level-3 prompt. Claude responds with a numbered plan
   (no file edits).
3. Read the plan, type any correction, then approve. Press `Shift+Tab`
   again to leave plan mode and let Claude execute.
4. Review the figure for layout and labeling before trusting the narrative.

**Expected artifacts**

- `figures/panel_overview.pdf`
- `notes/data_description.md`

**What a good answer usually notices**

- Revenue trends are similar pre-2015 and drift modestly apart afterward.
- Employee counts trend upward over time for both groups.
- Log revenue and log employees are positively related.

**Common Plan Mode pitfalls**

- Forgetting to *approve* after reading the plan -- Claude waits silently.
- Approving a plan that says "I will modify `data/raw/...`" -- read the plan
  before clicking yes.
- Using plan mode for trivial 1-line tasks -- it adds friction without
  benefit; skip it.

## Exercise 3: Prompt Refactor

**Reference model answer**

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

**What to check**

- Every one of the six components is present.
- The output locations are explicit.
- Verification is concrete rather than vague.

## Exercise 4: Write Your Own `CLAUDE.md`

**Reference workflow**

1. Copy the template.
2. Fill in `Repository Structure`, `Coding Standards`, and `Current Status`.
3. Start a fresh Claude session so the file is loaded automatically.
4. Test both a normal coding request and a guardrail-violating request.

**Expected behavior**

- Claude summarizes the project using your custom context.
- Claude follows rules like `pathlib`, type hints, and naming conventions.
- Claude refuses or pushes back on requests that touch read-only paths such as
  `data/raw/`.

## Exercise 5: Create a Skill and Use Subagents

**Reference workflow**

1. Copy `example_skill/SKILL.md` into
   `.claude/skills/data-diagnostics/SKILL.md`.
2. Create the verifier subagent **via the `/agents` UI** (recommended for
   first-timers): pick `Create new agent -> Project`, set
   `name=verifier`, `model=haiku`, `tools=Read, Grep, Glob`, paste the
   short system prompt. Confirm; the UI writes
   `.claude/agents/verifier.md` for you.
3. Equivalent **shell route** (for repo templates / CI):
   `cp example_subagent/verifier.md .claude/agents/verifier.md`.
4. Run `/data-diagnostics data/synthetic_panel.csv`.
5. Ask Claude to use the verifier subagent to review the diagnostics report.
6. Ask Claude to use subagents to research event-study implementation details.

**Expected artifacts**

- `.claude/skills/data-diagnostics/SKILL.md`
- `.claude/agents/verifier.md`
- `notes/diagnostics_*.md` or an equivalent diagnostics note

**What to check**

- The skill runs a reusable multi-step workflow.
- The subagent is used for isolated review/research, not as a generic synonym
  for "do more work."
- You used the `/agents` UI at least once; you understand that the UI is just
  a friendly wrapper around the same `.md` files the shell route writes.

## Exercise 6: Data -> Figures -> LaTeX Pipeline

**Reference workflow**

1. Start from `data/synthetic_panel.csv`.
2. Run `/data-diagnostics` or an equivalent diagnostic pass first.
3. Generate `code/estimate_did.py`, `code/plot_did.py`, and `code/make_table.py`.
4. Save regression output to JSON, figure output to `figures/`, and LaTeX to
   `paper/tables/`.
5. Run a verification prompt that checks magnitude, significance, and pre-trends.

**Expected artifacts**

- `results/did_results.json`
- `figures/event_study.pdf`
- `figures/event_study.png`
- `paper/tables/tab_did.tex`
- Optionally `run_all.py`

**What to check**

- The two-way FE estimate is in the neighborhood of the true effect.
- Output paths are deterministic and script-based.
- The table is raw LaTeX with `booktabs`, not a screenshot or pasted image.

## Exercise 7: Replicate a Method

**Reference workflow**

1. Pick a bounded target: one figure or one table.
2. Start with figure analysis before implementation.
3. Force progress tracking into `notes/plan.md`, `notes/todo.md`, and
   `notes/blocked.md` when needed.
4. Compare the generated result with the paper at the end.

**Expected artifacts**

- `notes/plan.md`
- `notes/todo.md`
- `figures/replication/`
- `code/replicate_[paper].py`
- `notes/replication_assessment.md`

**What to check**

- The agent does not use author code.
- The stopping rule is explicit.
- The final assessment compares paper values against reproduced values.

## Exercise 8: Mincer Warm-Up Demo

**Reference workflow**

1. Run `mincer_demo.py` once to know the target numbers and figure layout.
2. In a fresh project, paste the Level-3 prompt and let Claude produce the
   script, the table, and the figure.
3. Diff the generated table against the reference; coefficients should match
   to four decimals.

**Expected coefficients** (CPS 1976, N = 526):

| Variable       | Coef    | SE      |
|----------------|---------|---------|
| Constant       |  0.3905 | 0.1022  |
| Education      |  0.0841 | 0.0070  |
| Experience     |  0.0389 | 0.0048  |
| Experience$^2$ | -0.0007 | 0.0001  |
| Female         | -0.3372 | 0.0363  |

R$^2$ = 0.3996. The assertion `0.07 < b1 < 0.10` must fire.

**What to check**

- Table uses `booktabs` (top / mid / bottom rules). Stars at 1/5/10%.
- Figure has a serif font, no gridlines, and a visible fitted line.
- `outputs/` directory exists and holds both files.

**Common mistakes**

- Forgetting the partial-residual nature of the fitted line -- a raw line
  through the scatter will look too steep because it ignores `exper` and
  `female`.
- Using a float `exper_sq` computed from an already-squared column by accident.

## Exercise 9: Use a Specialist Subagent

**Reference workflow**

1. Write a *deliberately* naive DiD script: no FE, robust (not clustered) SE,
   no pre-trend check.
2. Run `> Use the code-reviewer subagent on code/toy_did.py` -- expect
   mostly style and correctness flags.
3. Run `> Use the econometrics-reviewer subagent on code/toy_did.py` with the
   treatment assignment specified -- expect identification and inference
   flags the generic reviewer missed.
4. Fix one issue at a time and re-audit.

**Canonical list of specialist findings**

- `REQUEST CHANGES`: clustering should be at the firm level (treatment level),
  not HC1.
- `REQUEST CHANGES`: two-way FE (firm + year) are missing; the coefficient
  currently blends level and trend variation.
- `UNSURE / REQUEST CHANGES`: staggered adoption is mentioned -- TWFE with
  heterogeneous effects is biased; recommend Callaway-Sant'Anna or
  de Chaisemartin-D'Haultfoeuille.
- `REQUEST CHANGES`: no pre-trend check or event-study plot.
- `APPROVE` after fixes: add firm + year FE, cluster at firm, report a short
  event-study figure.

**What to check**

- The specialist's review cites line numbers and quotes the offending snippet.
- The specialist flags *identification*, not just *implementation*.
- Fixing one issue at a time keeps the diff reviewable.

## Exercise 10: Install a Hook and a Real Skill

### Part A -- Audit-log and data-guard hooks

**Expected behaviour**

- After any file edit, `.claude/audit.log` gains one line with a timestamp,
  tool name, and file path.
- Any attempt to `Edit` or `Write` inside `data/raw/` is blocked with
  `"data/raw/ is read-only per CLAUDE.md"`.
- On session exit, any staged changes are auto-committed with message
  `claude: session auto-commit`.

**Common mistakes**

- `jq` not installed -- hooks silently fail. Install with `brew install jq`
  or `apt install jq`.
- Hooks configured globally (`~/.claude/settings.json`) firing on every
  project, including ones without `data/raw/`. Prefer project-local hooks.
- Forgetting to commit the hooks file so a collaborator does not inherit the
  guardrail.

### Part B -- Strategic-revision skill

**Expected `notes/revision_plan.md`**

- Each referee comment is a bullet with `[type / effort / source]` tags.
- At least one `## Block N (parallel)` section.
- A `## Conflicts flagged` section listing the engineered R1-vs-R2 clash.
- No silent paraphrasing -- every bullet contains a verbatim quote.

**What to check**

- Tasks are **discrete** (one ask per bullet), not paraphrased.
- The conflict you engineered is surfaced, not quietly reconciled.
- Dependencies are mapped (`Block 2 depends on Block 1`).

## Exercise 11: Design a Monte Carlo Study

**Reference plan (`notes/mc_plan.md`)**

- Estimand: $\beta_1$ in $y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \varepsilon$.
- DGPs: (i) homoskedastic $\varepsilon \sim N(0, 1)$;
  (ii) heteroskedastic $\varepsilon \sim N(0, (1 + x_1^2))$.
- Grid: $N \in \{200, 1000, 5000\}$; 1000 reps per cell.
- Seeds: master seed from `sha256(plan)`; per-cell seeds derived deterministically.
- Outcomes: bias, RMSE, empirical size at $\alpha = 0.05$, empirical power
  against $H_1: \beta_1 = 0.1$.
- Runtime target: < 5 min on a laptop (parallelised with `joblib`).

**Expected output**

- Baseline DGP: bias $\approx 0$, size $\approx 0.05$, power rising with $N$.
- Heteroskedastic DGP: bias $\approx 0$, **size above 0.05** (HC1 helps but
  does not fully close the gap at small $N$), power comparable to baseline.

**What to check**

- The designer **waited for approval** after writing the plan -- did not
  immediately start running simulations.
- Every random draw is reproducible from the master seed.
- The memo in `notes/mc_memo.md` names the specific cell where the estimator
  fails, not just "looks fine."

**Common mistakes**

- Running 10 000 reps because "more is better" -- wastes compute without
  changing the qualitative answer.
- Forgetting to assert that the **base** DGP has empirical size near 0.05 --
  if it doesn't, there is a bug, not a power issue.
- Reporting only bias; size and power are where estimators fail silently.

## Exercise 12: Run an Autonomous Ralph Loop

Expected behaviour: Claude solves the ridge-regression stub in 1--3
iterations.

A correct `fit_ridge` is a one-liner:

```python
def fit_ridge(X, y, lam):
    p = X.shape[1]
    return np.linalg.solve(X.T @ X + lam * np.eye(p), X.T @ y)
```

What to look for in the loop trace:
- Iteration 1 typically reads the test file, reads the stub, writes a
  draft, runs `pytest`, and either succeeds or surfaces a shape error.
- Iteration 2 (if needed) tightens shapes or fixes the regularisation
  term placement. Three iterations is rarely needed for this task.
- The completion-promise line `ALL_TESTS_PASS` should appear verbatim
  in the final iteration's output; the plugin terminates on match.
- `git log --oneline` should show 1--2 commits made inside the loop.

Common failure modes seen in classroom runs:
- Loop runs forever because the prompt didn't pin the completion-promise
  string verbatim. Fix: copy `ALL_TESTS_PASS` exactly into both the prompt
  and the `--completion-promise` flag.
- `pytest` cannot import `code.estimator` because `code/__init__.py` is
  missing. Fix: `touch code/__init__.py tests/__init__.py` before launch,
  or rely on Claude to add them on iteration 2 (it usually does).
- Cost runs above $1 because Claude was launched on Opus. For this size of
  task, switch to Sonnet (`/model sonnet`) before starting the loop.

For Exercise 12b (snarktank/ralph): expect the PRD step to produce 5--8
discrete stories. The first iteration almost always implements
"data loading + smoke test"; later iterations bolt on cluster-robust SE,
the event-study plot, and the LaTeX table. Watch `progress.txt` grow.
Treat the final state of the feature branch as a junior PR -- read the
diff, run the tests yourself, then squash-merge.

## Instructor Notes

- Exercise 0 exists so no student shows up to Exercise 1 having never typed
  `claude`. Ten minutes; do not skip.
- Exercise 1 and Exercise 2 should feel quick; do not let setup swallow the
  workshop.
- Exercise 5 is the bridge that makes Exercise 6 smoother. Students who skip
  the skill/subagent step often reinvent ad hoc workflows later.
- Exercises 8--12 are designed for self-study. In a classroom setting, pick
  one as a demo rather than running all of them.
- For Exercise 6 and Exercise 7, prefer clean artifacts and verification over
  ambitious scope.
- Exercise 12 (Ralph) is the most striking demo for a live workshop: 60--90
  seconds of preparation, then watching Claude write code, run tests, and
  commit with no further input. Plan a buffer for plugin install on a stale
  Claude Code version.
