# Repository instructions

These instructions apply only to the `axolotl-pm-skill` repository. Read them together with `SKILL.md` when maintaining this skill. They do not replace system instructions, user instructions, or the instructions of a target plugin repository.

## Keep the skill self-consistent

- Treat `SKILL.md` as the entrypoint and references as routed supporting guidance.
- Keep one canonical rule in one place. Link to it instead of copying a second version into another reference.
- Review all human-facing Markdown files after a policy change. Do not review only the lines changed by the current diff.
- Keep examples, validator behavior, README structure, and repository instructions consistent.
- Keep research-only names and links out of canonical documentation unless the deliverable explicitly requires them.

## Prose and Markdown

- Write standalone bullet items as complete sentences that begin with an uppercase letter and end with a period.
- Avoid semicolons in ordinary prose. Use a period, comma, or a new sentence instead.
- Do not use em dash or en dash characters as sentence punctuation. Use an ASCII hyphen only when a dash is necessary.
- Use straight double quotes in authored prose.
- Keep code, regex, URLs, legal text, direct quotations, and literal syntax unchanged when the exception is required.
- Use inline code for literal technical terms and fenced code blocks for multiline code, configuration, commands, logs, patches, and output.
- Check both raw Markdown and its rendered structure when a Markdown change affects a user-facing document.

## Required checks

- Run `python scripts/validate_skill.py` after editing the skill.
- Run `python -m unittest discover --start-directory tests --pattern "test_*.py"` after changing validator behavior or its tests.
- Run the official Codex skill validator before publishing a revision.
- Review the final diff and search every prose file for forbidden punctuation, lowercase checklist fragments, label-shaped prose, prompt context, and unsupported claims.
- Report local checks, hosted CI, published releases, and external settings as separate evidence.
