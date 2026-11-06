# Plugin workflow

## Structure

Use the repository's existing layout. A conventional plugin has:

```text
plugin.yml
CI build workflow
README.md
LICENSE
resources/
src/Vendor/PluginName/
```

Do not add `resources/`, tests, Composer, or a new framework just because a historical corpus contains them. Add them when the feature or repository workflow needs them.

## Lifecycle and boundaries

- Keep `onEnable()` focused on loading configuration, creating services, registering listeners/commands, and scheduling required tasks.
- Use `onDisable()` to close database connections, cancel or release resources, unregister generated packs, and flush state when the API requires it.
- Prefer focused command, listener, task, storage, and service classes once the entry point becomes difficult to reason about.
- Register listeners and commands using the target Axolotl-PM/PocketMine API confirmed during discovery.
- Do not do blocking I/O on the server thread unless the repository and operation make that safe.
- Treat event cancellation, priority, and ordering as part of the plugin contract.

## Configuration and resources

- Put user-editable defaults in `resources/config.yml` or the repository's established resource path.
- Keep config keys, defaults, validation, and README examples synchronized.
- Version or migrate configuration when changing its shape. Do not silently discard existing user values.
- For language files, SQL schema, resource packs, or other assets, verify that the build includes the files and that runtime paths work inside a PHAR.

## Commands, permissions, and dependencies

- Keep command names, aliases, usage, permissions, defaults, and implementation in sync with `plugin.yml`.
- Declare required and optional plugins explicitly. Use soft dependencies only when the feature genuinely degrades without them.
- Prefer stable public APIs of dependencies over internals or reflection.
- If an integration is optional, isolate it behind a capability check or adapter.

## Plugin documentation

At minimum document the feature, requirements, installation, configuration, commands, permissions, integrations, compatibility, and license. A small plugin can be concise, but an operator should not need to read source code to install or configure it.
