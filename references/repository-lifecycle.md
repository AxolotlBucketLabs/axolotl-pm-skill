# Repository lifecycle

Use this reference when creating or auditing a repository, commit, pull request, version, changelog, release, README, or GitHub Actions workflow.

## Preserve the repository's identity

Use the repository's existing naming and release conventions when they are established. For a new project, choose names from the actual artifact identity, not from every keyword in the request.

- Keep the GitHub repository name, plugin name, virion name, Composer package name, namespace, and artifact name distinct when their ecosystems require different formats.
- Do not add platform, API, AI, or organization suffixes merely because they appear in the prompt. Names such as `Plugin-PM5`, `Plugin-API5`, and `Plugin-AI` need a project-specific reason.
- Preserve an upstream project's identity for a compatibility continuation when the license and maintenance policy allow it. Explain the provenance and the maintained scope in the README.
- Use a concise description that states what the artifact does. Do not repeat the prompt, advertise an unverified relationship, or call a project official without evidence.
- Set a real homepage, focused lowercase topics, and badges only when the corresponding site, topic, service, or artifact exists. A repository README URL is an acceptable fallback homepage when no project site exists.
- Check repository settings separately from local files. The GitHub home-page inclusion controls for Releases, Deployments, and Packages are not proven by a local workflow or CLI metadata response.

Do not invent a website, Discord invite, package registry, release, deployment, topic, or organization relationship to fill an empty field.

## Commit messages

Follow the repository's local commit convention first. If no convention exists, use Conventional Commits:

```text
<type>(<scope>): <imperative description>

[optional body]

[optional footer]
```

Use a small set of meaningful types:

```text
feat fix docs refactor test build ci chore perf revert
```

Keep the subject short, preferably under 50 characters and no more than 72. Use lowercase after the colon, write an action, and omit the final period. Use a body only when the motivation, compatibility impact, migration, or non-obvious tradeoff cannot be understood from the diff. Wrap body lines to about 72 characters.

Keep each commit focused on one logical change. Split unrelated documentation, formatting, dependency, and behavior changes unless the repository's workflow requires them together.

Do not put these into an ordinary commit message:

- the prompt or a user's private context.
- an agent identity or generated-by notice.
- a work log or tool transcript.
- a date recording when the agent edited the file.
- claims about tests, CI, or releases that were not actually checked.
- promotional wording such as "fully modernized" or "production ready".

Breaking changes belong in a `BREAKING CHANGE:` footer or the repository's established equivalent. Issue and pull request references belong in the footer when they are useful to the project.

## Version and release identity

Use Semantic Versioning when the artifact has a public API or a versioned plugin contract. Keep one version source of truth and derive the other representations from it.

- Use a three-part version such as `1.2.3` in `plugin.yml` and `virion.yml` when those manifests expose a version field. Do not add `v` to a manifest version unless the target format explicitly requires it.
- Use the repository's established Git tag convention. `v1.2.3` is a common tag name, but the `v` is a tag convention rather than part of the SemVer value.
- Keep the manifest version, Git tag, GitHub Release title, changelog heading, PHAR metadata, and artifact identity consistent. If one field is authoritative, update derived fields from it instead of editing every field independently.
- Do not add a Composer `version` field only to mirror a Git tag when the package workflow already derives Composer versions from tags.
- Keep server API, Minecraft protocol, PHP runtime, plugin version, virion version, and package version as separate contracts.
- Do not put `PM5`, `API5`, or a server version into the plugin name to represent compatibility. Put compatibility in the manifest, README, and release notes.

Apply the SemVer change rules:

- PATCH for a backward-compatible bug fix.
- MINOR for backward-compatible public functionality or a deprecation.
- MAJOR for a breaking public API or behavior change.
- a prerelease such as `1.2.3-beta.1` only when the artifact is intentionally unstable.

Once a release is published, do not change its contents and keep moving the same version tag. Create a new version for every correction.

## Changelog and release notes

Use a curated changelog for users, not a dump of commit messages. Prefer the Keep a Changelog shape when the project maintains a changelog:

```markdown
## [Unreleased]

## [1.2.0] - 2026-11-07

### Added

- Add the user-visible feature.

### Fixed

- Preserve the existing behavior that was broken.

### Compatibility

- Axolotl-PM API 5
- PHP 8.4 or newer
```

Do not create empty change sections. Include only categories that contain a notable user-facing change. Mention migrations, breaking changes, security fixes, and important compatibility limits. Do not include internal work logs, every test count, or a list of unchanged files unless the release policy requires it.

A normal GitHub release description should usually contain:

1. one short summary of the release.
2. the notable `Added`, `Changed`, `Fixed`, `Removed`, `Deprecated`, or `Security` items.
3. compatibility or migration instructions when they matter.
4. artifact or checksum information when users need it.

Keep verification proportional. A short statement that names the relevant checks is enough for an ordinary release. A detailed evidence record belongs in a release review or audit when the project requires one.

Build and verify the candidate from the exact commit intended for release. Create or move the tag only after the artifact, manifest, resources, dependencies, and runtime entry point have been checked. Do not rebuild different bytes after verification and call them the same release.

## README scope and length

There is no universal README word count. Choose the smallest README that lets a new user identify, install, use, troubleshoot, and verify the artifact.

Use these as soft budgets, not gates:

- A small plugin usually needs 6 to 8 main sections and about 150 to 500 words outside code blocks.
- A normal plugin or library usually needs 7 to 10 main sections and about 300 to 800 words outside code blocks.
- A large project may need about 500 to 1,200 words in the README, with deeper task-specific documentation moved into `docs/`.

Do not add sections only to reach a count. Omit configuration, integrations, contributing, architecture, troubleshooting, or development sections when the project has nothing useful to say there.

Keep each section proportional. The description usually needs one or two short paragraphs. List only user-visible behavior under features. State verified versions and extensions under requirements. Make installation a short sequence that can be followed without guessing. Document only settings users need to change. Use a table for commands and permissions when there are multiple entries. Include one complete usage example that matches the current API. Separate declared, tested, and unverified compatibility ranges. State the actual license and attribution requirements.

Move long API references, architecture explanations, migration guides, and troubleshooting trees out of the README when they stop helping a first-time user complete the common task.

## Date hygiene

Do not add dates to README files, source comments, headings, or ordinary documentation merely to record when an agent edited them. Git, GitHub commits, pull requests, and releases already provide that history.

Use dates only when they are part of the information contract, such as:

- a published release or changelog entry.
- a security advisory.
- a migration deadline.
- an archived compatibility snapshot.
- a protocol or server support timeline.
- a policy that has an explicit review process.

Do not add `Last updated` unless the document has a real maintenance reason and a person or workflow will update it. Prefer a tested compatibility statement such as `Tested against Axolotl-PM 5.51.1` over a vague freshness label.

Do not change copyright years, generated headers, or historical dates unless the task requires that exact change and the source of truth is known.

## Workflow freshness and action pins

Before creating or changing a workflow:

1. Inspect the repository's current workflow, instructions, runner, PHP or language matrix, and release path.
2. Resolve each third-party action to its official repository.
3. Check the official release page and changelog for the selected action.
4. Check whether the current reference is deprecated, unsupported, or behind the current stable major.
5. Select a compatible stable release and pin its full commit SHA when reproducibility or supply-chain control matters.
6. Put a truthful version comment beside the SHA and verify that the SHA belongs to the official action repository and resolves to that tag.
7. Run the repository's workflow validator or `actionlint` when available.
8. Run the hosted workflow and inspect the final job result when the task changes CI.
9. Configure Dependabot for GitHub Actions when the repository owns a long-lived workflow and the project wants automated update pull requests.

Do not copy an old workflow from a sample project without checking its actions and runtime assumptions. Do not use `@latest`, `@main`, or `@master` for a reproducible release workflow. Do not upgrade every action just because a newer release exists. If an older version is retained, record the compatibility reason in the change or repository maintenance notes.

Do not treat a YAML parse, local linter, or generated artifact as proof that the hosted workflow is current. A green workflow proves only the checks that actually ran.

## Lifecycle completion check

Before reporting a repository or release task as complete, check the layers that apply:

- repository name, owner, visibility, description, homepage, topics, branch, and license.
- README identity, badges, links, examples, and compatibility claims.
- commit and pull request text for prompt context, dates, verbosity, and unsupported claims.
- manifest, package, tag, changelog, release, and artifact version agreement.
- action freshness, full SHA pins, runner compatibility, permissions, and workflow result.
- candidate artifact contents, runtime behavior, hosted CI, and public release state separately.

Report any layer that was not checked instead of treating a nearby check as proof.
