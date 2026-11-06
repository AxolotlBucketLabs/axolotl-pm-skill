#!/usr/bin/env python3
"""Validate the structure and routing links of this Codex skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


EXPECTED_NAME = "axolotl-pm-skill"
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|FIXME|REPLACE_ME|YOUR_[A-Z_]+)\b")
REFERENCE_RE = re.compile(r"\]\((references/[^)]+)\)")


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def main() -> int:
    skill_dir = Path(__file__).resolve().parents[1]
    skill_file = skill_dir / "SKILL.md"
    ui_file = skill_dir / "agents" / "openai.yaml"

    if not skill_file.is_file():
        fail("SKILL.md is missing")
    if not ui_file.is_file():
        fail("agents/openai.yaml is missing")

    skill_text = skill_file.read_text(encoding="utf-8")
    if not skill_text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")

    frontmatter_end = skill_text.find("\n---\n", 4)
    if frontmatter_end == -1:
        fail("SKILL.md frontmatter is not closed")

    frontmatter = skill_text[4:frontmatter_end]
    name_match = re.search(r"^name:\s*([^\s]+)\s*$", frontmatter, re.MULTILINE)
    description_match = re.search(r"^description:\s*(.+?)\s*$", frontmatter, re.MULTILINE)
    if name_match is None or name_match.group(1) != EXPECTED_NAME:
        fail(f"SKILL.md name must be {EXPECTED_NAME}")
    if description_match is None or not description_match.group(1).strip('"\''):
        fail("SKILL.md description must be non-empty")
    if PLACEHOLDER_RE.search(skill_text):
        fail("SKILL.md contains an unfinished placeholder")

    ui_text = ui_file.read_text(encoding="utf-8")
    if not re.search(r'^\s*display_name:\s*["\'].+["\']\s*$', ui_text, re.MULTILINE):
        fail("agents/openai.yaml needs a quoted display_name")
    if not re.search(r'^\s*short_description:\s*["\'].{25,64}["\']\s*$', ui_text, re.MULTILINE):
        fail("agents/openai.yaml needs a quoted 25-64 character short_description")

    for reference in REFERENCE_RE.findall(skill_text):
        if not (skill_dir / reference).is_file():
            fail(f"referenced file does not exist: {reference}")

    print(f"Skill is valid: {EXPECTED_NAME}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
