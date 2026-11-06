# Quality and security rules

Use this reference for implementation and code review. These rules are adapted from the user-provided [Poggit submission rules](https://gist.github.com/NhanAZ/992c5ba4211252d202d8d4e8aac080c6), but they are written as Axolotl-PM/PMMP engineering guidance rather than marketplace policy.

## Must: preserve readable, collision-safe code

- Do not obfuscate PHP or hide behavior behind `eval()`, encoded source, arbitrary reflection, or opaque generated code.
- Give every plugin a unique author/project namespace. Keep plugin classes, interfaces, traits, and bundled libraries inside the intended namespace or a deliberately shaded dependency namespace.
- Keep the public namespace stable after release unless the change is intentionally breaking and the migration is documented.
- Use descriptive variable names in public or long-lived code. Short names such as `$i`, `$x`, `$y`, `$z`, `$pk`, or `$ev` are acceptable only in tightly scoped loops, coordinate math, or packet code.

## Must: declare and isolate dependencies

- Declare required plugin/library dependencies in the manifest and build configuration used by the repository.
- Treat optional integrations as optional: detect availability, isolate the adapter, and preserve a useful fallback or clear diagnostic.
- Do not call another plugin's API merely because it is commonly installed.
- Keep virion dependencies explicit in `virion.yml`, `composer.json`, `devtools.yml`, or the repository's actual build metadata.
- After packaging, inspect the artifact for namespace collisions, missing shaded code, and resources that were declared but not included.

## Must: protect the server thread

- Do not perform blocking HTTP, cURL, MySQL, heavy SQLite, or other wait-for-I/O operations on the main thread during normal gameplay.
- Do not wait synchronously for a worker or async task from the main thread.
- Avoid repeatedly scanning a persistent dataset such as all players, accounts, blocks, or entities on the main thread. Use indexes, caches, bounded work, pagination, or async processing.
- Keep startup/shutdown work proportional and explain unavoidable blocking work.
- When an operation is intentionally small and synchronous, document its bound and why it is safe for the target server.

## Must: handle data safely

- Never interpolate untrusted or runtime data into SQL. Use prepared statements, bound parameters, `bindValue()`, `bind_param()`, libasynql, or the target database abstraction.
- Store generic plugin data in the host plugin's data directory.
- Namespace persistent database tables, keys, files, cache entries, NBT tags, generated resource packs, and temporary files to avoid collisions.
- Validate input at public boundaries, but do not treat validation as a replacement for parameter binding or output encoding.
- Do not deserialize or execute remote content unless the format and trust boundary are explicit and safely constrained.

## Must: use the stable server API first

- Prefer the public Axolotl-PM/PocketMine API over packet interception, internal classes, numeric IDs, or implementation details.
- Use packet/protocol APIs only when the public API cannot provide the required behavior or the project is explicitly a protocol library. Isolate that code and document the reason.
- Prefer server-provided vanilla constants, parsers, and factories over hardcoded IDs or duplicated protocol data when the target version provides them.
- Do not use `dispatchCommand()` to perform internal operations unless the command template is authored and controlled by the project. Prefer a direct public method or service call.
- Do not use command-preprocess events to block commands when permissions or command ownership can express the policy safely.

## Must: make commands and permissions ownable

- Commands registered by a plugin must be identifiable as owned by that plugin.
- If using a fallback prefix, use the plugin name rather than initials or an arbitrary abbreviation.
- Permission strings must use a plugin-specific prefix and must match between manifest and implementation.
- Keep command aliases, usage, permission, default access, and implementation synchronized.

## Must: clean runtime behavior

- Do not emit decorative startup/shutdown messages that add no operational value.
- Log actionable state: failed dependency, migration, disabled integration, build/resource failure, or a meaningful load summary.
- Close or unregister resources in the appropriate lifecycle method. Cleanup should be safe to call from error paths when practical.
- Do not silently swallow errors that leave a feature partially active. Report a useful diagnostic and choose a safe fallback.

## Compatibility rule for Axolotl-PM

Do not import the historical rule "unofficial server software is unsupported" as a blanket ban. Axolotl-PM is itself the target in this skill. Instead:

- identify whether the project targets Axolotl-PM, upstream PocketMine-MP, or both;
- declare the target and API floor explicitly;
- inspect the locked source or exact revision for signatures and behavior;
- test each claimed target separately;
- never claim upstream compatibility merely because an Axolotl-PM API looks similar.

## Review severity

Treat namespace collisions, remote code execution, unsafe SQL, blocking gameplay I/O, missing required dependencies, and unbounded main-thread work as release-blocking findings. Treat log wording, English fallback, naming polish, and optional documentation improvements as lower-severity unless the target repository or publication policy makes them mandatory.
