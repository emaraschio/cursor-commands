# define-agent-goal (end-user notes)

Turn a rough task into an agent **Goal** before autonomous or long-running work. The agent drafts; you approve; execution waits.

## When to use

- Before delegating multi-step work (code, ops, triage, cross-repo chores)
- When you want **human-reviewed autonomy** instead of "just go fix it"
- Before chaining into `requirement-to-implementation` for software delivery

## Quick start

Invoke `/define-agent-goal` with nothing (agent will ask) or paste the intake block:

```markdown
**Task:** [what you want done]
**Context:** [files, docs, requirements, links, tickets]
**Constraints:** [scope limits, style rules, deadlines, things to avoid]
**Definition of done:** [what success looks like]
```

When all four fields are clear, the agent should skip redundant questions and draft the Goal.

## What you get back

1. **Sections 1 to 6 Goal** :  outcome, verification (with **3 to 5 checkbox success criteria**), constraints, boundaries, iteration policy, stopping condition
2. **Section 7 Helper agent goals** :  only when the task implies parallelism (cross-repo, audits, explore+implement, etc.)
3. **Approval handshake** :  agent will not execute until you confirm
4. **Copyable intake template** :  prefilled for similar future tasks

## Saving goals (opt-in)

The Goal in chat is authoritative. Saving to disk is **optional**:

- The agent may **offer** `docs/agent-goals/<kebab-slug>.md` if your project has a `docs/` folder
- The file is written **only after you explicitly say yes** to save (approving the Goal is not enough)
- If you never confirm, nothing is written

Example slug: goal title "Reduce flaky tests in service-a" → `docs/agent-goals/reduce-flaky-tests-service-a.md`

## Gotchas

| Gotcha | What to do |
|--------|------------|
| Agent starts working in the same turn | Remind it: plan-only until Goal is approved |
| Vague "make it better" tasks | Expect clarifying questions; do not accept unbounded boundaries |
| Parallel work without section 7 | Task likely needs helpers; ask for section 7 mini-goals per repo/slice/role |
| Auto-saved file under `docs/` | Should not happen; save requires explicit confirm |
| Software implementation | Approve Goal first, then `/requirement-to-implementation` or a new turn |
| IAM / tool permissions | Use `agent-risk-review` for access design; Goal covers task outcome, not IAM |
| Large read-only audits | Use `scoped-audit` to run; use `define-agent-goal` to design delegation first if needed |

## Maintainer docs

Behavioral eval: [eval/cases.md](eval/cases.md). Ship gate sections: **A, S**.
