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

Use the task templates when you already know the target model family:
- [gpt-task-template.prompt.md](.github/prompts/gpt-task-template.prompt.md)
- [claude-task-template.prompt.md](.github/prompts/claude-task-template.prompt.md)

Use the specialist agents when the task is broader than a single prompt:
- [public-release-auditor.agent.md](.github/agents/public-release-auditor.agent.md)
- [fix-and-recheck.agent.md](.github/agents/fix-and-recheck.agent.md)
- [prompt-evaluator.agent.md](.github/agents/prompt-evaluator.agent.md)
- [model-adapter-designer.agent.md](.github/agents/model-adapter-designer.agent.md)

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

## License

This repository is licensed under CC BY 4.0.

You may use, adapt, and share the material, including commercially, as long as you provide attribution.
