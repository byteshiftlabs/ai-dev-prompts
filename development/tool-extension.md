---
pack: task-workflows
summary: Covers external tools, browser automation, notebooks, and CI-style extensions.
tags: [workflow, tools, extension]
---

# Tool Extension

Use this guide when the assistant must operate beyond its default tool set.

This includes external tool servers, browser automation, notebook execution, GitHub or CI integrations, domain-specific automation, and SDK-driven helper workflows.

## Core Principle

Treat tool extension as an operating-environment decision, not just a prompt decision.

Only add tools when the new capability clearly improves the task and the permission model is understood.

## When To Extend The Tool Surface

Good reasons:

- browser checks are required for UI work
- notebook execution is required for iterative data analysis
- GitHub or CI integration is required for PR review or issue workflows
- a domain-specific tool can replace manual, error-prone steps
- the current tool set cannot observe or verify the thing that matters

Bad reasons:

- novelty
- adding another tool without adding useful capability
- adding a broad external integration for a narrow one-off task
- using external tools when local tools already cover the need

## Capability Questions

Before recommending or using an extension, answer:

1. What task gap does the extension fill?
2. Is the capability actually available in the host?
3. How is permission granted or denied?
4. What data leaves the local environment, if any?
5. What is the fallback if the extension is unavailable?

Do not recommend an extension without stating the extra cost and permission implications.

## Extension Categories

### Browser and UI automation

Use for:

- visual validation
- interaction testing
- screenshot-driven iteration

Check:

- whether the host supports browser automation directly or through an external server
- whether local development servers must be started first

### Notebook and analysis tools

Use for:

- iterative data exploration
- plotting
- exploratory analysis of datasets or metrics

Check:

- execution permissions
- artifact handling
- whether notebook state is reproducible or only exploratory

### GitHub and CI automation

Use for:

- issue triage
- PR review
- workflow execution
- repository metadata operations

Check:

- explicit permission scopes
- differences between local and CI runtime behavior

### Domain-specific tools

Use for:

- browser-based testing
- infrastructure inspection
- package analysis
- repository-specific automation

Check:

- whether the tool overlaps with existing tools
- whether the tool output is stable enough for automation

## Permission And Safety Rules

Document:

- what the tool can read
- what the tool can modify
- whether approval is one-time or per action
- whether permissions differ between local and hosted runs

For any extension that accesses external systems, say plainly whether code, prompts, data, or screenshots leave the local environment.

## Fallback Design

Every extension recommendation should include a fallback.

Examples:

- if browser automation is unavailable, fall back to static code review and manual test instructions
- if notebook execution is unavailable, fall back to a script-based analysis pass
- if GitHub integration is unavailable, fall back to local git workflow and manual PR text preparation

## Prompt

```
Assess or design a tool-extension strategy for [PROJECT_NAME].

Host: [HOST]
Task: [TASK]
Current tools: [CURRENT_TOOLS]
Candidate extension: [EXTENSION]

Do the following:
1. Explain what gap the extension fills.
2. Verify that the host can support it.
3. Describe permission and safety implications.
4. State what verification becomes possible with the extension.
5. Provide a fallback if the extension is unavailable.

[content-integrity constraint]
```

## Variations

### External server evaluation

```
Evaluate whether an external tool server is justified for this workflow.
Do not recommend it unless the missing capability is real and the permission model is acceptable.
```

### Browser-testing setup

```
Design a browser-automation setup for UI verification.
Include server startup requirements, approval flow, and fallback when automation is unavailable.
```

### CI integration review

```
Review the assistant's CI or GitHub integration.
Check permissions, available tools, verification coverage, and where the workflow still depends on unsupported capabilities.
```

## Pairing Guidance

Use this guide with:

- [development/host-integration.md](host-integration.md) for host capability checks
- [development/hooks.md](hooks.md) when extensions interact with hook-based enforcement
- [development/prompt-evaluation.md](prompt-evaluation.md) when comparing extended vs non-extended workflows

## Tips

- Add tools only when they change what the assistant can verify or do.
- Permission clarity matters as much as capability.
- Prefer the smallest extension that closes the task gap.
- Keep the fallback explicit.