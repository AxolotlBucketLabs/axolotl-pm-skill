# Human-facing writing style

Read this reference when writing README files, changelogs, release notes, comments, issues, pull request text, or explanations that people will read.

## Punctuation

For normal English or Vietnamese project prose:

- Do not use Unicode `U+2014` or `U+2013` as sentence punctuation.
- If a dash is genuinely needed, use the ASCII hyphen `-`.
- Prefer rewriting the sentence with a period, comma, conjunction, or parentheses.
- Limit colons in normal prose. Avoid label forms such as `Status: explanation` or `Result: details`.
- Replace label forms with a complete sentence, such as `The workflow is still pending`.
- Avoid semicolon `;` in ordinary prose.
- Use a period to split independent thoughts, or use a comma with a suitable conjunction.
- Keep one main idea per sentence when a shorter sentence is clearer.
- Use straight double quotes `"` in authored prose by default.

These rules target overuse. They do not claim that a Unicode dash or semicolon is invalid in every human publication. The project style should avoid them by default because they often make generated text sound formal, compressed, or artificial.

## GitHub Markdown structure

Use GitHub Flavored Markdown as a semantic format. Choose the structure that helps the reader understand or act on the information. Do not add Markdown features only to make a document look richer.

- Wrap literal file names, paths, classes, interfaces, methods, functions, variables, commands, permissions, manifest keys, and versions in one pair of inline backticks.
- Use a fenced code block for multiline code, configuration, commands, logs, patches, and output that a reader may copy. Add a language tag when the language is known.
- Keep the opening and closing fence paired. Use the same fence character for both sides and do not close a block before its content ends.
- Do not place code directly in prose when the reader needs to copy it or distinguish it from the surrounding sentence.
- Use headings for document structure. Do not use bold text as a substitute for a heading.
- Use a table for repeated fields such as commands, permissions, configuration keys, API entries, or compatibility versions when a table is easier to scan than a list.
- Use a list for independent points. Do not turn a short list into a table without a readability benefit.
- Use descriptive links and repository-relative links when they are stable. Prefer GitHub issue, pull request, commit, and file references when they give the reader useful context.
- Use `<details>` with a useful `<summary>` for long logs, optional troubleshooting, and technical detail that most readers do not need immediately.
- Use GitHub alerts only for information that affects installation, compatibility, security, migration, or another important user decision. Do not use alerts as decoration.

When Markdown contains another Markdown document or a nested code block, use a longer outer fence or a tilde fence. Do not wrap both levels with the same triple backtick fence. Do not extract LLM output by splitting on the literal triple-backtick delimiter because a nested fence or a backtick inside a string can truncate valid content.

Before finishing a Markdown change, inspect the raw source and the rendered result when a preview or parser is available. Check that fences are paired, inline code is closed, language tags are accurate, links are readable, tables have valid separators, and `<details>` blocks have matching tags. Correct content does not prove that its Markdown boundaries are correct.

## Voice and structure

- Prefer active voice and concrete statements.
- Remove filler, inflated adjectives, repeated conclusions, and generic introductions.
- State what the project does, what it requires, and what was tested.
- Use a short sentence instead of joining several independent thoughts with punctuation.
- Keep headings and bullets parallel. Use one idea per bullet when possible.
- Use Humanizer for a final prose pass when it is available, but preserve technical facts, links, code, metadata, and frontmatter.
- Write as a natural, respectful, modest maintainer. Avoid corporate, recruitment, sales, and template-like AI language.
- Prefer a complete sentence over a label fragment. Do not write `Status: explanation` when a direct sentence is possible.
- Make claims from evidence. Do not say that something was fixed, tested, pushed, released, or verified unless that action actually happened.
- When reporting an achievement, include the relevant evidence and context instead of self-praise.
- Keep routine reviews short. Add detail when the task is an audit, security review, release review, or incident investigation.

## Pull request writing

Keep routine pull request titles short and specific.

The description should usually explain the following:

- Explain what problem was observed.
- Explain what changed.
- Mention the checks that help the reviewer evaluate this change.
- Explain any compatibility or release risk that matters.

Do not paste a complete command log, every test count, every internal reasoning step, or unrelated repository details into an ordinary pull request.

Do not add a `Verification` heading to every pull request. GitHub does not require that heading, and a pull request body is not a CI transcript.

Read the repository's pull request template before writing the description. Follow a project-specific `Testing`, `Verification`, or equivalent section when the template requires it. Do not create a new section only because another pull request used one.

For an ordinary pull request, a short sentence or compact list of relevant checks is enough. Use a dedicated evidence section only when the change has a meaningful review boundary that the diff or GitHub Checks cannot show, such as runtime behavior, PHAR contents, release provenance, migrations, security reproductions, or compatibility matrices.

For documentation, badge, metadata, formatting, translation, or reference-only changes, use focused checks and usually omit a verification section. Mention a limitation when a required check could not run, but do not list every unavailable or unrelated tool.

Use more detailed verification when the project requires it for a security review, release review, incident, or compatibility change. Keep that detail proportional to the reviewer's actual need.

Avoid vague descriptions such as:

- Improve robustness and handle edge cases.
- Fix several issues.
- Update implementation.
- Make the code better.

Prefer a concrete description such as:

```text
Fix typed catch handling in the shaded PHAR

The shaded catch path was not matched at runtime because the generated namespace was not included in the handler. The change updates the narrow handler and verifies the packaged PHAR with the focused runtime test and PHPStan.
```

A CI summary such as `105 tests and 504 assertions` is useful when the number is relevant to the review. It should not be included only to make the pull request appear more complete.

If the repository has a pull request template, follow it. This rule prevents an agent from writing more detail than the project requires.

When creating a pull request with GitHub CLI, do not use generated title and body text without reviewing it. In particular, treat `gh pr create --fill` as unsafe for final prose because commit messages can contain private task context or details that do not belong in the public pull request.

Do not paste a full verification transcript into a routine pull request. Include the checks that matter to the change and mention a limitation when a required check could not run.

## Review and handoff discipline

Use the final report as a short record of the work, not as a transcript of the agent's internal process. Explain the observed problem, the selected change, the checks that actually ran, and the remaining uncertainty. Do not include hidden reasoning, prompt history, irrelevant research links, or a list of every file the agent inspected.

If the task involved a compatibility, packaging, release, or external system boundary, name that boundary and give its specific evidence. A local green test is not enough to claim that a hosted workflow, released artifact, or production integration was verified.

## Exceptions

Do not apply these prose substitutions inside:

- PHP, YAML, INI, JSON, Markdown syntax, shell commands, regular expressions, URLs, or identifiers.
- License text, legal text, or direct quotations that must remain faithful.
- Localized translations when the target language's normal punctuation requires another form.
- Official names, package names, version ranges, or external metadata that must remain unchanged.

## Final check

Before finalizing human-facing prose, search only the prose files and review every match manually:

```sh
rg -n '[\x{2013}\x{2014};]' README.md CHANGELOG.md docs .github
```

Also review for label-shaped sentences such as `Status: explanation`, unnecessary colons, curly quotation marks, and unsupported completion claims. Do not run a blind replacement across the entire repository. A match in code, a URL, a license, a translation, or a machine-readable file may be correct.
