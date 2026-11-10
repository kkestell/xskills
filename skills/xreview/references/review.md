# Review the implementation, not its story

## Establish the exact change

Read the work log, original request or preserved brief, plan when supplied,
referenced design/dependencies, and repository instructions.
Confirm the task ID and repository. Extract the full **Code base** commit ID and
the latest **Code snapshot** tree ID from the log, and verify both with
`git cat-file -t`. For missing or ambiguous anchors, ask the caller to establish
them. Do not infer the task from recent commits or the plan's filename.

Take a fresh snapshot of the checkout as the shared contract describes, and
compare it with the logged one: `git diff --stat LOGGED_SNAPSHOT FRESH_SNAPSHOT`.
If code, config or tests differ, the log does not describe what is in front of
you; return that to the caller instead of reviewing. Record-only differences
are expected.

Set `CODE_BASE` and `SNAPSHOT` to the validated IDs. Inspect the full
`git diff --name-status "$CODE_BASE" "$SNAPSHOT"` and
`git diff "$CODE_BASE" "$SNAPSHOT"`. On a repair round, also read
`git diff PREVIOUS_SNAPSHOT "$SNAPSHOT"` to see what the fix changed, but review
the whole change from the base. Include tests, build and deployment
configuration and source under `.agents/skills/` where relevant. Only explicitly
identified workflow records are excluded from code analysis. Look at complete
touched files, callers and contracts, not only added lines.

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
   fixed original base, snapshot history, and the log's
   scope/check claims. Separate missing implementation, an implementation defect
   despite clear guidance, incorrect plan guidance, and missing evidence. No
   word-count target applies to code, work logs or review reports.

Do not let unrelated legacy defects expand the review into a repository-wide
audit. Relevant pre-existing code that makes the changed behavior unsafe or
unreadable is not exempt merely because it was not added in this diff. Explain
that relationship and return any material scope decision to the parent/user.

## Review user interface design

Apply this section to any change a user sees or interacts with. Read the
repository's design, UI and interface-text rules first, and identify the
reference surface: the screen or component the user or project treats as the
standard of careful design. A request or brief that names one settles it;
otherwise use the established surface most similar to the changed one. Hold the
change to that surface's design language.

Judge the rendered interface alongside the code. Use current screenshots or the
running app, in every supported theme and at both comfortable and narrow widths.
A screenshot captured before the reviewed snapshot is not evidence for it.

1. **Consistency:** compare spacing, sizes, alignment, color, type, icon
   weight, hover and focus treatment, and motion against the reference surface.
   Check that content edges line up with neighboring controls, padding stays even
   when a scrollbar takes space, wrapped rows keep their alignment, and text
   fades or truncates only when it overflows. Report each mismatch with the
   reference's value.
2. **Information design:** for each row, card or panel, establish what the user
   most needs and check that it leads. Report icons that spend space without
   carrying meaning, lines that repeat what another element already shows,
   decoration that competes with primary content, and lists that interleave
   items a user would expect grouped together. Report affordances foreign to the
   product's platform, such as web-style underlined links and hover-revealed
   external links in a desktop app; a context menu usually carries those actions.
   Check interface text against the project's rules, including its rules on
   separator characters and punctuation.
3. **Motion and layout stability:** check that content keeps its height while
   it streams or updates, that a height change happens inside its animation
   rather than before or after it, and that revealing a hidden tab, panel or
   tree does not replay the opening animations of everything inside it. Check
   reduced-motion behavior.
4. **Visibility and focus:** state that should follow what the user can see,
   such as marking items read or clearing an indicator, must depend on actual
   visibility, not on selection while another view covers it. Check that focus
   lands where the user expects after navigation, including on returning to a
   view, and stays put when a view only moves.
5. **Accessibility:** check roles, accessible names, keyboard reach to
   hover-revealed controls, focus order, and nested interactive elements.
6. **Reuse:** search the codebase for an existing component, hook or style
   that the new markup or logic repeats, and report the copy with the shared
   piece that replaces it.

Match depth to the interface's maturity. Hold settled surfaces to the full
standard. For interface the user is still iterating on, report only what breaks
or looks broken in normal use; polish and hardening of a design that is still
changing waste the next iteration. Report a test gap when a visibility, focus or
motion regression the review found has no test that would catch its return.

## Review test hygiene

Apply this section to every change that adds, edits, removes or depends on
tests. Read the repository's testing rules first, including any stated time
budget for the suite or a package. Hold the tests to the same standard as
product code: a slow, flaky or leaky suite is a defect.

1. **Speed:** compare the suite and the touched packages against the budget or
   their usual time, and report a regression with its measurement. Find where
   a slow test waits: per-test durations, the test run alone, and its child
   processes. A test that is fast alone and slow in its package waits on
   something tests share. Report tests that build binaries, start real
   processes, create repositories or start services when a plain fixture or an
   in-process call proves the same behavior; independent tests that run
   serially; and setup repeated per case that one shared fixture could hold.
2. **Waiting:** tests wait on conditions, never fixed sleeps or timing guesses.
   A timeout used as a test seam is set before the work it governs starts and
   is large enough that normal work under parallel load never trips it.
3. **Isolation:** tests never read or change the user's configuration, state,
   workspaces or running processes, and use no network. Each test takes its
   paths from a temporary directory and its dependencies through constructors
   or explicit parameters. Report mutation of process-wide state, such as
   environment variables, the working directory, global tool configuration or
   configuration shared across checkouts, because it leaks between tests and
   forces them to run serially. Check that tests stop every process they start
   and remove every hook, file and setting they install. Check that tools
   with machine-dependent defaults are pinned; an unset Git identity, for
   example, triggers a host-name lookup that can take seconds.
4. **Flakiness:** treat an intermittent failure as a race in the test or the
   product until its cause is named. Read the evidence that the cause is fixed:
   a repeated run of the affected test under the race detector or equivalent,
   with run count and failure rate before and after, compared on the base
   revision. A retry, longer timeout or skipped assertion is not a fix. When the
   race is in the product, the fix belongs in the product.
5. **Value and coverage:** tests assert observable behavior through public
   entry points; report assertions on private state, markup or styling that is
   not itself the protected behavior, and the same behavior repeated at every
   layer. When the change deletes or rewrites tests, trace each removed case to
   the code path it exercised and confirm another test still reaches it.
   Deleting the only test of a consequential path, such as a rollback, cleanup
   or data-loss guard, is a finding even when the work log calls the case
   redundant. Deleting a fast test saves no time; judge it on value alone.
6. **Readability:** a helper does one thing. Report helpers that switch between
   unrelated mechanisms on a parameter, fixtures whose names or comments
   misstate what they catch, and cases a reader cannot connect to the behavior
   they protect.

## Findings and verdict

Append a round to `.agents/reviews/ID.md` with the shared metadata. Include:

- **Reviewed range:** full Code base and reviewed snapshot, current checkout
  identity, request/plan/brief and work-log paths.
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
  evidence at the new snapshot; identify remaining issues and any new findings.
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

Return the report and reviewed range to the caller. Do not make the fixes,
stage or commit anything. Under xauto the parent routes fixes to xwork and
obtains review of the full updated change while preserving the original base.
