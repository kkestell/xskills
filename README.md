# xskills

Four skills for planning, implementing, and reviewing code changes with Claude
Code, Codex, and OpenCode. Plans settle consequential engineering decisions and
divide large requests into bounded execution assignments. Reviews independently
inspect the implemented code.

| Skill | Purpose |
| --- | --- |
| `xtask` | The entry point. Coordinate planning, implementation, independent review, and corrections through committed completion, stopping only for decisions that need the user. |
| `xplan` | Research a request and write implementation-ready execution plans, or a task brief for small work, each listing the assumptions the developer must check. |
| `xwork` | Implement a plan or brief, verify the result, and write the work log. |
| `xreview` | Independently review the implemented code, test hygiene, interface design, and conformance to the plan. |

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
  --skill xplan xwork xreview xtask --agent claude-code codex opencode
```

Implementation and committing workflows require a Git repository. `xtask` requires child-session
or subagent support in the host; it stops if neither is available.

## Use

Start a task with `xtask` and the request:

```text
xtask Add short-circuit logical operators using the existing compiler stages.
```

`xtask` runs each stage in a fresh worker. Before work starts, it shows you
the planner's **Check your assumptions** list in one message: each decision or
unconfirmed assumption, led by the consequence you will notice, with `xtask`'s
recommendation to keep the planner's choice or change it, and why. You answer
only the entries you want changed. After that it stops only for plan findings,
blocking review findings, and questions of intent or scope. Ask it to stop
after every stage if you want to step through.

Each stage also runs on its own, given the request or exact artifact path:

```text
xplan Add short-circuit logical operators using the existing compiler stages.
xwork .agents/plans/2026-11-09-001-logical-operators.md
xreview .agents/work/2026-11-09-001-logical-operators.md
```

`xreview` takes the work log of the change to review. `xplan`, `xwork` and
`xreview` leave everything uncommitted. `xtask` runs every stage in one checkout
and makes one local commit per plan, holding its code, tests and records, once
its review is accepted. The
skills do not push changes.

Records live under `.agents/plans/`, `.agents/work/`, and `.agents/reviews/`,
sharing a task ID of the form `YYYY-MM-DD-NNN-slug`. Each skill writes its records from the templates in
its `templates/` directory. The [workflow contract](skills/xtask/references/workflow.md) defines
handoffs and commits.

## Planning standard

Small tasks use briefs, short plan files of at most 400 words. A plan is at
most 1,500 words; larger requests are split into execution units, each with its
own plan. Consequential decisions are resolved before implementation.
