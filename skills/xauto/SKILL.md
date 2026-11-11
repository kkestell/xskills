---
name: xauto
description: Orchestrate xplan, xwork, and xreview in child sessions (or subagents when child sessions are unavailable), resolve findings, and finish with the task's code and .agents records in one local commit. Use only when the user invokes xauto or explicitly requests this autonomous workflow. Do not invoke kauto or push changes.
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
task ID, exact checkout, inputs/output paths,
allowed edits, check requirements and existing verification evidence, expected
handoff (including session provenance) and stopping condition.
Include where the result will be used. Supply a plan or request, not assumptions
the worker is supposed to independently verify. Ask each worker to begin its
final response with a one-line handoff (task ID, stage, artifact path,
verdict), because some hosts deliver only the start of a child's reply.

Run stage workers in the task checkout itself, one at a time. Workers never
stage or commit; their files stay uncommitted until the final commit. Reuse the
same implementer for fix rounds and the same reviewer for re-review rounds.
Confirm each child's actual directory before using its results.

## Plan

- Start a planner with `xplan <request>` and no production-code edit authority.
  The planner researches tricky questions, settles engineering decisions and
  returns ready plans, a tiny-task brief, or concrete blockers.
- Inspect the returned artifacts and coverage of the request. If a plan is
  blocked or leaves the request uncovered, return a concrete correction to the
  planner.
- For truly tiny work, retain the planner's bounded brief for xwork and skip the
  separate plan artifact; the later work log records the reason. Do not bypass
  normalization by calling a large unresolved assignment a brief.
- A split request is not finished after its first unit. Track unit dependencies
  in the shared design, execute every requested unit in order, and recheck shared
  interfaces/intermediate states when a dependency changes.

## Work → review the implementation

- Dispatch an implementer with **`xwork .agents/plans/ID.md`**, or the explicit
  tiny-task brief. xwork implements, verifies and writes its log.
- Check the handoff against Git and the recorded test output; a child's “done”
  message is not evidence of the right tree or completed checks.
- Start an independent reviewer with **`xreview .agents/work/ID.md`**. Give
  the request, plan/brief, work log and
  relevant repository instructions. The reviewer reads code and tests, not just
  the log, and appends a review round without fixing the implementation.
- Pass through inspectable check results from the work log. Ask the
  reviewer to inspect/reuse that evidence first and identify any remaining
  uncertainty before selecting fresh checks. Do not routinely request focused
  repetitions, a full package run and the repository suite again for the same
  unchanged code. Explicit fresh-run requirements still apply.
- Send actionable findings to the implementer. It fixes them and appends a log
  entry. Return the complete updated change to
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
2. No code, config or test file changed after the final accepted review.
3. Work logs contain the executed plan/brief, parent/worker native conversation
   IDs (or explicit unavailable reasons), run/reused verification evidence and
   review paths. Set them `complete`.
4. Make the single final commit as the shared contract describes. Verify with
   Git, preserve unrelated work, and do not push or automatically merge into a
   different branch.
5. Save each child's session provenance before ending sessions, and follow the
   host's cleanup rules. Failed cycles leave their work uncommitted and report
   it with the blockers, not success.

Return a concise outcome, task IDs, artifact paths, branch and final commit ID,
checks, review verdicts and any remaining limitations. The parent owns this
verification and final report; do not merely concatenate worker summaries.
