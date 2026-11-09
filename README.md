# xskills

Four skills for planning, implementing, and reviewing code changes with Claude
Code, Codex, and OpenCode. Plans settle consequential engineering decisions and
divide large requests into bounded execution assignments. Reviews assess the
amount of work separately from the detail describing it.

| Skill | Purpose |
| --- | --- |
| `xplan` | Research a request and write implementation-ready execution plans, or a task brief for small work. |
| `xwork` | Implement a plan or explicit brief, verify the result, and commit the code and work log locally. |
| `xreview` | Normalize a plan's assigned work and exposition from supplied material, or independently review the actual implementation. |
| `xauto` | Coordinate planning, independent reviews, implementation, and corrections through committed completion. |

## Install

Requires Node.js 22.20+ and npm. From a clone, run:

```sh
git clone https://github.com/kkestell/xskills.git
cd xskills
make install
```

`make install` uses [Vercel's skills CLI](https://github.com/vercel-labs/skills)
to install all four skills globally for **Claude Code, Codex, and OpenCode**.
It installs from the local checkout; pull updates and run it again to refresh
the installed skills. The suite shares references, so install all four together.

To install directly from GitHub without cloning or Make:

```sh
npx --yes skills add kkestell/xskills --global --yes \
  --skill xplan xwork xreview xauto --agent claude-code codex opencode
```

Python 3.9+ is needed for the bundled plan-metrics helper. Implementation and
committing workflows require a Git repository. `xauto` requires child-session
or subagent support in the host; it stops if neither is available.

## Use

Ask your agent to invoke a skill with the request or exact artifact path:

```text
xplan Add short-circuit logical operators using the existing compiler stages.
xreview plan .agents/plans/2026-11-09-001-logical-operators.md
xwork .agents/plans/2026-11-09-001-logical-operators.md
xreview work .agents/work/2026-11-09-001-logical-operators.md
```

Or delegate the complete workflow:

```text
xauto Add short-circuit logical operators using the existing compiler stages.
```

`xreview` requires an explicit `plan` or `work` mode and a target. `xplan` and
standalone `xreview` write artifacts without committing by default. `xwork`
commits task-owned code and its log locally; `xauto` also commits planning and
review records. The skills do not push changes automatically.

Records live under `.agents/plans/`, `.agents/work/`,
`.agents/reviews/plans/`, and `.agents/reviews/work/`, sharing a task ID of the
form `YYYY-MM-DD-NNN-slug`. Shared designs belong in `.agents/designs/` when
needed. The [workflow contract](skills/xauto/references/workflow.md) defines
handoffs, revision anchors, and commit ownership.

## Planning standard

Work size and explanation detail are separate judgments. Small tasks use briefs;
large requests need smaller execution assignments and, when useful, shared design.
Consequential decisions must be resolved before implementation.
That remains the planner's responsibility: `xreview plan` is not a design,
correctness, test-feasibility or readiness review. `xreview work` still reviews
the actual implementation for correctness.

The [normalization rubric](skills/xreview/references/normalization.md) starts
with an **experimental 600–1,500-word** execution-plan band. It is an inspection
signal, not a validated optimum or an effort estimate. Padding and removing
necessary constraints do not repair a plan. The bundled
[metrics helper](skills/xreview/scripts/plan_metrics.py) measures saved plans
and can use explicitly curated project references.

Plan assessment uses one [self-contained prompt](skills/xreview/references/plan-assessment.md)
over the plan, supplied request/shared guidance and precomputed metrics, treated
as data. It returns separate work-size and exposition judgments, concise evidence
and actionable notes, with one or more of `skip-plan`, `expand-guidance`,
`split-work`, `trim-detail`, `clarify-scope`, or exclusive `accept`. Loading files,
measuring length and saving reports happen outside that tool-free assessment.
The existing instruction-based harness cannot enforce a single isolated model
call or disable tools; it does not implement an automatic normalization gate.
Luna's earlier prompt experiments did not validate such a gate. Historical
implementation-token usage is still under investigation, with no adopted thresholds.

Run local metric and instruction-contract checks (no model calls):

```sh
python3 -m unittest discover -s skills/xreview/tests -v
```
