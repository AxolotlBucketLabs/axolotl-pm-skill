---
name: axolotl-pm-skill
description: "Develop, review, document, test, and package Axolotl-PM or PocketMine-MP plugins, virions, and reusable PHP libraries. Use when a task mentions Axolotl-PM, PocketMine plugins, plugin.yml, virion.yml, DevTools, Poggit, or a PMMP library."
---

# Axolotl-PM Skill

Use this skill for work that extends a Bedrock server through an Axolotl-PM/PocketMine plugin or through a reusable library/virion.

The goal is not to imitate one historical maintainer. Use the current repository as the primary source of truth, then apply Axolotl-PM conventions and only then use broader PMMP/Poggit patterns.

## Route the task

- Treat the work as a **plugin** task when it has `plugin.yml`, a `PluginBase` entry point, commands, permissions, listeners, tasks, resources, or server lifecycle behavior.
- Treat it as a **virion/library** task when it has `virion.yml`, an `antigen`, Composer packaging, a reusable public API, or a consumer plugin that shades/injects it.
- If both are present, keep the reusable library boundary separate from the host-plugin adapter and read both relevant references below.

Read only the references relevant to the task:

- [project-discovery.md](references/project-discovery.md) before making assumptions about an unfamiliar repository or Axolotl-PM version.
- [style-and-naming.md](references/style-and-naming.md) when creating or reviewing PHP code, comments, names, or class boundaries.
- [plugin-workflow.md](references/plugin-workflow.md) for plugin lifecycle, commands, events, config, resources, and permissions.
- [virion-workflow.md](references/virion-workflow.md) for library API, `virion.yml`, shading, dependencies, and consumer integration.
- [quality-and-security-rules.md](references/quality-and-security-rules.md) when implementing or reviewing runtime, namespace, dependency, command, data, SQL, protocol, security, or performance behavior.
- [devtools-workflow.md](references/devtools-workflow.md) when a project needs Axolotl-PM folder loading, virion sharing, PHAR packaging, extraction, or DevTools-backed CI.
- [writing-style.md](references/writing-style.md) when writing README files, changelogs, release notes, comments, issues, or other prose for humans.
- [readme-release.md](references/readme-release.md) when writing documentation, CI, packaging, compatibility claims, or release artifacts.
- [repository-publishing.md](references/repository-publishing.md) when creating, publishing, or auditing a GitHub repository's metadata, topics, homepage, or home-page features.
- [public-release-review.md](references/public-release-review.md) only when preparing a public submission, marketplace release, or Poggit-style acceptance review.

## Non-negotiable discovery rules

1. Inspect the target repository before coding. At minimum, look for `composer.json`, `composer.lock`, `plugin.yml`, `virion.yml`, `devtools.yml`, `.poggit.yml`, `README*`, `.github/workflows`, `src/`, `resources/`, and tests.
2. Do not assume an Axolotl-PM API is identical to an upstream PMMP API. Confirm the class, method signature, namespace, and behavior from the locked dependency or the checked-out source.
3. Prefer the repository's existing convention over a generic template. Preserve namespace layout, lifecycle registration, error handling, configuration style, and build commands unless the task asks for a migration.
4. Separate facts from compatibility assumptions. Record the PHP version, plugin API floor, exact development revision, tested revisions, and unverified range whenever those details affect the result.

## Implementation defaults

- Prefer `declare(strict_types=1)` and typed parameters, return types, and properties for new code, subject to the target's actual PHP/API constraints.
- Use lower camel case for PHP methods and variables, descriptive domain names for public APIs, and short loop variables only where their scope makes the meaning obvious.
- Keep plugin entry points focused on bootstrap and lifecycle wiring. Move substantial command, listener, task, storage, and service logic into focused classes when the repository's scale warrants it.
- Keep a virion reusable and host-agnostic. The host plugin should provide lifecycle context and server integration; consumers should not need to know the library's internal implementation.
- Document public APIs, lifecycle requirements, non-obvious invariants, compatibility limitations, and packaging requirements. Do not add comments that merely restate obvious code.
- Do not make `final`, Composer, PHPUnit, a particular brace style, or a particular factory/singleton pattern universal rules. Adopt them when the target repository or API design supports them.
- Apply the security and performance gates in [quality-and-security-rules.md](references/quality-and-security-rules.md) to new runtime code and reviews; do not treat historical Poggit acceptance policy as a substitute for repository-specific requirements.
- Apply the human-facing prose rules in [writing-style.md](references/writing-style.md) to README files, changelogs, release notes, comments, issues, and explanations. Do not apply those prose rules to code or machine-readable data.
- When writing a README or release workflow, apply the badge and license rules in [readme-release.md](references/readme-release.md).

## Verification before completion

Before saying the work is complete:

- run the repository's available lint, static-analysis, unit/integration-test, and build commands;
- if no test command exists, perform the strongest available PHP lint and a clean package/build smoke test;
- verify manifests, namespaces, dependency declarations, resources, permissions, and README examples against the implementation;
- inspect the produced PHAR or consumer artifact when packaging is involved;
- distinguish "works on the fixture/pinned revision" from "compatible with every Axolotl-PM release in the declared range".
