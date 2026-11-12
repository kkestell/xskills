# Review: <task ID>

## Round <N>

- Task: `<YYYY-MM-DD-NNN-slug>`
- Independence: <"I did not write this code; the implementer was <name>.", or
  the self-review disclosure>
- Reviewed change: <checkout and branch>; request/plan/brief `<path>`; work log
  `<.agents/work/ID.md>`

### Verdict

<accept | changes-required | blocked>: <one to three sentences of reasons>

### Findings

<Blocking findings only.>

1. **<Priority>: <one-line defect>.** `<path>:<line>` or `<symbol>`.
   <Concrete failure or violated invariant, the evidence for it, and the
   smallest coherent correction.>

### Plan findings

<Evidence that the plan or a settled decision is wrong, and its consequence.
These go to the user and do not affect the verdict.>

### Resolution of earlier findings

| Finding | Status | Evidence in current code |
| --- | --- | --- |
| <round.N> | <resolved / unresolved / partially resolved> | `<path>:<line>`: <what shows it> |

### Notes

- <Non-blocking issue, such as a test for an unlikely path or polish, with its
  location and suggested change.>

### Verification

- Run: `<exact command>`: <result>. <Why a fresh run was needed.> Evidence:
  <location>.
- Reused: `<exact command>`: <result>, from <work log or evidence location>.
- Not run: <required check and the reason, or omit this line>.

<Omit Findings, Plan findings, Resolution and Notes when empty. A no-findings round replaces
Findings with a brief justification of the difficult invariants.>
