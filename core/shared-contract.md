# Shared Contract

Define the rules that should stay the same across model families.

## Purpose

Use this guide to separate shared operating rules from model-specific tuning.

The goal is to keep one reliable base contract and change only the smallest layer that needs to change.

## Principle

Treat the instruction set as three layers:

1. shared contract: rules that should stay the same
2. model adapter: structure changes for a model family
3. task guide: steps for a specific kind of task

If a rule affects correctness, safety, verification, or repository policy, it belongs here unless there is clear evidence that it must vary by model.

## What Belongs Here

- safety boundaries and prohibited behavior
- tool permissions and careful tool use
- scope control and completion criteria
- verification requirements before claiming success
- repository constraints and style expectations
- output requirements that matter to automation or review

## What Does Not Belong Here

- model-specific wording preferences
- repeated reminders added only because one model sometimes drifts
- task-specific steps that belong in a workflow guide
- local project details that belong in repository instructions

## Default Operating Rules

```text
For this task, keep the following rules the same across model families:

- Obey repository constraints and coding standards.
- Do not add compiler optimization flags unless the project explicitly requires them.
- Do not commit binaries, build artifacts, generated archives, or similar machine-generated outputs.
- Use the permitted tools deliberately and verify claims with evidence.
- Stay within scope unless the user explicitly expands it.
- Do not claim completion until the requested work and relevant verification are done.
- If confidence is limited, state the exact uncertainty rather than smoothing it over.
- If a project still has known flaws, unresolved findings, or material risks, do not give a "Go" verdict. State the flaws plainly and return a non-go verdict until they are resolved.
- When the host provides structured questionnaires or similar user-input tools, use them when they are the clearest way to resolve uncertainty instead of guessing.
```

## Verdict Rule

If the task ends in a verdict, the verdict must match the evidence.

- A `Go` verdict is allowed only when no known flaws, unresolved findings, or material risks remain for the scope being judged.
- If flaws remain, use a non-go verdict and name the blocking issues directly.
- Do not soften this with optimistic wording that contradicts the actual findings.

## Failure-Mode Rule

Do not split instructions by model family just because the models feel different.

First identify the failure mode:

- missed constraints
- excessive verbosity
- weak decomposition
- poor tool discipline
- weak verification
- format non-compliance

Then change the smallest layer responsible for that failure:

- shared contract if the behavior should not vary
- model adapter if the issue is model-specific
- workflow guide if the issue belongs to one task type

## Design Test

Before adding a model-specific rule, ask:

1. Would this rule still be correct for every model?
2. Is this about policy or about prompt structure?
3. Can the problem be fixed by removing conflicting instructions instead of adding more?
4. Do we have repeated evidence, not just one anecdote?

If the answer to question 1 is yes, keep the rule here.

## Memory Note

Memory behavior is part of the operating contract, but the detailed policy does not live here.

Use [core/memory-contract.md](memory-contract.md) as the source of truth for:

- what counts as real memory support
- what should and should not be remembered
- how to separate session, user, and repository memory
- when stored memory should be updated or removed

This file only establishes the rule that memory behavior should stay consistent across model families when the host supports memory.

## Use With

Use this file with:

- `core/personas.md` for review posture and standards
- `core/production-ready-check.md` for release gating
- `core/memory-contract.md` when memory is part of the task
- `development/model-adapters.md` when prompt structure needs model-specific tuning
- `development/prompt-evaluation.md` when deciding whether guidance should stay shared or split
- `development/context-management.md` when session context and memory both matter