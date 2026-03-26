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

Do not load everything by default.
Prefer one compact context bundle per task.

Use it like this:

1. Start with [prompt-bootstrap.prompt.md](.github/prompts/prompt-bootstrap.prompt.md) unless you already know the exact workflow file you need.
2. Keep [core/shared-contract.md](core/shared-contract.md) as the stable rules layer. It should define the invariant standards for verification, scope, and tool use.
3. If the task involves remembered instructions or user preferences, check whether the host actually supports durable memory. When it does, use [core/memory-contract.md](core/memory-contract.md) together with [development/context-management.md](development/context-management.md).
4. Add [development/model-adapters.md](development/model-adapters.md) only when the prompt needs to be shaped differently for a model family such as GPT or Claude.
5. Load one task workflow from [development](development) or [setup](setup) based on the job:
	- use [development/debugging.md](development/debugging.md) for root-cause debugging
	- use [development/code-review.md](development/code-review.md) for normal review work
	- use [development/test-generation.md](development/test-generation.md) for tests
	- use [development/git-workflow.md](development/git-workflow.md) for commits, PRs, and releases
	- use [core/production-ready-check.md](core/production-ready-check.md) when release readiness is the goal
6. Use the task templates in [.github/prompts](.github/prompts) when you already know the target model family and want a ready prompt wrapper:
	- [gpt-task-template.prompt.md](.github/prompts/gpt-task-template.prompt.md)
	- [claude-task-template.prompt.md](.github/prompts/claude-task-template.prompt.md)
7. Use the specialist agents in [.github/agents](.github/agents) when the job is broader than a single prompt and needs orchestration across multiple steps:
	- [public-release-auditor.agent.md](.github/agents/public-release-auditor.agent.md)
	- [fix-and-recheck.agent.md](.github/agents/fix-and-recheck.agent.md)
	- [prompt-evaluator.agent.md](.github/agents/prompt-evaluator.agent.md)
	- [model-adapter-designer.agent.md](.github/agents/model-adapter-designer.agent.md)

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

Practical rule of thumb:
- use the bootstrap when you want routing
- use the shared contract when you want stable rules
- use the memory contract with context-management when the host can actually persist memory across sessions
- use a development or setup guide when you know the task
- use a prompt template when you know the model family
- use an agent when the work needs a dedicated multi-step workflow

## Prompt And Agent Layers

The repository is meant to be used in layers.

### 1. Shared Rules Layer

Start with [core/shared-contract.md](core/shared-contract.md).

This is the invariant layer. It holds the rules that should stay stable across tasks and model families, such as verification standards, scope control, and tool discipline.

When the host supports durable memory, [core/memory-contract.md](core/memory-contract.md) extends this layer with rules for what to remember, what not to remember, and how to separate user memory from session or repository memory.

### 2. Model Adapter Layer

Use [development/model-adapters.md](development/model-adapters.md) when the wording or structure should change for a model family without changing the underlying rules.

This layer is for model-specific shaping, not for changing the task requirements.

### 3. Task Workflow Layer

Load the task-specific guide from [development](development) or [setup](setup).

Examples:
- [development/context-management.md](development/context-management.md) for session context and memory decisions
- [development/debugging.md](development/debugging.md) for debugging
- [development/code-review.md](development/code-review.md) for review work
- [development/test-generation.md](development/test-generation.md) for tests
- [development/git-workflow.md](development/git-workflow.md) for commits, PRs, and releases
- [core/production-ready-check.md](core/production-ready-check.md) for release readiness

This layer tells the agent what kind of work to do and how to do it.

### 4. Prompt Entry Layer

Use the files under [.github/prompts](.github/prompts) when you want a ready entry point.

- [prompt-bootstrap.prompt.md](.github/prompts/prompt-bootstrap.prompt.md) is the main router
- [gpt-task-template.prompt.md](.github/prompts/gpt-task-template.prompt.md) is the GPT-family task template
- [claude-task-template.prompt.md](.github/prompts/claude-task-template.prompt.md) is the Claude-family task template

This layer is the wrapper that turns the selected guidance into a concrete prompt.

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
