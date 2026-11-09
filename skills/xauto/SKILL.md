---
name: xauto
description: Orchestrate xplan, xreview plan, xwork, and xreview work in child sessions (or subagents when child sessions are unavailable), resolve findings, and finish with all task-owned code and .agents records committed locally. Use only when the user invokes xauto or explicitly requests this autonomous workflow. Do not invoke kauto or push changes.
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
   for the needed disposition. Do not promise a commit on the user's original
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
   them. Use fresh reviewer context, not a fork containing the author's private
   reasoning. A plan assessor receives only the prepared plan/request/shared
   guidance and metrics; a work reviewer may inspect code and prior public findings.
   Neither is the worker that wrote the reviewed plan/implementation.
5. Capture the parent's session provenance using the shared contract. Request
   each worker's coordinator ID and native conversation ID in its handoff;
   preserve them in the work log before cleanup, not just transient worker names.

## Dispatch explicit stage briefs

Each worker gets the objective, relevant user constraints, skill and invocation,
task ID, exact checkout and starting HEAD, inputs/output paths, allowed edits,
commit authority, check requirements and existing verification evidence, expected
handoff (including session provenance) and stopping condition.
Include where the result will be used. Supply a plan or request, not assumptions
the worker is supposed to independently verify.

Stages are sequential in a shared checkout. Default to one writer at a time;
run separate units concurrently only when their files and dependencies are truly
independent and integration/review ownership is explicit. Confirm each child's
actual directory/HEAD; integrate isolated-worker handoff commits before the next
stage, as described in the shared contract. Never delete an untransferred result.

## Plan → normalize the plan

- Start a planner with `xplan <request>` and no production-code edit authority.
  The planner researches tricky questions, settles engineering decisions and
  returns ready plans, a tiny-task brief, or concrete blockers.
- Inspect the returned artifacts and coverage. Commit plan/shared-design records
  as `plan`, then send each execution plan to an independent worker using
  **`xreview plan .agents/plans/ID.md`**. Supply the request/shared guidance,
  including linked shared designs' transitive execution guidance, and precomputed
  metrics, with exact input anchors. Keep file loading, measurement and report
  saving outside the one-pass, tool-free assessment described by
  xreview. Do not ask this assessor to inspect repositories, validate design or
  test feasibility, or certify readiness. The skill harness cannot enforce a
  single isolated model call; disclose that limitation. Commit its normalization
  round as `plan-review`.
- For findings, return a concrete correction assignment to the planner. Commit
  the revised plan. The parent checks the corrections against the findings and
  relevant evidence, records their disposition and the final plan/guidance blobs,
  and proceeds when supported normalization corrections are resolved and the
  planner has supplied a ready plan. Normalization `accept` alone does not
  establish engineering correctness or readiness. This is the parent's
  execution decision, not a claim that the reviewer approved unseen revisions.
  Do not send every revision through another full plan review. Additional
  normalization assessment needs a specific size/detail question that the prior
  assessment and correction check cannot settle; name it and request only that
  assessment. Engineering questions go to the planner, not this check.
  Wording, metadata and routine corrections do not justify restarting review.
  Shared-design edits require checking affected units, not automatically
  commissioning another review of each one.
- For truly tiny work, retain the planner's bounded brief for xwork and skip the
  separate plan/review artifacts; the later work log records the reason. Do not
  bypass normalization by calling a large unresolved assignment a brief.
- A split request is not finished after its first unit. Track unit dependencies
  in the shared design, execute every requested unit in order, and recheck shared
  interfaces/intermediate states when a dependency changes.

## Work → review the implementation

- Dispatch an implementer with **`xwork .agents/plans/ID.md`**, or the explicit
  tiny-task brief. Supply the normalized plan, execution decision (or unchanged
  normalization acceptance), and linked-guidance blobs. Acceptance is not proof
  that the implementation design has been independently validated.
  Authorize only task-owned code and log commits. xwork records a fixed Code base,
  commits verified code, then separately commits its log with a known Code head.
- Check the handoff against Git and the recorded test output; a child's “done”
  message is not evidence of the right tree, completed checks or committed files.
  Resolve integration mappings and use task-checkout hashes in the final log.
- Start an independent reviewer with **`xreview work .agents/work/ID.md`**. Give
  the request, plan/brief, complete Code base..Code head range, work log and
  relevant repository instructions. The reviewer reads code and tests, not just
  the log, and writes a review without fixing the implementation. Commit its
  review as `work-review`.
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
  the planner and parent before continuing. Apply the same correction check to
  affected dependent units; additional normalization assessment needs a named
  size/detail uncertainty, not merely a changed plan blob. Design validation
  remains with planning/implementation and the independent work review.
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
   and its final code has an independent accepted work review.
2. Every code/test/config change after a unit's reviewed Code head is covered by
   a later unit's accepted review range on the integrated task checkout, or goes
   back through verification and work review. Known workflow-record-only changes
   need no code re-review. Account for all commits/diffs, not just matching path
   names. Integration conflict fixes and broken earlier contracts require renewed
   checks/review; a later accepted unit does not automatically excuse them.
3. Work logs contain the accepted plan/brief, fixed base, final reviewed head,
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
