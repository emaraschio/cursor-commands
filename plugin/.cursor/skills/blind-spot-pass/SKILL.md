---
name: blind-spot-pass
description: >-
  Run a pre-build blind spot pass before the agent builds anything. Treat the
  user's prompt as the map and the real project as the territory: classify gaps
  across known knowns, known unknowns, unknown knowns, and unknown unknowns;
  ask 5 to 10 high-leverage interview questions; log assumptions in
  implementation notes on follow-up builds. Plan-only, no execution in the same
  turn. Use for blind spot pass, find unknowns, assumption interview, or
  before writing, coding, or speccing when the prompt may be incomplete.
user-invocable: false
---
# Blind spot pass

## Role

You run a **blind spot pass** before building. The user gives a rough plan, goal, or prompt; you treat it as the **map** and the real project as the **territory**. You classify what is known and unknown across four quadrants, then ask the highest-leverage interview questions so building does not start on hidden assumptions. This skill is **plan-only**: it delivers the pass and questions, it does not build in the same turn.

## When to use

Use before writing, coding, product specs, or any build where the prompt may be incomplete. Run this when the user wants to **find unknowns** or surface unstated context before the agent acts. For a greenfield fog map with parallel tracks, use `pathfinder`. For a six-part delegation contract, use `define-agent-goal`. For a runnable prompt, use `structure-prompt`.

## Workflow

Run phases in order. Do not deliver the pass until Phase 3. **Do not execute** the task, scaffold code, or run destructive commands when delivering the pass unless the user explicitly says to skip the pass and build now.

### Phase 0: Intake

1. Extract the **rough plan** (goal, constraints, audience, deliverables, links, notes) from the message.
2. If the plan is missing, ask one focused question before proceeding.
3. Produce a one-sentence restatement of what the user wants built and for whom.

### Phase 1: Discovery

Ask structured clarifying questions (use `AskQuestion` when available) only for gaps the plan leaves open:

- Who is the audience and what does success look like for them?
- What is explicitly out of scope?
- What constraints (time, stack, compliance, dependencies) are implied but unstated?
- What decisions would most change structure, architecture, scope, workflow, or quality if answered differently?

Aim for **4 to 6** high-signal questions before drafting. Skip anything the user already answered.

### Phase 2: Draft the pass

Fill the **pass template** below. Keep it to about one page: prefer tables and bullets over prose. While drafting:

- Treat the user's prompt as the **map**; infer the **territory** (real constraints, stakeholders, edge cases) that the map may omit.
- Populate **all four quadrants**. Mark a quadrant as thin only when the context genuinely has nothing for it, and say so.
- Rank **5 to 10 interview questions** by leverage: prefer questions whose answers would materially change structure, architecture, audience, scope, workflow, or quality.
- Do not invent facts to fill a quadrant. Label inference as inference; keep genuine unknowns in unknown unknowns.

### Phase 3: Deliver

1. Post the blind spot pass in chat using the template headings (sections 1 to 5).
2. If the host workspace has a `docs/` directory, offer to save it as `docs/blind-spot-passes/<kebab-slug>.md`. Write the file only after the user confirms.
3. Suggest the follow-up: answer the interview questions, then run `define-agent-goal`, `requirement-to-implementation`, or explicit build instructions in a new turn.

### Follow-up builds (after the pass)

When the user continues building in a later turn, maintain an **Implementation notes** section in your responses or in the host doc. Log each material assumption you make (what you assumed, why, and what would change if wrong). Update the log as assumptions shift.

## Pass template

Use this structure for the final deliverable:

```markdown
# Blind spot pass: <short title>

## 1. Known knowns
What the user clearly specified. One line each.

## 2. Known unknowns
Questions the user raised but did not answer.

## 3. Unknown knowns
Likely unstated context the user probably holds (audience, constraints, prior art, politics).

## 4. Unknown unknowns
Risks, edge cases, dependencies, or decisions not yet considered.

## 5. High-leverage questions
5 to 10 interview questions, ranked by how much the answer would change
structure, architecture, audience, scope, workflow, or quality.
```

Populate every section with concrete content. Leave a quadrant explicitly thin only when the context genuinely has nothing for it, and say so.

## Safety

- Do not execute the task, scaffold code, or run destructive commands in the same turn as delivering the pass unless the user explicitly says to skip the pass and build now.
- Redact secrets, tokens, credentials, PII, and PHI in both the plan you echo and the pass you produce.
- Do not invent facts to fill a quadrant. An inference belongs in unknown knowns with a question that confirms it.
- Never imply a native Cursor product feature; this is a portable planning document for Cursor agents.

## Distinction from other commands

- **`pathfinder`**: greenfield **fog map** with decision frontiers, next-move tags per unknown, parallel tracks, and next three actions. Blind spot pass uses the **four-quadrant** model and a pre-build **interview**, not parallel project tracks.
- **`define-agent-goal`**: six-part **delegation contract** (outcome, verification, constraints, boundaries, iteration, stopping) for one autonomous task. Blind spot pass surfaces **what the prompt omitted** before any Goal is written.
- **`structure-prompt`**: produces a **runnable prompt**. Blind spot pass produces a planning artifact and interview questions, not a finished prompt.
- **`scoped-audit`**: read-heavy cataloging of an existing surface. Blind spot pass is forward-looking assumption surfacing before building something new.

## Guardrails

- Classify all four quadrants explicitly; do not skip unknown knowns or unknown unknowns, and mark thin quadrants when context is sparse.
- Ask 5 to 10 high-leverage interview questions ranked by impact on structure, architecture, audience, scope, workflow, or quality; avoid trivia that would not change the output.
- Pass before build: deliver the pass and stop; do not edit code, scaffold, or run destructive commands in the same turn unless the user explicitly says to skip the pass and build now.
- On follow-up builds, keep an Implementation notes section logging material assumptions as work proceeds.
