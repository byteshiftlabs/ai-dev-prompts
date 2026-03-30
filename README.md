# AI Development Prompts

Reusable prompt patterns for AI-assisted software development.

## What This Repo Is

This repository is a prompt toolkit for software work.

Use it to:
- start from one entry point
- load only the guides that matter for the task
- keep shared rules stable across model families
- handle memory clearly when the host supports it
- reuse specialist agents for broader audit or evaluation work

## How To Use This Repo

Treat this repository as a routing system, not a pile of files.

Start with this README. Its job is to help you choose the smallest useful set of guides for the task.

Do not load everything by default.
Use one small guide bundle per task.

### Two-Pass Workflow

Use two passes when you want the model to choose the right guides before it starts the real work.

Pass 1, routing:
- give the user request together with this README
- let the model choose the smallest useful set of guides
- treat that pass as setup, not execution

Pass 2, execution:
- keep the original task context if the host preserves it
- otherwise restate the task briefly and accurately
- pass the selected guides from pass 1
- use those guides as the working instructions for the task

Routing rule:
- run the README routing step once per task
- run it again only if the task changes in a meaningful way or the earlier setup context is gone

### Recommended Order

If you are assembling context by hand, use this order:

1. [prompt-bootstrap.prompt.md](.github/prompts/prompt-bootstrap.prompt.md) if you want guided routing
2. [core/shared-contract.md](core/shared-contract.md)
3. [core/memory-contract.md](core/memory-contract.md) and [development/context-management.md](development/context-management.md) if memory or session control matters
4. [development/model-adapters.md](development/model-adapters.md) if model-family tuning matters
5. one main workflow guide from [development](development) or [setup](setup)
6. a small number of supporting guides only when they are clearly needed
7. a prompt template or specialist agent last

## Prompt And Agent Layers

The repository is organized into layers. Use this section as a map.

### 1. Shared Rules Layer

[core/shared-contract.md](core/shared-contract.md) holds the rules that should stay the same across tasks and model families.

If the host supports memory, [core/memory-contract.md](core/memory-contract.md) explains what should be remembered and where it belongs.

### 2. Model Adapter Layer

Use [development/model-adapters.md](development/model-adapters.md) when prompt structure should change for a model family without changing the task itself.

### 3. Task Workflow Layer

Choose the task-specific guide from [development](development) or [setup](setup).

Examples:
- [development/context-management.md](development/context-management.md) for session context and memory decisions
- [development/host-integration.md](development/host-integration.md) for first-use assistant setup, host capability checks, and instruction-file placement
- [development/hooks.md](development/hooks.md) for pre-tool and post-tool checks and automated feedback
- [development/commands.md](development/commands.md) for reusable command workflows
- [development/tool-extension.md](development/tool-extension.md) for external tools, browser automation, notebooks, and CI or GitHub integrations
- [development/debugging.md](development/debugging.md) for debugging
- [development/code-review.md](development/code-review.md) for review work
- [development/test-generation.md](development/test-generation.md) for tests
- [development/git-workflow.md](development/git-workflow.md) for commits, PRs, and releases
- [core/production-ready-check.md](core/production-ready-check.md) for release readiness

### 4. Prompt Entry Layer

Use the files under [.github/prompts](.github/prompts) when you want a ready prompt wrapper around the selected guide set.

- [prompt-bootstrap.prompt.md](.github/prompts/prompt-bootstrap.prompt.md) is the main router
- [gpt-task-template.prompt.md](.github/prompts/gpt-task-template.prompt.md) is the GPT task template
- [claude-task-template.prompt.md](.github/prompts/claude-task-template.prompt.md) is the Claude task template

### 5. Specialist Agent Layer

Use the files under [.github/agents](.github/agents) when the job is broader than a single prompt or needs a dedicated workflow.

Examples:
- [public-release-auditor.agent.md](.github/agents/public-release-auditor.agent.md) for high-recall release audits
- [fix-and-recheck.agent.md](.github/agents/fix-and-recheck.agent.md) for fixing findings and rechecking them
- [prompt-evaluator.agent.md](.github/agents/prompt-evaluator.agent.md) for prompt comparisons
- [model-adapter-designer.agent.md](.github/agents/model-adapter-designer.agent.md) for adapter design work

Use an agent when you need coordination across a broader workflow. Use a prompt when you need a focused task setup.

## Repository Layout

- [core](core): shared rules and release gates
- [development](development): task-specific workflows for coding, reviews, tests, debugging, context, memory, git, and audits
- [setup](setup): project setup, architecture, documentation, and reproducibility guidance
- [.github/prompts](.github/prompts): prompt entry files and model-family templates
- [.github/agents](.github/agents): specialist agent definitions

## License

This repository is licensed under CC BY 4.0.

You may use, adapt, and share the material, including commercially, as long as you provide attribution.

## Attribution

If you reuse or adapt this repository, credit:
- `byteshiftlabs`
- `https://github.com/byteshiftlabs/ai-dev-prompts`

If you made changes, say that clearly in your attribution.

Example:

```text
Based on AI Development Prompts by byteshiftlabs
https://github.com/byteshiftlabs/ai-dev-prompts
Used under CC BY 4.0. Changes were made.
```
