# AI Development Prompts

Reusable prompt patterns for AI-assisted software development.

## What This Repo Is

This repository is a prompt toolkit for software work.

It is organized so you can:
- start from one entry point
- load only the guidance needed for the task
- keep shared rules stable across model families
- handle memory explicitly when the host supports durable memory
- reuse specialist agents for audits, prompt tuning, and findings-ledger fixes

## How To Use This Repo

Treat this repository as a routed system, not a flat pile of prompt files.

The README is the routing entry point.
Use it first to decide which guide files belong in the real task context.

Do not load everything by default.
Prefer one compact context bundle per task.

Use the routing flow below to choose the smallest useful guide set for the task.
The later sections explain what each layer and file group is for.

### Two-Pass Workflow

Use this repository in two passes when you want the model to choose the right guidance before the real task starts.

The goal is to avoid duplicating the task description when the host can already preserve it.

Pass 1, routing:
- pass the user request together with this README
- let the model identify the smallest useful set of guide files
- treat that step as selection only, not final task execution

Pass 2, execution:
- keep using the existing conversation context if the host preserves the conversation, including the original user request
- if you are starting a fresh call and the original request is no longer available, pass either the original request or a short task capsule that restates it accurately
- pass the guide files selected in pass 1
- use those selected files as the actual execution instructions for the task

Practical example:
- first pass: user request + [README.md](README.md)
- second pass in the same conversation: existing conversation context + selected guide files such as [core/shared-contract.md](core/shared-contract.md) + one primary workflow such as [development/debugging.md](development/debugging.md) + any small supporting set chosen in pass 1
- second pass in a fresh call: short task capsule or original request + the same selected guide files

This keeps the routing context small and makes the execution context explicit.

Routing frequency rule:
- run the README routing step once per task, not once per session
- run it again only if the task changes materially or the conversation context no longer preserves the original request and selected guidance

### Context Load Order

If you are passing files as context on purpose, use this order:

1. Start with [prompt-bootstrap.prompt.md](.github/prompts/prompt-bootstrap.prompt.md).
	It decides what should be loaded next.
2. Pass [core/shared-contract.md](core/shared-contract.md).
	This establishes the invariant rules before any model-specific or task-specific guidance is added.
3. Pass [development/model-adapters.md](development/model-adapters.md) only if the active model family needs adapter guidance.
	This comes after the shared contract because it may shape presentation, but it should not change the core rules.
4. If the task involves remembered instructions or user preferences, decide whether the host supports durable memory.
	- If yes, pass [core/memory-contract.md](core/memory-contract.md) and then [development/context-management.md](development/context-management.md).
	- If no, pass [development/context-management.md](development/context-management.md) without the memory contract and treat the information as session-only.
5. Pass the one primary task workflow file from [development](development) or [setup](setup).
	This should be the main procedure for the task.
6. If needed, pass a small number of secondary workflow files that the bootstrap selected.
	Do not add extra guides just because they seem related.
7. Only after the guide set is settled, pass the model-specific prompt wrapper from [.github/prompts](.github/prompts) or a specialist agent from [.github/agents](.github/agents).

In short, the loading sequence is:

`bootstrap -> shared contract -> optional memory/context layer -> optional model adapter -> primary task workflow -> secondary supporting guides if needed -> prompt template or specialist agent`

When using the two-pass workflow above, this README belongs to the routing pass and the files in this load order belong to the execution pass.

## Prompt And Agent Layers

The repository is organized into layers. Use this section as a map of what each layer is for, not as a second loading procedure.

### 1. Shared Rules Layer

The invariant layer is [core/shared-contract.md](core/shared-contract.md).
It holds the rules that should stay stable across tasks and model families, such as verification standards, scope control, and tool discipline.

When the host supports durable memory, [core/memory-contract.md](core/memory-contract.md) extends this layer with rules for what to remember, what not to remember, and how to separate user memory from session or repository memory.

### 2. Model Adapter Layer

Use [development/model-adapters.md](development/model-adapters.md) when the wording or structure should change for a model family without changing the underlying rules.

This layer is for model-specific shaping, not for changing the task requirements.

### 3. Task Workflow Layer

Choose the task-specific guide from [development](development) or [setup](setup).

Examples:
- [development/context-management.md](development/context-management.md) for session context and memory decisions
- [development/debugging.md](development/debugging.md) for debugging
- [development/code-review.md](development/code-review.md) for review work
- [development/test-generation.md](development/test-generation.md) for tests
- [development/git-workflow.md](development/git-workflow.md) for commits, PRs, and releases
- [core/production-ready-check.md](core/production-ready-check.md) for release readiness

This layer tells the agent what kind of work to do and how to do it.

### 4. Prompt Entry Layer

Use the files under [.github/prompts](.github/prompts) when you want a ready prompt wrapper around the selected guide set.

- [prompt-bootstrap.prompt.md](.github/prompts/prompt-bootstrap.prompt.md) is the main router
- [gpt-task-template.prompt.md](.github/prompts/gpt-task-template.prompt.md) is the GPT-family task template
- [claude-task-template.prompt.md](.github/prompts/claude-task-template.prompt.md) is the Claude-family task template

This layer turns the selected guidance into a concrete prompt.

### 5. Specialist Agent Layer

Use the files under [.github/agents](.github/agents) when the job is broader than a single prompt or needs a dedicated workflow.

Examples:
- [public-release-auditor.agent.md](.github/agents/public-release-auditor.agent.md) for high-recall release audits
- [fix-and-recheck.agent.md](.github/agents/fix-and-recheck.agent.md) for findings-ledger fixes
- [prompt-evaluator.agent.md](.github/agents/prompt-evaluator.agent.md) for prompt comparisons
- [model-adapter-designer.agent.md](.github/agents/model-adapter-designer.agent.md) for adapter design work

Use an agent when you need orchestration. Use a prompt when you need a focused single-task setup.

## Repository Layout

- [core](core): cross-cutting rules and release gates
- [development](development): task-specific workflows for coding, reviews, tests, debugging, context and memory handling, git, and audits
- [setup](setup): project setup, architecture, documentation, and reproducibility guidance
- [.github/prompts](.github/prompts): entry prompts and model-family templates
- [.github/agents](.github/agents): specialist agent definitions

## License

This repository is licensed under CC BY 4.0.

You may use, adapt, and share the material, including commercially, as long as you provide attribution.

## Attribution

If you reuse or adapt this repository, please credit:
- `byteshiftlabs`
- `https://github.com/byteshiftlabs/ai-dev-prompts`

If you made changes, say that clearly in your attribution.

Example:

```text
Based on AI Development Prompts by byteshiftlabs
https://github.com/byteshiftlabs/ai-dev-prompts
Used under CC BY 4.0. Changes were made.
```
