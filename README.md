# AI Development Prompts

Reusable prompt patterns for AI-assisted software development.

---

## Quick Start

Load what you need from the categories below.

Start with `core/` when you want cross-cutting guidance that applies across most sessions.

Workspace custom agents live under `.github/agents/` and can orchestrate the prompt files and core guides for you.

---

## Prompts by Category

### `core/` — Cross-Cutting Guides
| Prompt | When to use |
|--------|-------------|
| [personas.md](core/personas.md) | Role-based standards and review tone that can be layered onto other workflows |
| [production-ready-check.md](core/production-ready-check.md) | Public-release gate and final quality checklist |

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
| [context-management.md](development/context-management.md) | Control what the AI remembers |
| [data-structure-design.md](development/data-structure-design.md) | Design structures that eliminate special cases |
| [debugging.md](development/debugging.md) | Diagnose and fix issues |
| [error-handling.md](development/error-handling.md) | Design exception patterns and logging |
| [exhaustive-review.md](development/exhaustive-review.md) | Coverage-driven review protocol for high-recall audits |
| [fix-and-recheck.prompt.md](development/fix-and-recheck.prompt.md) | Consume an audit findings file, fix issues in severity order, and recheck |
| [git-workflow.md](development/git-workflow.md) | Commits, branches, PRs |
| [incremental-development.md](development/incremental-development.md) | Build in small, verified steps |
| [performance.md](development/performance.md) | Efficiency guidelines without premature optimization |
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
