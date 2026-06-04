# AI Development Prompts

Reusable prompt patterns for AI-assisted software development.

---

## Quick Start

Load what you need from the categories below.

Start with `core/` when you want cross-cutting guidance that applies across most sessions.

If you need a single entry point that classifies the task and chooses the relevant guides for you, start with `.github/prompts/prompt-bootstrap.prompt.md`.

Workspace custom agents live under `.github/agents/` and can orchestrate the prompt files and core guides for you.

## Recommended Workflow

Use the repository as a routed prompt system rather than a flat library of prompt files.

1. Start with `.github/prompts/prompt-bootstrap.prompt.md`
	- Give it the task, the project context, and the target model family.
2. Let the bootstrap classify the task
	- It should identify the primary task type and only a few secondary concerns.
3. Let the bootstrap choose the minimum relevant guides
	- It should load the shared contract first, then the model adapter, then only the task-relevant guides.
   	- If the user asks the agent to remember instructions or preferences, it should route into `development/context-management.md` alongside the shared contract.
4. Draft the task prompt from the selected guides
	- Use `.github/prompts/gpt-task-template.prompt.md` for GPT-family models.
	- Use `.github/prompts/claude-task-template.prompt.md` for Claude-family models.
5. Use specialist agents when the task is broader than a single prompt
	- `.github/agents/public-release-auditor.agent.md` for release audits
	- `.github/agents/fix-and-recheck.agent.md` for findings-ledger fixes
	- `.github/agents/prompt-evaluator.agent.md` for prompt benchmark analysis
	- `.github/agents/model-adapter-designer.agent.md` for adapter tuning

The default rule is:

- keep invariant rules in `core/shared-contract.md`
- keep model-specific prompt shaping in `development/model-adapters.md`
- keep evaluation-driven split decisions in `development/prompt-evaluation.md`
- keep task procedures in the relevant `development/` or `setup/` guide

Do not start by loading many guides manually.
Start with the bootstrap and let it justify both selected and excluded guides.

---

## Prompts by Category

### `core/` — Cross-Cutting Guides
| Prompt | When to use |
|--------|-------------|
| [personas.md](core/personas.md) | Role-based standards and review tone that can be layered onto other workflows |
| [production-ready-check.md](core/production-ready-check.md) | Public-release gate and final quality checklist |
| [shared-contract.md](core/shared-contract.md) | Stable cross-model agent rules: verification, scope, tool discipline, and completion criteria |

### � `setup/` — Project Initialization
| Prompt | When to use |
|--------|-------------|
| [architecture.md](setup/architecture.md) | Review system structure and dependencies |
| [dev-principles.md](setup/dev-principles.md) | Establish guiding principles before writing code |
| [documentation.md](setup/documentation.md) | Generate code documentation and READMEs |
| [ml-project-bootstrap.md](setup/ml-project-bootstrap.md) | Initialize new ML/research projects |
| [reproducibility.md](setup/reproducibility.md) | Ensure consistent, reproducible results |

### 📁 `development/` — During Development
| Prompt | When to use |
|--------|-------------|
| [api-design.md](development/api-design.md) | Stable interfaces, backward compatibility |
| [chain-of-thought.md](development/chain-of-thought.md) | Step-by-step reasoning and meta-prompting |
| [code-review.md](development/code-review.md) | Audit code for style, bugs, maintainability |
| [content-integrity.md](development/content-integrity.md) | Load when factual accuracy matters |
| [context-management.md](development/context-management.md) | Control session context and decide when durable user preferences should be remembered |
| [data-structure-design.md](development/data-structure-design.md) | Design structures that eliminate special cases |
| [debugging.md](development/debugging.md) | Diagnose and fix issues |
| [error-handling.md](development/error-handling.md) | Design exception patterns and logging |
| [exhaustive-review.md](development/exhaustive-review.md) | Coverage-driven review protocol for high-recall audits |
| [fix-and-recheck.prompt.md](development/fix-and-recheck.prompt.md) | Consume an audit findings file, fix issues in severity order, and recheck |
| [git-workflow.md](development/git-workflow.md) | Commits, branches, PRs, and release/versioning conventions |
| [incremental-development.md](development/incremental-development.md) | Build in small, verified steps |
| [model-adapters.md](development/model-adapters.md) | Thin model-family tuning layer without forking the full prompt stack |
| [performance.md](development/performance.md) | Efficiency guidelines without premature optimization |
| [prompt-evaluation.md](development/prompt-evaluation.md) | Benchmark and compare prompt layers across models before splitting guidance |
| [public-release-audit.prompt.md](development/public-release-audit.prompt.md) | Ready-to-run prompt artifact for one-pass public release audits |
| [refactoring.md](development/refactoring.md) | Restructure without changing behavior |
| [scope-control.md](development/scope-control.md) | Stay focused, avoid scope creep |
| [task-decomposition.md](development/task-decomposition.md) | Break complex tasks into steps |
| [test-generation.md](development/test-generation.md) | Generate comprehensive test suites |

---

## Example Session

```
"Add feature X"
└── Load development/task-decomposition.md → break it down

"Let's build it"
└── Load development/incremental-development.md → step by step

"Review this code"
└── Load development/code-review.md → audit

"Write tests"
└── Load development/test-generation.md → generate tests

"Set review standards"
└── Load core/personas.md → choose a review persona

"Tune prompts for GPT and Claude"
└── Load core/shared-contract.md + development/model-adapters.md + development/prompt-evaluation.md

"Bootstrap a prompt from one entry file"
└── Run .github/prompts/prompt-bootstrap.prompt.md → choose relevant guides → route into GPT or Claude template

"Commit and PR"
└── Load development/git-workflow.md → commit, push, PR

"Prepare for public release"
└── Load core/production-ready-check.md → full checklist

"Fix findings from an audit"
└── Load development/fix-and-recheck.prompt.md → close items in severity order and recheck

"Run audit then transition into fixes"
└── Use .github/agents/public-release-auditor.agent.md → handoff to fix-and-recheck.agent.md
```

---

## License

CC BY 4.0 — Use freely with attribution.
