# Repository publishing and metadata

Read this reference when creating a GitHub repository, moving a project into an organization, preparing a public repository, or auditing repository presentation. Repository creation is not complete when the files are pushed: the hosting metadata and discoverability settings are part of the deliverable.

## Required repository details

Before reporting a repository as published, inspect and set the following when they are in scope:

- repository name and owner;
- visibility;
- concise description that matches the actual artifact;
- homepage/Website URL pointing to a real project landing page, documentation site, or the repository README when no separate site exists;
- focused lowercase topics that describe the ecosystem, artifact type, and primary technologies;
- default branch;
- root license and license badge;
- README links and badges pointing to the final owner/repository;
- CI, release, package, deployment, and community links only when the corresponding service or artifact exists.

Do not invent a website, Discord invite, release, package registry, deployment target, or topic merely to fill a field. A repository URL with a `#readme` fragment is an acceptable temporary homepage when there is no separate documentation site; replace it when a real project site becomes available.

Keep topics useful rather than exhaustive. Prefer a small set such as `axolotl-pm`, `pocketmine-mp`, `pmmp`, `php`, `pmmp-plugin`, `virions`, and `codex-skill` over a tag dump or unrelated popularity terms.

## Home-page feature toggles

After repository creation, inspect the repository's Settings → General → Features → home-page inclusion controls. For a project that uses GitHub Releases, include **Releases**. Leave **Deployments** and **Packages** disabled unless the repository actually publishes deployments or packages that users should discover from the home page.

The supported `gh repo edit` command exposes description, homepage, topics, visibility, merge settings, Issues, Projects, Wiki, and Discussions, but it does not expose the Releases/Deployments/Packages home-page inclusion controls. The public repository update GraphQL input likewise does not provide those fields. Do not claim that these three toggles were changed after only running the CLI.

If the controls are unavailable through the current CLI/API, report them as UI-pending and give the maintainer the exact path. A human or an approved browser workflow must change them in GitHub's repository settings, then the agent should re-check the visible state.

## Verification

Use authenticated, read-only checks after changing metadata:

```sh
gh repo view OWNER/REPOSITORY --json nameWithOwner,isPrivate,url,homepageUrl,description,defaultBranchRef,repositoryTopics
gh api repos/OWNER/REPOSITORY/topics
```

Then verify that the README's badges and links use the same final owner/repository. Distinguish these evidence layers:

- CLI/API output proves repository metadata and topics;
- the GitHub Settings UI proves home-page inclusion toggles;
- a successful Actions run proves the workflow ran, not that repository presentation settings are correct.

If the project moved from another owner, preserve the old repository unless the user explicitly asks to delete it. Update links and badges before treating the move as complete.
