---
name: "Prompt Bootstrap"
description: "Use before drafting a task prompt. Classifies the problem, selects only the relevant prompt guides, applies the shared contract, and chooses the right model adapter."
agent: "agent"
argument-hint: "Describe the task, project context, and target model family"
tools:
  - read
  - search
---

# Prompt Bootstrap

Use this file as the master entry point before generating a task-specific prompt.

Your job is to set up the prompt stack, not to solve the task yet.

## Inputs

- `TASK`: what the user wants done
- `PROJECT_CONTEXT`: repository, stack, constraints, and current state
- `MODEL_FAMILY`: target model family, for example GPT or Claude

## Required Setup Order

1. Read [core/shared-contract.md](../../core/shared-contract.md) first.
2. Read [development/model-adapters.md](../../development/model-adapters.md) second.
3. Classify the task before loading anything else.
4. Use the guide-selection matrix below to decide what to load.
5. Load only the guides relevant to that task from the routing table below.
6. If the task involves remembered instructions, user preferences, or memory behavior, first determine whether the host actually supports durable memory.
7. If the host supports durable memory and the task involves remembered instructions or preferences, also load [core/memory-contract.md](../../core/memory-contract.md) and [development/context-management.md](../../development/context-management.md).
8. If the host does not support durable memory but the task still involves remembered instructions or preferences, load [development/context-management.md](../../development/context-management.md) and treat the information as session context unless the runtime provides a persistence mechanism.
9. If the task is ambiguous or high-risk, also load [development/prompt-evaluation.md](../../development/prompt-evaluation.md).
10. Produce a setup summary and then draft the final task prompt.

## Task Classification

Classify the request into one primary task type before selecting guides:

- implementation
- debugging
- refactoring
- code review
- release audit
- test generation
- architecture or design
- documentation
- repository workflow
- prompt design or prompt evaluation

Then identify any secondary concerns:

- strict scope control needed
- ambiguous requirements
- high factual-integrity risk
- multi-stage task
- public release impact
- durable user preferences or instructions involved
- model-specific tuning required

Use one primary task type and as few secondary concerns as possible.

## Guide-Selection Matrix

Use this matrix before the routing table.

| If the task is mainly about... | Load these guides first | Usually do not load by default |
|--------------------------------|--------------------------|--------------------------------|
| implementing a feature or change | `development/task-decomposition.md`, `development/incremental-development.md` | `development/exhaustive-review.md` |
| debugging a failure or regression | `development/debugging.md`, `development/context-management.md` | `development/code-review.md` unless the user explicitly asked for a review |
| restructuring code without changing behavior | `development/refactoring.md`, `development/scope-control.md` | `development/public-release-audit.prompt.md` |
| reviewing code quality in normal development | `development/code-review.md` | `development/exhaustive-review.md` unless recall and coverage are the main goal |
| auditing for release readiness or maximum recall | `development/exhaustive-review.md`, `core/production-ready-check.md` | `development/code-review.md` as the primary review protocol |
| generating or improving tests | `development/test-generation.md` | `development/public-release-audit.prompt.md` |
| designing APIs, modules, or structures | `development/api-design.md` or `development/data-structure-design.md`, plus `development/task-decomposition.md` if the work is multi-stage | `development/debugging.md` |
| writing docs or README material | `setup/documentation.md`, plus `development/content-integrity.md` when accuracy matters | `development/refactoring.md` |
| commits, branches, or PR hygiene | `development/git-workflow.md` | `development/exhaustive-review.md` |
| storing or updating durable user instructions or preferences in a memory-capable host | `core/shared-contract.md`, `core/memory-contract.md`, `development/context-management.md` | unrelated implementation guides |
| storing or updating remembered instructions when the host is not memory-capable | `core/shared-contract.md`, `development/context-management.md` | unrelated implementation guides |
| prompt-system design or model tuning | `core/shared-contract.md`, `development/model-adapters.md`, `development/prompt-evaluation.md` | unrelated implementation guides |

## Overlap And Exclusion Rules

Use these rules to resolve common collisions:

### Code Review vs Exhaustive Review

- Use [development/code-review.md](../../development/code-review.md) for normal quality review, maintainability review, or targeted cleanup.
- Use [development/exhaustive-review.md](../../development/exhaustive-review.md) when the goal is high recall, explicit coverage accounting, a findings ledger, or release readiness.
- Do not load both by default.
- Load both only when the task explicitly needs normal code-quality criteria and exhaustive coverage protocol together.

### Debugging vs Refactoring

- Use [development/debugging.md](../../development/debugging.md) when the primary goal is to find the root cause of incorrect behavior.
- Use [development/refactoring.md](../../development/refactoring.md) when behavior is meant to stay the same and the structure is the target.
- If the request is "fix the bug and clean up the area," debugging is primary and refactoring is secondary.

### Scope Control vs Task Decomposition

- Load [development/scope-control.md](../../development/scope-control.md) when there is clear risk of feature creep or opportunistic cleanup.
- Load [development/task-decomposition.md](../../development/task-decomposition.md) when the task is genuinely multi-step.
- It is common to load both together.

### Content Integrity

- Load [development/content-integrity.md](../../development/content-integrity.md) when the output includes factual claims, docs, release notes, architecture claims, or audit conclusions.
- Do not load it for routine local code edits unless the task explicitly touches factual output.

### Chain Of Thought

- Load [development/chain-of-thought.md](../../development/chain-of-thought.md) only when the task needs explicit staged reasoning before execution, such as ambiguous requests, difficult trade-off analysis, architecture decisions, or non-trivial debugging.
- Do not load it for straightforward code changes, routine reviews, or tasks where concise execution matters more than exposed reasoning.
- If loaded, prefer the smallest relevant variation rather than the entire file's style by default.

### Prompt Evaluation

- Load [development/prompt-evaluation.md](../../development/prompt-evaluation.md) when the task is about deciding whether guidance should stay shared or split by model family.
- Do not load it for ordinary code tasks.

## Routing Table

Select the smallest relevant set of guides.

### Cross-cutting standards

- Review posture or stricter standards: [core/personas.md](../../core/personas.md)
- Public release or final gate: [core/production-ready-check.md](../../core/production-ready-check.md)

### Problem framing and control

- Limit scope: [development/scope-control.md](../../development/scope-control.md)
- Manage task context: [development/context-management.md](../../development/context-management.md)
- Durable user preferences or remembered instructions in a memory-capable host: [core/memory-contract.md](../../core/memory-contract.md), [development/context-management.md](../../development/context-management.md), and [core/shared-contract.md](../../core/shared-contract.md)
- Remembered instructions when the host is not memory-capable: [development/context-management.md](../../development/context-management.md) together with [core/shared-contract.md](../../core/shared-contract.md)
- Explicit staged reasoning for ambiguous or high-complexity tasks: [development/chain-of-thought.md](../../development/chain-of-thought.md)
- Break down complex work: [development/task-decomposition.md](../../development/task-decomposition.md)
- Build incrementally: [development/incremental-development.md](../../development/incremental-development.md)

### Implementation and code change tasks

- Debugging: [development/debugging.md](../../development/debugging.md)
- Refactoring: [development/refactoring.md](../../development/refactoring.md)
- API/interface design: [development/api-design.md](../../development/api-design.md)
- Data-structure design: [development/data-structure-design.md](../../development/data-structure-design.md)
- Error handling: [development/error-handling.md](../../development/error-handling.md)
- Performance: [development/performance.md](../../development/performance.md)

### Quality and review tasks

- Code review: [development/code-review.md](../../development/code-review.md)
- Exhaustive audit: [development/exhaustive-review.md](../../development/exhaustive-review.md)
- Test generation: [development/test-generation.md](../../development/test-generation.md)
- Content/factual accuracy: [development/content-integrity.md](../../development/content-integrity.md)

### Release and workflow tasks

- Public release audit artifact: [development/public-release-audit.prompt.md](../../development/public-release-audit.prompt.md)
- Fix from findings ledger: [development/fix-and-recheck.prompt.md](../../development/fix-and-recheck.prompt.md)
- Git and commit workflow: [development/git-workflow.md](../../development/git-workflow.md)

### Project setup tasks

- Architecture review: [setup/architecture.md](../../setup/architecture.md)
- Development principles: [setup/dev-principles.md](../../setup/dev-principles.md)
- Documentation generation: [setup/documentation.md](../../setup/documentation.md)
- Reproducibility: [setup/reproducibility.md](../../setup/reproducibility.md)
- ML bootstrap: [setup/ml-project-bootstrap.md](../../setup/ml-project-bootstrap.md)

## Selection Rules

- Do not load guides just because they are available.
- Prefer the minimum set that fully covers the task.
- If two guides overlap, keep the more task-specific one and mention the overlap.
- Exclude guides that add duplicated control logic without improving coverage or correctness.
- State why a plausible guide was not selected when the choice is non-obvious.
- Keep the shared contract invariant across model families.
- Apply model-specific wording changes only through the adapter layer.

## Output Format

Return exactly these sections:

### Selected Guides
- list each selected file and why it is relevant

### Excluded Guides
- list any plausible but rejected guide and why it was not loaded

### Shared Rules
- summarize the invariant rules that must remain stable

### Model Adapter
- state the chosen adapter behavior for `MODEL_FAMILY`

### Draft Prompt
- provide the final task prompt using only the selected guidance

## Inputs To Process

TASK: [TASK]
PROJECT_CONTEXT: [PROJECT_CONTEXT]
MODEL_FAMILY: [MODEL_FAMILY]