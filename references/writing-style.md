# Human-facing writing style

Read this reference when writing README files, changelogs, release notes, comments, issues, pull request text, or explanations that people will read.

## Punctuation

For normal English or Vietnamese project prose:

- Do not use Unicode `U+2014` or `U+2013` as sentence punctuation.
- If a dash is genuinely needed, use the ASCII hyphen `-`.
- Prefer rewriting the sentence with a period, comma, conjunction, or parentheses.
- Limit colons in normal prose. Avoid label forms such as `Status: explanation` or `Result: details`.
- Replace label forms with a complete sentence, such as `The workflow is still pending because the UI setting has not been checked.`
- Avoid semicolon `;` in ordinary prose.
- Use a period to split independent thoughts, or use a comma with a suitable conjunction.
- Keep one main idea per sentence when a shorter sentence is clearer.
- Use straight double quotes `"` in authored prose by default.

These rules target overuse. They do not claim that a Unicode dash or semicolon is invalid in every human publication. The project style should avoid them by default because they often make generated text sound formal, compressed, or artificial.

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

The description should usually explain:

- what problem was observed;
- what changed;
- what evidence was checked;
- any compatibility or release risk that matters.

Do not paste a complete command log, every test count, every internal reasoning step, or unrelated repository details into an ordinary pull request.

Use more detailed verification when the project requires it for a security review, release review, incident, or compatibility change.

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

## Exceptions

Do not apply these prose substitutions inside:

- PHP, YAML, INI, JSON, Markdown syntax, shell commands, regular expressions, URLs, or identifiers;
- license text, legal text, or direct quotations that must remain faithful;
- localized translations when the target language's normal punctuation requires another form;
- official names, package names, version ranges, or external metadata that must remain unchanged.

## Final check

Before finalizing human-facing prose, search only the prose files and review every match manually:

```sh
rg -n '[\x{2013}\x{2014};]' README.md CHANGELOG.md docs .github
```

Also review for label-shaped sentences such as `Status: explanation`, unnecessary colons, curly quotation marks, and unsupported completion claims. Do not run a blind replacement across the entire repository. A match in code, a URL, a license, a translation, or a machine-readable file may be correct.
