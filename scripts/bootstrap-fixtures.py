#!/usr/bin/env python3
"""Generate eval/fixtures.yaml for ship-gate cases (non-Setup)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from eval_lib import (
    SKILLS_DIR,
    case_body,
    extract_pass_text,
    has_setup,
    iter_ship_gate_cases,
    parse_ship_gate,
)

PILOT_COMMANDS = frozenset(
    {"commit", "commit-changes-main", "create-pr-main", "merge-open-prs"}
)

REQUIREMENT_TO_IMPLEMENTATION_CASES: dict[str, dict] = {
    "A1": {
        "rubric": "required",
        "pass_anchor": "SKILL.md",
        "pass_must_reference_skill": True,
        "skill_required": ["Intake", "Phase"],
    },
    "S1": {
        "rubric": "required",
        "skill_required": ["approved", "Do not implement"],
        "pass_must_reference_skill": True,
    },
}

MERGE_OPEN_PRS_CASES: dict[str, dict] = {
    "A1": {
        "rubric": "required",
        "skill_required": ["Docker", "limit", "FIFO", "auto_if_green"],
        "pass_must_reference_skill": True,
    },
    "A2": {
        "rubric": "required",
        "skill_required": ["--no-docker", "blocker"],
        "pass_must_reference_skill": True,
    },
    "A3": {
        "rubric": "required",
        "skill_required": ["--limit", "deferred"],
        "pass_must_reference_skill": True,
    },
    "A4": {
        "rubric": "required",
        "skill_required": ["--dry-run", "gh pr merge"],
        "pass_must_reference_skill": True,
    },
    "A5": {
        "rubric": "required",
        "skill_required": ["FIFO"],
        "pass_must_reference_skill": True,
    },
    "E3": {
        "rubric": "required",
        "skill_required": ["babysit"],
        "pass_anchor": "babysit",
        "pass_must_reference_skill": True,
    },
}


def bootstrap_entry(command: str, case_id: str, section: str, skill_md: str, pass_text: str) -> dict:
    if command == "merge-open-prs" and case_id in MERGE_OPEN_PRS_CASES:
        return dict(MERGE_OPEN_PRS_CASES[case_id])
    if command == "requirement-to-implementation" and case_id in REQUIREMENT_TO_IMPLEMENTATION_CASES:
        return dict(REQUIREMENT_TO_IMPLEMENTATION_CASES[case_id])

    if section == "S" and case_id == "S1":
        return {
            "rubric": "required",
            "skill_forbidden": ["force-push"],
            "pass_must_reference_skill": False,
        }
    if section == "S" and case_id == "S2":
        entry: dict = {"rubric": "required", "pass_must_reference_skill": False}
        if "secret" in skill_md.lower():
            entry["skill_required"] = ["secret"]
        return entry
    if case_id == "A1":
        reqs: list[str] = []
        lower_skill = skill_md.lower()
        if "conventional" in lower_skill:
            reqs.append("conventional")
        if command == "commit-changes-main":
            if "main" in lower_skill or "master" in lower_skill:
                reqs.append("main")
        if command == "create-pr-main":
            if "pull request" in lower_skill:
                reqs.append("pull request")
        if command == "seo-audit":
            reqs.append("SEO")
        if command == "fix-git-issues":
            reqs.append("git")
        entry: dict = {
            "rubric": "required",
            "pass_anchor": "SKILL.md",
            "pass_must_reference_skill": True,
        }
        if reqs:
            entry["skill_required"] = reqs
        return entry
    if case_id == "A2":
        return {"rubric": "required", "pass_must_reference_skill": False}

    return {"rubric": "required", "pass_must_reference_skill": False}


def render_fixtures(command: str, gate_ids: list[str], cases: dict[str, dict]) -> str:
    gate_str = ", ".join(gate_ids)
    lines = [
        "schema_version: 1",
        f"command: {command}",
        f"ship_gate: [{gate_str}]",
        "cases:",
    ]
    for case_id in sorted(cases.keys(), key=lambda x: (x[0], len(x), x)):
        lines.append(f"  {case_id}:")
        entry = cases[case_id]
        for key, val in entry.items():
            if isinstance(val, bool):
                lines.append(f"    {key}: {'true' if val else 'false'}")
            elif isinstance(val, list):
                lines.append(f"    {key}:")
                for item in val:
                    lines.append(f'      - "{item}"')
            else:
                lines.append(f'    {key}: "{val}"')
    return "\n".join(lines) + "\n"


def bootstrap_command(command: str, overwrite: bool = False) -> bool:
    from eval_lib import COMMANDS_DIR

    cmd_path = COMMANDS_DIR / f"{command}.md"
    if not cmd_path.is_file():
        print(f"skip {command}: no command file", file=sys.stderr)
        return False

    gate_ids = parse_ship_gate(cmd_path.read_text(encoding="utf-8"))
    if not gate_ids:
        print(f"skip {command}: no ship_gate", file=sys.stderr)
        return False

    out_path = SKILLS_DIR / command / "eval" / "fixtures.yaml"
    if out_path.exists() and not overwrite and command in PILOT_COMMANDS:
        print(f"skip {command}: fixtures exist (pilot)", file=sys.stderr)
        return False

    skill_md = (SKILLS_DIR / command / "SKILL.md").read_text(encoding="utf-8")
    cases_text = (SKILLS_DIR / command / "eval" / "cases.md").read_text(encoding="utf-8")

    from eval_lib import parse_cases_by_section

    by_section = parse_cases_by_section(cases_text)
    case_entries: dict[str, dict] = {}

    for sec in gate_ids:
        for case_id in by_section.get(sec, []):
            body = case_body(cases_text, case_id)
            if has_setup(body):
                continue
            pass_text = extract_pass_text(body)
            case_entries[case_id] = bootstrap_entry(
                command, case_id, sec, skill_md, pass_text
            )

    if not case_entries:
        print(f"skip {command}: no fixture cases", file=sys.stderr)
        return False

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        render_fixtures(command, gate_ids, case_entries),
        encoding="utf-8",
    )
    print(f"wrote {out_path} ({len(case_entries)} cases)", file=sys.stderr)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("commands", nargs="*", help="Command names (default: all)")
    parser.add_argument("--all", action="store_true", help="All commands with ship_gate")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    if args.all:
        names = [c for c, g, _, _ in iter_ship_gate_cases() if g]
    elif args.commands:
        names = args.commands
    else:
        parser.error("specify command names or --all")

    ok = 0
    for name in names:
        if bootstrap_command(name, overwrite=args.overwrite):
            ok += 1
    print(f"bootstrapped {ok}/{len(names)} commands", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
