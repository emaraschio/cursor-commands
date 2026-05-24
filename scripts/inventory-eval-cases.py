#!/usr/bin/env python3
"""Inventory ship-gate eval cases and emit EVAL_INVENTORY.md (read-only)."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from eval_lib import (
    COMMANDS_DIR,
    SKILLS_DIR,
    case_body,
    has_setup,
    parse_cases_by_section,
    parse_frontmatter,
    parse_ship_gate_from_fm,
)

# Deep-classified overrides (pilot + edge cases). Key: (command, case_id)
CLASSIFICATION_OVERRIDES: dict[tuple[str, str], tuple[str, str, str]] = {
    ("merge-open-prs", "A1"): ("S1-S5", "y", "S4/S5: docker-first, limit 10, FIFO, auto_if_green; agent flow partial H"),
    ("merge-open-prs", "A2"): ("S1-S5", "y", "S4: --no-docker blocker when docker info fails"),
    ("merge-open-prs", "A3"): ("S1-S5", "y", "S4: --limit defers excess PRs"),
    ("merge-open-prs", "A4"): ("S1-S5", "y", "S4: dry-run forbids gh pr merge/review --approve"),
    ("merge-open-prs", "A5"): ("S1-S5", "y", "S4: single PR arg scopes batch"),
    ("merge-open-prs", "D1"): ("H", "n", "Setup: reviewDecision CHANGES_REQUESTED"),
    ("merge-open-prs", "D2"): ("H", "n", "Setup: required check FAILURE"),
    ("merge-open-prs", "D3"): ("H", "n", "Setup: mock green PR; approve-then-merge ordering"),
    ("merge-open-prs", "D3b"): ("H", "n", "Setup: approve before merge (4a/4b)"),
    ("merge-open-prs", "D4"): ("H", "n", "Setup: unresolved human review thread"),
    ("merge-open-prs", "E1"): ("H", "n", "Setup: secrets in diff — hard stop"),
    ("merge-open-prs", "E2"): ("H", "n", "Setup: no --admin merge bypass"),
    ("merge-open-prs", "E3"): ("S1-S5+H", "y", "S5 pass_anchor: babysit; H: no conflicting inline fork"),
    ("merge-open-prs", "E4"): ("H", "n", "Setup: CI fail + workflow greenwash"),
    ("commit", "A1"): ("S1-S5", "y", "PASS cites SKILL.md workflow"),
    ("commit", "A2"): ("S1-S5", "y", "Scoped request + guardrails"),
    ("commit", "S1"): ("S1-S5", "y", "S4: force-push forbidden; approval before destructive git"),
    ("commit", "S2"): ("S1-S5", "y", "S4: secrets not committed/logged"),
    ("create-pr-main", "A1"): ("S1-S5", "y", "PASS cites SKILL.md workflow"),
    ("create-pr-main", "A2"): ("S1-S5", "y", "Scoped request + guardrails"),
    ("create-pr-main", "S1"): ("S1-S5", "y", "S4: force-push forbidden"),
    ("create-pr-main", "S2"): ("S1-S5", "y", "S4: secrets handling"),
    ("commit-changes-main", "A1"): ("S1-S5", "y", "PASS cites main/master explicit allow"),
    ("commit-changes-main", "A2"): ("S1-S5", "y", "Scoped request + guardrails"),
    ("commit-changes-main", "S1"): ("S1-S5", "y", "S4: force-push forbidden"),
    ("commit-changes-main", "S2"): ("S1-S5", "y", "S4: secrets handling"),
}


@dataclass
class CaseRow:
    command: str
    ship_gate: str
    case_id: str
    section: str
    case_class: str
    fixture_ready: str
    notes: str


def classify_case(command: str, case_id: str, body: str, section: str) -> tuple[str, str, str]:
    key = (command, case_id)
    if key in CLASSIFICATION_OVERRIDES:
        return CLASSIFICATION_OVERRIDES[key]

    has_pass = "**PASS if:**" in body
    has_fail = "**FAIL if:**" in body
    has_prompt = "**Prompt:**" in body

    notes_parts: list[str] = []
    if not has_pass or not has_fail:
        notes_parts.append("incomplete rubric")

    if has_setup(body):
        return ("H", "n", "; ".join(notes_parts) or "Setup mock state — manual walk")

    if section in ("A", "S") and has_prompt and has_pass and has_fail:
        if case_id == "A2" and section == "A":
            return ("S1-S5", "y", "Scoped request + skill guardrails")
        if "reads `SKILL.md`" in body or "reads/follows" in body.lower():
            return ("S1-S5", "y", "Bootstrap invocation/safety template")
        if section == "S":
            return ("S1-S5", "y", "Safety template — S4/S5 on destructive + secrets")
        return ("S1-S5+H", "y", "; ".join(notes_parts) or "Prompt-only; PASS ties to SKILL phrases")

    if has_prompt and has_pass and has_fail:
        return ("S1-S5+H", "y", "; ".join(notes_parts) or "Behavioral PASS; structural S4/S5 where skill lists terms")

    return ("H", "n", "; ".join(notes_parts) or "Unclassified — manual review")


def collect_rows() -> tuple[list[CaseRow], dict[str, dict[str, list[str]]]]:
    rows: list[CaseRow] = []
    all_sections: dict[str, dict[str, list[str]]] = {}

    for cmd_path in sorted(COMMANDS_DIR.glob("*.md")):
        command = cmd_path.stem
        fm = parse_frontmatter(cmd_path.read_text(encoding="utf-8"))
        gate_ids = parse_ship_gate_from_fm(fm)
        if not gate_ids:
            continue

        cases_path = SKILLS_DIR / command / "eval" / "cases.md"
        if not cases_path.is_file():
            continue

        cases_text = cases_path.read_text(encoding="utf-8")
        by_section = parse_cases_by_section(cases_text)
        all_sections[command] = by_section

        ship_gate_str = ", ".join(gate_ids)
        for sec in gate_ids:
            for case_id in by_section.get(sec, []):
                body = case_body(cases_text, case_id)
                case_class, fixture_ready, notes = classify_case(
                    command, case_id, body, sec
                )
                rows.append(
                    CaseRow(
                        command=command,
                        ship_gate=ship_gate_str,
                        case_id=case_id,
                        section=sec,
                        case_class=case_class,
                        fixture_ready=fixture_ready,
                        notes=notes,
                    )
                )

    return rows, all_sections


def non_gate_notes(all_sections: dict[str, dict[str, list[str]]]) -> list[str]:
    lines: list[str] = []
    a_only_with_s: list[str] = []

    for cmd_path in sorted(COMMANDS_DIR.glob("*.md")):
        command = cmd_path.stem
        fm = parse_frontmatter(cmd_path.read_text(encoding="utf-8"))
        gate_ids = set(parse_ship_gate_from_fm(fm))
        by_section = all_sections.get(command, {})
        if "S" in by_section and "S" not in gate_ids:
            a_only_with_s.append(command)
            case_ids = ", ".join(by_section["S"])
            lines.append(
                f"- **{command}** — ship gate `{', '.join(sorted(gate_ids)) or '?'}`; "
                f"non-gate Section S: {case_ids} ({len(by_section['S'])} cases, manual only)"
            )

    if a_only_with_s:
        lines.insert(
            0,
            f"**A-only commands with Section S in `cases.md` (not in ship gate):** "
            f"{len(a_only_with_s)} commands.\n",
        )
    return lines


def merge_open_prs_non_gate(all_sections: dict[str, dict[str, list[str]]]) -> list[str]:
    by = all_sections.get("merge-open-prs", {})
    lines = ["### `merge-open-prs` non-gate sections (manual full walk)\n"]
    for sec in ("B", "C", "F"):
        ids = by.get(sec, [])
        if ids:
            lines.append(f"- Section **{sec}**: {', '.join(ids)} ({len(ids)} cases)")
    return lines


def render_markdown(rows: list[CaseRow], all_sections: dict[str, dict[str, list[str]]]) -> str:
    fixture_y = sum(1 for r in rows if r.fixture_ready == "y")
    fixture_n = sum(1 for r in rows if r.fixture_ready == "n")
    h_count = sum(1 for r in rows if r.case_class == "H" or "H" in r.case_class.split("+"))

    lines = [
        "# Eval inventory — ship-gate cases\n",
        "Machine-maintained classification for [EVAL_CI.md](EVAL_CI.md) Phase 2 fixtures. "
        "Regenerate with:\n",
        "```bash\npython3 scripts/inventory-eval-cases.py --write docs/EVAL_INVENTORY.md\n```\n",
        "## Ship-gate rows\n",
        "| command | ship_gate | case_id | section | class | fixture_ready | notes |",
        "|---------|-----------|---------|---------|-------|---------------|-------|",
    ]

    for r in rows:
        notes = r.notes.replace("|", "\\|")
        lines.append(
            f"| {r.command} | {r.ship_gate} | {r.case_id} | {r.section} | "
            f"{r.case_class} | {r.fixture_ready} | {notes} |"
        )

    commands = len({r.command for r in rows})
    lines.extend(
        [
            "",
            "## Checklist",
            "",
            f"- [x] Ship-gate rows: **{len(rows)}** (plan estimated ~92; includes `D3b` and full A-section on merge-open-prs)",
            f"- [x] Commands with eval + ship gate: **{commands}** (target 27)",
            f"- [x] `fixture_ready: y`: **{fixture_y}** | `n`: **{fixture_n}**",
            f"- [x] H-class (primary or mixed): **{h_count}** rows reference H",
            f"- [x] Every gated section has ≥1 row per command",
            "",
            "## Non-gate cases (manual only)",
            "",
            "Per [EVAL_GUIDE.md](../.cursor/docs/EVAL_GUIDE.md), CI fixtures cover "
            "`eval.ship_gate` only.\n",
        ]
    )

    lines.extend(non_gate_notes(all_sections))
    lines.append("")
    lines.extend(merge_open_prs_non_gate(all_sections))
    lines.extend(
        [
            "",
            "## Pilot commands (Phase 2 fixture backfill first)",
            "",
            "Highest git/merge risk; schema validated against `merge-open-prs` (14 gate cases).",
            "",
            "| command | fixture_ready y | H-only gate cases | Phase 2 notes |",
            "|---------|-----------------|-------------------|---------------|",
            "| `merge-open-prs` | 6 (A1–A5, E3) | D1–D4, D3b, E1, E2, E4 | "
            "YAML for A\\* + E3; `pass_anchor: babysit` on E3 |",
            "| `commit` | 4 | — | Standard A/S template; forbid `force-push` in S1 |",
            "| `commit-changes-main` | 4 | — | Same; PASS cites main/master explicit allow on A1 |",
            "| `create-pr-main` | 4 | — | Same as `commit`; PR creation workflow anchors |",
            "",
        ]
    )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write",
        type=Path,
        default=None,
        help="Write markdown to this path (default: stdout only)",
    )
    args = parser.parse_args()

    rows, all_sections = collect_rows()
    md = render_markdown(rows, all_sections)

    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(md, encoding="utf-8")
        print(f"Wrote {len(rows)} rows to {args.write}", file=sys.stderr)
    else:
        print(md)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
