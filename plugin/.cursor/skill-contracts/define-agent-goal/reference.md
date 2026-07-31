# define-agent-goal (end-user notes)

Turn a rough task into an agent **Goal** before autonomous or long-running work. The agent drafts; you approve the Goal; execution waits for a later **execute now**.

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

1. **Sections 1 to 6 Goal**: outcome, verification (with **3 to 5 checkbox success criteria**), constraints, boundaries, iteration policy, stopping condition
2. **Section 7 Helper agent goals**: only when the task implies parallelism (cross-repo, audits, explore+implement, etc.); each helper includes iteration and stopping
3. **Two-step handshake**: approve the Goal first; say **execute now** later to run
4. **Copyable intake template**: prefilled for similar future tasks

## Two-step handshake

| You say | Agent should |
|---------|----------------|
| (nothing yet / edits) | Keep refining the Goal; do not start the task |
| "approved" / "LGTM" on the Goal | Acknowledge; **do not** start the task |
| "execute now" (later message) | Begin the underlying work under the approved Goal |
| "skip the Goal, just do it" | Only then may skip Goal definition and execute (explicit) |

## Saving goals

After Goal delivery, the agent **always** writes:

`<host-repo-root>/agent-goals/<kebab-slug>.md`

- Folder is at the **repository root**, never under `docs/`
- Ensure `/agent-goals/` is in `.gitignore`; never commit Goals
- Host-repo = the repo the Goal's work targets (multi-root: do not pick an arbitrary first folder)
- Legacy `docs/agent-goals/` is wrong; do not use it

Example slug: goal title "Reduce flaky tests in service-a" → `agent-goals/reduce-flaky-tests-service-a.md`

## Gotchas

| Gotcha | What to do |
|--------|------------|
| Agent starts working after "approved" | Remind it: wait for **execute now** |
| Vague "make it better" tasks | Expect clarifying questions; do not accept unbounded boundaries |
| Parallel work without section 7 | Ask for section 7 mini-goals (with iteration and stopping) |
| Section 7 on a simple single-file fix | Ask to omit helpers; single-agent is fine |
| Wrote under `docs/agent-goals/` | Move to root `agent-goals/` and gitignore it |
| Software implementation | Approve Goal, then **execute now** or `/requirement-to-implementation` |
| IAM / tool permissions | Use `agent-risk-review` for access design; Goal covers task outcome, not IAM |
| Large read-only audits | Use `scoped-audit` to run; use `define-agent-goal` to design delegation first if needed |

## Maintainer docs

Behavioral eval: [eval/cases.md](eval/cases.md). Ship gate sections: **A, S**.
