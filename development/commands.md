---
pack: task-workflows
summary: Guidance for reusable command workflows and command-driven host integrations.
tags: [workflow, commands, host]
---

# Commands

Use reusable commands to package recurring workflows into stable, low-friction entry points.

This guide applies to hosts that support reusable commands, command files, prompt wrappers, helper scripts, or similar entry points.

## Core Principle

Use commands for repeatable workflow entry, not for hiding complexity.

A command is justified when it does one recurring job clearly and saves the user from repeatedly restating the same setup.

Good command candidates:

- release audit
- fix-and-recheck loop
- dependency audit
- prompt evaluation run
- narrow repository-specific workflows with stable inputs

Bad command candidates:

- one-off tasks
- vague commands like `/do-everything`
- commands that silently bundle unrelated workflows
- commands whose side effects are unclear from the name

## Command Design Rules

Every command should define:

- its purpose
- expected arguments
- whether arguments are optional or required
- what context it assumes
- what files or tools it may touch
- what success looks like

Commands should be clear enough that a new user can tell when to use them and what will happen.

## Naming Rules

Prefer names that are:

- short
- action-oriented
- specific to the workflow

Good examples:

- `/release-audit`
- `/fix-findings`
- `/review-pr`
- `/prompt-benchmark`

Bad examples:

- `/run`
- `/work`
- `/full-process`

## Argument Design

Accept only the minimum arguments that actually vary.

Good argument examples:

- target file or module
- issue number
- prompt variant name
- environment or host name

Do not force users to pass arguments that the command can derive reliably from the current repository or session.

If arguments are free-form, state how they will be interpreted.

## Command Contract

Document for each command:

- trigger syntax
- argument format
- expected preconditions
- output format or artifact expectations
- whether the command is read-only or may modify files

If the host requires a restart or reload after adding commands, state that explicitly.

## Command Composition

Commands may call into other guides, but each command should still expose one clear workflow.

Prefer:

- one command per recurring task
- small reusable commands over giant umbrella commands
- explicit pairing with routing when the task is broad

Avoid:

- commands that smuggle in review, refactor, release, and docs work all at once
- commands that bypass verification rules
- commands that duplicate each other with slightly different names

## Prompt

```
Design or review a reusable command for [PROJECT_NAME].

Host: [HOST]
Workflow to automate: [WORKFLOW]
Expected arguments: [ARGUMENTS]
Expected permissions or tools: [TOOLS]

Do the following:
1. Decide whether this workflow should be a command.
2. Define the command purpose and argument contract.
3. Keep the command scope narrow and explicit.
4. State what it reads, writes, or verifies.
5. Describe the success condition.
```

## Variations

### Command creation

```
Create a reusable command for a recurring workflow.
Choose the smallest stable interface that captures the real task.
```

### Command audit

```
Audit the existing command set for overlap, vague naming, hidden side effects, and missing argument documentation.
Recommend consolidation where appropriate.
```

### Command migration

```
This workflow currently exists as a prompt or manual checklist.
Convert it into a command-friendly interface without losing verification requirements.
```

## Pairing Guidance

Use this guide with:

- [development/host-integration.md](host-integration.md) to verify that the host supports commands
- [development/task-decomposition.md](task-decomposition.md) when the workflow is multi-stage
- [development/prompt-evaluation.md](prompt-evaluation.md) when deciding whether a command actually improves reliability

## Tips

- Keep commands boring and predictable.
- Make arguments explicit, but not noisy.
- Prefer command names that describe the workflow result, not the implementation detail.
- If the host does not support commands, fall back to prompt templates or documented helper scripts.