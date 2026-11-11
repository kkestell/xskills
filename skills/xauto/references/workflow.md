# Shared x-workflow contract

Read this contract from xplan, xwork, xreview, and xauto. Install all
four skills together. Repository instructions and explicit user constraints take
precedence; surface a conflict rather than silently changing the workflow.

## Identity and document paths

Work from the repository root. New records use **`.agents/`**, not `agents/`.
Use one immutable task ID per bounded execution assignment:
`YYYY-MM-DD-NNN-short-kebab-slug` (local date; sequence zero-padded to at least
three digits). Find the largest sequence for that date across the artifact
directories below, then use the next unused one, independent of slug. The parent
allocates IDs before dispatch; children reuse them. Standalone skills allocate
once and check for collisions before creating files. Do not overwrite an unrelated
artifact, renumber an existing task, or move legacy inputs automatically.

| Record | Repository-relative path |
| --- | --- |
| Execution plan | `.agents/plans/ID.md` |
| Work log | `.agents/work/ID.md` |
| Implementation review | `.agents/reviews/ID.md` |
| Shared design / split-unit scope map, only when needed | `.agents/designs/ID.md` |

Plans, logs and reviews share exactly the same basename. Append numbered review
rounds to the review file; preserve earlier findings and dispositions. Append to plans and logs rather than rewriting their history. Do not overwrite a review round with a later
approval. An existing input outside this layout may be read in place; write new
records here, recording its exact path. Adopt its ID only if it is unambiguous.
Use the latest applicable review and recorded finding dispositions for readiness;
do not select an older favorable verdict or leave required corrections unresolved.

For split work, assign each execution unit its own ID. A shared design lists all
units, dependencies, contracts and the mapping to the entire requested outcome.
Do not treat the shared design as a giant execution plan. Tiny work uses a brief
in the work log, not a padded plan; record why plan creation was skipped.

Use repository-relative paths in metadata, explicitly labeled as such. If using
Markdown links, calculate links relative to the containing document, not the
repository root.

### Session provenance

Distinguish the coordinator's session/worker ID from the harness's **native
conversation ID**. A worker name alone cannot locate a conversation after child
cleanup. For the parent and every stage worker, capture the role/name,
coordinator session/worker ID, harness, full native conversation ID, and actual
model/effort when exposed. Obtain IDs from current-session context or an exposed
session-metadata tool/documented harness interface; do not infer them from titles
or directories. Ask workers to return their own native IDs in their handoffs.
Claude Code exposes its native conversation ID as `CLAUDE_CODE_SESSION_ID`. In
Hypercube, a child's coordinator ID is its name, and the parent's session ID
appears in its system context.

Each artifact records its author's provenance. The parent consolidates one
stage-to-conversation table in the work log, including itself and repair workers,
**before ending children**. Persist native IDs even when the coordinator's child
records will be deleted. Do not copy full transcripts or credentials into Git.
If an interface does not expose an ID, record `unavailable` with the reason and
known harness/checkout/stage timestamps as lookup context. Do not invent an ID,
scan unrelated conversations, or add a telemetry service to fill the gap. Missing
metadata alone does not invalidate otherwise verified code.

## Records

Keep metadata readable; a Markdown field list is sufficient. No database or
additional run-manifest format is required.

Keep records focused on what the next reader needs. The plan owns the design;
the log owns changes, deviations and verification; reviews own findings and
independent assessment. Link to existing explanations rather than rewriting them
in every artifact. A no-findings review needs a verdict, a brief
justification of the tricky invariants, checks/evidence and limitations—not a
second implementation walkthrough. Expand for substantive findings or necessary
proof, not to satisfy a report-length quota. Preserve consequential constraints and unresolved finding dispositions when shortening.

**Plan:** task ID, status (`draft`, `ready`, `blocked`, or `superseded`), source
HEAD when available, author, dependencies/shared-design paths, and the request
or a faithful outcome brief. Ready means engineering decisions are settled.

**Work log:** task ID, plan path, executed plan `git hash-object -- PATH` blob
and **Guidance blobs** (paths and hashes of linked local shared designs and their
transitive execution guidance, hashed as actually read, not just link text), or
the full task brief and reason for skipping a plan; author, status
(`implemented`, `blocked`, `complete`), changed paths, deviations, exact verification commands/results,
session-provenance table, review paths and outstanding limitations. Append repair
entries rather than erasing the initial execution history. Record each check's
relevant environment. Keep evidence locatable through a log/output
reference or the native conversation and relevant tool result, without copying
entire successful command outputs into each review.

**Review round:** task ID, author, work-log path, verification evidence, numbered findings with
locations, resolution status, and verdict (`accept`, `changes-required`, or
`blocked`). State limitations; an unverified required check is not a passing one.

Task work stays uncommitted in the task checkout until xauto's single final
commit, so the change under review is the working tree against HEAD:
`git diff HEAD` plus the untracked files `git status` lists. Review all of it,
including every fix, and inspect the relevant whole files and their
callers/invariants.

Workflow records are not implementation. Exclude only their explicitly named
paths when analyzing code changes; **do not blanket-exclude `.agents/`**, which
may contain real skill source, scripts or other deliverables.

## Git ownership and the final commit

Workers never commit. xplan, xwork and xreview write files in the task checkout
and leave them uncommitted. xauto's parent makes one local commit at
completion; split work lands as that one commit with an `X-Task` trailer per
unit. Nothing authorizes pushing, rewriting history, merging into an
unrelated branch, or committing user work.

Use a clean, exclusive task checkout, so every change in it belongs to the task.
If the current checkout has unrelated changes, preserve them and use an
available isolated checkout, or ask for a safe disposition. Never
stash/reset/clean user work automatically. If pre-existing edits overlap the
task or are its intended starting state, establish their disposition before
isolating; a clean HEAD checkout must not silently omit required user work.

The normal xauto sequence, all in the one task checkout:

1. The planner writes the plan or shared design.
2. xwork implements, verifies and writes the work log.
3. The independent reviewer reviews the whole change and appends a review
   round. Route fixes to the implementer and repeat steps 2–3.
4. The parent verifies the final state and marks the log `complete`.
5. The parent stages the task's named paths (code, tests and records), inspects
   the staged diff, and makes **one commit**. Its subject describes the change,
   its body summarizes it, and it ends with an `X-Task: ID` trailer. Do not use
   `git add .`, `git add -A`, or `git commit -a`. Return the commit ID in chat;
   no record needs to contain it.

Tiny work skips step 1; preserve its brief in the log. Standalone xwork stops
after step 2 at `implemented`; standalone xreview stops after writing its round.
Both leave their changes uncommitted for the user. Record a blocked execution
honestly; do not label it complete to satisfy the cycle.

### Verification ownership and reuse

xwork owns completion of required plan/repository checks. Independent review
means independent inspection and judgment, not automatic repetition of every
command. The reviewer first inspects the existing evidence and confirms its
relevant environment, scope and result. Reuse matching, inspectable
results unless repository/user instructions require a fresh review run or a
concrete uncertainty needs another check. A pass claim without usable evidence
is not enough. Mark results as `run` or `reused`, naming their source and why any
new run adds evidence. Do not silently drop required coverage to save time.

For new verification, choose the narrowest check that answers the open question.
A focused regression or a full package/suite run may be appropriate; running
both, repeating race tests, or rerunning the full build needs distinct coverage
or a stated reason, not merely a new worker or workflow stage. The parent passes
existing evidence forward and does not trigger another check round just to
finalize records.

Checks apply to the working tree as it stood when they ran. If any code,
config or test file changes after a check, rerun the affected check.
Record-only changes do not invalidate matching code-check results. Once the
final review is accepted, commit before anything else touches the checkout. In
split work, each unit's review covers the whole working-tree change; a change to
an earlier unit's code after its acceptance needs renewed verification and
review, and broken earlier contracts send the affected plan back for revision.
Completion means the accepted review matches the final code and that code is
committed, not merely that `git status` looks clean.

## Stage workers

Run every stage worker in the task checkout, one at a time. Give each worker its
exact directory, stage, task ID, input/output paths and allowed
edits. Confirm its actual checkout before using its results; tool
defaults may create a different worktree. A worker must not stage, commit, stash
or reset anything.

### Hypercube

Children cannot create children, so xauto runs in a top-level session. Start it
in a top-level worktree session; that worktree and its branch are the task
checkout. Create stage workers as fresh children with `dir: "."` so they share
it. Reuse them through messages for later rounds; parked sessions resume their
conversation. Completion reports carry only the first 400 characters of a
child's final response; read artifacts and Git, or `read_session`, for the
rest. xauto leaves the task branch unmerged; the user merges it into the
original checkout.
