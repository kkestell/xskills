---
name: xauto
description: Orchestrate xplan, xwork, and xreview in child sessions (or subagents when child sessions are unavailable), resolve findings, and finish with all task-owned code and .agents records committed locally. Use only when the user invokes xauto or explicitly requests this autonomous workflow. Do not invoke kauto or push changes.
---

# Orchestrate the complete x-workflow

The current session is the parent coordinator. Read
`references/workflow.md` before dispatching. Read the other three skills as
needed; their stage semantics and the shared contract apply to every worker.
Do not run an unrelated kauto workflow because of a name typo in a request.

## Prepare and allocate

1. Establish the requested outcome, constraints and scope. Find the Git root,
   current branch/HEAD, applicable instructions and dirty/index state. Git is
   required; stop rather than silently initialize it. Choose one clean exclusive
   task checkout. Preserve unrelated work; isolate when possible, otherwise ask
   for the needed disposition. When the host lets only the coordinator delegate
   and gives it no way to move itself into an isolated checkout (as in
   Hypercube), isolation means starting the coordinator there: if the current
   checkout has unrelated changes, ask the user to restart xauto in a
   top-level worktree session. Do not promise a commit on the user's original
   branch when working on a separate branch.
2. Allocate the task ID and canonical artifact paths. A planner may propose
   multiple bounded units plus shared design; the parent assigns additional IDs
   centrally and preserves coverage of the complete request.
3. Discover the available delegation tools. Use **child sessions first**; only
   when unavailable use subagents. Follow the host's delegation/lifecycle rules.
   Do not assume a tool name or fake fresh context with another message in the
   parent. If neither mechanism exists, stop and explain that the independent
   orchestrated workflow is unavailable; do not silently run every role inline.
4. Inherit model/harness/effort unless the user or applicable instructions select
   them. Use fresh reviewer context, never a fork containing the author's
   private reasoning. The reviewer may see the request, code, artifacts and
   prior public findings, but is not the worker that wrote the reviewed
   implementation. Start the planner and implementer fresh as well; fork the
   planner only when the requirements were settled in the parent's own
   conversation and a brief cannot carry them.
5. Capture the parent's session provenance using the shared contract. Request
   each worker's coordinator ID and native conversation ID in its handoff;
   preserve them in the work log before cleanup, not just transient worker names.

## Dispatch explicit stage briefs

Each worker gets the objective, relevant user constraints, skill and invocation,
task ID, exact checkout and starting HEAD, inputs/output paths, allowed edits,
commit authority, check requirements and existing verification evidence, expected
handoff (including session provenance) and stopping condition.
Include where the result will be used. Supply a plan or request, not assumptions
the worker is supposed to independently verify. Ask each worker to begin its
final response with a one-line handoff (task ID, stage, artifact path, commit
IDs, verdict), because some hosts deliver only the start of a child's reply.

Run stage workers in the task checkout itself, one at a time, so their commits
land directly on the task branch. Reuse the same implementer for fix rounds and
the same reviewer for re-review rounds. Give a worker its own isolated checkout
only for separate units whose files and dependencies are truly independent,
with explicit integration/review ownership. Confirm each child's actual
directory/HEAD; integrate isolated-worker handoff commits before the next stage,
as described in the shared contract. Never delete an untransferred result.

## Plan

- Start a planner with `xplan <request>` and no production-code edit authority.
  The planner researches tricky questions, settles engineering decisions and
  returns ready plans, a tiny-task brief, or concrete blockers.
- Inspect the returned artifacts and coverage of the request. If a plan is
  blocked or leaves the request uncovered, return a concrete correction to the
  planner. Commit plan/shared-design records as `plan`.
- For truly tiny work, retain the planner's bounded brief for xwork and skip the
  separate plan artifact; the later work log records the reason. Do not bypass
  normalization by calling a large unresolved assignment a brief.
- A split request is not finished after its first unit. Track unit dependencies
  in the shared design, execute every requested unit in order, and recheck shared
  interfaces/intermediate states when a dependency changes.

## Work → review the implementation

- Dispatch an implementer with **`xwork .agents/plans/ID.md`**, or the explicit
  tiny-task brief. Authorize only task-owned code and log commits. xwork records a fixed Code base, commits verified code,
  then separately commits its log with a known Code head.
- Check the handoff against Git and the recorded test output; a child's “done”
  message is not evidence of the right tree, completed checks or committed files.
  Resolve integration mappings and use task-checkout hashes in the final log.
- Start an independent reviewer with **`xreview .agents/work/ID.md`**. Give
  the request, plan/brief, complete Code base..Code head range, work log and
  relevant repository instructions. The reviewer reads code and tests, not just
  the log, and writes a review without fixing the implementation. Commit its
  review as `review`.
- Pass through inspectable check results for the recorded Code head. Ask the
  reviewer to inspect/reuse that evidence first and identify any remaining
  uncertainty before selecting fresh checks. Do not routinely request focused
  repetitions, a full package run and the repository suite again for the same
  unchanged code. Explicit fresh-run requirements still apply.
- Send actionable findings to the implementer. It commits fixes and an appended
  log entry, retaining the original base. Return the complete updated change to
  the independent reviewer; prior findings need resolution evidence, not a fresh
  empty checklist. Preserve all review rounds. The reviewer can be reused while
  independent of the author; no role may approve code it just wrote.
- If implementation exposes an invalid design, route the decision back through
  the planner and parent before continuing, and recheck affected dependent units.
  Do not let xwork silently expand scope or leave the hard choice until coding.

## Resolve findings and finish honestly

Proceed without routine confirmation, but ask when intent, scope, permissions or
a material tradeoff genuinely requires the user. Stop on unavailable required
tools/checks or disputed decisions. Continue ordinary repairs while they make
progress; if a round repeats the same failed approach, needs a user decision or
exceeds an explicit budget, stop and report the unresolved evidence rather than
spawning an indefinite review loop. Never accept a defect to finish the cycle.

Before success, the parent verifies:

1. Every requested execution unit is implemented, required checks actually passed,
   and its final code has an independent accepted review.
2. Every code/test/config change after a unit's reviewed Code head is covered by
   a later unit's accepted review range on the integrated task checkout, or goes
   back through verification and review. Known workflow-record-only changes
   need no code re-review. Account for all commits/diffs, not just matching path
   names. Integration conflict fixes and broken earlier contracts require renewed
   checks/review; a later accepted unit does not automatically excuse them.
3. Work logs contain the executed plan/brief, fixed base, final reviewed head,
   actual commits, parent/worker native conversation IDs (or explicit unavailable
   reasons), run/reused verification evidence and review paths. Set them `complete`
   and commit remaining task-owned records as `complete`.
4. All task-owned changes and new records are committed on the reported branch.
   Verify with Git, preserve unrelated work, and do not push or automatically
   merge into a different branch. Original code heads need not equal final HEAD
   because later commits contain records or other independently accepted units.
5. Save each child's session provenance and integrate/save every result before
   ending sessions that remove their branches/worktrees. Leave a reachable
   committed result and follow the host's cleanup rules. Failed cycles report
   partial commits and blockers, not success.

Return a concise outcome, task IDs, artifact paths, branch and final commit IDs,
checks, review verdicts and any remaining limitations. The parent owns this
verification and final report; do not merely concatenate worker summaries.
