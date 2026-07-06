---
name: "Llama Task Template"
description: "Use after the bootstrap step to draft a Llama-oriented task prompt with an explicit role, concrete constraints, and only the guidance that matters."
agent: "agent"
argument-hint: "Describe the task, project context, and selected guides"
tools:
  - read
---

# Llama Task Template

Draft a task prompt for a Llama model.

Use these references:

- [core/shared-contract.md](../../core/shared-contract.md)
- [development/model-adapters.md](../../development/model-adapters.md)
- [prompt-bootstrap.prompt.md](./prompt-bootstrap.prompt.md)

Requirements:

1. Start with the invariant rules from the shared contract.
2. Open with a clear role or persona statement.
3. Break multi-part work into explicit sub-tasks.
4. State formatting and scope constraints literally and concretely.
5. Ask directly for step-by-step reasoning when the task needs it.
6. Include only the guides selected by the bootstrap step.

Output structure:

- Task summary
- Shared contract
- Selected guides
- Llama adapter rules
- Execution steps
- Verification and stop condition

Inputs:

- `TASK`: [TASK]
- `PROJECT_CONTEXT`: [PROJECT_CONTEXT]
- `SELECTED_GUIDES`: [SELECTED_GUIDES]
