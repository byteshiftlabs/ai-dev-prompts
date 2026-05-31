---
pack: task-workflows
summary: Covers assistant host setup, runtime support checks, and integration boundaries.
tags: [workflow, host, integration]
---

# Host Integration

Configure the assistant for the actual host runtime before doing substantive work.

This guide covers the operating environment around the model:

- host capabilities
- instruction-file placement
- persistent project summaries
- memory availability
- tool permissions
- reusable commands and automation entry points

Use this guide when the task is about assistant setup, first-use configuration, runtime behavior, or adapting the prompt system to a specific host.

## Core Principle

Do not treat all assistant hosts as interchangeable.

Before relying on memory, hooks, commands, browser automation, notebooks, GitHub actions, or external tools, verify that the host actually supports them and document how they are configured.

Good prompts are not enough if the host is set up incorrectly.

## First-Use Setup

On first use in a new host or repository:

1. Identify the host and what it supports.
2. Determine where project-level instructions belong.
3. Determine whether local-only or machine-level instructions also exist.
4. Check whether memory is available and how it is separated from session context.
5. Check how tool permissions are granted, denied, or scoped.
6. Look for an existing project summary file and refresh it if stale.
7. Only then start substantive implementation work.

If the host does not support a capability, do not pretend it exists. Use the nearest supported option and say so plainly.

## Capability Checklist

Verify which of these the host supports:

- memory support
- repository-scoped memory
- session summaries or compaction
- instruction files at project, local, or machine scope
- tool permission controls
- pre-tool or post-tool hooks
- reusable commands
- external tool servers or similar integrations
- notebook execution
- browser automation
- GitHub or CI automation

Record only capabilities that are confirmed.

## Instruction Layers

Separate instruction sources by scope.

### Project-level instructions

Use for shared repository rules that should be committed and visible to collaborators.

Examples:

- architecture constraints
- testing and verification rules
- repository-specific build and release workflow
- shared output conventions

### Local user instructions

Use for personal workflow preferences that should not be committed.

Examples:

- preferred verbosity
- preferred tools among equivalent options
- local machine workflow notes

### Machine or global instructions

Use for cross-project defaults that apply to nearly all work.

Examples:

- default communication style
- default tool restrictions
- personal safety boundaries beyond repository policy

Do not store repository policy in machine-level instructions unless it truly applies everywhere.

## Persistent Project Summary

If the host supports a persistent project summary file, keep one.

The summary should stay compact and practical. It should help the assistant orient quickly without forcing it to reload the entire repository each time.

Good contents:

- project purpose
- main entry points
- major directories
- key commands for build, test, and run
- important architectural boundaries
- high-risk files or interfaces
- repository-specific constraints that repeatedly matter

Bad contents:

- long prose copied from documentation
- stale implementation details
- temporary task notes
- speculative architecture claims

Refresh the summary when project structure, key commands, or important constraints change.

## Tool Permission Rules

Determine how the host grants tool access before asking the model to rely on tools.

Check:

- whether tools are enabled by default or require allow-listing
- whether write tools need explicit approval
- whether external integrations need separate permission entries
- whether the permission model differs between local runs and CI or GitHub automation

Do not write prompts that assume tools are available when the host may block them.

## Commands, Hooks, And Automation

If the host supports reusable commands, hooks, or workflow automation, define clearly:

- when they should be used
- what they are allowed to do
- what feedback they send back to the model
- what happens when they block an action

Prefer a small number of high-value automations over a large number of overlapping ones.

Good early candidates:

- post-edit lint or type-check hooks
- secret-file access blocking hooks
- reusable release-audit commands
- duplicate-code checks for high-risk directories

## Host Capability Matrix

Use a compact matrix when documenting runtime behavior:

| Capability | Supported? | How it is configured | Fallback if absent |
|------------|------------|----------------------|--------------------|
| Memory support | yes/no | [tool or mechanism] | session context only |
| Project instructions | yes/no | [file or setting] | explicit prompt context |
| Hooks | yes/no | [config path] | manual verification step |
| Commands | yes/no | [command mechanism] | prompt templates |
| External tools | yes/no | [integration mechanism] | local tool subset |
| CI or GitHub automation | yes/no | [workflow path] | local execution |

Keep this matrix factual. Do not mark support as available unless it has been verified.

## Prompt

```
Configure the assistant for [PROJECT_NAME] in its actual host environment.

Host/runtime: [HOST]
Task: [TASK]
Known capabilities: [CAPABILITIES]
Instruction files or config locations: [FILES]

Do the following:
1. Verify actual host capabilities before relying on them.
2. Separate project, local, machine, session, and memory concerns.
3. Identify the correct place for persistent project summary information.
4. Document tool permissions and runtime constraints.
5. Recommend the smallest reliable setup that supports the task.
```

## Variations

### First-time repository setup

```
Set up this repository for first-time assistant use in the current host.
Identify instruction files, memory support, tool permissions, and any persistent project summary mechanism.
Keep the setup minimal and reproducible.
```

### Host migration

```
This prompt system was designed in one coding host and is being moved to another.
Map the old behavior to the new host honestly.
List capabilities that carry over, capabilities that must be reimplemented, and capabilities that do not exist.
```

### Runtime audit

```
Audit the current assistant runtime configuration for hidden assumptions.
Check memory, permissions, hooks, commands, and external tool integrations.
Flag anything the prompts assume but the host does not actually provide.
```

## Tips

- Treat host capability checks as a prerequisite, not an afterthought.
- Keep persistent project summaries short and maintainable.
- Prefer explicit fallbacks over pretending a feature exists.
- When a host supports multiple instruction scopes, decide which one owns each rule.
- If the task is about remembered instructions, use this guide with [core/memory-contract.md](../core/memory-contract.md) and [development/context-management.md](context-management.md).