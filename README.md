# AI Development Prompts

Reusable prompt patterns for AI-assisted software development.

## What This Repo Is

This repository is a prompt toolkit for software work.

It is organized so you can:
- start from one entry point
- load only the guidance needed for the task
- keep shared rules stable across model families
- reuse specialist agents for audits, prompt tuning, and findings-ledger fixes

## Start Here

If you want one entry point, start with [prompt-bootstrap.prompt.md](.github/prompts/prompt-bootstrap.prompt.md).

The bootstrap is the default router. It classifies the task, selects the minimum relevant guides, and points you to the right task template or workflow file.

If you already know the task type, you can also go straight to the relevant workflow file in [development](development) or [setup](setup).

Use the task templates when you already know the target model family:
- [gpt-task-template.prompt.md](.github/prompts/gpt-task-template.prompt.md)
- [claude-task-template.prompt.md](.github/prompts/claude-task-template.prompt.md)

Use the specialist agents when the task is broader than a single prompt:
- [public-release-auditor.agent.md](.github/agents/public-release-auditor.agent.md)
- [fix-and-recheck.agent.md](.github/agents/fix-and-recheck.agent.md)
- [prompt-evaluator.agent.md](.github/agents/prompt-evaluator.agent.md)
- [model-adapter-designer.agent.md](.github/agents/model-adapter-designer.agent.md)

## Prompt And Agent Layers

The repository is meant to be used in layers.

### 1. Shared Rules Layer

Start with [core/shared-contract.md](core/shared-contract.md).

This is the invariant layer. It holds the rules that should stay stable across tasks and model families, such as verification standards, scope control, and tool discipline.

### 2. Model Adapter Layer

Use [development/model-adapters.md](development/model-adapters.md) when the wording or structure should change for a model family without changing the underlying rules.

This layer is for model-specific shaping, not for changing the task requirements.

### 3. Task Workflow Layer

Load the task-specific guide from [development](development) or [setup](setup).

Examples:
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
- [development](development): task-specific workflows for coding, reviews, tests, debugging, git, and audits
- [setup](setup): project setup, architecture, documentation, and reproducibility guidance
- [.github/prompts](.github/prompts): entry prompts and model-family templates
- [.github/agents](.github/agents): specialist agent definitions

## Most Common Files

Use these first unless the bootstrap selects something else:

| File | Purpose |
|------|---------|
| [core/shared-contract.md](core/shared-contract.md) | Stable working rules that should not drift across tasks or models |
| [development/model-adapters.md](development/model-adapters.md) | Model-family differences without forking the whole prompt stack |
| [development/git-workflow.md](development/git-workflow.md) | Commit, branch, PR, and release conventions |
| [core/production-ready-check.md](core/production-ready-check.md) | Public-release checklist and final gate |
| [development/code-review.md](development/code-review.md) | Normal code review workflow |
| [development/test-generation.md](development/test-generation.md) | Test design and coverage guidance |
| [development/debugging.md](development/debugging.md) | Root-cause debugging workflow |

## Recommended Use

Treat this repository as a routed system, not a flat pile of prompt files.

The intended order is:
1. Start with the bootstrap.
2. Let it choose the smallest useful set of guides.
3. Keep shared rules in [core/shared-contract.md](core/shared-contract.md).
4. Keep model-specific behavior in [development/model-adapters.md](development/model-adapters.md).
5. Keep task procedures in the relevant [development](development) or [setup](setup) guide.

In short:
- use the shared contract for stable rules
- use model adapters for model-family differences
- use development/setup guides for task procedures
- use prompt files as entry points
- use agent files for broader multi-step workflows

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
