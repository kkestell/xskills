# Review: <task ID>

## Round <N>

- Task: `<YYYY-MM-DD-NNN-slug>`
- Author: <role/name>, <harness>, <model/effort>; coordinator ID `<id>`;
  native conversation ID `<id or "unavailable: reason">`
- Independence: <"I did not write this code; the implementer was <name>.", or
  the self-review disclosure>
- Reviewed change: <checkout and branch>; request/plan/brief `<path>`; work log
  `<.agents/work/ID.md>`

### Verdict

<accept | changes-required | blocked>: <one to three sentences of reasons>

### Findings

1. **<Priority>: <one-line defect>.** `<path>:<line>` or `<symbol>`.
   <Concrete failure or violated invariant, the evidence for it, and the
   smallest coherent correction.>

### Resolution of earlier findings

| Finding | Status | Evidence in current code |
| --- | --- | --- |
| <round.N> | <resolved / unresolved / partially resolved> | `<path>:<line>`: <what shows it> |

### Notes

- <Informational observation that does not block acceptance.>

### Verification

- Run: `<exact command>`: <result>. <Why a fresh run was needed.> Evidence:
  <location>.
- Reused: `<exact command>`: <result>, from <work log or evidence location>.
- Not run: <required check and the reason, or omit this line>.

<Omit Findings, Resolution and Notes when empty. A no-findings round replaces
Findings with a brief justification of the difficult invariants.>
