---
name: xreview
description: Independently review an implementation with xreview LOG, reading the actual code, tests and their hygiene, clarity, user interface design and conformance to the plan or brief across the work log's recorded revision range. Write a linked .agents/reviews record without editing the reviewed code. Use only when invoked or explicitly requested, including delegation by xauto.
---

# Review an implementation

Read `../xauto/references/workflow.md` for shared IDs, `.agents/` paths, revision
anchors and Git ownership. Install all four x-skills together.

## Dispatch explicitly

```text
xreview <work log filename>
```

Require a target. If it is absent or ambiguous, ask; do not guess from the latest
file, current branch or staged changes. A bare filename resolves in
`.agents/work/`; an explicit path is read exactly, including legacy inputs outside
that directory. Do not move or overwrite an input merely to normalize its path.

Read `references/review.md`. The work log locates the task and revision range; it
is not a substitute for inspecting the actual implementation. Write
`.agents/reviews/ID.md`.

Reuse the task ID. For an input without a usable ID, allocate one by the shared
contract and record the original path. Append numbered rounds, with fresh
revision anchors, rather than replacing previous evidence or approval. Preserve
prior findings and explicitly record whether and how each was resolved.

## Independence and authority

Under xauto, be a distinct worker from the implementation's author. Standalone
xreview may be a self-review if the user chose that context, but must disclose
that limitation instead of claiming independence. Do not delegate another review
or launch a worker unless separately authorized.

Read/investigate/run appropriate checks, and write only the review record. Do
not fix code, stage or commit by default. Return findings to the implementer;
the parent handles artifact commits and review loops. An explicitly authorized
isolated-worker handoff may commit its review record alone, with the task/stage
trailers. This exception does not authorize code edits.

The handoff must include exact input/output paths, reviewed revisions, verdict,
actionable findings, checks run or reused with their evidence sources, session
provenance (including native conversation ID), and limitations. Keep acceptance
reports concise using the shared contract: preserve the assessment and anchors,
not a repeated tour of the implementation. `accept` cannot coexist with
unresolved required corrections or blockers. Neither a clean tree nor a worker's
successful summary establishes correctness.
