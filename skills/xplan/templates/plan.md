# <Plan title: the change, stated as an outcome>

- Task: `<YYYY-MM-DD-NNN-slug>`
- Status: <draft | ready | blocked | superseded>
- Source HEAD: `<full commit ID>`
- Author: <role/name>, <harness>, <model/effort>; coordinator ID `<id>`;
  native conversation ID `<id or "unavailable: reason">`
- Shared design: <`.agents/designs/ID.md`, or "none">
- Dependencies: <task IDs this plan needs first, or "none">

## Outcome and boundaries

<The request, or a faithful brief of it. Observable behavior when done,
constraints that bind the implementation, and explicit non-goals.>

## Current system

<Relevant paths and symbols, the data and control flow the change touches, and
existing behavior to preserve. Cite what you inspected.>

## Design

<Who owns each responsibility; contracts, data shapes, transitions, ordering and
failure behavior. State each decision and, for a consequential one, the
alternative rejected and why.>

## Implementation sequence

1. <Concrete change tied to paths/symbols, and the behavior that results.>
2. <...>

## Verification

- <Acceptance case, regression or failure path, and where its test belongs.>
- Commands: `<runnable check>`
- Manual: <required manual check, or omit this line>

## Handoff

<Readiness, work-size assessment, detail assessment, and plan_metrics.py result.
A blocked plan names the exact decision or evidence it needs.>
