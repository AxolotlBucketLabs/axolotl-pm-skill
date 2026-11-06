# PHP style, naming, and comments

This is a decision guide, not a formatter configuration. Match the local project before applying these defaults.

## Observed ecosystem tendencies

The archive corpus shows two related styles:

- plugins are lifecycle- and event-driven, with names such as `onEnable`, `onRun`, `onCommand`, `onJoin`, `onQuit`, and `onBlockBreak`;
- virions are API-driven, with names such as `create`, `register`, `handle`, `get`, `send`, `parse`, `validate`, `flush`, and `close`.

Both generally use lower camel case for methods and variables. Common plugin variables include `$player`, `$sender`, `$event`, `$args`, `$config`, `$item`, and `$block`; reusable libraries more often use `$value`, `$key`, `$callback`, `$query`, `$path`, `$request`, `$options`, and `$parameters`.

These are useful vocabulary signals, not requirements. Use names from the actual domain and existing API rather than forcing a familiar word.

## Recommended defaults for new code

- Add `declare(strict_types=1)` when the target PHP version and surrounding code support it.
- Type parameters, return values, and properties. Use nullable and union types deliberately, not merely to satisfy a checker.
- Prefer explicit visibility and narrow public APIs.
- Use `final` for concrete service/value classes when extension is not part of the contract; leave extension points open when consumers are expected to subclass.
- Keep lifecycle methods small and delegate behavior to named services.
- Avoid public mutable state when an invariant can be protected by a method or value object.
- Use descriptive names in public methods. `$i`, `$x`, `$y`, `$z`, `$pk`, and similar short names are acceptable for tightly scoped loops, coordinates, and packet code.

Do not impose one brace placement, import ordering, constructor style, or singleton policy unless the repository already enforces it or the task explicitly requests a style migration.

## Comments and docblocks

Use docblocks for public API contracts that are not obvious from the signature, including:

- callback shapes and generic collections;
- exceptions and failure behavior;
- lifecycle requirements;
- serialization or protocol formats;
- compatibility and resource-pack limitations.

Use inline comments only for non-obvious intent, invariants, workarounds, protocol quirks, or ordering requirements. Avoid comments that narrate `get`, `set`, or obvious conditionals.

When changing behavior, update comments and README examples that describe that behavior. Remove stale comments instead of adding a second explanation beside them.
