# Official Axolotl-PM sources

Use this reference to find the official Axolotl-PM documentation, source code, support communities, runtime baseline, and Bedrock protocol guidance. These links are starting points, not a replacement for checking the exact dependency and source revision used by the target project.

## Canonical links

- [Axolotl-PM documentation](https://axolotl-pm.org/docs/) covers installation, configuration, plugins, permissions, API versioning, plugin manifests, protocol updates, and internal development topics.
- [Axolotl-PM source code](https://github.com/axolotl-pm/PocketMine-MP) is the primary source for implementation behavior and exact API signatures.
- [Plugin development docs](https://axolotl-pm.org/docs/developers/plugin-docs-index) collects the API versioning, event, plugin format, and manifest references.
- [API versioning](https://axolotl-pm.org/docs/developers/plugin-docs/api-version-spec) explains how plugin API versions map to Axolotl-PM server versions.
- [Plugin manifest reference](https://axolotl-pm.org/docs/developers/plugin-docs/plugin-manifest) documents `plugin.yml`, dependencies, extensions, and `mcpe-protocol`.
- [Axolotl-PM Discord](https://discord.axolotl-pm.org) is the main Axolotl-PM community and support server.
- [AxolotlBucketLabs Discord](https://discord.gg/Pk4FrNvHnM) is the organization community server.
- [AxolotlBucketLabs DevTools](https://github.com/AxolotlBucketLabs/DevTools) is the preferred development and packaging tool when the project targets Axolotl-PM.
- [Axolotl-PM PHP binaries](https://github.com/axolotl-pm/PHP-Binaries/releases) contains the maintained server PHP builds and production recommendations.
- [Current stable composer.json](https://raw.githubusercontent.com/axolotl-pm/PocketMine-MP/stable/composer.json) is the source for the server's PHP and dependency constraints.
- [Current stable CI workflow](https://raw.githubusercontent.com/axolotl-pm/PocketMine-MP/stable/.github/workflows/main.yml) shows the PHP versions currently tested by the core repository.

The Axolotl-PM documentation currently links to `apidoc.pmmp.io` for generated API pages. Treat that site as a general or legacy Doxygen reference. For Axolotl-specific behavior, the locked Axolotl-PM source and dependency metadata take precedence.

## Source and version precedence

When sources disagree, use this order:

1. The target repository's local instructions and existing behavior.
2. Its locked `composer.lock`, manifest, build metadata, and exact Axolotl-PM source revision.
3. The official Axolotl-PM documentation for the matching release or API branch.
4. The maintained Axolotl-PM repositories and release notes.
5. Upstream PocketMine-MP documentation or historical PMMP examples.

Do not copy a version, namespace, signature, event, packet ID, or manifest field from an upstream PMMP example until the Axolotl-PM source confirms it.

## PHP baseline and project default

Read the target server and project constraints instead of silently changing an existing compatibility contract.

- The current Axolotl-PM stable source declares PHP `^8.1`, requires 64-bit PHP, and requires additional server extensions. This is the upstream server baseline. It is not the default runtime policy for new AxolotlBucketLabs projects.
- AxolotlBucketLabs projects created or substantially migrated with this skill use PHP 8.4 as the default minimum and build runtime unless the user selects another target or an authoritative dependency requires a different range.
- For the AxolotlBucketLabs default, use a Composer requirement such as `^8.4`, run the default build and static-analysis workflow on PHP 8.4, and state the resulting requirement in the README. Do not change an existing lower minimum without an explicit migration request and compatibility evidence.
- Current Axolotl-PM PM 5.x PHP binaries identify PHP 8.4 as the recommended production runtime.
- PHP 8.5 binaries are available, but their release notes warn that plugins may not work on that runtime. Treat PHP 8.5 as an optional compatibility target and test it explicitly before claiming support. It is not a universal maximum.
- The current Axolotl-PM CI matrix tests PHP 8.1 through PHP 8.5. CI coverage is evidence of testing, not a reason to change a project's declared minimum.
- Keep the declared minimum, tested versions, recommended runtime, build runtime, and unsupported range separate in the README and release notes.
- Do not claim a universal maximum PHP version. Record the target project's own Composer and dependency constraints. Composer's `^8.4` constraint permits compatible PHP 8.x releases and excludes PHP 9.x, subject to the rest of the dependency graph.
- A plugin or virion must declare the narrowest PHP requirement supported by its code and dependencies. Do not raise the minimum only because a newer server binary or build tool exists.

Recheck these facts when the target branch, server release, PHP binaries, or dependency lock changes.

## Bedrock protocol and transport

- Keep Minecraft game version, Bedrock network protocol version, Axolotl-PM API version, `plugin.yml` API, `mcpe-protocol`, and the `axolotl-pm/bedrock-protocol` package version separate.
- For packet-level work, inspect the exact `axolotl-pm/bedrock-protocol`, `axolotl-pm/bedrock-data`, block upgrade schema, and item upgrade schema versions selected by the target lock file.
- The current Axolotl-PM source uses a versioned `axolotl-pm/bedrock-protocol` package. Do not copy its current package version into another project without checking that project's server branch and lock file.
- Read the [plugin manifest reference](https://axolotl-pm.org/docs/developers/plugin-docs/plugin-manifest) before using `mcpe-protocol`. It is a plugin compatibility field, not a substitute for the plugin API declaration.
- Read the [protocol update guide](https://axolotl-pm.org/docs/developers/internals-docs/updating-minecraft-protocol) when adding or changing packets, protocol data, or Minecraft version support.
- Read the [NetherNet documentation](https://axolotl-pm.org/docs/installation/nethernet-usage) before assuming RakNet is the active transport. Transport behavior depends on the target server and Minecraft version.
- Prefer the stable Axolotl-PM API over packet interception. Use protocol internals only when the public API cannot provide the required behavior or the project is explicitly a protocol library.

Protocol IDs and packet structures are versioned data. Never infer them from memory or from a different Minecraft release.
