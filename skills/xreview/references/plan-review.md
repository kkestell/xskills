# Plan review mode

Judge two independent things: **how much work is assigned** and **how completely
and economically its consequential decisions are specified**. Do not approve a
tiny or monster plan merely because its description suits its scope.

Read `normalization.md` before evaluating. Its numeric targets are
explicit experimental defaults, not a validated universal optimum.

## Establish evidence

Read the request, plan, referenced shared designs, and applicable instructions.
Record the shared contract's Guidance blobs for linked local execution guidance,
including transitive design inputs; approval applies to those inputs as read.
Inspect relevant current code, tests and external contracts to resolve doubts
that could affect the verdict. Verify paths and interfaces instead of demanding
the plan repeat available context. Treat missing source context as a limitation,
not evidence that a decision was omitted. Do not invent additional requirements.
The dispatcher has resolved the supplied plan filename; do not substitute a
different plan or silently switch to code-review mode.

Distinguish an unresolved design choice from routine execution preparation.
Searching exhaustive matches or confirming tool availability is not itself a
design blocker. Trace the available invariants before demanding more research;
a blocker must name the consequential behavior or contract that remains open.

Collect the plan's substantive delivery obligations, including test-only work.
For each, name the changed responsibility, behavioral/algorithmic decision,
integration dependencies and verification burden. Use these as evidence of work,
not as equally weighted points. Expand umbrella assignments enough to see their
scope. Distinguish explicitly excluded future work from unresolved current work.
If scope remains unbounded, classify it unknown, not confidently small.

## Assess work size independently of length

Use the reference-assignment comparison in `normalization.md`:

- **Too small:** ordinary localized work whose essential instructions fit in a
  request/brief. Recommend skipping the separate plan, preserving constraints.
- **Right-sized:** a bounded, worthwhile execution assignment comparable to the
  reference units, with no hidden family of separate mechanisms.
- **Too large:** several substantive mechanisms, feature slices, or lifecycle
  transitions need distinct bounded assignments, even if tightly related and
  thoroughly described. Propose concrete units, prerequisites, shared contracts,
  intermediate states, and verification. Preserve coverage of the request.
- **Unknown:** current work is not enumerated or evidence is insufficient. Name
  what must be clarified; do not use a low item count as a small-work verdict.

Neither file count, line churn, obligation count, nor prose length alone settles
this assessment. A small patch can require substantial decisions; a mechanical
large diff can be routine. Explicitly compare a proposed assignment with a
reference when the boundary is unclear. Do not force a numeric score from
incomparable responsibilities.

## Assess detail independently of work size

For each consequential choice ask: can an implementer proceed without selecting
behavior, architecture, ownership, contracts, algorithms, lifecycle semantics or
verification strategy? A ready plan has these settled, accurately grounded in
the system. Routine coding choices do not need prewritten function bodies.

Also check whether settled decisions and verification examples are correct.
Trace test scenarios through the actual syntax, scope, lifetime and test APIs;
an impossible scenario or unspecified-behavior oracle is not verification.
Incorrect settled guidance is a correctness finding, not automatically anemia
or bloat. Report it separately and block acceptance until corrected; do not
force every defect into one of the size/detail labels.

- **Anemic:** identify the assigned work and specific unresolved choice, why the
  existing guidance/referenced design does not settle it, and the implementation
  consequence. Recommend a concrete decision or bounded research to settle it.
  “Needs more detail” is not a finding.
- **Bloated:** quote substantial removable material and propose a shorter
  replacement/deletion that preserves behavior and constraints. Repeated
  explanations, full implementation dumps and irrelevant machinery are evidence;
  one spare sentence or useful rationale is not enough. Moving required work to
  another plan is scope splitting, not proof of excessive detail.
- **Appropriate:** consequential decisions and verification are clear without
  implementing the entire patch in the plan.
- **Both:** report specific missing decisions and unnecessary material separately.
- **Unknown:** explain which missing context prevents judgment.

Measure the saved plan with the bundled helper; do not estimate its word count
by eye when a tool can calculate it:

```sh
python3 <xreview-skill-dir>/scripts/plan_metrics.py --plans .agents/plans --plan PATH
```

If tools are unavailable, use a supplied measured count or disclose that length
was not measured. Do not report a guessed number as a measurement.

To use curated project references, also pass `--accepted reference-plans.json`.
The manifest is a JSON list of plan paths relative to `--plans`. Only mark
references accepted after inspecting work size and detail; historical existence
or implementation completion is not acceptance. Do not silently curate a
favorable sample to make the current plan pass.

The helper reports historical quartiles separately from the active target.
Outside-target length requires explicit investigation of brief/expand or
split/trim alternatives. Corrections need a concrete scope, decision or detail
finding, not the count alone. If no such defect remains, explain the reference
comparison and the provisional band's mismatch before accepting; do not invent
filler or cut necessary guidance. This does not exempt genuinely tiny or monster
assignments from normalization. Inside-target length does not demonstrate
readiness. Never use words per obligation as an anemia/bloat formula.

## Report and stop

Make one substantive assessment of the supplied plan and report all supported
findings together. Review is not a certification loop for every textual revision.
Under xauto, the parent verifies ordinary corrections and records the execution
decision; do not require a new independent verdict merely because a blob changed.
If asked for further assessment, focus on the named consequential question and
affected decisions, not a new search for optional improvements. Do not promote a
preferred wording, routine coding choice or hypothetical guarantee into a blocker.

Write or append a numbered round to `.agents/reviews/plans/ID.md`, following
the shared contract's metadata and exact reviewed-plan blob. If chat-only output
was explicitly requested, return the same metadata and findings there. Include:

1. **Verdict:** work size, detail, readiness; primary and secondary actions from
   `skip-plan`, `expand-guidance`, `split-work`, `trim-detail`, `clarify-scope`,
   `resolve-decisions`, `accept`. Accept is exclusive of corrective actions.
2. **Evidence:** actionable findings with plan locations/quotes, relevant
   code/design evidence, consequences, and proposed correction. For acceptance,
   briefly identify the consequential choices independently checked; reference
   plan sections instead of repeating its obligation inventory or design.
3. **Normalization:** active numerical target and source, measured length,
   comparison with reference assignments, and confidence/limitations. Length is
   an advisory signal; explain the corrective disposition, not a fake score.
4. **Handoff:** exact decisions, cuts or execution boundaries needed to pass.

Keep a no-findings report short without omitting metadata, author/native-session
provenance, the normalization assessment, meaningful evidence or limitations.
Plan review does not require running implementation tests or builds; inspect
the proposed verification's feasibility unless a specific uncertainty warrants
a bounded experiment. Record any such experiment and why it was needed.

Prioritize unknown scope and excessive work before detail repair. Report
coexisting problems rather than disguising them as one label. A blocked plan
cannot be accepted. Do not infer a planning defect merely because later code
violated clear guidance. Return concrete corrections to the planner/caller;
the review's `accept` verdict refers only to the recorded plan revision.
