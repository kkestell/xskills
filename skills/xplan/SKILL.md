---
name: xplan
description: Research a code or behavior change and write a short, implementation-ready execution plan with consequential engineering decisions resolved. Use when the user invokes xplan or explicitly asks for this planning workflow. Do not implement the change.
---

# Implementation-ready planning

The deliverable is a set of decisions an implementer can execute: not a
promise to decide later, and not the patch written in prose.

Read `../xtask/references/workflow.md` for IDs, paths and Git rules.

## Investigate

1. Establish the outcome, constraints, exclusions and acceptance criteria.
   Read the repository instructions and the code, tests and build commands the
   change touches.
2. Trace the current behavior through the actual paths and symbols, and find
   the existing patterns to reuse. Check external APIs in their documentation
   or a focused experiment when the answer could change the design.
3. Settle the consequential choices: ownership, interfaces and data shapes,
   state transitions, errors, compatibility, migration and verification, as
   far as this change has them. Choose the simplest complete design.
4. Settle ordinary engineering choices yourself. Ask only for missing intent,
   authorization, or a tradeoff the evidence cannot settle. If an answer is
   unavailable, mark the plan `blocked` and name exactly what is needed.

## Size the assignment

- Routine localized work gets a brief: kind `brief`, holding the outcome,
  constraints, affected code, checks, and assumptions if any qualify.
- A normal assignment gets one plan: a few cohesive changes whose
  implementation and checks fit in one unit of attention.
- Larger work splits into units, each with its own plan, prerequisites and
  checks. Return a scope-to-unit map so the whole request stays covered.

## Write the plan

Write each plan once to `.agents/plans/ID.md` from `templates/plan.md`, with
IDs in execution order. **A plan is at most 1,500 words, a brief at most 400.**
A plan that cannot fit is too large an assignment: split it. Corrections after
writing are edits to the affected lines.

Sections:

- **Outcome and boundaries:** observable behavior, constraints, non-goals.
- **Current system:** the paths, symbols and flow the change touches, and the
  behavior to preserve.
- **Design:** the actual decisions, and for a consequential one the
  alternative rejected and why.
- **Check your assumptions:** the decisions and unconfirmed assumptions the
  user would be surprised to find after the code is written, such as changed
  or dropped behavior, slower paths, compatibility breaks, narrowed scope, new
  dependencies, migrations, and readings of an ambiguous request. Lead each
  with its consequence and give the evidence behind it in a sentence. Usually
  three to seven entries; write "None." when nothing qualifies. Internal coding
  choices stay in Design.
- **Implementation sequence:** ordered changes tied to paths and symbols.
- **Verification:** acceptance cases, regressions and failure paths, where
  their tests go, and the commands to run. Check that each scenario is
  possible with the real syntax and test APIs.

Use a snippet only for an essential interface, type or invariant. Leave local
names, routine wiring and helper bodies to the implementer.

When the user changes assumption entries, edit the affected plans and mark
each entry with its outcome. Return any decision the change reopens instead of
choosing it yourself.

Return the plan paths, readiness, the scope-to-unit map and any blockers. Do
not edit production code, stage, commit or delegate.
