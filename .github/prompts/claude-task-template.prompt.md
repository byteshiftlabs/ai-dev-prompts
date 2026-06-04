---
name: "Claude Task Template"
description: "Use after the bootstrap step to draft a Claude-oriented task prompt with clean grouping, low redundancy, and relevant guidance only."
agent: "agent"
argument-hint: "Describe the task, project context, and selected guides"
tools:
  - read
---

# Claude Task Template

Draft a task prompt for a Claude-family model.

Use these references:

- [core/shared-contract.md](../../core/shared-contract.md)
- [development/model-adapters.md](../../development/model-adapters.md)
- [prompt-bootstrap.prompt.md](./prompt-bootstrap.prompt.md)

Requirements:

1. Start with the invariant rules from the shared contract.
2. Group related constraints instead of scattering them.
3. Keep the prompt clear, compact, and low in redundancy.
4. State the exact mechanical requirements once, plainly.
5. Include only the guides selected by the bootstrap step.
6. Avoid instruction collisions caused by repeated or overlapping reminders.
7. Keep verification concrete even when the prompt framing is high-level.

Output structure:

- Task summary
- Shared contract
- Selected guides
- Claude adapter rules
- Execution pattern
- Verification and stop condition

Inputs:

- `TASK`: [TASK]
- `PROJECT_CONTEXT`: [PROJECT_CONTEXT]
- `SELECTED_GUIDES`: [SELECTED_GUIDES]