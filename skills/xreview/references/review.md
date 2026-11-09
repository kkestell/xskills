# Review the implementation, not its story

## Establish the exact change

Read the work log, original request or preserved brief, plan when supplied,
referenced design/dependencies, and repository instructions.
Confirm the task ID and repository. Extract full **Code base** and **Code head**
commit IDs from the log; verify that both exist and base is an ancestor of head.
For missing or ambiguous anchors, ask the caller to establish them. Do not infer
the task from `HEAD~1`, the last commit message, or the plan's filename.

Set `CODE_BASE` and `CODE_HEAD` to those validated IDs. Inspect the full
`git diff --name-status "$CODE_BASE" "$CODE_HEAD"`,
`git diff "$CODE_BASE" "$CODE_HEAD"`, and task commit history. These are the
recorded endpoints, not the checkout's possibly newer literal `HEAD`.
Use the recorded implementation commits as provenance,
not as a reason to ignore other changes in the range. Include tests, build and
deployment configuration and source under `.agents/skills/` where relevant.
Only explicitly identified workflow records are excluded from code analysis.
Look at complete touched files, callers and contracts, not only added lines.

Check the current checkout against recorded Code head and `git status`, including
untracked files. Later review/log-only commits are expected. If implementation
differs, require a current committed code anchor and verification before accepting;
do not silently review a stale snapshot while approving the working tree. Do not
discard uncommitted work to obtain the recorded revision. Use an available safe
read-only view or isolated checkout for historical inspection, and disclose it.

## Review behavior and engineering

1. **Required outcomes:** trace each requested behavior and consequential plan
   decision through the actual code. Check omissions, accidental scope expansion,
   altered semantics and deviations. A plan is not authorization for invented
   extra work. A plan defect discovered here still needs correction; implementation
   conformity does not excuse an incorrect design.
2. **Correctness and integration:** follow data/control flow, ownership and
   lifetimes, errors, state transitions, algorithm invariants and external
   contracts where relevant. Investigate uncertainties that could change the
   verdict. Do not impose speculative durability, fallback or future extensibility
   guarantees merely because a failure is imaginable.
3. **Whole-file clarity and proportionality:** assess what a reader must understand
   in the touched files. Hard-to-follow code is a blocking finding without needing
   a failing test: name the confusing responsibility/control flow and a concrete
   simplification or split. Flag unnecessary abstractions, duplicated state,
   dead code and mechanisms unsupported by the request. Do not prescribe a large
   redesign merely to satisfy a stylistic preference.
4. **Verification:** inspect real assertions and fixtures, not test names or the
   log's pass claims. Check behavior, regressions and feasible failure scenarios;
   invalid/unspecified-behavior examples are not proof. First inspect the existing
   check evidence and confirm it applies to the reviewed revision, relevant
   environment and required coverage, including fixes/integration. Follow the
   shared verification-reuse policy: reuse sufficient matching evidence unless
   fresh execution is explicitly required. Independent reasoning and inspection
   remain mandatory even when command results are reused.
   For a concrete coverage gap, doubtful result or remaining correctness question,
   run a focused regression or broader check that addresses it and say why. Do
   not routinely rerun both focused repetitions and a full suite/build. Inspect
   docs-only changes without builds unless instructions require them. Missing
   usable evidence for a required check must be obtained, not waived.
5. **History and handoff:** verify the recorded plan and linked-guidance blobs,
   fixed original base, full implementation range, actual commits, and the log's
   scope/check claims. Separate missing implementation, an implementation defect
   despite clear guidance, incorrect plan guidance, and missing evidence. No
   word-count target applies to code, work logs or review reports.

Do not let unrelated legacy defects expand the review into a repository-wide
audit. Relevant pre-existing code that makes the changed behavior unsafe or
unreadable is not exempt merely because it was not added in this diff. Explain
that relationship and return any material scope decision to the parent/user.

## Findings and verdict

Append a round to `.agents/reviews/ID.md` with the shared metadata. Include:

- **Reviewed range:** full Code base/head, current checkout identity, relevant
  later record-only changes, request/plan/brief and work-log paths.
- **Verdict:** `accept`, `changes-required`, or `blocked`; concise reasons and
  an explicit independence statement.
- **Findings:** stable identifiers, priority, exact path/line or symbol, concrete
  defect/consequence, supporting evidence, and the smallest coherent correction.
  Correctness findings should describe a real failure or violated invariant;
  clarity findings should show what is hard to follow and how to simplify it.
- **Verification:** distinguish commands independently `run` from results
  `reused`; name the exact command, target revision, result and evidence source.
  Explain why any fresh run was needed. Reference existing results instead of
  copying full output; list failures, omissions and environmental blockers.
  Do not mark absent checks passed.
- **Resolution table, when prior findings exist:** each finding's status and
  evidence at the new Code head; identify remaining issues and any new findings.
  An empty new-finding list is not evidence that old findings were fixed.

For a no-findings round, say so and give a brief independent justification of
the difficult invariants, not a second implementation walkthrough. Keep exact
anchors, author/native-session provenance, check sources and limitations. Do not
add empty findings/resolution sections or restate the plan to make the review
look thorough. Substantive findings and necessary proof may take more space.

Every material finding, including hard-to-follow touched code, prevents acceptance.
Informational observations may be separate notes, not silently deferred defects.
Missing evidence for a required check blocks acceptance, but lack of unrelated
environment/context is not automatically a design or code defect.

Return the report and reviewed range to the caller. Do not make the fixes or
commit the review unless explicit handoff authority permits it. Under xauto the
parent commits this round, routes fixes to xwork, and obtains review of the full
updated change while preserving the original base.
