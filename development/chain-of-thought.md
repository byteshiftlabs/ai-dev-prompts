# Chain of Thought

Request step-by-step reasoning for complex problems.

## Prompt

```
[PROBLEM_OR_TASK]

Think through this step by step:
1. First, understand what is being asked
2. Identify the key components or constraints
3. Consider possible approaches
4. Choose the best approach and explain why
5. Then implement the solution

Show your reasoning before providing the final answer.
```

## Placeholders

- `[PROBLEM_OR_TASK]`: The complex problem to solve

## Variations

### Debugging with reasoning
```
Debug this issue: [DESCRIPTION]

Step through the problem:
1. What is the expected behavior?
2. What is the actual behavior?
3. What are possible causes?
4. How can we verify each cause?
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
2. Are there any bugs or edge cases?
3. Is it readable and maintainable?
4. What improvements would you suggest and why?
```

## Tips

- Chain-of-thought improves accuracy on complex, multi-step problems
- Explicitly asking for reasoning prevents jumping to conclusions
- Useful for debugging, architecture, and any non-trivial decision
- "Explain your thinking" catches errors before they become code

---

## Meta-Prompting

Force explicit reasoning before implementation. Catches misunderstandings before wasted effort and surfaces hidden assumptions.

### Prompt

```
Before writing any code, respond with:

## Understanding
What I understood from this request:

## Assumptions
What I'm assuming (that wasn't explicitly stated):

## Questions
Clarifications I need (if any):

## Approach
How I plan to implement this:

Wait for my confirmation before proceeding.

---

[TASK]
```

### Variations

#### Quick meta-check
```
[TASK]

Before implementing: What's your interpretation? What could go wrong?
```

#### Assumption surfacing
```
[TASK]

List every assumption you're making. I'll correct any that are wrong before you start.
```

#### Risk identification
```
[TASK]

Before coding, identify:
1. The trickiest part of this task
2. Where bugs are most likely to hide
3. What you're least certain about
```

### Tips

- Especially valuable for ambiguous or complex requests
- The 2-minute pause saves hours of rework
- Combine with a [persona](personas.md) for structured expert reviews
