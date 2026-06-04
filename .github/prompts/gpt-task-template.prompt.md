---
name: "GPT Task Template"
description: "Use after the bootstrap step to draft a GPT-oriented task prompt with explicit ordering, completion checks, and relevant guidance only."
agent: "agent"
argument-hint: "Describe the task, project context, and selected guides"
tools:
  - read
---

# GPT Task Template

Draft a task prompt for a GPT-family model.

Use these references:

- [core/shared-contract.md](../../core/shared-contract.md)
- [development/model-adapters.md](../../development/model-adapters.md)
- [prompt-bootstrap.prompt.md](./prompt-bootstrap.prompt.md)

Requirements:

1. Start with the invariant rules from the shared contract.
2. Keep the prompt operational and explicit.
3. Put the most important constraints first.
4. Use numbered steps when the task has multiple stages.
5. State the completion check explicitly.
6. Include only the guides selected by the bootstrap step.
7. Do not duplicate instructions unless the task is high-risk and the repetition is justified.

Output structure:

- Task summary
- Shared contract
- Selected guides
- GPT adapter rules
- Execution steps
- Verification and stop condition

Inputs:

- `TASK`: [TASK]
- `PROJECT_CONTEXT`: [PROJECT_CONTEXT]
- `SELECTED_GUIDES`: [SELECTED_GUIDES]