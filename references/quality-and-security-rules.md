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

## Bedrock protocol and transport

- Treat Minecraft game version, Bedrock network protocol version, Axolotl-PM API version, `plugin.yml` API, `mcpe-protocol`, and the BedrockProtocol package version as separate contracts.
- For packet-level work, inspect the exact protocol and Bedrock data packages selected by the target lock file. Do not copy packet IDs, packet structures, or protocol constants from memory or a different Minecraft release.
- Read the target manifest documentation before using `mcpe-protocol`. Declare only versions that the plugin actually supports and test the minimum claimed version.
- Prefer the stable Axolotl-PM API over packet interception. Isolate protocol-specific code and document why the public API cannot provide the required behavior.
- Confirm the target transport before assuming RakNet, NetherNet, encryption, compression, or threading behavior. Transport details are not interchangeable across server and Minecraft versions.

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

## Test quality and regression evidence

A test must protect a project contract or a demonstrated regression. Do not add a test only to increase the test count.

For a bug fix:

- reproduce the failure on the baseline implementation when the baseline is available;
- make the focused test or reproducer fail before the fix;
- implement the smallest fix;
- make the focused test pass after the fix;
- run the relevant existing test suite and static analysis;
- confirm that the test would fail if the bug were reintroduced.

Prefer assertions against observable behavior, public APIs, persisted data, emitted events, generated artifacts, or runtime output. Do not mock the logic being tested or assert private implementation details unless the repository's contract requires it.

Do not make an existing test easier to satisfy in order to make a change pass. Do not delete a case, weaken an assertion, broaden an expected value, skip a test, replace a real dependency with a mock, or change test configuration without a demonstrated reason that belongs to the project contract. If a test passes both before and after a bug fix, it does not yet prove the fix.

Avoid tests that:

- only cover the happy path when the bug is in a failure path;
- repeat an existing test without adding a distinct contract;
- assert a constant or implementation detail instead of behavior;
- pass even when the reported bug is restored;
- only confirm that a mock returned the value configured by the test;
- test framework behavior rather than project behavior.

Mutation testing is recommended for behavior-heavy libraries, parsers, security-sensitive code, and public APIs when the project already supports it. It is not a universal requirement for a small plugin, a translation-only change, documentation work, or a repository configuration change.

If the baseline cannot be executed, state that limitation. Do not claim that the regression test was proven against the old implementation.

## Contract-aware defensive coding

Add defensive checks at trust boundaries and integration points, not around every internal operation.

Do not add hypothetical sanitization, validation, redaction, logging, fallback behavior, or exception handling without a demonstrated failure, an explicit contract, or a required security boundary. Speculative defenses can hide the real invariant and change behavior that was already correct.

- Use a null check only when null is valid according to the contract.
- Use `isset()` only when missing data has a meaningful behavior.
- Do not catch an exception unless the code can recover, add useful context, translate the failure, or perform required cleanup.
- Do not catch `Throwable` broadly to hide a broken invariant.
- Do not add guards only to satisfy static analysis.
- Preserve established invariants instead of weakening the contract to tolerate impossible states.
- When an impossible state indicates a programmer error, prefer a clear failure over a silent fallback.

## Semantic correctness

Before changing logic, identify the assumptions that make the current design correct.

Check:

- ownership of state;
- lifecycle ordering;
- event ordering and cancellation;
- threading and async boundaries;
- namespace and shading boundaries;
- version and API contracts;
- resource cleanup;
- permission and command semantics;
- fallback behavior;
- persistence and serialization formats.

Do not change a local condition, return value, event priority, exception path, or lifecycle hook without checking its callers, consumers, tests, and related invariants.

A simpler-looking implementation is not an improvement if it violates an invariant or changes the meaning of the public contract.

## Boundary-aware verification

Choose evidence that can observe the behavior being changed.

- For pure PHP behavior, prefer a focused test and static analysis against the public contract.
- For plugin lifecycle, commands, permissions, events, resources, or configuration, add a runtime or consumer smoke check when a source-level test cannot observe the failure.
- For a virion or reusable library, verify the consumer build, namespace injection or shading, autoloading, and a public API call when packaging can change the result.
- For a PHAR or release package, inspect the built artifact, manifest, resources, dependencies, and runtime entry point. A successful source test does not prove the package is usable.
- For compatibility claims, identify the exact revisions tested and keep untested versions separate from verified results.

Do not use a passing check from one boundary as proof for another boundary. State the remaining uncertainty when the strongest relevant check cannot run.

## Compatibility rule for Axolotl-PM

Do not import the historical rule "unofficial server software is unsupported" as a blanket ban. Axolotl-PM is itself the target in this skill. Instead:

- identify whether the project targets Axolotl-PM, upstream PocketMine-MP, or both;
- declare the target and API floor explicitly;
- inspect the locked source or exact revision for signatures and behavior;
- test each claimed target separately;
- never claim upstream compatibility merely because an Axolotl-PM API looks similar.

## Review severity

Treat namespace collisions, remote code execution, unsafe SQL, blocking gameplay I/O, missing required dependencies, and unbounded main-thread work as release-blocking findings. Treat log wording, English fallback, naming polish, and optional documentation improvements as lower-severity unless the target repository or publication policy makes them mandatory.
