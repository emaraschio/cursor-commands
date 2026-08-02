---
name: gauntlet-loop
description: >-
  Beat a real-world quality bar with a Gauntlet Loop: take a GOAL and a
  REAL-WORLD EQUIVALENT, decompose into independent parts, assign specialist
  builders, and gate each part behind a separate fresh-context critic that
  inspects the artifact and compares it against the reference. Pass only if
  better than the reference; otherwise return the largest specific gap.
  Builders never evaluate their own work. Use when the user invokes
  /gauntlet-loop or asks to run a gauntlet, builder/critic loop, or beat a
  real example.
disable-model-invocation: true
user-invocable: false
---
# Gauntlet loop

## Role

You run a **Gauntlet Loop**: raise quality by competing against a real example, not against a vague "make it better". You decompose the GOAL, assign specialist builders, and let **critics alone** decide when each part passes. A part passes only when the critic judges the generated artifact **better than the REAL-WORLD EQUIVALENT**. Otherwise the critic returns the **largest specific gap** and the builder iterates. Do **not** let builders evaluate their own work.

## When to use

Use when the user invokes `/gauntlet-loop`, asks to beat a real-world equivalent, run a builder/critic gauntlet, or set a concrete quality bar via an excellent existing example. For a six-part Goal before autonomous work without a reference bar, use `define-agent-goal`. For post-build judgment autopsy, use `decision-audit`. For thinning instructions from a bare run, use `instruction-ablation`.

## Gauntlet charter

> Goal plus a real example as the bar. Decompose. Specialist builders. Fresh-context critics inspect the artifact and compare. Blind when possible. Pass only if better. Else largest specific gap. Cap and stall. Builders never grade themselves.

## Workflow

Run phases in order.

### Phase 0: Intake

1. Require two fields:
   - **GOAL**: the finished result to produce
   - **REAL-WORLD EQUIVALENT**: name, URL, attachment, or description of an excellent existing example that sets the quality bar
2. If either field is missing, ask one focused question per gap. Do not invent the reference or a vague substitute bar.
3. Optionally accept: iteration cap (default **5** rounds per part), constraints, scope limits, and how to access the reference (files, URL, demo).
4. If the work is production-destructive and constraints lack explicit consent for that blast radius, stop and ask before building.

### Phase 1: Decompose

1. Break the GOAL into **independent parts** (or the fewest weakly coupled parts you can).
2. For each part, state a **part quality bar**: what "better than the reference" means for that slice (feel, fidelity, completeness, polish).
3. Prefer parts that can build and critique in parallel. Note true dependencies and order those sequentially.
4. Publish the part list before building so the user can correct the split.

### Phase 2: Build

1. Assign each part to a **specialist builder** (subagent when available; otherwise a focused builder prompt scoped to that part only).
2. Run independent builders in parallel when the harness allows.
3. Builders produce the artifact for their part. They do **not** declare pass/fail against the reference.

### Phase 3: Critique

For every part with a new or revised artifact:

1. Assign a **separate critic** with **fresh context**. Prefer a subagent. If subagents are unavailable, run a **fresh-context simulation**: a critic prompt that receives only the artifact, the reference material (or both unlabeled), and the part quality bar. No build transcript, no builder rationalizations.
2. Record **critic mode** per part: `subagent` or `fresh-context simulation`.
3. The critic must **inspect the generated artifact itself** (read files, run/play when feasible, view the UI). Do not pass from a builder summary alone.
4. The critic compares the artifact **directly** against the REAL-WORLD EQUIVALENT (whole or the part-relevant slice).
5. **Blind side-by-side when possible**: present both without saying which is generated. If blind comparison is not feasible (e.g. the reference is a live product the critic already knows), state that the comparison was **not blind**.
6. Verdict:
   - **Pass** only if the generated artifact is **better than the reference** on the part quality bar.
   - Otherwise **fail**: identify the **largest specific gap** (one concrete, observable deficit versus the reference) and return the part to the builder.

### Phase 4: Loop

1. On fail, send the largest specific gap back to the builder for that part only. Retest with a new critic pass (fresh context again).
2. Respect the **iteration cap** (default 5 rounds per part, or the intake override).
3. **Stall rule**: if the same gap repeats twice with no measurable improvement, stop looping that part, report the stall, and continue other parts.
4. Do not invent a pass to escape the cap. Do not soft-pass on "close enough".

### Phase 5: Deliver

Post the report using the template below. List every part with rounds, critic mode, blind status, final verdict, and remaining gaps. End with a halt line for stalled or capped parts that need a human call.

## Deliverable template

```markdown
# Gauntlet loop

## 1. Intake
- GOAL: ...
- REAL-WORLD EQUIVALENT: ...
- Iteration cap: N (default 5)

## 2. Parts

| Part | Quality bar (vs reference) | Dependencies |
|------|----------------------------|--------------|
| ... | ... | none / part-X |

## 3. Results

| Part | Rounds | Critic mode | Blind? | Verdict | Largest remaining gap |
|------|--------|-------------|--------|---------|------------------------|
| ... | k/N | subagent / fresh-context simulation | yes / no (why) | pass / fail (capped) / fail (stalled) | ... or none |

## 4. Outstanding
Parts that did not pass: gaps, recommended next move, or "all passed".

## 5. Halt
Approve outstanding parts, raise the cap, or revise the reference bar before I continue looping.
```

## Safety

- Redact secrets, tokens, credentials, PII, and PHI in intake, artifacts, and reports.
- Do not run production-destructive actions unless constraints explicitly consent.
- Do not claim a critic pass without inspecting the artifact and comparing to the reference.
- Do not fabricate blind comparison when it was not blind.

## Distinction from other commands

- **`define-agent-goal`**: forward six-part Goal before autonomous work. This skill adds a **real-world quality bar** and builder/critic adjudication.
- **`decision-audit`**: post-build choice autopsy. This skill runs **during** construction against a reference.
- **`instruction-ablation`**: thins instructions from a bare run. This skill raises artifact quality against an example.
- **`prompt-eval-debug`**: tiny eval suite for a pasted prompt. This skill gauntlets **artifacts**, not prompt wording alone.
- **`thermo-nuclear-code-quality-review`**: maintainability review of existing code. This skill is a **build-and-beat** loop, not a review-only pass.

## Guardrails

- **GOAL and REAL-WORLD EQUIVALENT required.** Ask one focused question per missing field; never invent the reference.
- **Do not let builders evaluate their own work.** Hand the artifact to a separate critic with fresh context.
- **Critic uses fresh context.** Critic receives only the artifact, the reference (or both unlabeled), and the part bar.
- **Pass only if better than the reference.** Otherwise return the largest specific gap; never soft-pass on close enough.
- **Largest specific gap, not vague feedback.** Name one concrete, observable deficit versus the reference.
- **Blind side-by-side when possible.** Unlabeled comparison when feasible; otherwise state the comparison was not blind.
- **Cap and stall, never infinite loop.** Stop at the iteration cap or when the same gap repeats twice with no improvement.
