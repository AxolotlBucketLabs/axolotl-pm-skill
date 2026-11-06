# Virion and reusable-library workflow

## Boundary

A virion is a reusable library, not a standalone server plugin. Keep server-specific lifecycle wiring in the consumer plugin unless the library's purpose is explicitly a server adapter.

The library should expose a small, stable API. Hide packet formats, resource-pack internals, storage layout, cache coordination, and shading details behind that API.

## Metadata and namespace

Inspect and preserve the repository's `virion.yml` contract, especially:

- `name` and version;
- `antigen` namespace;
- Axolotl-PM/PocketMine API and PHP constraints;
- library dependencies;
- any resource or build metadata required by the target DevTools/VirionTools version.

Keep PHP namespace, directory layout, Composer autoload, `antigen`, and consumer examples consistent. A namespace collision is a packaging bug, not a cosmetic issue.

## API design

- Prefer explicit construction or a named factory over an undocumented global singleton.
- If a plugin instance is required, make that requirement visible in the constructor/factory and explain why.
- Make cleanup idempotent when consumers may call it from `onDisable()` or error paths.
- Return domain objects or well-defined scalar results instead of leaking implementation arrays when the API will be reused.
- Validate inputs at the public boundary and describe failure behavior.
- Keep callback, async, serialization, and exception contracts documented.

## Packaging and consumers

Verify both development and production modes:

- folder-plugin development with a shared virion source;
- consumer build that shades/injects the library into a standalone PHAR;
- resources retained at the expected protected path;
- dependency versions resolved exactly as the build expects;
- multiple consumers, static runtime state, and resource-pack UUID behavior where relevant.

Do not tell users to install a virion directly in `plugins/`. Provide a consumer example or a minimal integration snippet instead.

## README expectations

A virion README should answer:

1. What problem does the library solve?
2. Is it a standalone plugin? Usually no.
3. What PHP, API, extension, and consumer-build requirements apply?
4. How is it installed through DevTools/VirionTools or Composer?
5. What is the smallest working usage example?
6. What are the public API and lifecycle calls?
7. What limitations, compatibility gaps, or resource conflicts exist?
8. What license applies to source and bundled assets?
