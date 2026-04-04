---
pack: task-workflows
summary: Helps compare prompts and decide whether guidance should stay shared or split.
tags: [workflow, prompts, evaluation]
---

# Prompt Evaluation

Use small, repeatable evaluations to decide what should stay shared and what should split by model family.

## Purpose

Prompt tuning without evaluation turns into folklore.

Use this guide to compare prompt layers across models, isolate failure modes, and decide whether a change belongs in the shared contract, a model adapter, or a task guide.

## Evaluation Rule

Change one layer at a time.

If you change the shared contract, the adapter, and the workflow in one pass, you will not know which change caused the result.

## Suggested Benchmark Set

Build a compact benchmark of real tasks from your repository or workflow.

Include at least one task from each category:

- repository exploration
- bug fixing
- narrow refactoring
- code review
- strict formatting compliance
- tool-use discipline
- ambiguous-request handling
- verification and stop-when-done behavior

Ten to twenty tasks is usually enough to expose recurring patterns.

## Evaluation Matrix

For each task, record:

- model family and version
- shared contract version
- adapter version
- workflow prompt version
- task outcome
- verification quality
- notable failure mode

Use a simple table like this:

| Task | Model | Shared Contract | Adapter | Workflow | Outcome | Main Failure Mode |
|------|-------|-----------------|---------|----------|---------|-------------------|
| Refactor parser | GPT | v1 | gpt-v1 | shared-refactor | pass | none |
| Refactor parser | Claude | v1 | claude-v1 | shared-refactor | partial | missed formatting rule |

## Failure-Mode Taxonomy

Classify failures before editing prompts:

- missed hard constraint
- poor scope control
- weak decomposition
- incorrect tool use
- insufficient verification
- low factual precision
- format non-compliance
- unnecessary verbosity
- premature stopping

Do not use vague labels like "felt weaker" or "less smart."

## Decision Rules

Use these rules after the evaluation pass:

- If multiple models fail the same rule, fix the shared contract or the workflow
- If one model family fails and the others are stable, tune the adapter first
- If only one workflow shows the issue, change the workflow before touching the shared layer
- If a prompt change improves one metric but hurts verification or scope control, reject it

## Example Review Prompt

```text
Compare these benchmark results across model families.

For each recurring failure mode:
1. Identify the most likely prompt layer responsible
2. Recommend the smallest change that could fix it
3. Explain what should remain shared versus what should become model-specific
4. Reject changes that add redundancy without evidence
```

## Operating Advice

- Prefer production-like tasks over synthetic trivia
- Re-run a small control set after every meaningful prompt change
- Keep old prompt versions so regressions are traceable
- Optimize for reliability, not just elegance or verbosity
- Treat anecdotes as leads, not conclusions