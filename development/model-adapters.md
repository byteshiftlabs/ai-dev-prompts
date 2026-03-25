# Model Adapters

Tune prompt shape by model family without forking the full agent stack.

## Purpose

Use this guide when the same workflow behaves differently across model families.

Keep the shared contract stable. Change only the prompt shape, instruction ordering, and redundancy level needed to improve reliability for the active model.

## Adapter Strategy

Apply model-specific tuning only in a thin adapter layer.

Do not rewrite task workflows unless evaluation shows that the workflow itself is the problem.

## Shared Baseline

These rules should remain shared unless evidence proves otherwise:

- safety and policy boundaries
- repository constraints
- tool-use permissions
- required verification
- stop conditions and completion criteria

## GPT-Family Adapter

GPT-family models usually respond well to explicit operational structure.

Prefer:

- clear priority ordering
- direct success criteria
- numbered steps for multi-stage tasks
- explicit separation between planning, execution, and verification
- concrete format requirements near the top of the prompt

Watch for:

- overfitting to literal wording
- excessive compliance text in the final answer
- rigid behavior when too many overlapping rules are present

Recommended adjustments:

```text
Use the shared contract as written.

For this model family:
- Put the most important constraints first.
- Use numbered execution steps for complex tasks.
- State the completion check explicitly.
- Keep formatting rules concrete and close to the requested output.
```

## Claude-Family Adapter

Claude-family models usually benefit from cleaner grouping and less duplicated instruction pressure.

Prefer:

- semantically grouped rules
- fewer repeated constraints
- concise but explicit scope boundaries
- higher-level framing followed by a short execution pattern

Watch for:

- smoothing over precise operational rules when the instruction stack is noisy
- following the spirit of a rule while missing a required mechanical detail
- answering elegantly without showing enough concrete verification

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

- Forking the whole prompt stack after one bad run
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