---
pack: task-workflows
summary: Guidance for designing or reviewing automated hooks and feedback loops.
tags: [workflow, hooks, automation]
---

# Hooks

Use hooks to react to tool calls and feed clear feedback back into the assistant workflow.

Hooks are runtime controls, not prompt replacements.

Use them when the host supports commands that run before or after tool calls and when repeated failures can be prevented or corrected automatically.

## Core Principle

Use hooks for repeated, mechanical checks.

Do not use hooks to hide poor prompt design or to create overlapping automation that is hard to understand.

A hook is worthwhile when all of the following are true:

1. the failure mode recurs often
2. the check can be expressed mechanically
3. the hook feedback is specific enough for the model to act on
4. the cost of running the hook is justified by the reduction in errors

## Hook Types

### Pre-tool hooks

Run before a tool call.

Use them to:

- block access to sensitive files
- prevent destructive operations
- enforce path restrictions
- stop forbidden actions before they happen

### Post-tool hooks

Run after a tool call.

Use them to:

- run lint or type checks after edits
- re-run targeted tests
- detect duplicate code in watched areas
- feed concrete diagnostics back into the workflow

Post-tool hooks cannot undo an action that already happened. Their job is to provide fast corrective feedback.

## When To Use Hooks

Good candidates:

- blocking reads of secret files
- type-check or lint verification after edits
- duplicate-code detection in critical directories
- formatting checks after file creation or modification
- enforcing rules for high-risk tools

Bad candidates:

- subjective style preferences
- tasks that need human judgment more than mechanical checks
- heavy full-repository jobs after every small edit
- hooks that overlap and produce conflicting feedback

## Hook Design Rules

Design hooks so the assistant can recover from them.

Every hook should define:

- which tool calls it watches
- what input fields it expects
- what condition triggers feedback or blocking
- what each exit result means in the host
- what feedback message the model should receive

Good hook feedback is concrete.

Good:

- `Blocked read of .env because secrets must not be exposed. Use .env.example instead.`
- `Type check failed in src/api.ts: 3 call sites still use the old function signature.`

Bad:

- `Action not allowed.`
- `Quality check failed.`

## Hook Contracts

Document the hook contract clearly for the active host:

- how hook input is provided
- what output channel is used for feedback
- which exit codes allow, warn, or block
- whether the host supports pre-tool blocking, post-tool feedback, or both

Do not assume a host-specific contract unless the host has been verified.

## Recommended Early Hooks

### Secret-file access blocker

Purpose:
- block reads of `.env`, secret config files, tokens, keys, or credential stores

Best as:
- pre-tool hook

Expected feedback:
- tell the assistant which safe alternative it should use instead

### Type-check or lint hook

Purpose:
- catch signature drift, broken imports, and simple structural mistakes immediately after edits

Best as:
- post-tool hook

Expected feedback:
- include actual diagnostics, not a generic failure message

### Duplicate-code hook

Purpose:
- prevent new helper functions, queries, or components that duplicate existing ones in a high-risk directory

Best as:
- post-tool hook

Expected feedback:
- identify the existing file or symbol that should be reused

## Cost Control

Hooks can easily become slow and noisy.

To keep them useful:

- watch only the tools and directories that matter
- prefer targeted checks over full-repository checks
- avoid running expensive jobs after every trivial edit
- measure whether the hook is catching real problems or just adding friction

If a hook fires often but rarely changes behavior, redesign it or remove it.

## Prompt

```
Design or review hooks for [PROJECT_NAME] in [HOST].

Task: [TASK]
Target tools or actions: [TOOLS]
Watched files or directories: [PATHS]
Known failure mode: [FAILURE_MODE]

Do the following:
1. Decide whether a hook is justified for this failure mode.
2. Choose pre-tool or post-tool behavior.
3. Define the hook contract clearly for the host.
4. Keep the hook feedback specific enough for the assistant to act on.
5. Minimize cost and overlap with other automation.
```

## Variations

### Blocking sensitive files

```
Create a pre-tool hook policy that blocks access to sensitive files such as `.env`.
The feedback must state why access is blocked and what safe alternative file the assistant should use.
```

### Auto-feedback after edits

```
Design a post-tool hook that runs targeted verification after file edits.
Prefer the smallest reliable check, such as a type checker, linter, or focused test subset.
Feed the exact diagnostics back to the assistant.
```

### Duplicate-prevention workflow

```
Design a hook workflow that detects likely duplicate code in a critical directory.
The feedback must point to the existing implementation that should be reused.
```

## Pairing Guidance

Use this guide with:

- [development/host-integration.md](host-integration.md) to verify that the host actually supports hooks
- [development/context-management.md](context-management.md) when hook feedback changes the active session flow
- [development/prompt-evaluation.md](prompt-evaluation.md) when deciding whether a hook meaningfully improves reliability

## Tips

- Start with one or two high-value hooks, not ten mediocre ones.
- Hook feedback should be operational, short, and concrete.
- Keep hooks deterministic where possible.
- If a host does not support hooks, fall back to explicit manual verification steps and say so plainly.