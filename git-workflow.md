# Git Workflow

Conventions for commits, branches, and pull requests.

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
Use past participle for all commit messages. Be brief, clear, and concise.
List each change with a hyphen.

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

Description must include:
- Summary: What was changed and why
- Changes: Bullet list of specific modifications
- Testing: How the changes were verified

Keep all sections brief and factual.
```

## Tips

- One logical change per commit
- Reference issue numbers when applicable (e.g., "Fixed #123")
- Apply this format consistently across all byteshiftlabs repositories
