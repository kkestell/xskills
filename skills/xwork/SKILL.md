---
name: xwork
description: Implement a decision-complete plan with xwork PLAN, or an explicitly supplied bounded task brief, verify the change, and write a linked .agents/work log, leaving everything uncommitted. Use only when the user invokes xwork or explicitly requests this workflow, including delegation by xtask.
---

# Execute a bounded assignment

Read `../xtask/references/workflow.md` for IDs, paths and Git rules. This
skill implements, verifies and logs; it does not redesign the assignment or
review its own work.

## Start

- Resolve the supplied filename exactly; a bare filename resolves in
  `.agents/plans/`. If it is ambiguous, ask.
- Read the repository instructions, the plan and the plans it depends on.
  Reuse the plan's task ID. Do not execute a blocked plan.
- Given a brief as text (`xwork --brief <task brief>`), save it as a brief in
  `.agents/plans/ID.md` first. If it turns out to need real design work,
  return it for planning.
- Confirm the checkout and `git status` before editing.

## Implement and verify

1. Inspect the actual code and tests rather than trusting the plan's paths and
   API assumptions. Follow the plan's responsibilities, contracts and scope.
   Keep touched files easy to follow.
2. Settle routine coding details yourself. If evidence shows a consequential
   decision cannot work, stop that work and return the evidence and the
   decision needed. Record every deviation and why.
3. Add meaningful tests for the required behavior and regressions.
4. Run the plan's required checks and the repository's applicable checks on
   the final change. For documentation-only changes, inspect the documents.
   A missing dependency, failed check or skipped check is not a pass.
5. Inspect the complete diff, including untracked files, for scope and
   accidental changes.

## Write the work log

Write `.agents/work/ID.md` from `templates/work-log.md`: what changed by path
and responsibility, deviations, each check's exact command and result with a
log path, and limitations. Link to the plan instead of repeating it. Set
status `implemented`, or `blocked` with the failure if a required check
fails. On a repair round, append a repair entry; leave earlier entries as
written.

Do not stage, commit, stash, reset or push. Return the task ID, plan and log
paths, check results, deviations and blockers.
