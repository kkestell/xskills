---
name: xplan
description: Research a code or behavior change and write a detailed, implementation-ready execution plan with consequential engineering decisions resolved. Use when the user invokes xplan or explicitly asks for this planning workflow. Do not implement the change.
---

# Implementation-ready planning

The deliverable is a set of decisions an implementer can execute, not a promise
to decide later and not a patch written in prose. Normalize both the amount of
assigned work and the detail explaining it. A well-described monster assignment
is still too large; a polished tiny plan should have been a task brief.

Read `../xauto/references/workflow.md` for shared IDs, `.agents/` artifact paths,
record metadata and orchestrated handoffs. Install the four x-skills together.

## Investigate before committing to a design

1. Establish the requested outcome, constraints, exclusions, and acceptance
   criteria. Read applicable repository instructions and inspect relevant code,
   tests, build commands, and existing architecture. Preserve user changes.
   Distinguish requirements from your proposed mechanisms.
2. Trace the current behavior end to end. Record actual paths and symbols and
   the existing patterns the change should reuse. Investigate external contracts
   in authoritative documentation or a focused experiment when uncertainty could
   change the design. Do not substitute guesses about an API for research.
3. Keep a temporary decision list: question, evidence, choice, consequence.
   Resolve architecture, responsibility/ownership, interfaces and data shapes,
   state transitions, ordering, errors, compatibility, migration, and verification
   **where relevant to this change**. Do not manufacture each of these concerns
   for a change that does not have them. Compare whole alternatives, including
   operational and transition costs, then choose the simplest complete solution.
4. Resolve ordinary engineering choices yourself. Ask the user only for genuinely
   missing intent, authorization, or a material tradeoff the evidence cannot
   settle. First research what can be researched. If an answer is unavailable,
   mark the artifact blocked, explain exactly what is needed, and do not claim
   it is implementation-ready. A bounded investigation may precede the plan;
   “implementer will work it out” is not a resolved decision.

Before declaring a blocker, assemble the evidence already available: trace
owners and callers and explain how their invariants settle the question. Missing
files are not automatically missing engineering decisions. Locating exhaustive
matches, choosing an unused artifact name, or checking tool availability is
ordinary execution preparation unless it exposes a consequential unresolved
contract. Name the particular behavior or competing designs that cannot be
settled; do not block on a generic instruction to “confirm all assumptions”.
Conversely, do not hide a genuine unresolved choice in a limitations footer
while declaring the plan ready. Research the specific missing evidence first.

## Bound the execution assignment

Read `references/normalization.md` for the size/detail rubric
and experimental numerical targets.

Inventory substantive implementation and test deliverables independently of
prose length. Expose the internal responsibilities of a “core”, “rewrite”, or
“integration”; an umbrella heading does not make them one small task. Repeated
wiring is not automatically a new mechanism, and test-only work is real work.

- For routine localized work below the planning threshold, return a task brief
  with necessary constraints, affected code, and checks instead of creating a
  separate plan. If the user explicitly requires an artifact, label it a brief.
- For oversized work, settle the shared design first, then produce bounded
  execution plans with concrete scope, prerequisites, interface assumptions,
  intermediate-state behavior, and checks. Units need not ship independently.
  Do not silently drop any requested outcome. Include a scope-to-unit map so
  the complete request remains covered. Do not hide several large assignments
  under one “implementation step”.
- For a normal assignment, write one execution plan. Prefer a few cohesive,
  consequential changes whose implementation and verification fit in one unit
  of attention; compare with project reference assignments when available.

## Write the plan

Write `.agents/plans/ID.md` from `templates/plan.md`, reusing the parent's task
ID or allocating it by the shared contract. Keep its metadata and only sections
that help execution; combine them when clearer. Put necessary shared
design/split-unit maps in `.agents/designs/ID.md` from `templates/design.md`,
with distinct IDs for execution units. The plan's sections:

- **Outcome and boundaries:** observable behavior, constraints, non-goals.
- **Current system:** relevant paths/symbols, data/control flow, existing behavior
  to preserve. Cite what you inspected, not an exhaustive file inventory.
- **Chosen design and decisions:** who owns each responsibility; contracts,
  data flow, transitions, integration and failure behavior; why consequential
  alternatives were rejected. State the actual decision, not a menu of options.
- **Implementation sequence:** ordered, concrete changes tied to paths/symbols,
  dependencies and the resulting behavior. Explain the tricky algorithm or
  transition sufficiently to avoid another design exercise during coding.
- **Verification:** meaningful acceptance cases, regressions and failure paths,
  where tests belong, runnable commands, and any required manual checks.
- **Handoff:** readiness, work-size assessment, detail assessment, and any genuine
  blocker. A ready plan has no open consequential engineering decisions.

Use small code snippets for essential interfaces, data types, protocol examples,
or an algorithm invariant when prose would be ambiguous. Do not transcribe all
function bodies, enumerate routine edits, or provide the entire implementation.
Exact local names and straightforward helper extraction can remain coding
details; behavior, ownership, algorithms and contracts cannot.

Validate verification examples against the actual system's syntax, scope,
lifetime and test APIs. An impossible scenario or unspecified-behavior oracle
does not demonstrate correctness. Distinguish structural assertions from valid
end-to-end behavior, and choose feasible checks for each invariant.

Make the complete guidance accessible from each execution plan. A specific link
to a settled shared design avoids duplication; “see roadmap” does not bound work.

## Check before handoff

After writing an execution plan, run the bundled
`scripts/plan_metrics.py --plans .agents/plans --plan PATH` using the script's
actual installed path. Use a preselected curated reference manifest if one
exists. Measure the saved text rather than guessing its word count; if tools
are unavailable, disclose that instead of reporting an invented measurement.
Size and detail are separate axes; repairing one must not conceal the other.
Repair missing decisions, remove demonstrably unnecessary detail, or split work
and recheck the resulting units. Preserve consequential constraints when trimming.
Do not pad to reach a word target. If useful guidance cannot fill a standalone
plan, use a brief. Outside-target length requires an explicit size/detail
assessment, not automatic rejection or exemption. Correct demonstrated defects;
do not manufacture missing guidance or removable detail from the count alone.
If count is the only outlier, record the reference comparison and why the
provisional band does not describe this assignment. Never excuse demonstrably
tiny or monster assignments merely because their descriptions suit their scope.

Finish with links, readiness, the significant choices, session provenance
(including native conversation ID when exposed), and remaining blockers.
Do not edit production code, run a full build for prose-only changes, stage,
commit, or delegate unless separately authorized.
