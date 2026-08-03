---
pack: task-workflows
summary: Guidance for branches, commits, PR flow, and release hygiene.
tags: [workflow, git, release]
---

# Git Workflow

Conventions for commits, branches, pull requests, and releases.

## Setup (Required)

```
Before making any commits, configure your identity in each local repo:

git config user.name "Your Full Name"
git config user.email "your.email@example.com"

This ensures every branch, commit, and PR is traceable to its author.
Verify with: git config --list
```

## Commit Messages

```
Use past participle for all commit messages. Keep them brief, clear, and specific.
List grouped changes with hyphen bullets when a multi-line message is needed.

Examples:
- Added user authentication module
  - Added login and logout functions
  - Added session token management
  - Added password hashing

- Fixed null pointer exception in parser
  - Added null check before dereferencing
  - Added unit test for edge case

- Renamed ambiguous variables, removed magic numbers
  - Renamed `ns` to `premise_module`
  - Replaced hardcoded 10 with MIN_RESULTS_PER_TERM
  - Replaced hardcoded 2026 with CURRENT_YEAR
```

## Branch Naming

```
Branch names must be self-explanatory and follow the pattern:

[label]/[brief-description]

The [label] prefix must match an existing GitHub label in the repository.
If no suitable label exists, suggest creating one before creating the branch.

Examples (using byteshiftlabs standard labels):
- feature/user-authentication
- fix/parser-null-pointer
- code-refactor/remove-magic-numbers
- docs-refactor/api-reference
- tests/validation-coverage
```

## Pull Requests

```
PR titles follow the same format as commit messages (past participle).

When creating a PR:
- Assign the PR creator to the PR
- Apply the proper existing GitHub label(s)
- If no suitable label exists, suggest creating a new label and wait for user approval before proceeding

Description must include:
- Summary: What changed, in a sentence or two
- Changes: One line per change, grouped by theme or file
- Testing: What was actually run

State what changed and nothing else. Leave out the reasoning behind the
change, how the problem was found, why an alternative was rejected, and what a
tool does. Explaining why is the developer's job, not yours.

Facts a reviewer needs belong in: a corrected value, a count, a removed file.
Sentences beginning "because", "this means", or "the cause was", and any
recounting of what you checked and in what order, stay out. A before/after
table beats a paragraph explaining a discrepancy.

Keep all sections brief and factual.
```

## Releases

```
Use semantic versioning for all tags and GitHub Releases:

- vX.Y.Z for final releases
- vX.Y.Z-alpha.N, vX.Y.Z-beta.N, or vX.Y.Z-rc.N for pre-releases when needed

Bump rules:
- Patch (Z): backward-compatible bug fixes, release hardening, CI/tooling fixes, test-only coverage, and documentation corrections
- Minor (Y): backward-compatible feature additions or meaningful supported-scope expansion
- Major (X): breaking changes or compatibility resets

Release names and annotated git tags must match exactly.
Create releases from the merged default branch unless the repository documents a maintenance-branch workflow.

Release notes must include:
- Summary: what changed and why this version exists
- Changes: bullet list of user-visible fixes/features
- Verification: how the release was tested or validated
```

## Tips

- Keep one logical change per commit
- Reference issue numbers when applicable (for example, `Fixed #123`)
- Apply this format consistently across byteshiftlabs repositories unless a repository documents different rules
- Audit findings files must stay local and must not be pushed to byteshiftlabs repositories
- Before committing, check whether README.md or ROADMAP.md need updating to reflect the change. See [documentation.md](../setup/documentation.md#keeping-readmemd-and-roadmapmd-in-sync).
