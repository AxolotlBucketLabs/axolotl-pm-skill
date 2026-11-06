# Axolotl-PM Skill

[![CI](https://github.com/AxolotlBucketLabs/axolotl-pm-skill/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/AxolotlBucketLabs/axolotl-pm-skill/actions/workflows/validate.yml) [![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![Discord](https://img.shields.io/discord/1568295845374206052?label=discord&logo=discord&color=5865F2)](https://discord.gg/Pk4FrNvHnM)

Axolotl-PM Skill helps Codex develop, review, document, test, and package Axolotl-PM or PocketMine-MP plugins, virions, and reusable PHP libraries.

It keeps the repository's own conventions as the primary source of truth, then applies Axolotl-PM and PocketMine-MP practices where they are relevant. The skill is designed for the full project lifecycle, from discovery and implementation through quality checks, DevTools packaging, documentation, and release review.

## What it covers

- Plugin lifecycle, commands, permissions, events, resources, configuration, and localization.
- Virion and reusable-library boundaries, public APIs, Composer packaging, shading, and consumer integration.
- PHP style, naming, static analysis, YAML validation, security, performance, and reproducible builds.
- AxolotlBucketLabs DevTools workflows for folder loading, shared virions, PHAR packaging, extraction, and CI.
- README, badge, license, compatibility, changelog, and release guidance.
- Repository identity, commit messages, version mapping, release notes, README scope, date hygiene, and CI freshness.
- Human-facing writing rules for natural README, changelog, release note, comment, and issue prose.
- GitHub Flavored Markdown structure for inline code, fenced code, tables, alerts, links, and collapsed details.
- Maintainer posture that keeps changes focused, evidence-based, proportional, and aligned with the project's direction.
- GitHub repository metadata, homepage and topic setup, discoverability checks, and UI-only feature settings.
- Official Axolotl-PM documentation, source, community, PHP runtime, API version, and Bedrock protocol references.
- Conditional use of related skills such as Find Skills, Humanizer, and Graphify when the task benefits from them.

## Layout

```text
axolotl-pm-skill/
├── .github/
│   ├── dependabot.yml
│   └── workflows/
│       └── validate.yml
├── AGENTS.md
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── devtools-workflow.md
│   ├── official-sources.md
│   ├── plugin-workflow.md
│   ├── project-discovery.md
│   ├── public-release-review.md
│   ├── quality-and-security-rules.md
│   ├── readme-release.md
│   ├── repository-lifecycle.md
│   ├── repository-publishing.md
│   ├── style-and-naming.md
│   ├── virion-workflow.md
│   └── writing-style.md
├── scripts/
│   └── validate_skill.py
└── tests/
    └── test_validate_skill.py
```

## Installation

Install this repository as a Codex skill using the Codex skill installer, with `AxolotlBucketLabs/axolotl-pm-skill` as the GitHub source. For a manual installation, place the repository folder at:

```text
~/.codex/skills/axolotl-pm-skill
```

Keep the folder name and the `name` value in `SKILL.md` aligned so automatic skill discovery can identify it consistently.

## Development

Run the repository validator after editing the skill:

```sh
python scripts/validate_skill.py
```

The official Codex `skill-creator` validator should also be run before publishing a new revision. The local validator checks the frontmatter, skill name, required UI metadata, linked references, scaffold placeholders, Markdown fence boundaries, prose punctuation, checklist bullets, research-only context leaks, workflow action pins, and GitHub Actions Dependabot configuration without requiring third-party packages.

Run the validator regression tests with:

```sh
python -m unittest discover --start-directory tests --pattern "test_*.py"
```

When changing a reference, update the routing link in `SKILL.md` if its activation condition changes. Keep detailed, mode-specific instructions in references rather than expanding the entrypoint with duplicated material.

## License

This project is released under the MIT License.
