---
mode: ask
description: "Use when performing a high-recall public-release audit in one structured pass. Creates or updates a single markdown findings ledger with coverage tracking, severity-ranked issues, unreviewed areas, and an ordered fix plan."
tools:
  - codebase
  - edits
---

# Public Release Audit

Run a high-recall, coverage-driven audit of a project before public release.

## Inputs

- `PROJECT_NAME`: project or repository name
- `PROJECT_CONTEXT`: short description of the project, stack, and release goals
- `OUTPUT_MD_FILE`: path to the audit findings markdown file to create or update
- `OPTIONAL_PERSONA`: optional standards/tone layer, for example Silvanus from `core/personas.md`

## Prompt

```text
Perform an exhaustive public-release audit of PROJECT_NAME in one structured pass.

Context:
PROJECT_CONTEXT

Use development/exhaustive-review.md as the canonical audit protocol.
Follow its workflow, output structure, and evidence rules exactly.

Use core/production-ready-check.md as the public-release gate.
It defines what must be true before a public release is acceptable.

Use these supporting guides where relevant:
- development/code-review.md
- development/test-generation.md
- development/error-handling.md
- development/content-integrity.md

Optional tone / standards layer:
OPTIONAL_PERSONA

Create or update OUTPUT_MD_FILE immediately and keep it as the authoritative audit ledger.

Additional rules for this release audit:
- Do not claim complete certainty without evidence.
- Do not silently skip docs, tests, packaging, or release assets.
- Do not treat checklist completion as proof; verify with code, tests, docs, or commands.
- If runtime verification is needed, say exactly what should be run.
- If the repository is too large for full confidence, state the exact limit and what remains unchecked.
- For byteshiftlabs repositories, keep the audit findings file local-only. Do not commit or push it.
- End with a clear release recommendation: release now / do not release, plus preconditions.
```

## Example Invocation

```text
PROJECT_NAME: premise
PROJECT_CONTEXT: Python research search tool with CLI, GUI, multiple external APIs, cache layer, packaging metadata, and unit tests. Goal is public release with outstanding code, docs, and tests.
OUTPUT_MD_FILE: docs/audit-findings.md
OPTIONAL_PERSONA: Use Silvanus Trold for standards and bluntness, but keep the audit constructive and evidence-based.
```

## Expected Output Characteristics

- One markdown findings file, updated during the audit
- Explicit coverage accounting
- Explicit reuse of exhaustive-review.md as the protocol source of truth
- A release decision grounded in core/production-ready-check.md