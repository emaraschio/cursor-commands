# gauntlet-loop: behavioral evaluation

Evaluates agent behavior when following only `SKILL.md`. No code execution.

## Ship gate

Walk sections **A, S, R** before committing changes to `SKILL.md` or the slash command.

## Scoring

PASS | PARTIAL | FAIL. PARTIAL = fail. Target: 0 FAIL, ≥90% adjusted on full walk.

## Live smoke (manual IDE)

Structural CI cannot catch skipped integration, missing pride gate, or critic-mode lies. Run this once after behavior changes.

### Setup (2 minutes)

1. Create a throwaway folder `project-a/` (or use `/tmp/project-a`).
2. Add a tiny **reference pack**:
   - `reference/index.html`: a one-screen landing page with a clear headline, one paragraph, and one primary button (any clean layout).
   - Optional: one screenshot of that page.
3. Do **not** put a finished competitor page in the workspace yet; the agent should build under `project-a/generated/`.

### Prompt (paste into a clean agent chat)

```text
/gauntlet-loop

GOAL: Ship a single-page landing for project-a that feels clearer and more polished than the reference pack. Output under project-a/generated/index.html.

REAL-WORLD EQUIVALENT: the reference landing in project-a/reference/ (inspectable HTML; optional screenshot in the same folder).

Reference pack: project-a/reference/index.html (and screenshot if present).

Iteration cap: 2
BUDGET: 6 total rounds

Constraints: no production deploys; stay inside project-a/. Taste domain: UI.
```

### Expect checklist

- [ ] Asks nothing inventing a pack (pack path is given); may clarify GOAL if needed
- [ ] Publishes a short part list (e.g. layout, copy, CTA) then proceeds
- [ ] Builders do not self-pass; critic mode recorded (`subagent` or `fresh-context simulation`)
- [ ] Gaps are concrete (not "make it better"); gap ledger rows appear
- [ ] After part passes, runs an **integration critic** on the whole page vs the pack before done
- [ ] Asks **pride gate** (UI taste domain) before treating ship as approved
- [ ] Stops at cap/BUDGET with `fail (capped)` / `fail (budget)` rather than soft-passing

### Negative smoke (30 seconds)

Same chat or a new one:

```text
/gauntlet-loop
GOAL: make project-a look like a famous design system
REAL-WORLD EQUIVALENT: that famous design system
```

Expect: blocks for an inspectable **reference pack**; does not grade from memory.
