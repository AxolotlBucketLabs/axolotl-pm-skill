# Public release and marketplace review

Read this reference only when the user asks to prepare a public release, submit to Poggit or another marketplace, or review whether a plugin is publishable. These are release-policy checks, not universal coding rules.

The source basis is the user-provided [Poggit submission rules](https://gist.github.com/NhanAZ/992c5ba4211252d202d8d4e8aac080c6). Recheck the destination marketplace's current policy before submission; do not assume historical Poggit policy is current or applies to Axolotl-PM.

## Purpose and scope

- The plugin should solve a concrete problem and describe that problem clearly.
- Avoid bundling unrelated features that create bloat or a confusing maintenance boundary.
- A private-server plugin may be intentionally narrow; do not reject it as “not useful to the majority” unless the destination marketplace requires that criterion.
- When a project duplicates an existing plugin, document the difference in purpose, maintenance status, compatibility, or user value.

## Provenance and completeness

- Submit code and assets with clear authorship and license provenance.
- For a fork or replacement, preserve attribution and check the original license and permission requirements.
- Do not republish an abandoned project as if it were original work.
- A release should be complete and functional. Mark experimental or incomplete features honestly and do not advertise them as stable.
- Do not ship arbitrary remote code execution, unsafe auto-updaters, obfuscated source, or remote behavior that can silently change the plugin's executable logic.

## External services

- Use an external API only when it is reasonably necessary for the feature.
- Document the provider, endpoint purpose, required credentials, data sent, rate limits, failure behavior, and whether a free/usable plan exists.
- Do not use a plugin as unsolicited advertising for a server, paid plan, or unrelated resource.
- Do not add artificial feature restrictions merely to coerce a purchase or subscription.

## Target and compatibility

- Release only against a stable, explicitly supported API target unless the destination has an experimental channel.
- For Axolotl-PM, state clearly that it is the target. Do not copy a policy that bans unofficial forks; instead, separate and test Axolotl-PM and upstream PocketMine-MP compatibility claims.
- Keep plugin name, manifest name, release name, namespace, and artifact name consistent. Do not put version numbers such as `-PM5` in the plugin name.

## User-facing documentation

- Provide an English description for a broad public release, with additional translations where useful.
- Explain purpose and behavior in text; screenshots or videos alone are not documentation.
- Use clean Markdown with sections for requirements, installation, configuration, commands, permissions, dependencies, compatibility, and license.
- Include a user-readable changelog for updates. Mention breaking changes, migrations, behavior changes, and important fixes rather than cosmetic repository edits.
- Include an SPDX-compatible open-source license at the project root and check licenses for bundled dependencies and assets.

## Virion/library publication

- A server-facing reusable library should normally be distributed as a virion or through the target's supported library mechanism rather than as a fake standalone plugin.
- A pure PHP library may be Composer-first or dual-distributed when it does not require server lifecycle integration.
- State whether the artifact is a standalone plugin, a virion, a Composer package, or a consumer example.
- Document the exact consumer build path, shading behavior, resource handling, and any limitation when multiple consumers run together.

## Final release checklist

Before submission, verify:

- the artifact is built from the intended commit;
- the manifest, README, changelog, license, namespace, and version agree;
- required dependencies and optional integrations are accurately declared;
- the PHAR or package contains the required source/resources and no accidental secrets or development files;
- the advertised API target and PHP range match what was actually tested;
- known limitations and unverified compatibility are stated.
