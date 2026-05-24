#!/usr/bin/env python3
"""Run structural ship-gate eval checks (no LLM)."""

from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from eval_lib import (
    COMMANDS_DIR,
    SKILLS_DIR,
    case_body,
    command_has_skill_ref,
    extract_pass_text,
    has_setup,
    iter_ship_gate_cases,
    load_fixtures,
    pass_aligns,
    rubric_complete,
)

ROOT = Path(__file__).resolve().parents[1]


@dataclass
class Failure:
    command: str
    case_id: str
    check_id: str
    message: str

    def line(self) -> str:
        return f"FAIL {self.command} {self.case_id} {self.check_id} {self.message}"


def check_fixture_case(
    command: str,
    case_id: str,
    case_entry: dict,
    skill_md: str,
    pass_text: str,
) -> list[Failure]:
    failures: list[Failure] = []

    for req in case_entry.get("skill_required") or []:
        if req.lower() not in skill_md.lower():
            failures.append(
                Failure(
                    command,
                    case_id,
                    "skill_required_missing",
                    f"SKILL.md missing required phrase: {req!r}",
                )
            )

    for forbidden in case_entry.get("skill_forbidden") or []:
        if forbidden.lower() in skill_md.lower():
            failures.append(
                Failure(
                    command,
                    case_id,
                    "skill_forbidden_present",
                    f"SKILL.md contains forbidden phrase: {forbidden!r}",
                )
            )

    must_align = case_entry.get("pass_must_reference_skill", False)
    if must_align and pass_text:
        anchor = case_entry.get("pass_anchor")
        if not pass_aligns(pass_text, skill_md, pass_anchor=anchor):
            failures.append(
                Failure(
                    command,
                    case_id,
                    "pass_alignment_failed",
                    "PASS line has no SKILL.md anchor (add pass_anchor in fixtures.yaml)",
                )
            )

    return failures


def run(
    strict: bool = False,
    command_filter: str | None = None,
) -> tuple[list[Failure], int, int]:
    failures: list[Failure] = []
    command_count = 0
    case_count = 0
    skill_ref_checked: set[str] = set()

    for command, gate_ids, cases_text, by_section in iter_ship_gate_cases(
        command_filter
    ):
        command_count += 1
        cmd_path = COMMANDS_DIR / f"{command}.md"
        cmd_text = cmd_path.read_text(encoding="utf-8")
        skill_path = SKILLS_DIR / command / "SKILL.md"
        skill_md = skill_path.read_text(encoding="utf-8")
        fixtures_path = SKILLS_DIR / command / "eval" / "fixtures.yaml"

        if command not in skill_ref_checked:
            skill_ref_checked.add(command)
            if not command_has_skill_ref(cmd_text):
                failures.append(
                    Failure(
                        command,
                        "-",
                        "command_no_skill_ref",
                        "## Steps must reference SKILL.md",
                    )
                )

        fixtures_data, fixtures_err = load_fixtures(fixtures_path)
        if fixtures_err and strict and fixtures_path.parent.exists():
            needs_file = any(
                not has_setup(case_body(cases_text, cid))
                for sec in gate_ids
                for cid in by_section.get(sec, [])
            )
            if needs_file:
                failures.append(
                    Failure(
                        command,
                        "-",
                        "fixtures_invalid",
                        fixtures_err,
                    )
                )

        fixture_cases: dict = {}
        if fixtures_data:
            if fixtures_data.get("command") != command:
                failures.append(
                    Failure(
                        command,
                        "-",
                        "fixtures_invalid",
                        f"command field is {fixtures_data.get('command')!r}",
                    )
                )
            raw_cases = fixtures_data.get("cases") or {}
            if isinstance(raw_cases, dict):
                fixture_cases = raw_cases

        for sec in gate_ids:
            for case_id in by_section.get(sec, []):
                case_count += 1
                body = case_body(cases_text, case_id)
                if not rubric_complete(body):
                    failures.append(
                        Failure(
                            command,
                            case_id,
                            "rubric_incomplete",
                            "missing **PASS if:** or **FAIL if:**",
                        )
                    )

                if has_setup(body):
                    continue

                entry = fixture_cases.get(case_id)
                if strict:
                    if not fixtures_path.is_file():
                        failures.append(
                            Failure(
                                command,
                                case_id,
                                "fixtures_missing",
                                "fixtures.yaml required in strict mode",
                            )
                        )
                        continue
                    if entry is None:
                        failures.append(
                            Failure(
                                command,
                                case_id,
                                "fixtures_missing",
                                f"no fixture entry for {case_id}",
                            )
                        )
                        continue

                if entry is not None:
                    failures.extend(
                        check_fixture_case(
                            command,
                            case_id,
                            entry,
                            skill_md,
                            extract_pass_text(body),
                        )
                    )

    return failures, command_count, case_count


def write_summary(path: Path, failures: list[Failure]) -> None:
    lines = [
        "## Eval fixtures",
        "",
        "| command | case_id | check_id | message |",
        "|---------|---------|----------|---------|",
    ]
    for f in failures:
        msg = f.message.replace("|", "\\|")
        lines.append(f"| {f.command} | {f.case_id} | {f.check_id} | {msg} |")
    if not failures:
        lines.append("| — | — | — | All checks passed |")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Require fixtures.yaml for every non-Setup ship-gate case",
    )
    parser.add_argument("--command", dest="command_filter", default=None)
    parser.add_argument(
        "--summary",
        type=Path,
        default=None,
        help="Write GitHub step summary (default: GITHUB_STEP_SUMMARY)",
    )
    args = parser.parse_args()

    failures, n_commands, n_cases = run(
        strict=args.strict,
        command_filter=args.command_filter,
    )

    summary_path = args.summary
    if summary_path is None:
        env_summary = os.environ.get("GITHUB_STEP_SUMMARY")
        if env_summary:
            summary_path = Path(env_summary)

    if summary_path:
        write_summary(summary_path, failures)

    if failures:
        for f in failures:
            print(f.line(), file=sys.stderr)
        return 1

    print(f"OK: {n_commands} commands, {n_cases} ship-gate cases checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
