---
name: xreview
description: Independently review an implementation with xreview LOG, reading the actual code, tests and their hygiene, clarity, user interface design and conformance to the plan or brief in the task checkout's uncommitted change. Write a linked .agents/reviews record without editing the reviewed code. Use only when invoked or explicitly requested, including delegation by xtask.
---

# Review an implementation

Read `../xtask/references/workflow.md` for IDs, paths and Git rules, and
`references/review.md` for what to review.

```text
xreview <work log filename>
```

Require a target; if it is absent or ambiguous, ask. A bare filename resolves
in `.agents/work/`; an explicit path is read exactly. The work log locates the
task; it does not replace reading the code.

Write `.agents/reviews/ID.md` from `templates/review.md`, reusing the task ID.
A later round appends `## Round N` and records how each earlier finding was
resolved.

Under xtask, the reviewer is never the implementer. Standalone xreview may be
a self-review if the user chose that, and says so. Write only the review
record: do not fix code, stage, commit or delegate.

Return the review path, verdict, blocking findings, plan findings, notes,
checks run or reused, and limitations. `accept` cannot coexist with an
unresolved blocking finding.
