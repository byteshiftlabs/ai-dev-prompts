---
pack: task-workflows
summary: Keeps work bounded and prevents opportunistic expansion.
tags: [workflow, scope, control]
---

# Scope Control

Stay focused on the immediate task and avoid scope creep.

## Prompt

```
Implement [TASK] in [PROJECT_NAME].

Scope rules:
- Focus only on what is explicitly requested
- Do not add features, optimizations, or improvements unless asked
- If you notice something out of scope that needs attention, note it separately or in a TODO comment. Do not implement it.
- If the request is ambiguous, ask for clarification rather than expanding scope
```

## Placeholders

- `[TASK]`: The specific task to complete
- `[PROJECT_NAME]`: Project context

## Variations

### Strict scope
```
Implement ONLY [SPECIFIC_CHANGE] in [FILE].
Do not modify any other functionality.
Do not refactor adjacent code.
Do not add error handling unless it is part of the request.
```

### Scope with notes
```
Implement [TASK].
If you encounter issues or improvements outside the scope, list them at the end under "## Out of Scope Notes" but do not implement them.
```

### Minimal code
```
Implement [TASK] with the minimum amount of code necessary.
- Write only the code required to accomplish the task
- Avoid abstractions, utilities, or helpers unless they are essential
- Do not add code "for future use" or "just in case"
- Prefer simple, direct implementations over clever or generic ones
```

## Tips

- "While I am here" is the start of scope creep
- Unrelated improvements belong in separate commits or PRs
- A focused PR is easier to review than one that also changes adjacent areas
- When in doubt, do less and ask
- Every extra line of code increases maintenance cost

## Exceptions: Fix on the Go

Some issues must be fixed immediately when encountered, regardless of current scope:

- **Magic numbers**: Fix immediately per [code-review.md](code-review.md). Do not leave bare literals for later.
- **Shadow variables**: Rename immediately per [code-review.md](code-review.md). They can cause subtle bugs.
- **Copyright years**: Update when you touch a file in a new calendar year.
