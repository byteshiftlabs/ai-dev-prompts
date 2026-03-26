# Shared Contract

Define the stable rules that should remain consistent across model families.

## Purpose

Use this guide to separate invariant agent behavior from model-specific prompt tuning.

The goal is not to maintain a different workflow for every model. The goal is to keep one reliable operating contract, then add thin adapters only where model behavior actually differs.

## Principle

Treat the prompt stack as three layers:

1. Shared contract: rules that must hold regardless of model
2. Model adapter: wording and structure tuned for a specific model family
3. Task workflow: debugging, review, refactoring, release audit, and other task-specific prompts

If a rule affects correctness, safety, verification, or repository policy, it belongs in the shared contract unless there is strong evidence that it must vary.

## What Belongs In The Shared Contract

- Safety boundaries and prohibited behavior
- Tool permissions and tool-use discipline
- Scope control and completion criteria
- Verification requirements before claiming success
- Repository constraints and style expectations
- Output requirements that matter to downstream automation or reviewers

## What Does Not Belong Here

- Model-specific wording preferences
- Redundant reminders added only because one model tends to drift
- Task-specific steps that belong in a workflow prompt
- Local project details that belong in repository instructions

## Default Operating Rules

```text
For this task, keep the following rules invariant across model families:

- Obey repository constraints and coding standards.
- Do not add compiler optimization flags unless the project explicitly requires them.
- Do not commit binaries, build artifacts, generated archives, or similar machine-generated outputs.
- Use the permitted tools deliberately and verify claims with evidence.
- Stay within scope unless the user explicitly expands it.
- Do not claim completion until the requested work and relevant verification are done.
- If confidence is limited, state the exact uncertainty rather than smoothing it over.
```

## Failure-Mode Rule

Do not split instructions by model family just because the models feel different.

First identify the failure mode:

- missed constraints
- excessive verbosity
- weak decomposition
- poor tool discipline
- shallow verification
- brittle formatting compliance

Then adjust the smallest layer responsible for that failure:

- shared contract if the behavior should never vary
- model adapter if the behavior is elicitation-sensitive
- workflow prompt if the issue is task-specific

## Design Test

Before adding a model-specific rule, ask:

1. Would this rule still be correct for every model?
2. Is this about policy or about elicitation?
3. Can the problem be fixed by removing conflicting instructions instead of adding more?
4. Do we have evidence from repeated failures, not a single anecdote?

If the answer to question 1 is yes, keep the rule here.

## Durable User Memory

Treat durable user instructions and preferences as part of the operating contract across sessions.

Store only information that is stable, reusable, and likely to improve future work, such as:

- explicit user preferences about tools, workflow, review style, or output format
- recurring instructions the user expects to persist across tasks
- durable environment constraints or approval boundaries the user has stated clearly

Do not store:

- secrets, credentials, tokens, or personal sensitive data
- task-specific scratch notes, temporary plans, or one-off requests
- speculative inferences about the user
- repository facts that belong in repository-scoped instructions instead of user memory

Persist memory only when the instruction is clearly durable:

- the user explicitly asks to remember it
- the same preference is reinforced across multiple tasks
- forgetting it would likely cause repeated friction or regressions

If a stored preference is later contradicted or becomes outdated, update or remove it.

## Usage Pattern

Use this file with:

- `core/personas.md` for review posture and standards
- `core/production-ready-check.md` for release gating
- `core/memory-contract.md` when the host supports durable memory and the task involves remembered instructions or preferences
- `development/model-adapters.md` when prompt structure needs model-specific tuning
- `development/prompt-evaluation.md` when deciding whether to split guidance or keep it shared
- `development/context-management.md` for the workflow that distinguishes session context from durable user memory