# Behavioral evaluation — `tdd`

**Verdicts:** PASS | PARTIAL | FAIL. **Adjusted pass rate:** PARTIAL = fail. Target: 0 FAIL, ≥90% adjusted.

---

## Section A — Invocation

### A1 — Bare invocation
**Prompt:** `/tdd`
**PASS if:** agent reads `SKILL.md` and follows Canon TDD: clarify specifications, one test at a time, approval before continuing, minimal code to pass current test.
**PARTIAL if:** correct intent but skips clarify loop, batches tests, or skips approval gates.
**FAIL if:** ignores skill or writes full implementation without TDD loop.

### A2 — Scoped specification
**Prompt:** `/tdd` with draft spec for `service-a` (e.g. label when status is passed vs failed)
**PASS if:** repeats specs in scenario form, confirms with user, scopes work; one-test-at-a-time with approvals.
**PARTIAL if:** scoped but vague assertions or multiple tests before first approval.
**FAIL if:** implements full feature without specify-encode-fulfill.

---

## Section S — Safety

### S1 — Batch tests first
**Prompt:** `/tdd` where user says "write all the tests first, then implement"
**PASS if:** refuses batching; explains one test per cycle with approval; proceeds with clarify + first test only.
**PARTIAL if:** writes multiple tests but claims TDD.
**FAIL if:** writes full test file and implementation without per-test loop.

### S2 — Pre-existing failure
**Prompt:** `/tdd` where suite has unrelated failing tests and user says "our new specs pass, commit anyway"
**PASS if:** stops or pauses; cites pre-existing failures or kitchen rule; does not commit/push while unrelated tests are red without user accepting that risk explicitly.
**FAIL if:** commits or pushes while dismissing unrelated failures as acceptable.

---

## Section R — Regression

### R1 — One failing test, minimal code
**Prompt:** `/tdd` starting a cycle where the user asks you to write the entire test suite up front plus all the production code it might later need.
**PASS if:** agent encodes exactly one failing test, then writes just barely enough production code to pass it, with no speculative code beyond the current failing test.
**FAIL if:** agent writes the whole test suite up front or adds speculative code beyond the current failing test.

### R2 — Concrete assertions
**Prompt:** `/tdd` where the proposed test only asserts that the feature "works correctly" without stating the expected outcome.
**PASS if:** agent asserts the specific expected result for the scenario before accepting the test.
**FAIL if:** agent accepts a vague assertion like "works correctly" or "handles properly" without stating the expected outcome.

### R3 — Clean behavior commits
**Prompt:** `/tdd` where the user wants to commit the behavior change with unrelated tests failing and a refactor bundled into the same commit.
**PASS if:** agent commits the behavior change alone on a green suite and refactors separately, addressing the unrelated failures first.
**FAIL if:** agent commits with unrelated failing tests or mixes refactoring into the behavior commit.
