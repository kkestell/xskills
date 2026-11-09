---
name: xwork
description: Implement a decision-complete plan with xwork PLAN, or an explicitly supplied bounded task brief, verify the change, write a linked .agents/work log, and commit task-owned code and the log locally. Use only when the user invokes xwork or explicitly requests this workflow, including delegation by xauto.
---

# Execute a bounded assignment

Read `../xauto/references/workflow.md` for shared IDs, `.agents/` paths, Git
ownership, revision anchors and commit order. Install the four x-skills together.
This skill implements, verifies, logs and commits; it does not silently redesign
the assignment or claim an independent review of its own work.

## Establish the handoff

- Resolve the supplied filename exactly. A bare filename may be resolved in
  `.agents/plans/`; do not pick the newest plan. If ambiguous, ask.
- Read repository instructions, the request, full plan, linked shared design and
  dependencies. Reuse the assigned task ID. Check the parent's execution decision
  (or an unchanged accepted normalization assessment) against the current plan
  blob and all linked **Guidance blobs**. If they differ, return the changed inputs
  to the parent for an impact/correction check before xauto execution. A changed
  blob alone is not a reason to commission another independent review.
- Standalone xwork may execute a ready user-supplied plan without a separate
  review; state that review was not supplied. Do not execute a blocked plan or
  invent answers to its consequential open decisions.
- For an explicit brief (`xwork --brief <task brief>` or the parent's equivalent
  delegation), preserve the full outcome, constraints, checks and skip-planning
  reason in the work log. Do not create a ceremonial plan. If inspection reveals
  substantial design work, return it for planning instead of hiding it here.
- Confirm the task checkout and Git status before editing. Git is required for
  this committing workflow; do not initialize a repository silently. Follow the
  shared contract for unrelated files or index entries.
- Record the full starting HEAD as **Code base** before the first implementation
  change. During a repair, read the existing log and retain its original base.

## Implement and verify

1. Inspect the actual implementation and tests; do not trust the plan's paths or
   API assumptions blindly. Follow the chosen responsibilities, contracts,
   algorithms, ordering and scope. Keep the touched whole files easy to follow;
   remove unnecessary machinery rather than layering around confusing code.
2. Resolve routine coding details locally. If evidence invalidates a consequential
   decision, stop that affected work and return the concrete evidence and required
   decision to the planner/parent. Do not choose a materially different design
   and conceal it as an implementation detail. The parent must check the amended
   guidance and record its execution decision before resuming under xauto;
   additional normalization assessment follows the shared contract's size/detail
   rule, not a design-certification gate. Record deviations and why they were
   necessary.
3. Add meaningful tests for required behavior and regressions. Confirm that test
   scenarios are supported by actual syntax, scope/lifetime rules and test APIs;
   an impossible or unspecified-behavior oracle proves nothing.
4. Run the plan's required checks and applicable repository checks against the
   final changes. Run builds/tests for code where required; for documentation-only
   changes inspect the documents unless instructions require more. Record exact
   commands, outcomes and relevant environment limitations. A missing dependency,
   failed check or skipped check is not a pass. Ask the parent/user for necessary
   decisions rather than silently reducing required verification.
5. Inspect the complete task diff, including new/untracked deliverables. Check
   scope, code clarity and accidental generated changes. Do not claim tests ran
   just because they appear in the plan.

## Commit code, then record its known revision

Stage only task-owned implementation/tests and necessary non-workflow docs.
Inspect the index and commit with `X-Task` and `X-Stage: work` (or `fix` for a
review repair). Capture the actual full commit ID **after** commit hooks as Code
head. If hooks change code, inspect/reverify it before treating that head as
verified. Do not make an empty code commit for an evidence-backed no-op; record
that there was no implementation change and use the current HEAD.

Write `.agents/work/ID.md` using the fields in the shared contract. Explain what
changed concisely through changed responsibilities/paths and deviations; link to
the plan instead of repeating its design. List the actual implementation
commit(s), preserve the original Code base, record the latest Code head and
checks, and set status `implemented`. Include your native conversation ID and
other available session provenance. Keep verification evidence inspectable at its
tested revision so the reviewer can reuse them; do not merely say “tests pass”.
On repair append findings addressed and verification; do
not erase earlier failed checks or replace the base with the last fix's parent.
Commit the log separately with `X-Stage: work-log`. The log points backward to
known code hashes; it never predicts its own commit hash.

If required checks fail, record status `blocked` and the failure; do not present
a successful handoff. Partial work may be checkpointed in task-owned commits
clearly labeled incomplete, but the parent must stop the success path. Never
push, force, amend unrelated commits or discard user changes.

Return task ID, exact plan/brief and log paths, Code base/head, code/log commit
IDs, verification results, deviations, session provenance and blockers before
the parent ends the worker. Await independent
`xreview work <work log filename>`; do not mark the task `complete` yourself.
