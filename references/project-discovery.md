# Project discovery and compatibility

Use this reference before changing an unfamiliar plugin, virion, or library.

## Convention precedence

Resolve decisions in this order:

1. Explicit user requirements.
2. Existing repository behavior and build configuration.
3. The locked Axolotl-PM/PocketMine source and declared PHP/API constraints.
4. Axolotl-PM and DevTools conventions.
5. General PMMP/PHP best practice.

Do not replace an existing local convention merely because another style is more familiar.

## First-pass inventory

Use `rg --files` and targeted `rg` searches. Inspect:

- `composer.json` and `composer.lock` for PHP, server, library, and analysis constraints;
- `plugin.yml` for plugin identity, main class, API, commands, permissions, dependencies, and load behavior;
- `virion.yml` for `antigen`, version, API, PHP and virion dependency metadata;
- `devtools.yml` and `.poggit.yml` for virion injection, build paths, and release behavior;
- `.github/workflows/` for pinned builders, test matrices, artifact names, and release gates;
- `README*`, `LICENSE`, `resources/`, `tests/`, `examples/`, and `docs/`;
- representative classes in `src/`, especially the entry point and one class from each major subsystem.

## Classify the artifact

Signals for a plugin:

- `plugin.yml` and a `PluginBase` subclass;
- `onEnable()`, `onDisable()`, command registration, event listeners, scheduled tasks;
- server-facing resources, configuration, permissions, or commands.

Signals for a virion/library:

- `virion.yml` and an `antigen` namespace;
- a public service, value object, parser, adapter, or provider API;
- consumer-side shading/injection rather than direct installation in `plugins/`;
- Composer metadata or a separate example consumer.

When both appear, identify which code is the reusable core and which code is the server/plugin adapter. Do not move server lifecycle assumptions into the reusable core without a concrete reason.

## Establish the real target

Write down the facts that matter to implementation:

- PHP version and extensions;
- Axolotl-PM/PocketMine package and exact locked revision;
- API version floor and any upper bound;
- DevTools/VirionTools revision;
- supported build modes: folder plugin, local virion, Composer consumer, or standalone PHAR;
- available test and static-analysis commands.

If the repository claims a broad compatibility range but only pins one development revision, preserve that distinction in the README and final report.
