---
mode: ask
description: "Use after an audit findings file exists. Fix issues in severity order, update the findings ledger in place, add missing tests, and re-run the audit or targeted verification before closing items."
tools:
  - codebase
  - edits
---

# Fix And Recheck

Consume an existing audit findings file, resolve issues in priority order, and update the same ledger with current status.

## Inputs

- `PROJECT_NAME`: project or repository name
- `FINDINGS_MD_FILE`: path to the existing audit findings markdown file
- `PROJECT_CONTEXT`: short description of the project, stack, and constraints
- `OPTIONAL_PERSONA`: optional standards/tone layer, for example Silvanus from `core/personas.md`

## Prompt

```text
Fix and recheck PROJECT_NAME using FINDINGS_MD_FILE as the source of truth.

Context:
PROJECT_CONTEXT

Use these guides together:
- development/exhaustive-review.md
- core/production-ready-check.md
- development/test-generation.md
- development/git-workflow.md
- development/error-handling.md

Optional tone / standards layer:
OPTIONAL_PERSONA

Requirements:
1. Read FINDINGS_MD_FILE first and treat it as authoritative.
2. Work strictly in severity order:
   - all Blockers first
   - then all Serious issues
   - then all Minor issues
3. Within each severity, work in numeric order unless a dependency forces a different sequence.
4. After each fix:
   - update FINDINGS_MD_FILE in place
   - mark the item as fixed / still open / partially fixed / regressed
   - add a short verification note
   - add or update tests when the issue should be test-covered
5. If a finding cannot be fixed safely, do not hand-wave it away.
   Record the blocker, why it remains open, and the exact follow-up needed.
6. After the fix pass, perform a recheck:
   - re-run the relevant tests or checks
   - re-audit changed areas
   - update the merge/release recommendation in FINDINGS_MD_FILE

Rules:
- Do not skip to minor cleanup while blocker or serious issues remain open.
- Do not silently change issue numbering unless you also update the ledger consistently.
- Do not mark an item fixed without evidence from code, tests, docs, or commands.
- Preserve unresolved items in the ledger; do not delete them to make the file look clean.
- If new issues are discovered during fixes, append them with the next available severity ID.
```

## Example Invocation

```text
PROJECT_NAME: premise
FINDINGS_MD_FILE: docs/audit-findings.md
PROJECT_CONTEXT: Python research search tool with CLI, GUI, external APIs, cache layer, packaging metadata, and unit tests. Goal is public release with outstanding code, docs, and tests.
OPTIONAL_PERSONA: Use Silvanus Trold for standards and bluntness, but keep the fix notes constructive and evidence-based.
```

## Expected Output Characteristics

- The findings ledger remains the single source of truth
- Issues are closed in severity order, not convenience order
- Every closed item has evidence
- Recheck results are written back into the same file
- The final recommendation reflects current reality, not the original audit