# Task Decomposition

Break complex requests into clear, numbered sub-tasks.

## Prompt

```
[COMPLEX_TASK]

Break this into numbered steps:
1. [First sub-task]
2. [Second sub-task]
3. [Third sub-task]
...

Execute each step in order, confirming completion before moving to the next.
```

## Placeholders

- `[COMPLEX_TASK]`: The large task to decompose

## Variations

### Pre-decomposed request
```
Implement the following in order:
1. First, [TASK_1]
2. Then, [TASK_2]
3. Finally, [TASK_3]

Complete each step fully before starting the next.
Report progress after each step.
```

### Ask for decomposition
```
I want to [GOAL].

What steps would you break this into?
List them before starting, so I can review the plan.
```

### Parallel-safe decomposition
```
These tasks are independent and can be done in any order:
- [TASK_A]
- [TASK_B]
- [TASK_C]

These depend on the above and must come after:
- [TASK_D] (requires A)
- [TASK_E] (requires B and C)
```

## Tips

- Numbered lists are clearer than prose for multi-step work
- Explicit ordering prevents AI from jumping ahead
- "Report after each step" gives you checkpoints
- Decomposition also helps estimate effort and catch missing requirements
- If unsure how to decompose, ask the AI to propose a breakdown first
