# Shared x-workflow contract

Read this contract from xplan, xwork, either xreview mode, and xauto. Install all
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
| Plan review | `.agents/reviews/plans/ID.md` |
| Implementation review | `.agents/reviews/work/ID.md` |
| Shared design / split-unit scope map, only when needed | `.agents/designs/ID.md` |

Plans and logs share exactly the same basename. Review mode is in the directory,
not a new task number. Append numbered review rounds to the appropriate review
file; preserve earlier findings, reviewed revisions and dispositions. Git commits
preserve changes to plans and logs. Do not overwrite a review round with a later
approval. An existing input outside this layout may be read in place; write new
records here, recording its exact path. Adopt its ID only if it is unambiguous.
Use the latest applicable review and recorded finding dispositions for its mode;
do not select an older favorable verdict or leave required corrections unresolved.
Plan acceptance addresses normalization only, not engineering readiness.

For split work, assign each execution unit its own ID. A shared design lists all
units, dependencies, contracts and the mapping to the entire requested outcome.
Do not treat the shared design as a giant execution plan. Tiny work uses a brief
in the work log, not a padded plan; record why plan creation/review was skipped.

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

Each artifact records its author's provenance. The parent consolidates one
stage-to-conversation table in the work log, including itself and repair workers,
**before ending children**. Persist native IDs even when the coordinator's child
records will be deleted. Do not copy full transcripts or credentials into Git.
If an interface does not expose an ID, record `unavailable` with the reason and
known harness/checkout/stage timestamps as lookup context. Do not invent an ID,
scan unrelated conversations, or add a telemetry service to fill the gap. Missing
metadata alone does not invalidate otherwise verified code.

## Records and revision anchors

Keep metadata readable; a Markdown field list is sufficient. No database or
additional run-manifest format is required.

Keep records focused on what the next reader needs. The plan owns the design;
the log owns changes, deviations and verification; reviews own findings and
independent assessment. Link to existing explanations rather than rewriting them
in every artifact. A no-findings plan assessment needs both axes, actions, concise
supplied-material evidence, metric/target sources, exact anchors and limitations.
A no-findings work review needs a verdict, exact anchors, a brief justification
of the tricky invariants, checks/evidence and limitations—not a second
implementation walkthrough. Expand for substantive findings or necessary
proof, not to satisfy a report-length quota. Preserve all revision anchors,
consequential constraints and unresolved finding dispositions when shortening.

**Plan:** task ID, status (`draft`, `ready`, `blocked`, or `superseded`), source
HEAD when available, author, dependencies/shared-design paths, and the request
or a faithful outcome brief. Ready means engineering decisions are settled, not
that an independent review has already accepted it.

**Work log:** task ID, plan path, accepted plan and linked-guidance blobs/review
path (or the full task brief and reason for skipping a plan), author, status
(`implemented`, `blocked`, `complete`), fixed **Code base**, latest **Code head**, implementation
commit list, changed paths, deviations, exact verification commands/results,
session-provenance table, review paths and outstanding limitations. Append repair
entries rather than erasing the initial execution history. Record each check's
target revision and relevant environment; one shared Code head is sufficient
when all results apply to it. Keep evidence locatable through a log/output
reference or the native conversation and relevant tool result, without copying
entire successful command outputs into each review.

**Plan review round:** task ID, mode `plan`, author, exact plan path and
`git hash-object -- PATH` blob, supplied request/shared-guidance input identities,
**Guidance blobs** (paths and hashes of supplied local shared designs and their
transitive execution guidance), source HEAD, metric/target sources, both axes,
actions, evidence and
limitations. Input loading, hashing, metrics and record saving are outside the
single-prompt assessment. Hash the actual inputs supplied, not just link text;
record unsupplied references as limitations, not as proven omissions. Do not
investigate source, contracts, invariants or test feasibility in plan assessment.
Its `accept` is normalization only, not a correctness/readiness verdict.
After corrections, the parent appends an **Execution decision**: author, finding
dispositions and evidence, final plan and Guidance blobs, and `proceed` or
`blocked`. Preserve the independent review's original verdict and anchors. The
parent verifies corrections; do not imply independent approval of unseen edits.
Before execution, compare the plan and guidance set with this decision (or an
unchanged accepted review). Changed guidance needs an impact/correction check,
not automatic independent re-review. Further normalization assessment is warranted
only for a named size/detail question the existing assessment and parent check
cannot settle. Engineering questions remain with planning/implementation and
work review, not a general plan-correctness gate. The planner still owns the
ready status; the parent must not infer it from normalization acceptance.

**Work review round:** task ID, mode `work`, author, work-log path, fixed Code
base and reviewed Code head, verification evidence, numbered findings with
locations, resolution status, and verdict (`accept`, `changes-required`, or
`blocked`). State limitations; an unverified required check is not a passing one.

Use full Git object IDs in records, copied from Git rather than retyped from a
worker's prose. Verify recorded commit IDs with Git before using them as anchors.
A Code head is a commit, not a branch name or “latest”. The Code base is the
task checkout's HEAD immediately before the
first implementation commit; **never advance it to the last fix**. Review the
entire `Code base..Code head` change, including all fixes, not merely HEAD's diff.
Also inspect the relevant whole files and their callers/invariants.

Workflow records are not implementation. Exclude only their explicitly named
paths when analyzing code changes; **do not blanket-exclude `.agents/`**, which
may contain real skill source, scripts or other deliverables.

## Git ownership and commit order

xwork authorizes local task commits. xauto authorizes the parent and its assigned
workers to make the local commits described here. Neither authorizes pushing,
rewriting history, merging into an unrelated branch, or committing user work.
xplan and xreview alone write their records but do not commit by default.

Use a clean, exclusive task checkout. If the current checkout has unrelated
changes, preserve them and use an available isolated checkout, or ask for a safe
disposition. Never stash/reset/clean user work automatically.
If pre-existing edits overlap the task or are its intended starting state,
establish their disposition before isolating; a clean HEAD checkout must not
silently omit required user work. Recheck the index before every commit; if it
contains foreign entries, stop rather than including
or unstaging them. Stage named task-owned paths, inspect the staged diff, then
commit. Do not use blanket `git add .`, `git add -A`, or `git commit -a`.

The normal xauto sequence is:

1. Parent commits the drafted plan/shared design (`plan`).
2. Reviewer writes a plan-review round. Parent commits it (`plan-review`). If
    corrections are needed, planner revises and parent commits a new `plan`
    revision. Parent verifies the corrections and records/commits its execution
    decision (`plan-review`); no automatic review loop. No implementation with
    unresolved normalization corrections, a blocked plan or mismatched
    plan/guidance anchors. Normalization is not engineering certification.
3. xwork implements and verifies, then commits **code/tests** (`work`, or `fix`
   for a review repair). Save the resulting full commit ID as Code head.
4. xwork writes/updates the work log with that known Code head and commits the
   **log separately** (`work-log`). This avoids a self-referential commit hash.
5. Independent reviewer reviews the recorded complete range. Parent commits the
   review round (`work-review`). Route fixes to the implementer, then repeat
   steps 3–5 with the original Code base and new Code head.
6. Parent verifies the final state, marks the log `complete`, adds final review
   references, and commits remaining **records only** (`complete`). No document
   needs to contain the hash of its own commit; return final hashes in chat.

Tiny work skips steps 1–2; preserve its brief in the log. Standalone xwork follows
steps 3–4 and stops at `implemented`, awaiting review. Standalone xreview writes
the review but leaves committing/fixing to the caller. Record a blocked execution
and any partial commits honestly; do not label it complete to satisfy the cycle.

Commit subjects should describe the change. Add stable trailers for analysis:

```text
X-Task: YYYY-MM-DD-NNN-short-slug
X-Stage: plan|plan-review|work|fix|work-log|work-review|complete
```

Use the one actual stage value, not the pipe-separated alternatives. A shared
design commit may name multiple `X-Task` trailers for its units. Do not squash
away these stage boundaries merely for tidiness.

### Verification ownership and reuse (implementation and work review)

xwork owns completion of required plan/repository checks. Independent review
means independent inspection and judgment, not automatic repetition of every
command. The reviewer first inspects the existing evidence and confirms its
revision, relevant environment, scope and result. Reuse matching, inspectable
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

Checks must apply to the code actually committed. If hooks or integration change
code after verification, inspect and rerun affected checks. Record-only commits
do not invalidate matching code-check results. After review, inspect
the entire diff/history from reviewed Code head to the current checkout, including
untracked files. Only known workflow-record changes may remain unreviewed. In a
split cycle, later units may add code after an earlier unit's reviewed head:
account for those changes through the later units' accepted review ranges on
the integrated task checkout. They do not invalidate the earlier review merely
by existing. Any code/config/test change not covered by such an accepted later
range, including integration repairs, needs verification and renewed work review.
If later work invalidates an earlier contract, revisit the affected plan/review
as well; accepted unit reviews are not a waiver for broken integration.
Completion means all **task-owned** changes and records are committed and the
accepted review matches the final code, not merely that `git status` looks clean.

## Child checkout handoffs

Prefer one parent-selected task checkout and serial stage workers. Give each
child its exact directory, stage, task ID, input/output paths, starting HEAD,
allowed edits and commit authority. Confirm its actual checkout/HEAD before
using its results; tool defaults may create a different worktree.

If a child is isolated, it must make an authorized handoff commit containing its
stage outputs, including plan/review records otherwise committed by the parent.
Transfer those commits to the task checkout before starting the next stage or
ending a child whose worktree/branch will be deleted. Preserve stage trailers.
Record original worker commits and their integrated equivalents in the log when
hashes change; anchor Code base/head and reviews in the **task checkout**, not
an ephemeral worker branch. A review of a different tree is not final approval.
Resolve integration conflicts through the assigned author and reverify/review
affected code. Keep a reachable committed result before any cleanup.
