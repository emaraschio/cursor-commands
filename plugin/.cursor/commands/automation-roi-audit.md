---
name: automation-roi-audit
version: 2
description: Interview a business function's workflows, label Human-only / AI-assisted / AI-owned steps, pick highest-ROI automation, warn on AI theater, recommend one one-week test
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/automation-roi-audit/eval/cases.md
  ship_gate: [A, S, R]
---

## Overview

Act as an AI operations consultant: intake business + function + workflow list, interview how each process runs, label steps, prioritize by money/margin/output, warn on traps, recommend one narrow one-week test. Audit only; does not implement the automation in the same turn. Full workflow: `.cursor/skill-contracts/automation-roi-audit/SKILL.md` (user install: `~/.cursor/skill-contracts/automation-roi-audit/SKILL.md`).

## Defaults

| Setting | Default |
|---------|---------|
| Profile | `generic` (sales / marketing / ops / customer support / content / finance) |
| Software-team profile | Optional; eng / product / platform / support / content / finance-adjacent |
| Interview | Required until each workflow has enough detail to label steps |
| Deliverable | Chat report; optional save under `docs/automation-roi-audits/` after confirm |
| Execution | Recommend only; no implementation in the same turn |
| Examples | Generic names only (`business-a`, `workflow-1`) |

## Steps

1. **Read** `.cursor/skill-contracts/automation-roi-audit/SKILL.md` for the full agent contract; if that file is missing, read `~/.cursor/skill-contracts/automation-roi-audit/SKILL.md`.
2. **Execute** phases in order (Intake → Interview gate → Deconstruct and label → ROI / warnings / one-week test → Deliver); do not skip the interview gate or implement the recommended automation.
3. **Report** the audit in chat; offer optional docs save only when the host has `docs/` and the user confirms.

## Anti-patterns

- **Interview before analyzing.** Trigger: user pastes a thin workflow list (names or one-liners only). Wrong: labeling steps and picking ROI immediately. Correct: interview until each workflow has enough process detail, then analyze. Reason: labels and ROI from thin lists invent process and ship bad bets.
- **Reject AI theater as the primary bet.** Trigger: a suggested automation that does not improve money, margin, or output. Wrong: ranking it as the highest-ROI opportunity. Correct: call it AI theater and pick a bet tied to money, margin, or output. Reason: theater burns time without changing the business.
- **Warn on rebuild-cheap-SaaS and distraction traps.** Trigger: the idea is a meeting-summary toy, a distraction, or rebuilding something like Calendly for pocket change. Wrong: recommending it as the one-week test. Correct: warn explicitly and steer to a narrower proprietary or high-leverage test. Reason: those traps look like progress and displace real ROI work.
- **Prefer proprietary edge.** Trigger: ranking automation opportunities. Wrong: generic wrapper automations ranked over process-specific leverage. Correct: tie the bet to proprietary data or domain workflow when available. Reason: proprietary edge is harder to copy and more likely to move money, margin, or output.
- **Write docs only after confirmation.** Trigger: host has a `docs/` directory. Wrong: writing `docs/automation-roi-audits/...` unprompted. Correct: offer the path and write only after the user confirms. Reason: unsolicited docs clutter the host workspace.
- **Do not implement the automation in the same turn.** Trigger: finishing the audit with a clear one-week test. Wrong: scaffolding code, PRs, or a follow-on skill without a new ask. Correct: deliver the report (and optional confirmed docs save) and stop. Reason: this skill audits; building skips review of the recommendation.

## Examples

- `/automation-roi-audit` with a business description, `content`, and a list of editorial workflows
- `/automation-roi-audit` with `--profile software-team` (or equivalent ask) for eng/product workflows
- `/automation-roi-audit` when the user only pastes workflow names (expect interview first)

## Maintainers

Behavioral eval: `.cursor/skill-contracts/automation-roi-audit/eval/cases.md`. Ship gate sections: **A, S, R** before changing `SKILL.md` or this command.
