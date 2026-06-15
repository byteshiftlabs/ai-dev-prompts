---
pack: task-workflows
summary: High-recall audit workflow for thorough coverage and explicit findings accounting.
tags: [workflow, audit, exhaustive]
---

# Exhaustive Review

Use this when you want the agent to maximize issue recall in a single invocation and maintain one authoritative findings document while it works.

## Reality Check

No prompt can guarantee detection of absolutely all issues in one pass.

What you *can* do is raise recall sharply by forcing the model to:
- map the review surface before judging code
- review by risk category instead of by vibe
- keep a coverage ledger so nothing is silently skipped
- record findings into a single markdown file as the source of truth
- distinguish confirmed issues from suspicions and unreviewed areas

This turns “one pass” into one *structured* pass with internal sub-stages.

If you want a ready-to-run artifact instead of assembling the prompt manually, use [public-release-audit.prompt.md](public-release-audit.prompt.md).

---

## Use This Instead Of Persona Alone

Personas change tone and standards.
They do not guarantee coverage.

For release-quality review, combine:
- a persona, if desired, for voice and standards
- this protocol, for coverage and output structure
- core/production-ready-check.md, for release gating

---

## Main Prompt

```
Perform an exhaustive review of [PROJECT_NAME] in one structured pass.

Your goal is not to be brief. Your goal is to maximize recall and leave no review surface unaccounted for.

Before judging code, do this in order:

1. Build a review inventory.
   Enumerate the relevant files, modules, entry points, tests, docs, config, packaging, CI, and release assets.
   Group them into review surfaces.

2. Build a coverage matrix.
   For each surface, track status as one of:
   - reviewed
   - partially reviewed
   - not reviewed
   - uncertain

3. Create or update [OUTPUT_MD_FILE] immediately.
   This file is the authoritative audit log for the session.
   Write into it as you work. Do not wait until the end.

4. Review every surface against these dimensions:
   - correctness and crashes
   - error handling and recovery
   - security and secrets exposure
   - concurrency and shared state
   - data integrity and serialization
   - API and CLI contract stability
   - configuration and packaging
   - documentation accuracy
   - test coverage and missing cases
   - release readiness and reproducibility

5. For every issue, record:
   - ID: B1/B2... S1/S2... M1/M2...
   - severity: Blocker, Serious, Minor
   - location: file and line
   - confidence: confirmed / likely / needs verification
   - why it matters
   - recommended fix
   - whether a test exists for it

6. For every area with no findings, explicitly say so.
   Silence is not allowed. Every review surface must end with a status.

7. End with these sections in [OUTPUT_MD_FILE]:
   - Executive Summary
   - Findings Table
   - Coverage Matrix
   - Unreviewed or Uncertain Areas
   - Merge / Release Recommendation
   - Ordered Fix Plan

Rules:
- Do not claim certainty where you do not have evidence.
- Do not collapse different issue classes into one generic note.
- Do not stop at code; include docs, tests, packaging, and public release assets.
- If context is too large, state exactly what was not reviewed.
- If a claim depends on runtime behavior, say how it should be verified.

[OPTIONAL_PERSONA]
[PROJECT_CONTEXT]
```

---

## Findings File Template

Use this structure for [OUTPUT_MD_FILE]:

```md
# [PROJECT_NAME] Audit Findings

## Executive Summary
- Total blockers:
- Total serious issues:
- Total minor issues:
- Overall recommendation:

## Findings Table
| ID | Severity | Confidence | File | Issue | Recommended Fix |
|----|----------|------------|------|-------|-----------------|

## Detailed Findings

### Blockers
#### B1
- Location:
- Confidence:
- Problem:
- Why it matters:
- Recommended fix:
- Test gap:

### Serious

### Minor

## Coverage Matrix
| Surface | Files / Modules | Status | Notes |
|---------|------------------|--------|-------|

## Unreviewed Or Uncertain Areas
- Surface:
- Why unreviewed or uncertain:
- Required follow-up:

## Merge / Release Recommendation
- Merge now / Do not merge
- Release now / Do not release
- Preconditions:

## Ordered Fix Plan
1. B1...
2. B2...
3. S1...
```

---

## High-Recall Variations

### Public Release Audit

```
Run an exhaustive public-release audit of [PROJECT_NAME].
Use exhaustive-review.md and core/production-ready-check.md together.
Write all findings to [OUTPUT_MD_FILE].
No review surface may be omitted without being listed under "Unreviewed Or Uncertain Areas".
```

### PR Audit With Findings File

```
Review this PR in one structured pass.
Do not only comment inline.
Create or update [OUTPUT_MD_FILE] with a severity-ranked findings file,
a coverage matrix, and an ordered fix plan.
```

### Fix-Then-Recheck Workflow

```
1. Run exhaustive-review.md and write findings to [OUTPUT_MD_FILE].
2. Fix findings in severity order.
3. Re-run the same audit.
4. In the same file, mark each prior finding as fixed / still open / regressed.
```

---

## Tips

- “One pass” should mean one invocation, not one shallow skim.
- The coverage matrix is the key mechanism: it prevents silent omission.
- Require explicit “no findings” statements per review surface.
- Require confidence labels so speculative comments do not masquerade as confirmed bugs.
- Require a findings file from the start, not as an afterthought.
- For large repos, review by subsystem and keep the file cumulative.