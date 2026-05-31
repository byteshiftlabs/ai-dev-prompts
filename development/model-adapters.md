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

### XML Tags for Claude

Claude parses structured sections more reliably when content is wrapped in XML tags. Use tags to separate instructions, context, examples, and output format.

```text
<instructions>
[task rules and steps]
</instructions>

<context>
[background the model needs to understand the task]
</context>

<example>
Input: [example input]
Output: [example output]
</example>

<output_format>
[what the response must look like]
</output_format>
```

Do not mix XML tag structure with markdown header structure at the same level. Use one or the other per block.

### Assistant Prefilling for Claude

Claude treats the start of its own turn as a strong formatting signal. Prefill the assistant turn with the exact token you want the response to begin with. This locks the output format before the model begins generating.

Example: to force a JSON response, end your human turn and open the assistant turn like this:

```text
[your prompt here]
```

The assistant will begin its response from that token, preventing preamble and enforcing format from the first character. Useful for locking JSON, YAML, code blocks, or specific section headers.

## Reasoning Model Adapter

Use this adapter for models that run extended internal reasoning before responding: Claude with extended thinking enabled, and OpenAI o1 / o3 family models.

These models internally generate a chain of reasoning that is not visible in the response. Because of this, the prompting patterns that work for standard models are counterproductive here.

**Do not use with reasoning models:**

- Explicit chain-of-thought instructions ("think step by step", "reason through this in order")
- Stepped reasoning templates from `chain-of-thought.md` — the model already does this internally
- Over-specified decomposition prompts that prescribe how to reason

**Do use with reasoning models:**

- Open-ended problem framing that gives the model room to explore
- Explicit constraints and success criteria (state what the answer must satisfy, not how to find it)
- Minimal instruction count — fewer instructions produce more thorough internal reasoning
- Direct questions rather than step-by-step procedures

Recommended adjustments:

```text
Use the shared contract as written.

For reasoning models (o1, o3, Claude extended thinking):
- State the problem and the success criteria. Do not prescribe reasoning steps.
- List hard constraints the answer must satisfy.
- Do not add chain-of-thought instructions — the model reasons internally.
- Keep the prompt shorter than you would for a standard model.
- Trust a longer, slower response. It reflects genuine internal exploration.
```

**Claude extended thinking:** Enable via the API `thinking` parameter. Do not instruct the model to think step by step in the prompt — set the budget tokens parameter instead and let the model allocate reasoning effort.

**o1 / o3:** These models perform best with direct task statements and explicit output format requirements. Do not add few-shot reasoning examples; they can anchor the model to a shallow pattern instead of letting it reason fully.

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