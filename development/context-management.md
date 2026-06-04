# Context Management

Control what context is provided to maximize efficiency and relevance.

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

## Durable Preference Workflow

When managing context, separate session context from durable user memory.

Persist to durable memory only after the work is clear enough to classify:

- store explicit user preferences about tools, communication style, output shape, or recurring workflow constraints
- store stable cross-task instructions that should still apply in a future session
- do not store active task state, temporary assumptions, repo-specific facts, or unresolved guesses

Good times to persist:

- immediately after the user says to remember a preference
- after a repeated correction reveals a stable preference
- at the end of a task when a reusable instruction has been confirmed

Do not persist:

- during early exploration when the signal is uncertain
- for one-off exceptions tied to a single task
- when the information belongs in repository memory or the current session only

When in doubt, keep it in session context first and persist only after durability is evident.

## Tips

- More context is not always better — irrelevant context can confuse
- Load context incrementally as needed
- When switching tasks, explicitly reset or summarize
- For long sessions, periodically confirm shared understanding
- Keep persistent constraints (like content-integrity) always active
- Use durable memory for confirmed cross-task user preferences, not for temporary task state
