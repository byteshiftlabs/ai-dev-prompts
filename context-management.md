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

## Tips

- More context is not always better — irrelevant context can confuse
- Load context incrementally as needed
- When switching tasks, explicitly reset or summarize
- For long sessions, periodically confirm shared understanding
- Keep persistent constraints (like content-integrity) always active
