# README, compatibility, and release workflow

## README shape by artifact

For a plugin, prefer a concise operator-focused README:

```text
identity and short description
features
requirements and installation
configuration
commands and permissions
integrations and compatibility
license
```

For a virion/library, prefer an API-focused README:

```text
identity and non-standalone warning
requirements
installation in a consumer build
quick-start code example
public API examples
lifecycle and cleanup
limitations/compatibility
license and asset notes
```

Use code examples that match the current method signatures. A short README is acceptable for a small plugin. A reusable library should usually include at least one complete consumer example.

## README Markdown structure

Keep the README easy to scan on GitHub. Apply the detailed prose and Markdown rules in [writing-style.md](writing-style.md), then use the following artifact-specific choices:

- Put badges near the project identity. Keep them on one or two compact lines and link each badge to a real destination.
- Put commands, permissions, configuration keys, compatibility versions, and artifact details in a table when there are several repeated entries.
- Put installation commands in a fenced `sh` block and code examples in a fenced block with the correct language tag.
- Use `<details>` for long troubleshooting sections, build logs, or optional implementation detail. Keep the summary useful without requiring the reader to expand it.
- Use a GitHub alert only for a compatibility limit, migration step, security warning, or other information that can block a successful installation or upgrade.
- If an example contains nested Markdown code fences, use a longer outer fence or a tilde fence so the inner content cannot close the outer block early.
- Do not put the whole README inside a code block. The document must remain navigable and its links, headings, tables, and examples must render normally.

## README badges and license defaults

- Put badges in a left-aligned block immediately below the project identity and short description. This keeps status information close to the project overview and wraps naturally on narrow screens.
- For a repository with GitHub Actions, add a CI badge linking to the workflow. For a repository that publishes GitHub Releases, add a release badge linking to the latest release.
- Use a license badge for the repository's actual license. Add a Discord badge only when the project has a real invite URL and server ID. Never leave a placeholder or invent a community link.
- Prefer two badge rows when needed: CI/release/license/community first, then platform, PHP, API, locale, or package metadata.
- Use MIT as the default license for new original plugin or library code when the user has not selected another license. Do not relicense copied or bundled third-party code. Preserve its original license and attribution.
- A badge must describe a verifiable state or destination. Do not add download, release, coverage, or community badges that have no corresponding artifact or service.

## Compatibility claims

Apply the PHP baseline and project default in [official-sources.md](official-sources.md#php-baseline-and-project-default).

Separate these facts:

- State the declared API floor.
- State the PHP version and extensions.
- State the exact dependency revision used by development and CI.
- State the revisions that were actually tested.
- State the revisions believed compatible but not independently tested.

Do not turn "the API constraint is `^5.0.0`" into "every Axolotl-PM 5.x release is verified". Update the README when implementation uses a newer method, changed packet behavior, extension, or resource-pack assumption.

## Build and release

Inspect the repository's existing build path first. Depending on the project, verify:

- Run `composer install` or the documented dependency setup.
- Run PHP lint and static analysis.
- Run unit or integration tests and a consumer smoke test when applicable.
- Run AxolotlBucketLabs DevTools or the repository's pinned DevTools or VirionTools build with the exact revision selected for the target.
- Inspect PHAR contents, the manifest, autoloading, shaded namespaces, and resources.
- Confirm the artifact name, version, changelog, license, and release notes.

Historical marketplace metadata can explain how an older project was built, but a new Axolotl-PM project should prefer a reproducible CI workflow when the repository supports it. Keep legacy marketplace configuration only when it is part of the requested distribution path.

## Release promotion

Use a candidate-first release process when the project publishes versioned artifacts.

- Identify the repository's source of truth for the version. Do not update several version fields independently when one manifest or release configuration already owns it.
- Build the candidate from the exact commit that is intended for release. Record the commit, artifact name, version, and relevant dependency revisions.
- Verify the candidate artifact, manifest, resources, dependencies, namespace shading, and runtime entry point before creating or moving a release tag.
- Promote the verified commit and artifact. Do not rebuild different bytes after verification and call them the same release. If a rebuild is necessary, verify it as a new candidate.
- Create a release, tag, download badge, or latest-release claim only after the corresponding GitHub state and artifact actually exist.
- Keep release notes focused on user-visible behavior, compatibility, migrations, and important fixes. Do not describe a release as stable when only a local build or an unverified CI job exists.

## Completion checklist

Before reporting completion, confirm:

- Confirm that the requested behavior is implemented.
- Confirm that the target API was checked from the actual dependency or source.
- Confirm that code and manifests agree.
- Confirm that README examples run against the current API.
- Confirm that tests, lint, static analysis, and build checks were run when available.
- Confirm that the final artifact was inspected when packaging was part of the task.
- State unsupported compatibility or untested paths explicitly.
