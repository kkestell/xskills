# Shared x-workflow contract

Read by xplan, xwork, xreview and xtask. Install all four skills together.
Repository instructions and explicit user constraints take precedence.

## IDs and records

Work from the repository root. Each execution unit has one task ID,
`YYYY-MM-DD-NNN-short-kebab-slug` (local date; sequence zero-padded to three
digits): the next sequence for that date across the directories below. The
planner assigns IDs in execution order when it writes the plans. IDs never
change afterwards.

| Record | Path |
| --- | --- |
| Plan or brief | `.agents/plans/ID.md` |
| Work log | `.agents/work/ID.md` |
| Review | `.agents/reviews/ID.md` |

The three records share the basename. Each skill writes its record from its
`templates/` directory and keeps it short: the plan owns the design, the log
owns changes, deviations and check results, the review owns findings. Link
instead of repeating. Correct a record with edits, not whole-file rewrites.
Reviews append numbered rounds.

Tiny work uses a brief: a plan file with kind `brief`. For split work, each
unit has its own plan; a decision several units share lives in the plan of the
first unit that implements it, and later plans name it as a dependency.

## Checks

xwork runs the required checks and records each command and result. The
reviewer reuses those results and runs a check only to answer a specific open
question. If code, config or tests change after a check, rerun the affected
check. A skipped or failed check is not a pass.

## Git

Workers never stage, commit, stash or reset. Each unit's work stays uncommitted
in the task checkout until its review is accepted; the change under review is
`git diff HEAD` plus untracked files from `git status`. Workflow records are
excluded from code review only by their exact paths, since `.agents/` can hold
real deliverables.

xtask commits each accepted unit before the next starts: stage the unit's code,
tests, plan, work log and review by name (never `git add .`, `-A` or
`commit -a`), inspect the staged diff, and make one commit whose subject
describes the change, whose body summarizes it, and which ends with an
`X-Task: ID` trailer. Never push, rewrite history or merge.

Use a clean checkout so every change in it belongs to the task. Preserve
unrelated work; never stash, reset or clean it.

## Stage workers

Run stage workers one at a time in the task checkout. Give each its directory,
task ID, input and output paths and allowed edits. Confirm its actual checkout
before using its results.

### Hypercube

Children cannot create children, so xtask runs in a top-level worktree
session; that worktree and its branch are the task checkout. Create workers as
fresh children with `dir: "."` and reuse them by message for later rounds.
Completion reports carry only the first 400 characters of a child's reply;
read the artifacts or `read_session` for the rest. The user merges the task
branch.
