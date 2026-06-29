---
pack: prompt-routing
summary: Describes how prompt structure should vary by model family without changing task rules.
tags: [routing, adapter, model-family]
---

# Model Adapters

Adjust prompt structure by model family without rewriting the whole system.

## Purpose

Use this guide when the same workflow behaves differently across model families.

Keep the shared contract stable. Change only the prompt structure, instruction order, and repetition level needed to improve reliability for the active model.

## Adapter Strategy

Apply model-specific tuning only in a thin adapter layer.

Do not rewrite task guides unless evaluation shows that the guide itself is the problem.

## Shared Baseline

These rules should remain shared unless evidence proves otherwise:

- safety and policy boundaries
- repository constraints
- tool permissions
- required verification
- stop conditions and completion criteria

## GPT-Family Adapter

GPT-family models usually respond well to explicit structure.

Prefer:

- clear priority ordering
- direct success criteria
- numbered steps for multi-stage tasks
- explicit separation between planning, execution, and verification
- concrete format requirements near the top of the prompt

Watch for:

- following wording too literally
- excessive compliance text in the final answer
- rigid behavior when too many overlapping rules are present
- defaulting to abstract, jargon-heavy language instead of plain explanations
- framing simple concepts in academic or consulting register when direct wording is clearer

Recommended adjustments:

```text
Use the shared contract as written.

For this model family:
- Put the most important constraints first.
- Use numbered execution steps for complex tasks.
- State the completion check explicitly.
- Keep formatting rules concrete and close to the requested output.
- Write in plain, direct language. Prefer concrete words over abstract nouns.
  Say "check that X matches Y" instead of "enforce a compatibility invariant".
  Say "the build fails if versions differ" instead of "a machine-enforced
  compatibility marker beyond documented release discipline".
  If a sentence would confuse a junior developer, rewrite it.
```

## Claude-Family Adapter

Claude-family models usually benefit from cleaner grouping and less repeated instruction.

Prefer:

- related rules grouped together
- fewer repeated constraints
- concise but explicit scope boundaries
- higher-level framing followed by a short execution pattern

Watch for:

- following the general idea while missing a specific mechanical requirement
- giving a polished answer without enough concrete verification

Recommended adjustments:

```text
Use the shared contract as written.

For this model family:
- Group related constraints together instead of repeating them.
- Remove redundant wording before adding stronger wording.
- Keep the workflow conceptually clear and avoid instruction collisions.
- Restate exact verification or output requirements once, plainly.
```

## When To Split A Workflow Prompt

Split a workflow prompt by model family only if all of the following are true:

1. The shared contract is already stable
2. The adapter layer has been tried first
3. The failure recurs in the same workflow across multiple tasks
4. Evaluation shows a real improvement from a workflow-specific split

If those conditions are not met, keep one shared workflow.

## Minimal Adapter Template

```text
Shared contract:
- [insert invariant rules]

Model adapter for [MODEL_FAMILY]:
- [instruction ordering rule]
- [verbosity or decomposition rule]
- [verification emphasis rule]

Task workflow:
- [task-specific procedure]
```

## Common Mistakes

- Forking the whole instruction set after one bad run
- Encoding style preferences as if they were safety rules
- Adding more reminders instead of removing conflicting ones
- Treating model folklore as evidence
- Changing both the adapter and workflow at the same time, which makes results hard to interpret

## Recommended Pairing

When tuning prompts by model family, use this guide together with:

- `core/shared-contract.md`
- `development/context-management.md`
- `development/task-decomposition.md`
- `development/prompt-evaluation.md`