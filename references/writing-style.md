# Human-facing writing style

Read this reference when writing README files, changelogs, release notes, comments, issues, pull request text, or explanations that people will read.

## Punctuation

For normal English or Vietnamese project prose:

- Do not use Unicode `U+2014` or `U+2013` as sentence punctuation.
- If a dash is genuinely needed, use the ASCII hyphen `-`.
- Prefer rewriting the sentence with a period, comma, conjunction, or parentheses.
- Avoid semicolon `;` in ordinary prose.
- Use a period to split independent thoughts, or use a comma with a suitable conjunction.
- Keep one main idea per sentence when a shorter sentence is clearer.

These rules target overuse. They do not claim that a Unicode dash or semicolon is invalid in every human publication. The project style should avoid them by default because they often make generated text sound formal, compressed, or artificial.

## Voice and structure

- Prefer active voice and concrete statements.
- Remove filler, inflated adjectives, repeated conclusions, and generic introductions.
- State what the project does, what it requires, and what was tested.
- Use a short sentence instead of joining several independent thoughts with punctuation.
- Keep headings and bullets parallel. Use one idea per bullet when possible.
- Use Humanizer for a final prose pass when it is available, but preserve technical facts, links, code, metadata, and frontmatter.

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

Do not run a blind replacement across the entire repository. A match in code, a URL, a license, a translation, or a machine-readable file may be correct.
