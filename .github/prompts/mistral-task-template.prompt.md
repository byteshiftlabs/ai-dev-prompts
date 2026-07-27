---
name: "Mistral Task Template"
description: "Use after the bootstrap step to draft a Mistral-oriented task prompt with a hierarchical structure, explicit format, and only the guidance that matters."
agent: "agent"
argument-hint: "Describe the task, project context, and selected guides"
tools:
  - read
---

# Mistral Task Template

Draft a task prompt for a Mistral model.

Use these references:

- [core/shared-contract.md](../../core/shared-contract.md)
- [development/model-adapters.md](../../development/model-adapters.md)
- [prompt-bootstrap.prompt.md](./prompt-bootstrap.prompt.md)

Requirements:

1. Start with the invariant rules from the shared contract.
2. Open with "You are a [role], your task is to [task]."
3. Organize the prompt into clearly labeled sections.
4. State output format explicitly; use structured output mode for strict formats.
5. Replace vague qualifiers with objective, measurable criteria.
6. Include only the guides selected by the bootstrap step.

Output structure:

- Task summary
- Shared contract
- Selected guides
- Mistral adapter rules
- Execution pattern
- Verification and stop condition

Inputs:

- `TASK`: [TASK]
- `PROJECT_CONTEXT`: [PROJECT_CONTEXT]
- `SELECTED_GUIDES`: [SELECTED_GUIDES]
