#!/usr/bin/env python3
"""Validate the structure, routing links, and CI policy of this Codex skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


EXPECTED_NAME = "axolotl-pm-skill"
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|FIXME|REPLACE_ME|YOUR_[A-Z_]+)\b")
REFERENCE_RE = re.compile(r"\]\((references/[^)]+)\)")
ACTION_USE_RE = re.compile(
    r"^\s*uses:\s*([^\s]+)@([^\s#]+)(?:\s+#\s*(.*?))?\s*$"
)
FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
FULL_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
VERSION_COMMENT_RE = re.compile(r"^v[0-9]+(?:\.[0-9]+){0,2}(?:[-+][0-9A-Za-z.-]+)?$")
MUTABLE_ACTION_REFS = {"HEAD", "develop", "dev", "latest", "main", "master"}


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def validate_workflows(skill_dir: Path) -> None:
    workflow_dir = skill_dir / ".github" / "workflows"
    if not workflow_dir.is_dir():
        fail(".github/workflows is missing")

    workflows = sorted((*workflow_dir.glob("*.yml"), *workflow_dir.glob("*.yaml")))
    if not workflows:
        fail(".github/workflows has no workflow files")

    for workflow in workflows:
        for line_number, line in enumerate(workflow.read_text(encoding="utf-8").splitlines(), 1):
            match = ACTION_USE_RE.match(line)
            if match is None:
                continue

            action, reference, version_comment = match.groups()
            if action.startswith("./"):
                continue
            if reference in MUTABLE_ACTION_REFS:
                fail(f"{workflow.name}:{line_number} uses mutable action ref {reference}")
            if FULL_SHA_RE.fullmatch(reference) is None:
                fail(f"{workflow.name}:{line_number} must pin {action} to a full commit SHA")
            if version_comment is None or VERSION_COMMENT_RE.fullmatch(version_comment.strip()) is None:
                fail(f"{workflow.name}:{line_number} needs a version comment beside {action}")


def validate_dependabot(skill_dir: Path) -> None:
    dependabot_file = skill_dir / ".github" / "dependabot.yml"
    if not dependabot_file.is_file():
        fail(".github/dependabot.yml is missing")

    dependabot_text = dependabot_file.read_text(encoding="utf-8")
    if re.search(r"^\s*-\s*package-ecosystem:\s*github-actions\s*$", dependabot_text, re.MULTILINE) is None:
        fail(".github/dependabot.yml must update GitHub Actions")
    if re.search(r"^\s*directory:\s*/\s*$", dependabot_text, re.MULTILINE) is None:
        fail(".github/dependabot.yml must monitor the repository root")


def validate_markdown_fences(skill_dir: Path) -> None:
    markdown_files = [skill_dir / "README.md", skill_dir / "SKILL.md"]
    markdown_files.extend(sorted((skill_dir / "references").glob("*.md")))

    for markdown_file in markdown_files:
        open_fence: tuple[str, int, int] | None = None
        for line_number, line in enumerate(markdown_file.read_text(encoding="utf-8").splitlines(), 1):
            match = FENCE_RE.match(line)
            if match is None:
                continue

            fence, suffix = match.groups()
            marker = fence[0]
            length = len(fence)
            if open_fence is None:
                open_fence = (marker, length, line_number)
                continue

            open_marker, open_length, open_line = open_fence
            if marker != open_marker or length < open_length or suffix.strip():
                continue
            open_fence = None

        if open_fence is not None:
            marker, length, line_number = open_fence
            fail(
                f"{markdown_file.name}:{line_number} has an unclosed "
                f"{length}-character {marker} Markdown fence"
            )


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

    validate_markdown_fences(skill_dir)
    validate_workflows(skill_dir)
    validate_dependabot(skill_dir)

    print(f"Skill is valid: {EXPECTED_NAME}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
