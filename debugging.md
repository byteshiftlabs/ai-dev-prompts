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

## Tips

- Always include actual error output - don't summarize
- Specify versions (Python, dependencies) when relevant
- Mention recent changes if the code was working before
