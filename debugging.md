# Debugging

Structured approach to diagnosing and fixing issues.

## Prompt

```
Debug the following issue in [PROJECT_NAME]:

**Symptom**: [WHAT_HAPPENS]
**Expected**: [WHAT_SHOULD_HAPPEN]
**Reproduction**: [STEPS_OR_COMMAND]
**Error output** (if any):
```
[PASTE_ERROR]
```

[content-integrity constraint]

Investigate the root cause, explain the issue, and apply the fix.
```

## Placeholders

- `[PROJECT_NAME]`: Project context
- `[WHAT_HAPPENS]`: Observed behavior
- `[WHAT_SHOULD_HAPPEN]`: Expected behavior
- `[STEPS_OR_COMMAND]`: How to reproduce
- `[PASTE_ERROR]`: Stack trace or error message
- `[content-integrity constraint]`: See [content-integrity.md](content-integrity.md)

## Variations

### Silent failure
```
[FUNCTION] returns wrong results without errors. Expected: [X], Got: [Y]. Trace the data flow and find where it diverges.
```

### Environment issue
```
Works on [ENV_A] but fails on [ENV_B]. Compare dependencies, configs, and identify the difference.
```

### Static analysis findings
```
Run static analysis on [PROJECT_NAME] and fix all findings:

cppcheck --inline-suppr --enable=all -I src/ src/

For each finding:
1. Understand the root cause (shadow variable, redundant condition, const-correctness, etc.)
2. Fix it properly — do not blindly suppress
3. If suppression is necessary (e.g., loop with side-effect index), add inline suppression with justification
4. Rebuild and re-run analysis until zero findings remain
5. Watch for cascading findings — fixing one condition may reveal the next one is also redundant
```

## Tips

- Always include actual error output - don't summarize
- Specify versions (Python, dependencies) when relevant
- Mention recent changes if the code was working before
