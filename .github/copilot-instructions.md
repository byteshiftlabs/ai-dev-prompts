# Copilot Instructions

Treat the guides in `core/` as baseline context for work in this workspace.

## Baseline Guides

- `core/personas.md`: default standards and review posture. Use it when reviewing, critiquing, or tightening quality. A persona is a standards layer, not a replacement for evidence.
- `core/production-ready-check.md`: default release gate. Use it when assessing public readiness, release quality, docs completeness, test completeness, packaging, or final polish.
- `core/shared-contract.md`: default cross-model operating contract. Use it when deciding which rules should stay stable across models and which should move into model adapters.

## Expected Behavior

- Before major reviews, audits, fix sweeps, or release preparation, consult the relevant `core/` guide first.
- For public-release or high-stakes audits, pair `core/production-ready-check.md` with `development/exhaustive-review.md`.
- When tuning prompts for different model families, keep `core/shared-contract.md` stable and apply model-specific changes through `development/model-adapters.md`.
- When a task needs prompt setup from a single entry point, start with `.github/prompts/prompt-bootstrap.prompt.md` and load only the guides it selects.
- When a persona is used, keep criticism evidence-based and actionable.
- Do not assume checklist completion proves quality. Verify claims with code, tests, docs, or commands.
- If any area is not reviewed, state that explicitly instead of implying full coverage.

## Working Rule

Use `core/` for cross-cutting standards.
Use `development/` for active workflows and task-specific procedures.
Use `setup/` for project initialization and foundational design guidance.