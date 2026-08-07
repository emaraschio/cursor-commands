---
name: design-agent-loop
version: 1
description: Design a reusable agent loop as a graph before running it - nodes with context, tools, expected output, and evidence, labeled transitions, retry caps, budget ceilings, approval gates, five eval cases, and one bottleneck to automate first
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/design-agent-loop/eval/cases.md
  ship_gate: [A, S, R]
---

## Overview

Design the loop, not the prompt. Intake TASK and COMPLETION CRITERIA, draw the node graph (input, plan, act, verify, retry or escalate, done), specify context / tools / expected output / evidence per node, label every transition trigger, cap retries and budget, gate irreversible nodes on human approval, keep unverifiable steps manual, design five eval cases with a scorecard, and pick one bottleneck to automate first. Two-step handshake: design only until the user says execute now, then run one test case and improve the loop. Full workflow: `.cursor/skill-contracts/design-agent-loop/SKILL.md` (user install: `~/.cursor/skill-contracts/design-agent-loop/SKILL.md`).

## Defaults

| Setting | Default |
|---------|---------|
| Required intake | `TASK` and `COMPLETION CRITERIA` |
| Graph spine | `input` to `plan` to `act` to `verify` to `retry` \| `escalate` to `done` |
| Node fields | Context, tools, expected output, evidence (all four required) |
| Max retries | `3` per retry edge |
| Budget | None beyond retry caps unless the user sets one (state it explicitly) |
| Eval cases | `5` (happy path, retry, escalate, exhaustion, malformed input) |
| Execution | Design only; one test case after an explicit `execute now` |
| Examples | Generic names only (`task-a`, `node-1`) |

## Steps

1. **Read** `.cursor/skill-contracts/design-agent-loop/SKILL.md` for the full agent contract; if that file is missing, read `~/.cursor/skill-contracts/design-agent-loop/SKILL.md`.
2. **Execute** phases in order (Intake → Graph draft → Node specification → Transitions → Controls → Eval design → Bottleneck → Deliver and halt); do not skip the repetition check and do not run the loop before an explicit `execute now`.
3. **Report** the loop in chat using the deliverable template, ending with the two-step handshake; on a later `execute now`, run exactly one eval case and propose loop revisions.

## Anti-patterns

- **TASK and completion criteria required.** Trigger: user asks for a loop with a vague task or no definition of done. Wrong: designing a graph against "make it good". Correct: ask one focused question per missing field before drawing anything. Reason: a graph built on an invented bar verifies nothing real.
- **Design the graph before running anything.** Trigger: the task looks small enough to just do. Wrong: executing the task while claiming to design its loop. Correct: design only, then halt for approval. Reason: running the work skips the review that makes the loop reusable.
- **Every node names its evidence.** Trigger: writing a node that "checks" or "reviews" something. Wrong: a verify node whose proof is "output looks correct". Correct: name an observable signal (exit code, diff, test result, schema match, row count) or fold the node in / mark it manual. Reason: a node without observable evidence cannot fail, so it cannot verify.
- **Name the trigger on every transition.** Trigger: drawing edges between nodes. Wrong: unlabeled arrows, or "if it fails" with no definition of failure. Correct: state the firing condition per edge; retry and escalate get distinct, non-overlapping triggers. Reason: unlabeled edges make the loop untestable and hide infinite retries.
- **Bound the loop with retries and a budget.** Trigger: adding a retry edge. Wrong: retry until it works. Correct: cap retries (default 3), set a wall-clock / token / spend ceiling with exhaustion behavior, or state explicitly that none exists. Reason: uncapped loops burn budget and never escalate.
- **Gate irreversible nodes on human approval.** Trigger: a node that writes to production, sends to customers, pays, deletes, merges, or deploys. Wrong: putting it inside an automatic retry path. Correct: require human approval before the node runs, including during the test run. Reason: a retry loop driving irreversible actions multiplies the blast radius.
- **Keep unverifiable steps manual.** Trigger: a step whose success cannot be observed. Wrong: inventing a verify node so the graph looks complete. Correct: mark it a manual carve-out and say why. Reason: fake verification is worse than none because it manufactures false confidence.
- **Automate one bottleneck, not the whole pipeline.** Trigger: a graph where every node could be automated. Wrong: automating all of them in the first pass. Correct: pick the single node costing the most human time with the clearest evidence; leave the rest manual. Reason: automating everything at once makes failures impossible to attribute.
- **Match evals to volume, judgment to one-offs.** Trigger: a loop that will run twice. Wrong: demanding a full eval suite before anything ships. Correct: build the suite for high-volume loops; keep a manual checklist for one-off or low-volume work and say why. Reason: formal testing that costs more than the work it guards is theater.
- **Graph approval is not permission to execute.** Trigger: user replies "looks good" or "approved" to the delivered graph. Wrong: starting the workload on that approval. Correct: acknowledge and wait for a later explicit `execute now`. Reason: approving a design is not authorizing the run it describes.
- **Run one test case, then improve the loop.** Trigger: the user says `execute now`. Wrong: running all five cases or the real workload to completion. Correct: run exactly one case, report the first node where reality diverged, propose revisions, stop. Reason: one case surfaces design flaws before they are repeated at scale.
- **Route one-shot delegation to define-agent-goal.** Trigger: work that runs once, with no verification step and no retry cycle. Wrong: drawing a plan / act / verify graph anyway. Correct: say there is no loop here and route to `define-agent-goal`. Reason: a graph for a single run adds ceremony without adding control.

## Examples

- `/design-agent-loop` with a TASK for triaging an error backlog and COMPLETION CRITERIA for a triaged issue
- `/design-agent-loop` with a TASK but no definition of done (expect one focused question first)
- `/design-agent-loop` for a one-time data migration (expect a route to `define-agent-goal`)
- `execute now` after graph approval (expect exactly one eval case, then proposed loop revisions)

## Maintainers

Behavioral eval: `.cursor/skill-contracts/design-agent-loop/eval/cases.md`. Ship gate sections: **A, S, R** before changing `SKILL.md` or this command.
