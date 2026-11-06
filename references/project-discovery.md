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

- Inspect `composer.json` and `composer.lock` for PHP, server, library, and analysis constraints.
- Inspect `plugin.yml` for plugin identity, main class, API, commands, permissions, dependencies, and load behavior.
- Inspect `virion.yml` for `antigen`, version, API, PHP, and virion dependency metadata.
- Inspect `devtools.yml` and `.poggit.yml` for virion injection, build paths, and release behavior.
- Inspect `.github/workflows/` for pinned builders, test matrices, artifact names, and release gates.
- Inspect `README*`, `LICENSE`, `resources/`, `tests/`, `examples/`, and `docs/`.
- Inspect representative classes in `src/`, especially the entry point and one class from each major subsystem.

## Classify the artifact

Signals for a plugin:

- Find `plugin.yml` and a `PluginBase` subclass.
- Find `onEnable()`, `onDisable()`, command registration, event listeners, and scheduled tasks.
- Check server-facing resources, configuration, permissions, and commands.

Signals for a virion/library:

- Find `virion.yml` and an `antigen` namespace.
- Expose a public service, value object, parser, adapter, or provider API.
- Use consumer-side shading or injection rather than direct installation in `plugins/`.
- Find Composer metadata or a separate example consumer.

When both appear, identify which code is the reusable core and which code is the server/plugin adapter. Do not move server lifecycle assumptions into the reusable core without a concrete reason.

## Establish the real target

Write down the facts that matter to implementation:

- Record the PHP version and extensions.
- Record the Axolotl-PM or PocketMine package and exact locked revision.
- Record the API version floor and any upper bound.
- Record the DevTools or VirionTools revision.
- Record supported build modes such as a folder plugin, local virion, Composer consumer, or standalone PHAR.
- Record available test and static analysis commands.

If the repository claims a broad compatibility range but only pins one development revision, preserve that distinction in the README and final report.

## API and invariant grounding

Before using a symbol or changing behavior, establish its source of truth.

- Search the locked dependency, checked-out server source, vendor tree, or generated signature for the exact class, method, event, constant, manifest field, and return type.
- Search existing repository call sites and tests for the established usage. Prefer a proven local pattern when it matches the current contract.
- When Axolotl-PM and PocketMine-MP look similar, compare the exact namespace, signature, lifecycle timing, return value, exception behavior, and supported version instead of copying the upstream implementation.
- Identify the invariant that the code relies on, such as ownership, event order, thread boundary, shading boundary, persistence format, or cleanup responsibility.
- If a symbol appears only in a prompt, a general memory, or an unrelated example, treat it as unverified until the repository or locked dependency confirms it.

Do not edit around an unverified API assumption. Record the missing evidence and investigate the dependency or source first.
