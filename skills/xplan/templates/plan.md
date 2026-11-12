# <Plan title: the change, stated as an outcome>

- Task: `<YYYY-MM-DD-NNN-slug>`
- Kind: <plan | brief>
- Status: <ready | blocked | superseded>
- Source HEAD: `<full commit ID>`
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

## Check your assumptions

<Most consequential first, usually three to seven, or "None.". Once the user
has settled the list, mark each entry kept or changed, and to what.>

1. **<Consequence the user will notice.>** <The decision or assumption that
   causes it.> <The alternative given up.> <The evidence, in a sentence.>
2. <...>

## Implementation sequence

1. <Concrete change tied to paths/symbols, and the behavior that results.>
2. <...>

## Verification

- <Acceptance case, regression or failure path, and where its test belongs.>
- Commands: `<runnable check>`
- Manual: <required manual check, or omit this line>
