---
name: strategic-revision
description: Parse one or more referee reports plus the editor letter into a prioritised, parallelisable revision plan with conflict flags and dependency mapping.
---

# /strategic-revision

## Description
Turn a batch of referee reports into a prioritised, parallelisable revision plan.
Inspired by Jukka Sihvonen's `strategic-revision` skill.

Given one or more referee reports plus the editor's letter, this skill parses
each comment into a discrete task, classifies it, maps dependencies between
tasks, flags conflicting requests, and groups everything into parallel
execution blocks.

## Instructions

You are a meticulous revision manager. When the user invokes
`/strategic-revision`, follow these steps exactly.

### Step 1: Collect inputs
- Expect one or more of: `referee1.md`, `referee2.md`, `editor.md` in the
  working directory. If not present, ask the user to paste the text.
- Also read `paper/main.tex` (or the closest manuscript) for section labels.

### Step 2: Parse each report into tasks
For every distinct request from a referee, extract:
- **Source:** which referee / editor comment number
- **Verbatim quote** (one or two sentences max)
- **Task type** (tag with exactly one):
  - `argumentative` — restructure a claim or add intuition
  - `empirical` — new regression, new robustness check, new data
  - `clarification` — wording, definitions, framing
  - `editorial` — typos, references, formatting
- **Target location** in the paper (section, equation, table, figure)
- **Effort estimate** (S/M/L)

### Step 3: Flag conflicts
Scan all tasks. For each pair, check whether the requests:
- ask for *opposite* things (e.g. R1 wants more theory, R2 wants less)
- point to the *same* object with different fixes
Report conflicts explicitly. Do not attempt to silently reconcile them.

### Step 4: Map dependencies
Mark task B as blocked by task A when completing A is required to do B
(e.g. "rerun regressions" blocks "update table 3").

### Step 5: Emit the revision plan
Save to `notes/revision_plan.md` with this structure:

```
# Revision Plan -- <paper title>

## Block 1 (can run in parallel)
- [ ] [empirical / M / R2-3] Rerun Table 2 with clustered SE.
      Quote: "…"
- [ ] [editorial / S / Editor-1] Fix citation style throughout.
      Quote: "…"

## Block 2 (depends on Block 1)
- [ ] [argumentative / L / R1-4] Rewrite Section 4.2 using new Table 2.
      Quote: "…"

## Conflicts flagged
- R1 #2 vs R2 #5: opposite requests on model choice. Needs editor call.

## Open questions for co-authors
- …
```

### Step 6: Do not write the response letter yet
This skill produces only the plan. The response letter is a separate step that
should be done after the empirical blocks are executed.

### Constraints
- Never modify `paper/main.tex` in this skill; only read it.
- Never paraphrase a referee comment beyond the verbatim quote plus classification.
- If a request is ambiguous, mark it `UNCLEAR` and quote the full sentence.
- Keep each task description under 30 words.

## Example usage

```
> /strategic-revision referee1.md referee2.md editor.md
```

Expected behavior: parses ~15 comments, produces 3 parallel blocks plus a
conflicts section. Execution time: ~2 minutes with Claude Sonnet.
