# xskills

Four skills for planning, implementing, and reviewing code changes with Claude
Code, Codex, and OpenCode. Plans settle consequential engineering decisions and
divide large requests into bounded execution assignments. Reviews independently
inspect the implemented code.

| Skill | Purpose |
| --- | --- |
| `xplan` | Research a request and write implementation-ready execution plans, or a task brief for small work. |
| `xwork` | Implement a plan or explicit brief, verify the result, and commit the code and work log locally. |
| `xreview` | Independently review the implemented code, tests, and conformance to the plan. |
| `xauto` | Coordinate planning, implementation, independent review, and corrections through committed completion. |

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
xwork .agents/plans/2026-11-09-001-logical-operators.md
xreview .agents/work/2026-11-09-001-logical-operators.md
```

Or delegate the complete workflow:

```text
xauto Add short-circuit logical operators using the existing compiler stages.
```

`xreview` takes the work log of the change to review. `xplan` and
standalone `xreview` write artifacts without committing by default. `xwork`
commits task-owned code and its log locally; `xauto` also commits plan and
review records. The skills do not push changes automatically.

Records live under `.agents/plans/`, `.agents/work/`, and `.agents/reviews/`,
sharing a task ID of the form `YYYY-MM-DD-NNN-slug`. Shared designs belong in
`.agents/designs/` when needed. The [workflow contract](skills/xauto/references/workflow.md) defines
handoffs, revision anchors, and commit ownership.

## Planning standard

Work size and explanation detail are separate judgments. Small tasks use briefs;
large requests need smaller execution assignments and, when useful, shared design.
Consequential decisions must be resolved before implementation.

The [normalization rubric](skills/xplan/references/normalization.md) starts
with an **experimental 600–1,500-word** execution-plan band. It is an inspection
signal, not a validated optimum or an effort estimate. Padding and removing
necessary constraints do not repair a plan. The bundled
[metrics helper](skills/xplan/scripts/plan_metrics.py) measures saved plans
and can use explicitly curated project references.
