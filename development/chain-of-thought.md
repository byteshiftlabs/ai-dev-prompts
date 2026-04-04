---
pack: task-workflows
summary: Adds explicit staged reasoning for ambiguous or high-complexity tasks.
tags: [workflow, reasoning, ambiguity]
---

# Structured Reasoning

Use explicit analysis for complex problems.

## Prompt

```
[PROBLEM_OR_TASK]

Work through this in order:
1. State what is being asked.
2. Identify the key constraints or moving parts.
3. Compare plausible approaches.
4. Choose the best approach and explain why.
5. Then implement the solution.

Summarize the reasoning that supports the result before providing the final answer.
```

## Placeholders

- `[PROBLEM_OR_TASK]`: The problem or task to solve

## Variations

### Debugging with reasoning
```
Debug this issue: [DESCRIPTION]

Work through the problem:
1. What is the expected behavior?
2. What is the actual behavior?
3. What are plausible causes?
4. How can each cause be checked?
5. What is the most likely root cause?
6. What is the fix?
```

### Architecture decision
```
Design [COMPONENT] for [PROJECT].

Reason through:
1. What are the requirements?
2. What are the constraints?
3. What patterns could apply?
4. What are the trade-offs of each?
5. Which approach fits best and why?
```

### Code review reasoning
```
Review [CODE] and explain:
1. What does this code do?
2. Are there bugs or edge cases?
3. Is it readable and maintainable?
4. What improvements would you suggest and why?
```

## Tips

- Explicit analysis improves accuracy on complex, multi-step problems
- Asking for reasoning reduces the chance of jumping to conclusions
- This is useful for debugging, architecture, and other non-trivial decisions
- A short analysis step can catch errors before they become code

---

## Pre-Implementation Check

Ask for a short analysis before implementation. This catches misunderstandings early and surfaces assumptions before work starts.

### Prompt

```
Before writing any code, respond with:

## Understanding
What I understood from this request:

## Assumptions
What I am assuming that was not explicitly stated:

## Questions
Clarifications I need, if any:

## Approach
How I plan to implement this:

Wait for my confirmation before proceeding.

---

[TASK]
```

### Variations

#### Quick pre-check
```
[TASK]

Before implementing: what is your interpretation, and what could go wrong?
```

#### Assumption surfacing
```
[TASK]

List every assumption you are making. I will correct any that are wrong before you start.
```

#### Risk identification
```
[TASK]

Before coding, identify:
1. The trickiest part of this task
2. Where bugs are most likely to hide
3. What you are least certain about
```

### Tips

- This is especially valuable for ambiguous or complex requests
- A short pause before implementation often prevents major rework
- Combine it with a [persona](../core/personas.md) when you want a specific review posture
