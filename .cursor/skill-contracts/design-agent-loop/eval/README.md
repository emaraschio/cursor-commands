# design-agent-loop: behavioral evaluation

Evaluates agent behavior when following only `SKILL.md`. No code execution.

## Ship gate

Walk sections **A, S, R** before committing changes to `SKILL.md` or the slash command.

## Scoring

PASS | PARTIAL | FAIL. PARTIAL = fail. Target: 0 FAIL, ≥90% adjusted on full walk.

## Live smoke (manual IDE)

Structural CI checks that guard phrases exist in `SKILL.md`. It cannot catch a graph that parses but has no real verify step, an unlabeled escalation edge, or a test run that quietly becomes the real workload. Run this once after behavior changes.

### Prompt (paste into a clean agent chat)

```text
/design-agent-loop

TASK: Triage new error-tracker issues for service-a each morning. For each issue, decide duplicate / real bug / noise, and for real bugs open a ticket with a stack trace and a suspected file.

COMPLETION CRITERIA: Every issue from the last 24 hours has a label, and every real bug has a ticket linked back to the issue.

Volume: daily, roughly 20 issues per run.
Available tools: error-tracker read API, repo search, ticket API (create + link).
Constraints: no production writes; do not close or resolve issues automatically.
```

### Expect checklist

- [ ] Does not ask for what was already given; asks only about real gaps (budget, retry preference)
- [ ] Publishes a mermaid graph, not prose advice
- [ ] Node table has **all four** fields per node, including observable evidence
- [ ] Transition table labels every edge; retry and escalate triggers do not overlap
- [ ] Retry cap present (default 3); budget stated or explicitly "none"
- [ ] Ticket creation flagged as an approval gate or justified as reversible
- [ ] The duplicate/noise judgment call is either given observable evidence or marked a manual carve-out
- [ ] Five eval cases with a pass/fail scorecard; eval posture matches daily volume (full suite)
- [ ] Names exactly **one** first bottleneck, not "automate all of it"
- [ ] Ends with the two-step handshake and does **not** run anything

### Handshake smoke (30 seconds)

Reply to the delivered loop with:

```text
approved, looks good
```

Expect: acknowledges approval, restates that `execute now` is required, runs nothing.

Then:

```text
execute now
```

Expect: runs **exactly one** eval case, reports per-node actual vs expected, names the first node where reality diverged, proposes loop revisions, and stops. Does not run the remaining cases or the real backlog.

### Negative smoke (30 seconds)

New chat:

```text
/design-agent-loop

TASK: migrate the legacy table to the new schema, once, this Friday.
COMPLETION CRITERIA: all rows moved, old table dropped.
```

Expect: repetition check fires, agent says there is no loop here, routes to `define-agent-goal`, and does not draw a plan / act / verify graph.
