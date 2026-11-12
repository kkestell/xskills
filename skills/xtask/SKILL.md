---
name: xtask
description: Entry point for the x-workflow. Orchestrate xplan, xwork, and xreview in child sessions (or subagents when child sessions are unavailable), presenting the planner's assumptions to the user in one list with its own recommendation on each, stopping only for decisions that need the user, and committing each plan's code and .agents records once its review is accepted. Use only when the user invokes xtask or explicitly requests this workflow. Do not invoke kauto or push changes.
---

# Orchestrate the x-workflow

The current session is the coordinator. Read `references/workflow.md` once at
the start. The workers read their own skills; the coordinator does not need
them.

The coordinator stops for the user only for:

- the assumptions list, before work starts;
- plan findings from a review;
- blocking review findings, before sending them to fixes;
- any question of intent, scope, permission or a material tradeoff;
- a failed required check or an unavailable required tool.

Otherwise it runs straight through to each unit's commit. The user may ask for
a stop after every stage; then it reports and waits after plan, work and
review.

## Prepare

1. Establish the request, constraints and scope. Find the Git root, branch and
   dirty state. Git is required. If the checkout has unrelated changes, ask
   the user to restart xtask in a clean worktree session.
2. Use child sessions to delegate; use subagents only when child sessions are
   unavailable. If neither exists, stop and say so.
3. Inherit model, harness and effort unless the user or instructions select
   others. Start every worker fresh. The reviewer is never the implementer.

## Briefs

Each worker gets the objective, the user's constraints, its skill and
invocation, task ID, checkout, input and output paths, allowed edits, and the
existing check results it can reuse. Ask it to begin its final reply with one
line: task ID, stage, artifact path, verdict.

## Plan

- Start a planner with `xplan <request>` and no production-code edit
  authority. It writes each plan once, with its **Check your assumptions**
  list, and returns the scope-to-unit map.
- Check that the units cover the whole request.
- Present every unit's assumptions to the user in one message, in unit order,
  numbered. For each entry give the consequence, the choice that causes it,
  the alternative given up, and your recommendation (keep the planner's
  choice or change it) with the reason. Base the recommendation on the
  planner's evidence; read code only where that evidence does not settle it.
  The user answers only the entries they want changed; the rest stand.
- Send the planner the changed entries in one message. It edits the affected
  plans; it does not rewrite them. If a change reopens other decisions, the
  planner returns the new entries and you present them the same way.
- Entries the user settles are requirements for the rest of the task.

## Work and review, per unit in dependency order

- Start an implementer with `xwork .agents/plans/ID.md`.
- Start a reviewer with `xreview .agents/work/ID.md`, giving it the request,
  plan and work log.
- On `accept`, commit the unit.
- Before presenting a review, check each blocking finding against the code.
  A finding that needs a contrived timing or sequence of events to occur
  becomes a note in the review record. If no blocking finding is left, treat
  the review as `accept`.
- On `changes-required`, present the remaining blocking findings. The user may
  drop, amend or add findings. Notes stay in the review record and are not
  presented. Send the settled findings
  to the same implementer; it fixes them, reruns the affected checks and
  appends a repair entry. Then send the same reviewer one focused re-review of
  the fix. A unit gets one re-review; whatever it leaves unresolved goes to
  the user.
- Plan findings go to the user. A plan change goes to the planner as an edit,
  and then to the implementer.
- If implementation shows a plan decision cannot work, route it to the
  planner and the user before continuing.

## Commit and finish

Commit a unit when its required checks passed, its latest review round is
`accept` or the user accepted the remaining findings, and nothing changed
after that review. Set the work log status to `complete` and commit as the
shared contract describes. End the unit's workers after its commit.

Return the task IDs, each unit's commit ID, branch, check results, review
verdicts and remaining limitations. Failed units stay uncommitted and are
reported with their blockers.
