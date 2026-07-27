---
name: "Grok Task Template"
description: "Use after the bootstrap step to draft a Grok-oriented task prompt with a Goal/Constraints/Tools/Deliverables structure and only the guidance that matters."
agent: "agent"
argument-hint: "Describe the task, project context, and selected guides"
tools:
  - read
---

# Grok Task Template

Draft a task prompt for a Grok model.

Use these references:

- [core/shared-contract.md](../../core/shared-contract.md)
- [development/model-adapters.md](../../development/model-adapters.md)
- [prompt-bootstrap.prompt.md](./prompt-bootstrap.prompt.md)

Requirements:

1. Start with the invariant rules from the shared contract.
2. Separate sections with XML tags or markdown headers.
3. For agentic or tool-using tasks, structure the prompt as Goal, Constraints, Available tools, Deliverables.
4. Use markdown deliberately in the response: bullets, bold, inline code, and tables where they fit.
5. Include only the guides selected by the bootstrap step.

Output structure:

- Task summary
- Shared contract
- Selected guides
- Grok adapter rules
- Execution pattern
- Verification and stop condition

Inputs:

- `TASK`: [TASK]
- `PROJECT_CONTEXT`: [PROJECT_CONTEXT]
- `SELECTED_GUIDES`: [SELECTED_GUIDES]
