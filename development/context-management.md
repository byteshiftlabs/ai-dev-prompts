---
pack: task-workflows
summary: Helps manage session context, remembered information, and context boundaries.
tags: [workflow, context, memory]
---

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

Ignore information not relevant to the current task.
If you need additional context, ask for specific files or information.
```

## Placeholders

- `[PROJECT_NAME]`: Project being worked on
- `[TASK]`: Current objective
- `[FILE_LIST]`: Files relevant to the task

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

## Memory Note

Deciding what to persist, how to classify it, and whether the host even
supports memory is not this file's job. [core/memory-contract.md](../core/memory-contract.md)
is the source of truth for all of that.

This file only covers session context — what stays in the current
conversation. Once something needs to survive past the session, hand it off
to the rules in memory-contract.md instead of deciding here.

## Tips

- More context is not always better — irrelevant context can confuse
- Load context incrementally as needed
- When switching tasks, explicitly reset or summarize
- For long sessions, periodically confirm shared understanding
- Interrupt early when drift is obvious; it is cheaper than recovering later
- Prefer compact checkpoint summaries over carrying full chat history forever
- Keep persistent constraints (like the shared contract's default operating rules) always active
- Use memory for confirmed cross-task preferences, not for temporary task state
