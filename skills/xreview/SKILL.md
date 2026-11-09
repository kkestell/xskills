---
name: xreview
description: Normalize an execution plan with xreview plan PLAN, or review the implementation with xreview work LOG. Plan mode assesses assigned work and exposition from supplied material only; work mode independently reviews actual code, tests, clarity and conformance. Write linked .agents/reviews records without editing the reviewed code. Use only when invoked or explicitly requested, including delegation by xauto.
---

# Review a plan or its implementation

Read `../xauto/references/workflow.md` for shared IDs, `.agents/` paths, revision
anchors and Git ownership. Install all four x-skills together.

## Dispatch explicitly

```text
xreview plan <plan filename>
xreview work <work log filename>
```

Require both mode and target. If either is absent/ambiguous, ask; do not guess
from the latest file, current branch, filename suffix or staged changes. A bare
filename resolves in `.agents/plans/` for plan mode or `.agents/work/` for work
mode; an explicit path is read exactly, including legacy inputs outside those
directories. Do not move or overwrite an input merely to normalize its path.

- **plan:** follow `references/plan-review.md`: prepare supplied inputs and metrics,
  use its self-contained, tool-free assessment prompt, then save the result to
  `.agents/reviews/plans/ID.md`. Assess assigned work and exposition only, not
  engineering correctness or readiness. Preparation/saving are outside assessment;
  the instruction-based harness does not enforce tool isolation or one model call.
- **work:** read `references/work-review.md`. The work log locates the task and
  revision range; it is not a substitute for inspecting actual implementation.
  Write `.agents/reviews/work/ID.md`.

Reuse the task ID. For an input without a usable ID, allocate one by the shared
contract and record the original path. Append numbered rounds, with fresh
revision anchors, rather than replacing previous evidence or approval. Preserve
prior findings and explicitly record whether and how each was resolved.

## Independence and authority

Under xauto, be a distinct worker from the reviewed artifact's author. Standalone
xreview may be a self-review if the user chose that context, but must disclose
that limitation instead of claiming independence. Do not delegate another review
or launch a worker unless separately authorized.

In work mode, read/investigate/run appropriate checks. In plan mode, load only
supplied material and precompute metrics outside the tool-free assessment; do not
investigate code, contracts or test feasibility. Write only the review record. Do
not rewrite the plan, fix code, stage or commit by default. Return findings to
the planner/implementer; the parent handles artifact commits and review loops.
An explicitly authorized isolated-worker handoff may commit its review record
alone, with the task/stage trailers. This exception does not authorize code edits.

The handoff must include exact input/output paths, reviewed revisions, assessment,
actionable findings, evidence sources (and run/reused checks in work mode), session
provenance (including native conversation ID), and limitations. Keep acceptance
reports concise using the shared contract: preserve the assessment and anchors,
not a repeated tour of the plan or implementation. `accept` is exclusive of
corrective actions. In plan mode, only normalization findings govern that action;
in work mode, unresolved required corrections or blockers prevent acceptance.
Neither a clean tree nor a worker's successful summary establishes correctness.
Plan-mode acceptance makes no implementation-correctness or readiness claim.
