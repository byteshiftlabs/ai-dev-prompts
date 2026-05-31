---
name: "Reasoning Model Task Template"
description: "Use after the bootstrap step to draft a task prompt for reasoning models (o1, o3, Claude extended thinking). Keeps instructions minimal and open-ended so the model can reason internally without prescriptive scaffolding."
agent: "agent"
argument-hint: "Describe the task, project context, and selected guides"
tools:
  - read
---

# Reasoning Model Task Template

Draft a task prompt for a reasoning model (OpenAI o1 / o3 or Claude with extended thinking enabled).

Use these references:

- [core/shared-contract.md](../../core/shared-contract.md)
- [development/model-adapters.md](../../development/model-adapters.md)
- [prompt-bootstrap.prompt.md](./prompt-bootstrap.prompt.md)

Requirements:

1. Start with the invariant rules from the shared contract.
2. State the problem and the success criteria. Do not describe how to reason.
3. List hard constraints the answer must satisfy.
4. Keep instruction count low — fewer instructions produce more thorough internal reasoning.
5. Do not add chain-of-thought instructions or stepped reasoning templates.
6. Do not include few-shot reasoning examples — they anchor the model to a shallow pattern.
7. State the required output format directly and once.
8. Include only the guides selected by the bootstrap step.

Output structure:

- Task summary
- Shared contract
- Selected guides
- Reasoning model adapter rules
- Success criteria and hard constraints
- Output format

Inputs:

- `TASK`: [TASK]
- `PROJECT_CONTEXT`: [PROJECT_CONTEXT]
- `SELECTED_GUIDES`: [SELECTED_GUIDES]
