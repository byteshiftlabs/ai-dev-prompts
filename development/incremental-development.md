# Incremental Development

Build software in small, verified steps rather than large leaps.

## Prompt

```
Implement [FEATURE] in [PROJECT_NAME] incrementally.

[content-integrity constraint]

Follow this approach:
1. Break the task into the smallest logical steps
2. Implement one step at a time
3. Verify each step works before proceeding
4. Commit after each verified step

Do not move to the next step until the current one is confirmed working.
```

## Placeholders

- `[FEATURE]`: What to implement
- `[PROJECT_NAME]`: Project context
- `[content-integrity constraint]`: See [content-integrity.md](content-integrity.md)

## Variations

### Data pipeline
```
Build the data pipeline for [PROJECT] in stages:
1. Data download/access — verify data is retrievable
2. Data loading — verify data loads correctly
3. Preprocessing — verify transformations are correct
4. Feature extraction — verify features match expectations
5. Output/storage — verify results are saved properly

Test each stage independently before connecting them.
```

### Feature implementation
```
Implement [FEATURE] in these steps:
1. Define the interface (function signatures, types)
2. Implement core logic with hardcoded test values
3. Add input validation
4. Add error handling
5. Connect to real data sources
6. Add tests

Verify each step before proceeding.
```

## Tips

- Smaller steps = easier debugging when something breaks
- "Works on my machine" after each step, not just at the end
- If a step is too big, break it down further
- Commit messages should reflect the incremental progress
