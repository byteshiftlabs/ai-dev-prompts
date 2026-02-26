# Scope Control

Stay focused on the immediate task. Avoid scope creep.

## Prompt

```
Implement [TASK] in [PROJECT_NAME].

[content-integrity constraint]

Scope rules:
- Focus only on what is explicitly requested
- Do not add features, optimizations, or improvements unless asked
- If you notice something out of scope that needs attention, note it as a TODO comment or mention it separately — do not implement it
- If the request is ambiguous, ask for clarification rather than expanding scope
```

## Placeholders

- `[TASK]`: The specific task to complete
- `[PROJECT_NAME]`: Project context
- `[content-integrity constraint]`: See [content-integrity.md](content-integrity.md)

## Variations

### Strict scope
```
Implement ONLY [SPECIFIC_CHANGE] in [FILE].
Do not modify any other functionality.
Do not refactor adjacent code.
Do not add error handling unless it's part of the request.
```

### Scope with notes
```
Implement [TASK].
If you encounter issues or improvements outside the scope, list them at the end under "## Out of Scope Notes" but do not implement them.
```

## Tips

- "While I'm here..." is the beginning of scope creep
- Unrelated improvements belong in separate commits/PRs
- A focused PR is easier to review than one that "also fixes a few things"
- When in doubt, do less and ask
