"""Shared parsing and checks for ship-gate eval CI."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
COMMANDS_DIR = ROOT / ".cursor" / "commands"
SKILLS_DIR = ROOT / ".cursor" / "skill-contracts"
INDEX_PATH = ROOT / ".cursor" / "docs" / "COMMANDS_INDEX.md"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
SECTION_RE = re.compile(r"^## Section ([A-Z])\b[^\n]*", re.MULTILINE)
CASE_RE = re.compile(r"^###\s+([A-Z]\d+b?)\s+—", re.MULTILINE)
SHIP_GATE_RE = re.compile(r"ship_gate:\s*\[([^\]]+)\]", re.IGNORECASE)
INDEX_ROW_RE = re.compile(r"^\|\s*`([^`]+)`\s*\|[^|]*\|[^|]*\|[^|]*\|\s*([^|]+)\s*\|", re.MULTILINE)

STOPWORDS = frozenset(
    {
        "the",
        "a",
        "an",
        "and",
        "or",
        "must",
        "should",
        "agent",
        "user",
        "if",
        "not",
        "for",
        "with",
        "that",
        "this",
        "when",
        "from",
    }
)

MIN_PHRASE_LEN = 4


def parse_frontmatter(text: str) -> dict[str, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    data: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip()
    return data


def parse_ship_gate_from_fm(fm: dict[str, str]) -> list[str]:
    raw = fm.get("ship_gate", "")
    if not raw:
        return []
    inner = raw.strip("[]")
    return [s.strip() for s in inner.split(",") if s.strip()]


def parse_ship_gate(command_text: str) -> list[str]:
    fm = parse_frontmatter(command_text)
    ids = parse_ship_gate_from_fm(fm)
    if ids:
        return ids
    m = SHIP_GATE_RE.search(command_text)
    if not m:
        return []
    return [s.strip() for s in m.group(1).split(",") if s.strip()]


def normalize_ship_gate_list(ids: list[str]) -> str:
    return ", ".join(sorted(ids, key=lambda x: (len(x), x)))


def parse_cases_by_section(cases_text: str) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in cases_text.splitlines():
        sm = SECTION_RE.match(line)
        if sm:
            current = sm.group(1)
            sections.setdefault(current, [])
            continue
        if current:
            cm = CASE_RE.match(line)
            if cm:
                sections[current].append(cm.group(1))
    return sections


def case_body(cases_text: str, case_id: str) -> str:
    pattern = rf"^###\s+{re.escape(case_id)}\s+—.*?(?=^###\s+|\Z)"
    m = re.search(pattern, cases_text, re.MULTILINE | re.DOTALL)
    return m.group(0) if m else ""


def parse_rubric(body: str) -> dict[str, bool]:
    return {
        "prompt": "**Prompt:**" in body,
        "pass": "**PASS if:**" in body,
        "fail": "**FAIL if:**" in body,
    }


def rubric_complete(body: str) -> bool:
    r = parse_rubric(body)
    return r["pass"] and r["fail"]


def has_setup(body: str) -> bool:
    return "**Setup:**" in body


def extract_pass_text(body: str) -> str:
    m = re.search(r"\*\*PASS if:\*\*\s*(.+?)(?=\n\*\*|\Z)", body, re.DOTALL)
    return m.group(1).strip() if m else ""


def extract_skill_phrases(skill_md: str) -> list[str]:
    phrases: list[str] = []

    for line in skill_md.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            text = stripped.lstrip("#").strip()
            if len(text) >= MIN_PHRASE_LEN:
                phrases.append(text)
        for match in re.finditer(r"\*\*([^*]+)\*\*", line):
            t = match.group(1).strip()
            if len(t) >= MIN_PHRASE_LEN:
                phrases.append(t)
        for match in re.finditer(r"`([^`]+)`", line):
            t = match.group(1).strip()
            if len(t) >= MIN_PHRASE_LEN:
                phrases.append(t)
        if "|" in line and stripped.startswith("|") and not stripped.startswith("|---"):
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            for cell in cells:
                if len(cell) >= MIN_PHRASE_LEN and not cell.startswith("-"):
                    phrases.append(cell)

    seen: set[str] = set()
    unique: list[str] = []
    for p in phrases:
        key = p.lower()
        if key not in seen:
            seen.add(key)
            unique.append(p)
    return unique


def _token_overlap(pass_text: str, phrases: list[str]) -> bool:
    pass_tokens = {
        w.lower()
        for w in re.findall(r"[a-zA-Z][a-zA-Z0-9_-]{3,}", pass_text)
        if w.lower() not in STOPWORDS
    }
    if not pass_tokens:
        return False
    for phrase in phrases:
        phrase_tokens = {
            w.lower()
            for w in re.findall(r"[a-zA-Z][a-zA-Z0-9_-]{3,}", phrase)
            if w.lower() not in STOPWORDS
        }
        if pass_tokens & phrase_tokens:
            return True
    return False


def pass_aligns(
    pass_text: str,
    skill_md: str,
    pass_anchor: str | None = None,
) -> bool:
    if pass_anchor:
        if pass_anchor.lower() in skill_md.lower():
            return True
        if pass_anchor.lower() in pass_text.lower():
            return True

    phrases = extract_skill_phrases(skill_md)
    lower_pass = pass_text.lower()
    for phrase in phrases:
        if phrase.lower() in lower_pass or lower_pass in phrase.lower():
            return True
        if phrase.lower() in skill_md.lower() and any(
            word in skill_md.lower() for word in pass_text.lower().split() if len(word) >= MIN_PHRASE_LEN
        ):
            # phrase from skill appears in PASS as substring
            if phrase.lower() in lower_pass:
                return True

    for phrase in phrases:
        if len(phrase) >= MIN_PHRASE_LEN and phrase.lower() in lower_pass:
            return True

    return _token_overlap(pass_text, phrases)


def load_fixtures(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    if not path.is_file():
        return None, "fixtures file not found"
    try:
        import yaml  # type: ignore[import-untyped]
    except ImportError:
        return _load_fixtures_simple(path)

    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as e:
        return None, f"invalid yaml: {e}"

    return _validate_fixtures_dict(data)


def _load_fixtures_simple(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    """Minimal YAML subset without PyYAML dependency."""
    text = path.read_text(encoding="utf-8")
    if "schema_version:" not in text or "cases:" not in text:
        return None, "missing schema_version or cases"
    command_m = re.search(r"^command:\s*(\S+)\s*$", text, re.MULTILINE)
    if not command_m:
        return None, "missing command field"
    cases: dict[str, dict[str, Any]] = {}
    current: str | None = None
    list_key: str | None = None
    for line in text.splitlines():
        cm = re.match(r"^  ([A-Z]\d+b?):$", line)
        if cm:
            current = cm.group(1)
            cases[current] = {}
            list_key = None
            continue
        if not current or not line.startswith("    "):
            continue
        stripped = line.strip()
        if stripped.startswith("- "):
            item = stripped[2:].strip().strip('"').strip("'")
            if list_key:
                cases[current].setdefault(list_key, [])
                lst = cases[current][list_key]
                if isinstance(lst, list):
                    lst.append(item)
            continue
        if ":" not in stripped:
            continue
        k, v = stripped.split(":", 1)
        k = k.strip()
        v = v.strip()
        list_key = None
        if not v:
            cases[current][k] = []
            list_key = k
            continue
        if v.startswith("[") and v.endswith("]"):
            inner = v[1:-1].strip()
            cases[current][k] = [
                s.strip().strip('"').strip("'")
                for s in inner.split(",")
                if s.strip()
            ]
        elif v in ("true", "false"):
            cases[current][k] = v == "true"
        else:
            cases[current][k] = v.strip('"').strip("'")
    data: dict[str, Any] = {
        "schema_version": 1,
        "command": command_m.group(1),
        "cases": cases,
    }
    return _validate_fixtures_dict(data)


def _validate_fixtures_dict(data: Any) -> tuple[dict[str, Any] | None, str | None]:
    if not isinstance(data, dict):
        return None, "fixtures root must be a mapping"
    if data.get("schema_version") != 1:
        return None, "schema_version must be 1"
    if not data.get("command"):
        return None, "missing command"
    cases = data.get("cases")
    if not isinstance(cases, dict):
        return None, "cases must be a mapping"
    return data, None


def index_ship_gate_for(command: str) -> str | None:
    if not INDEX_PATH.is_file():
        return None
    text = INDEX_PATH.read_text(encoding="utf-8")
    for m in INDEX_ROW_RE.finditer(text):
        if m.group(1) == command:
            return m.group(2).strip()
    return None


def command_has_skill_ref(command_text: str) -> bool:
    if "## Steps" not in command_text:
        return False
    steps_idx = command_text.find("## Steps")
    rest = command_text[steps_idx : steps_idx + 800]
    return "SKILL.md" in rest


def iter_ship_gate_cases(
    command_filter: str | None = None,
) -> list[tuple[str, list[str], str, dict[str, list[str]]]]:
    """Yield (command, gate_ids, cases_text, by_section) for each command."""
    results: list[tuple[str, list[str], str, dict[str, list[str]]]] = []
    for cmd_path in sorted(COMMANDS_DIR.glob("*.md")):
        command = cmd_path.stem
        if command_filter and command != command_filter:
            continue
        text = cmd_path.read_text(encoding="utf-8")
        gate_ids = parse_ship_gate(text)
        if not gate_ids:
            continue
        cases_path = SKILLS_DIR / command / "eval" / "cases.md"
        if not cases_path.is_file():
            continue
        cases_text = cases_path.read_text(encoding="utf-8")
        by_section = parse_cases_by_section(cases_text)
        results.append((command, gate_ids, cases_text, by_section))
    return results
