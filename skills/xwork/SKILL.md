---
name: xwork
description: Implement a decision-complete plan with xwork PLAN, or an explicitly supplied bounded task brief, verify the change, and write a linked .agents/work log, leaving everything uncommitted. Use only when the user invokes xwork or explicitly requests this workflow, including delegation by xauto.
---

# Execute a bounded assignment

Read `../xauto/references/workflow.md` for shared IDs, `.agents/` paths, Git
ownership and the work log's fields. Install the four x-skills together.
This skill implements, verifies and logs; it does not silently redesign
the assignment or claim an independent review of its own work.

## Establish the handoff

- Resolve the supplied filename exactly. A bare filename may be resolved in
  `.agents/plans/`; do not pick the newest plan. If ambiguous, ask.
- Read repository instructions, the request, full plan, linked shared design and
  dependencies. Reuse the assigned task ID. Record the plan blob and all linked
  **Guidance blobs** as read. Do not execute a blocked plan or invent answers to
  its consequential open decisions.
- For an explicit brief (`xwork --brief <task brief>` or the parent's equivalent
  delegation), preserve the full outcome, constraints, checks and skip-planning
  reason in the work log. Do not create a ceremonial plan. If inspection reveals
  substantial design work, return it for planning instead of hiding it here.
- Confirm the task checkout and Git status before editing. Git is required; do
  not initialize a repository silently. Follow the
  shared contract for unrelated files or index entries.

## Implement and verify

1. Inspect the actual implementation and tests; do not trust the plan's paths or
   API assumptions blindly. Follow the chosen responsibilities, contracts,
   algorithms, ordering and scope. Keep the touched whole files easy to follow;
   remove unnecessary machinery rather than layering around confusing code.
2. Resolve routine coding details locally. If evidence invalidates a consequential
   decision, stop that affected work and return the concrete evidence and required
   decision to the planner/parent. Do not choose a materially different design
   and conceal it as an implementation detail. Under xauto, resume only after the
   parent supplies amended guidance. Record deviations and why they were necessary.
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

## Write the work log

Do not stage, commit, stash or reset anything; the work stays uncommitted for
xauto's final commit or for the user. If anything changes after the checks
ran, rerun the affected checks.

Write `.agents/work/ID.md` from `templates/work-log.md`, using the fields in
the shared contract. Explain what
changed concisely through changed responsibilities/paths and deviations; link to
the plan instead of repeating its design. Record the checks and set status `implemented`. Include your
native conversation ID and other available session provenance. Keep verification
evidence inspectable so the reviewer can reuse it; do not
merely say “tests pass”. On repair append findings addressed, and verification;
do not erase earlier failed checks.

If required checks fail, record status `blocked` and the failure; do not present
a successful handoff. Never push, commit, force, or discard user changes.

Return task ID, exact plan/brief and log paths, verification results, deviations, session provenance and blockers before the
parent ends the worker. Await independent `xreview <work log filename>`; do not
mark the task `complete` yourself.
