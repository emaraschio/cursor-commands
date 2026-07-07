#!/usr/bin/env python3
"""Unit tests for eval_lib and fixture runner helpers."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from eval_lib import (
    extract_skill_phrases,
    has_setup,
    load_fixtures,
    parse_cases_by_section,
    pass_aligns,
    rubric_complete,
)
from importlib.machinery import SourceFileLoader

_run_mod = SourceFileLoader(
    "run_eval_fixtures",
    str(Path(__file__).resolve().parent / "run-eval-fixtures.py"),
).load_module()
run = _run_mod.run


class TestEvalLib(unittest.TestCase):
    def test_has_setup(self) -> None:
        self.assertTrue(has_setup("**Setup:** PR is draft"))
        self.assertFalse(has_setup("**Prompt:** /commit"))

    def test_rubric_complete(self) -> None:
        body = "**PASS if:** ok\n**FAIL if:** bad\n"
        self.assertTrue(rubric_complete(body))
        self.assertFalse(rubric_complete("**PASS if:** only"))

    def test_parse_cases_by_section(self) -> None:
        md = "## Section A — X\n\n### A1 — one\n**PASS if:** y\n"
        by = parse_cases_by_section(md)
        self.assertEqual(by["A"], ["A1"])

    def test_extract_skill_phrases(self) -> None:
        skill = "## Overview\n\nUse **conventional** commits and `SKILL.md`.\n"
        phrases = extract_skill_phrases(skill)
        self.assertTrue(any("conventional" in p.lower() for p in phrases))

    def test_pass_aligns_substring(self) -> None:
        skill = "## Steps\n\nRead **SKILL.md** for workflow.\n"
        pass_text = "agent reads SKILL.md and follows workflow"
        self.assertTrue(pass_aligns(pass_text, skill))

    def test_pass_aligns_anchor(self) -> None:
        skill = "## Safety\n\nFollow babysit skill.\n"
        pass_text = "mentions babysit behavior"
        self.assertTrue(pass_aligns(pass_text, skill, pass_anchor="babysit"))

    def test_pass_aligns_fails(self) -> None:
        skill = "## Overview\n\nUnrelated content only.\n"
        pass_text = "does something entirely different xyzabc"
        self.assertFalse(pass_aligns(pass_text, skill))

    def test_load_fixtures_simple(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "fixtures.yaml"
            path.write_text(
                """schema_version: 1
command: commit
ship_gate: [A, S]
cases:
  A1:
    rubric: required
    skill_required:
      - "conventional"
    pass_must_reference_skill: true
""",
                encoding="utf-8",
            )
            data, err = load_fixtures(path)
            self.assertIsNone(err)
            assert data is not None
            self.assertEqual(data["command"], "commit")
            self.assertIn("A1", data["cases"])


class TestRunFixtures(unittest.TestCase):
    def test_commit_pilot_passes_when_fixtures_present(self) -> None:
        root = Path(__file__).resolve().parents[1]
        commit_fixtures = root / ".cursor/skill-contracts/commit/eval/fixtures.yaml"
        if not commit_fixtures.is_file():
            self.skipTest("commit fixtures not backfilled yet")
        failures, _, _ = run(strict=True, command_filter="commit")
        self.assertEqual([], failures)


if __name__ == "__main__":
    unittest.main()
