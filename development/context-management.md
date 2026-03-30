# Context Management

Control what context is provided to maximize efficiency and relevance.

This file is mainly about session context.
If the host also supports memory, use it together with [core/memory-contract.md](../core/memory-contract.md).

## Prompt

```
For this session, the relevant context is:

Project: [PROJECT_NAME]
Current task: [TASK]
Key files: [FILE_LIST]
Constraints: [content-integrity constraint]

Ignore information not relevant to the current task.
If you need additional context, ask for specific files or information.
```

## Placeholders

- `[PROJECT_NAME]`: Project being worked on
- `[TASK]`: Current objective
- `[FILE_LIST]`: Files relevant to the task
- `[content-integrity constraint]`: See [content-integrity.md](content-integrity.md)

## Variations

### Context reset
```
Forget previous context. Starting fresh.

New task: [TASK]
Relevant files: [FILES]
```

### Context summary
```
Summarize what we've accomplished so far in this session, then continue with [NEXT_TASK].
```

### Selective context loading
```
For [TASK], I'm providing only:
- [FILE_A]: contains [purpose]
- [FILE_B]: contains [purpose]

Do not assume knowledge of other files in the project.
```

## Long-Session Control

Long sessions accumulate noise.

When the host supports session controls such as compaction, reset, rewind, interruption, or checkpoint summaries, use them deliberately instead of letting stale context pile up.

### Interruption

Interrupt the assistant when it is:

- exploring the wrong area
- repeating a failed approach
- drifting beyond scope
- about to perform an unwanted action

After interruption, restate the active task boundary in one or two lines.

### Session compaction

When the conversation contains useful context but too much low-value history, create a compact session summary and continue from that smaller state.

Good summary contents:

- current task
- decisions already made
- relevant constraints
- open problems
- completed verification

Bad summary contents:

- every failed attempt in detail
- stale hypotheses that were already disproven
- broad unrelated repository exploration notes

### Rewind or branch reset

If the host supports rewinding or jumping back in conversation state, use it when a long detour has polluted the session and the earlier state was cleaner.

Do not rely on rewind as a substitute for explicit summaries. Use it to discard bad branches, not to avoid making decisions.

### Hard reset

When switching to a materially different task, reset the active session context rather than dragging old assumptions forward.

After a reset, restate:

- the new task
- the relevant files or repository
- the constraints that still apply

### Checkpoint summaries

For long tasks, create short checkpoints at major transitions.

Useful checkpoint moments:

- after exploration and before implementation
- after implementation and before verification
- before switching subprojects or repositories
- before and after a release or audit pass

## Host Control Rule

Do not name host-specific commands unless the task or repository actually requires them.

Describe the control behavior generically first:

- interrupt current output
- compact session history
- reset task context
- rewind to an earlier clean state

Then map that behavior to the host only if the host capability is known.

## Durable Preference Workflow

When managing context, separate session context from user memory.

Write to memory only after the information is clear enough to classify:

- store explicit user preferences about tools, communication style, output shape, or recurring workflow constraints
- store stable cross-task instructions that should still apply later
- do not store active task state, temporary assumptions, repo-specific facts, or unresolved guesses

Memory decision test:

1. Is this clearly a stable user preference or recurring instruction?
2. Will it probably matter again in a future task?
3. Does it belong to user memory rather than repository memory?
4. Is it explicit enough that storing it will not distort the user's intent?

If the answer to any of these is no, keep it in session context only.

Good times to persist:

- immediately after the user says to remember a preference
- after a repeated correction reveals a stable preference
- at the end of a task when a reusable instruction has been confirmed

Good examples of saved user memory:

- "Do not use GitKraken for my repos"
- "Use plain English in commit messages"
- "Always assign the PR creator and apply labels when opening a PR"
- "Keep audit findings files local only"

Do not persist:

- during early exploration when the signal is uncertain
- for one-off exceptions tied to a single task
- when the information belongs in repository memory or the current session only

Do not persist examples like:

- "For this task, inspect file X first"
- "This repository currently uses tool Y"
- "We are halfway through the release checklist"
- speculative guesses about what the user might prefer

When in doubt, keep it in session context first and persist only after stability is clear.

## Host Capability Rule

Only use memory if the host actually supports writing it and retrieving it later.

If memory support is unavailable:

- keep the instruction in the current session context
- mention that cross-session persistence depends on the host runtime
- do not claim the preference will be remembered later

## Tips

- More context is not always better — irrelevant context can confuse
- Load context incrementally as needed
- When switching tasks, explicitly reset or summarize
- For long sessions, periodically confirm shared understanding
- Interrupt early when drift is obvious; it is cheaper than recovering later
- Prefer compact checkpoint summaries over carrying full chat history forever
- Keep persistent constraints (like content-integrity) always active
- Use memory for confirmed cross-task preferences, not for temporary task state
