# Normalization standard, experimental v1

## Separate the axes

The target is comparable implementation assignments at consistent detail.
`plan-assessment.md` is the self-contained assessment prompt and canonical
size/detail rubric. Plan mode uses supplied material only; this reference explains
the metric policy for input preparation and planning, not an investigation mandate.
Length measures exposition, not assigned work. No single weighted score
currently meets that goal: earlier obligation caps and words-per-obligation
rules failed historical tests. Keep inspectable evidence instead of hiding it
inside a formula.

### Work reference assignments

Use these as contrasts, not universal effort estimates:

- **Below the planning threshold:** change an existing diagnostic and add its
  regression; pass a callback through existing wrappers without introducing the
  async subsystem. A task brief can preserve the necessary constraint and check.
- **Normal execution assignment:** add one expression/operator family through
  existing parser, type checker, lowering and backend patterns, with its
  evaluation/conversion rules decided and targeted tests; or fix restored
  file/diff loading plus refresh ownership in the existing tab lifecycle.
  Several files and error/test cases can implement one coherent mechanism.
- **Needs splitting:** build an event-loop subsystem containing runnable task
  scheduling, timers and descriptor-wait integration; replace a browser UI with
  navigation, transcripts, editor, terminal and notifications. Shared architecture
  can settle their interaction, but does not make them one execution assignment.
- **Test-only normal work:** add a substantive local Git integration suite with
  fixture setup, lifecycle, failure coverage and reproducible commands. Zero
  production-code changes does not imply zero work or a trivial assignment.

Compare described responsibilities, decisions and test burden to these references.
For unfamiliar domains, use concrete project comparisons when supplied. If the
comparison is uncertain, state why and recommend a boundary rather than inventing
hours or blindly counting nouns. A complicated single algorithm may require a
shared design plus staged implementation/verification; split only where a real
bounded assignment exists, not into arbitrary word-sized chunks.

### Numerical targets for exposition

Start with **600–1,500 whitespace-separated words per execution plan**, inclusive.
This rounds the middle half (Q1 621.5, Q3 1469.75; inclusive quantiles) of the
existing 60-plan, six-repository corpus. It is a deliberately provisional
operating band, not a discovered optimum or an effort budget. Those histories
are selected workflow artifacts, not a quality-certified population, and their
distribution is not necessarily Gaussian. No normality assumption is needed.

- Below 600: consider whether this should be a brief or whether useful
  guidance is visibly missing. Do not approve solely for concision.
- Above 1,500: consider whether the assignment needs splitting, unnecessary
  detail needs trimming, or both. Do not delete constraints to hit a quota.
- Inside the band: still assess scope and exposition. An underdescribed large
  assignment can occupy 1,000 words. So can an inflated trivial change.
- The band triggers inspection, not a mechanical acceptance gate. Require
  corrections for actual size/detail defects. If only the count is outside,
  record the reference comparison and why the provisional band is mismatched;
  acceptance needs that reasoning, not an appeal to concision or comprehensiveness.
- Genuinely tiny work needs a brief; genuinely monster assignments need splitting.
  Trim detail too when excessive work and detail coexist. Adequacy for their own
  scope does not excuse them. If that repair would lose guidance, reconsider
  artifact boundaries rather than pad or discard constraints. Shared designs
  are not execution assignments and have no execution-plan word target; link
  specifically instead of duplicating.

For project adaptation, the helper reports raw historical Q1/median/Q3 but does
not automatically adopt them. A supplied, explicitly curated set of at least
**8** right-sized, sufficiently described, non-bloated reference plans activates its
floor(Q1)–ceil(Q3) word band. Eight is a modest experimental minimum for a pilot,
not statistical validation. With fewer references use the default and disclose
the sample. Reference curation is separate from assessment: consider duplicated
lineages, revisions and task-type skew before selecting the manifest. The script
deduplicates identical text; it cannot certify quality or detect all related
histories. Record the selected references and target in the review so the choice
can be revisited. Do not recompute a favorable target for each plan or equate
central historical churn with good work size.

Full word count includes snippets. The helper separately reports fenced-code
words to expose implementation dumps, not to penalize essential types/interfaces.
There is no validated code-percentage threshold. Do not collect more estimated
metrics or fit weights until a controlled test demonstrates a useful distinction.

## Guidance, not engineering certification

Plan mode can identify missing guidance visible in the supplied description and
recommend `expand-guidance`. It does not verify design decisions, prove invariants,
inspect source or validate test feasibility. Supplied shared guidance may settle
an exposition question without repetition; missing source context is not proof of
a gap. Routine coding details need no prescription. Do not invent recovery,
durability or extensibility requirements to fill a word band. Planning retains
responsibility for research and consequential decisions; work review retains its
implementation-correctness responsibility. Normalization acceptance certifies
neither of those activities.

## Status and evidence

Initial targets and exemplars draw on `scope-metric-engineering-log.md` and
`historical-calibration/{report,content-audit}.json` in the development workspace.
The prior fitted 2–4-obligation gate achieved only 11/24 action agreement;
word-density detail agreement was 6/23 against noisy model reference judgments.
Those are reasons not to ship that formula, not validated labels for these skills.
The bundled contrasts and length band remain experimental. Luna was used for
earlier prompt experiments; those did not validate an automatic normalization
gate. Historical implementation-token usage is still being investigated; there
are no established thresholds to derive from it. Report observed results
separately from aspirations; this check does not authorize new model experiments
or benchmark campaigns.
