---
name: define-agent-goal
description: >-
  Turn a rough task into a six-part agent Goal (outcome, verification,
  constraints, boundaries, iteration policy, stopping condition) so an agent
  can run with minimal babysitting. Plan-only, no execution in the same turn.
  Use for Goal, delegate, run without babysitting, or before long autonomous
  work. Pair with requirement-to-implementation for code delivery afterward.
---

# Define agent goal

## Role

You turn a rough task into a **Goal** an AI agent can follow: what done means, how to verify it, what must not break, where the agent may operate, how to retry, and when to ask the human. This skill **defines** the Goal; it does not execute the task in the same turn.

## When to use

Use when the user wants delegation design before autonomous or long-running agent work: code, ops, inbox cleanup, error backlog triage, or cross-repo chores. For implementing a software requirement after the Goal is approved, use `requirement-to-implementation` in a **follow-up** turn.

## Workflow

Run phases in order. Do not publish the final Goal until Phase 3 passes. **Do not execute** the task, edit code, or run destructive commands when delivering the Goal unless the user explicitly says to skip Goal definition and execute now.

### Phase 0: Intake

1. Extract the **task** from the user message (what they want done).
2. If the task is missing, ask one focused question before proceeding.
3. Produce a one-paragraph **task summary** restating what the agent would accomplish and for whom.

### Phase 1: Discovery

Ask structured clarifying questions (use `AskQuestion` when available). Cover only gaps not already answered:

- What must be true when complete (outcome)?
- How will success be verified (tests, metrics, manual checks)?
- What must not regress (constraints)?
- Which files, tools, MCP servers, accounts, or environments are in scope (boundaries)?
- How should the agent retry failed attempts (iteration policy)?
- When should the agent stop and ask the human (stopping condition)?

Aim for **4 to 6** non-obvious questions. Skip questions the user already answered.

### Phase 2: Draft Goal

Fill the **Goal template** below. Keep the deliverable **one page** (~500 to 900 words): prefer tables and bullets over long prose.

While drafting:

- Default **narrow** boundaries; expand only with user confirmation.
- Do not grant vague autonomy (e.g. "fix everything", "full access").
- Redact secrets, tokens, credentials, PII, and PHI in examples.

### Phase 3: Clarify gate (hard stop)

Before finalizing:

- If outcome, **verification**, or **stopping condition** is ambiguous, **stop** and ask.
- If boundaries are unknown, **stop** and ask.
- Do not publish the final Goal with TBD sections unless the user explicitly defers a decision; then return to Phase 1 on the next turn.

### Phase 4: Deliver

1. Post the final Goal in chat using the template headings (sections 1 to 6).
2. If the host workspace has a `docs/` directory, offer to save as `docs/agent-goals/<kebab-slug>.md`. Write the file only after the user confirms.
3. Suggest a follow-up: approve the Goal, then run the task in a new turn or invoke `requirement-to-implementation` for software work.

## Goal template

Use this structure for the final deliverable:

```markdown
# Agent goal: <short title>

## 1. Outcome
What must be true when complete.

## 2. Verification
How to test or prove the outcome (commands, checks, observability).

## 3. Constraints
What must not regress (behavior, SLOs, data, compliance).

## 4. Boundaries
Files, directories, tools, MCP servers, accounts, environments the agent may use.

## 5. Iteration policy
How to retry (max attempts, order of fixes, when to stop retrying).

## 6. Stopping condition
When to pause and ask the human (blockers, spend limits, ambiguity, production impact).
```

Populate every section with concrete content. Use "TBD" only when the user explicitly defers; then do not treat the Goal as final.

## Safety

- Do not execute the task, edit code, or run destructive commands in the same turn as delivering the Goal unless the user explicitly says to skip Goal definition and execute now.
- Never imply a native Codex Goals API or product feature; this is a portable Goal document for Cursor agents.
- No secrets, tokens, or PII in the Goal body.

## Distinction from other commands

- **`requirement-to-implementation`**: approved requirement → codebase plan → implement → document. This skill defines **how** an agent may run; RTI **builds** software after a separate approval.
- **`agent-risk-review`**: permission brief for tools/accounts (allowed / forbidden). This skill defines **task** outcome and verification, not IAM policy.
- **`scoped-audit`**: large read-heavy cataloging with verify-before-report. This skill is task-agnostic delegation design, not a repo-wide audit orchestrator.

## Guardrails

- Clarify a vague task before finalizing, fill all six Goal sections, and keep boundaries narrow instead of granting vague autonomy.
- Define the Goal without executing it: do not edit code or run destructive commands in the same turn without explicit consent to skip Goal definition.
- Do not claim a native Goals product feature; this is a portable Goal document.
