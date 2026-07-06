---
name: "Gemini Task Template"
description: "Use after the bootstrap step to draft a Gemini-oriented task prompt with clear delimiters, role and format stated up front, and only the guidance that matters."
agent: "agent"
argument-hint: "Describe the task, project context, and selected guides"
tools:
  - read
---

# Gemini Task Template

Draft a task prompt for a Gemini model.

Use these references:

- [core/shared-contract.md](../../core/shared-contract.md)
- [development/model-adapters.md](../../development/model-adapters.md)
- [prompt-bootstrap.prompt.md](./prompt-bootstrap.prompt.md)

Requirements:

1. Start with the invariant rules from the shared contract.
2. State role, constraints, and output format at the very start of the prompt.
3. Separate instructions, context, and examples with clear delimiters (XML tags or headings).
4. Include a few consistent examples rather than none.
5. Keep each prompt to one task; split multi-part work into separate prompts.
6. Include only the guides selected by the bootstrap step.

Output structure:

- Task summary
- Shared contract
- Selected guides
- Gemini adapter rules
- Execution pattern
- Verification and stop condition

Inputs:

- `TASK`: [TASK]
- `PROJECT_CONTEXT`: [PROJECT_CONTEXT]
- `SELECTED_GUIDES`: [SELECTED_GUIDES]
