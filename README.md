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

## Beginner Ramp-Up

If you are new to this repository, do not start by reading every guide.

Use this short path instead:

1. Start with this README when you are routing the guide set by hand. Use [.github/prompts/prompt-bootstrap.prompt.md](.github/prompts/prompt-bootstrap.prompt.md) only when your host wants a ready-made routing prompt.
2. Pick one concrete task, such as debugging a Python service or running a release audit.
3. Load [core/shared-contract.md](core/shared-contract.md) plus one main workflow guide for that task.
4. Add model-adapter, memory, or agent files only if the task actually needs them.

Good first combinations:

- Debugging: [core/shared-contract.md](core/shared-contract.md) + [development/debugging.md](development/debugging.md)
- Code review: [core/shared-contract.md](core/shared-contract.md) + [development/code-review.md](development/code-review.md)
- Release audit: [core/shared-contract.md](core/shared-contract.md) + [development/exhaustive-review.md](development/exhaustive-review.md) + [core/production-ready-check.md](core/production-ready-check.md)

## How To Use This Repo

Treat this repository as a routing system, not a pile of files.

Start with this README. Its job is to help you choose the smallest useful set of guides for the task.

Do not load everything by default.
Use one small guide bundle per task.

## External Packaging Note

This repository is designed for selective loading.

If you package it for an AI tool, search system, MCP server, or skill format:
- do not merge the whole repo into one default prompt payload
- start from the router and load only the files needed for the current task
- keep shared rules separate from task workflows, prompt templates, and specialist agents

The repo now includes lightweight metadata for that purpose:
- [meta/asset-manifest.yaml](meta/asset-manifest.yaml): defines packaging groups and export rules
- [meta/guide-index.yaml](meta/guide-index.yaml): describes what each guide is for and when to load it

For packaging or host integration, treat the entry point as `README.md` plus the `meta/` folder.

Validate the metadata with:

```bash
python3 scripts/validate_metadata.py
```

This validator checks that the metadata files point to real repository files, that guide markdown files keep the required frontmatter, and that internal markdown links still resolve.

### Two-Pass Workflow

Use this repository in two simple steps:

1. Use this README or the bootstrap prompt to choose the smallest useful set of guides.
2. Run the real task with only those guides loaded.

If the consumer is a tool rather than a person, pair this README with the metadata files under `meta/` before selecting guides.

Do the routing step once per task. Repeat it only if the task changes in a meaningful way or the earlier setup is no longer available.

### Worked Example

Task: debug a regression in a Python service after a refactor.

Small bundle:
- [core/shared-contract.md](core/shared-contract.md)
- [development/debugging.md](development/debugging.md)
- [development/context-management.md](development/context-management.md) only if the session is large or memory matters
- one prompt wrapper only if the host needs it

Why this bundle:
- the shared contract keeps baseline rules stable
- the debugging guide gives the task method
- context guidance is optional support, not default baggage

What not to load:
- release audit guides
- ML bootstrap guides
- specialist agents unless the task expands into a broader workflow

The point is to end up with a task-sized bundle, not the whole repository.

### Recommended Order

If you are assembling context by hand, keep the order simple:

1. start with [prompt-bootstrap.prompt.md](.github/prompts/prompt-bootstrap.prompt.md) or this README
2. load [core/shared-contract.md](core/shared-contract.md)
3. add memory or model-adapter guidance only if the task needs it
4. load one main workflow guide from [development](development) or [setup](setup)
5. add a prompt template or specialist agent last

The full routing logic lives in [prompt-bootstrap.prompt.md](.github/prompts/prompt-bootstrap.prompt.md).

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
- [development/debugging.md](development/debugging.md) for debugging
- [development/code-review.md](development/code-review.md) for review work
- [development/test-generation.md](development/test-generation.md) for tests
- [development/git-workflow.md](development/git-workflow.md) for commits, PRs, and releases
- [core/production-ready-check.md](core/production-ready-check.md) for release readiness

For host setup, hooks, commands, external tools, and other specialized workflows, see the rest of the files under [development](development).

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
