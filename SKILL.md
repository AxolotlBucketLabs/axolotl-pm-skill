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

## Maintainer posture

- Keep every change proportional to the demonstrated problem.
- Prefer the smallest maintainable solution that fits the existing project.
- Do not add files, abstractions, frameworks, dependencies, configuration, documentation, or comments without a current use case.
- Before adding a file, identify which workflow or consumer will use it. Avoid duplicate documentation and keep one canonical source for each fact.
- Keep README files, changelogs, comments, and release notes proportional to the project and the task.
- Write comments for intent, invariants, compatibility constraints, security decisions, or non-obvious failure behavior. Do not comment code that is already clear.
- Treat repository-local instructions, architecture, naming, workflows, and project identity as constraints. Do not replace them with a preferred template without a reason.
- Treat the user's requested implementation as a proposal to evaluate, not proof that it is the correct solution.
- Separate task context from deliverable requirements. User-provided links, names, examples, and background references inform the work but are not automatically copied into code, README files, repository metadata, comments, or release notes.
- Before carrying a prompt keyword or link into an artifact, check whether it belongs to the artifact's identity, dependency, attribution, or requested output. Otherwise keep it as context only.
- Do not repeat project names, platform names, organization names, or source links merely because the prompt contains them.
- Verify the underlying problem, current behavior, project fit, compatibility, maintenance cost, and security impact before implementing a significant change.
- Prefer investigation when the available evidence is insufficient.
- Push back respectfully when a request conflicts with evidence, project boundaries, security, licensing, or long-term maintenance.
- When pushing back, explain the concrete reason and provide the smallest practical alternative.
- Ask a focused question only when the missing information would materially change the implementation. Otherwise proceed with the best-supported assumption and state it.
- When a task touches dependencies, CI, releases, versioning, or public repository metadata, proactively run the project's documented maintenance checks.
- Prepare release notes, changelogs, artifacts, and verification evidence when the workflow requires them. Do not tag, publish, deploy, or contact external parties without the required authorization.
- Distinguish confirmed facts, reasonable inferences, unknowns, local changes, pushed changes, passing CI, released artifacts, and pending external settings.
- Communicate like a natural, respectful maintainer. Be concise for routine work and more detailed for audits, security reviews, release reviews, or incidents.
- Do not use corporate, recruitment, promotional, or template-like AI language.

## Change discipline

Use this workflow for non-trivial changes:

1. Research before editing. Inspect repository instructions, similar implementations, call sites, dependencies, tests, invariants, and compatibility boundaries. Do not edit tracked project files during the research phase unless the task is explicitly an investigation or reproduction task.
2. Prove the problem. Reproduce the bug or demonstrate the missing behavior on the current implementation. Do not implement a fix for a bug that only exists in the prompt or in an unverified assumption.
3. Compare solutions. Consider the smallest focused fix and a reasonable alternative when the change affects architecture, public APIs, compatibility, security, or release behavior. Record why the selected approach fits the repository.
4. Implement narrowly. Avoid unrelated refactors, opportunistic formatting, new abstractions, defensive checks, comments, or validation that are not required by the demonstrated problem.
5. Verify independently. Run the focused regression test or reproducer, relevant existing tests, static analysis, lint, and build checks that apply to the change. Do not treat an agent-generated report as proof.
6. Review for deletion. Inspect every new helper, wrapper, interface, guard, comment, test, and documentation block. If removing it preserves the verified behavior and project contract, remove it.
7. Report proportionally. Keep ordinary implementation and review summaries short. Include detailed evidence for audits, security work, release work, compatibility changes, and incidents.

## P0 completion gates

These gates apply before an agent presents a non-trivial change as complete.

- Do not fix a reported bug until the current behavior, failure, or missing contract has been observed in the repository or demonstrated by a reproducible example. If the baseline cannot run, say that the bug remains unverified.
- A regression test must fail against the old behavior and pass after the fix when the baseline can be executed. If it does not fail first, treat that as evidence that the test does not prove the regression yet.
- Do not delete tests, weaken assertions, loosen expected values, skip cases, alter fixtures, or change test configuration only to make a build pass. Do not mock the logic that the test is meant to verify.
- Before changing logic, inspect the relevant callers, consumers, lifecycle order, public API contract, persistence format, and version boundary. A locally reasonable condition can still violate a project invariant.
- Keep the diff proportional to the demonstrated problem. Every new helper, abstraction, validation rule, dependency, documentation file, and comment must have a current consumer or a clearly verified maintenance purpose.
- Verify the change independently with the strongest checks that apply. Report local tests, static analysis, packaging, hosted CI, runtime checks, and release state as separate evidence. Never turn an unexecuted check into a passing claim.
- Inspect the final diff for unrelated formatting, refactors, generated files, prompt context, private links, or copied wording. Remove anything that does not belong to the deliverable.
- Read the repository's pull request template before writing a pull request. Keep the title and description focused on the observed problem, the narrow change, the relevant evidence, and any real compatibility risk.

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
