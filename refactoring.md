# Refactoring

Structural code improvements without changing external behavior.

## Prompt

```
Refactor [FILE_OR_MODULE] in [PROJECT_NAME].

[content-integrity constraint]

Goals:
- Improve code organization and readability
- Reduce complexity and duplication
- Apply appropriate design patterns
- Maintain all existing functionality

Before any changes:
1. Identify current issues (coupling, duplication, complexity)
2. Propose the refactoring approach
3. Confirm approach before proceeding

After refactoring, verify behavior is unchanged.
```

## Placeholders

- `[FILE_OR_MODULE]`: Target code to refactor
- `[PROJECT_NAME]`: Project context
- `[content-integrity constraint]`: See [content-integrity.md](content-integrity.md)

## Variations

### Extract module
```
Extract [FUNCTIONALITY] from [FILE] into a separate module.
- Identify all related functions, classes, and constants
- Create new module with clear single responsibility
- Update imports in original file
- Ensure no circular dependencies
```

### Break up monolith
```
[FILE] is too large ([X] lines). Split it into focused modules:
- Analyze responsibilities and group related code
- Propose module boundaries
- Extract each group into its own file
- Create an __init__.py if needed for clean imports
```

### Reduce duplication
```
Find and eliminate code duplication in [PROJECT_OR_MODULE]:
- Identify repeated patterns (3+ occurrences)
- Extract common logic into reusable functions/classes
- Replace duplicates with calls to shared code
```

### Simplify conditionals
```
Simplify complex conditional logic in [FILE]:
- Replace nested if/else with early returns
- Extract condition checks into named functions
- Consider lookup tables or polymorphism for switch-like patterns
```

### Dependency injection
```
Refactor [MODULE] to use dependency injection:
- Identify hardcoded dependencies
- Convert to constructor/parameter injection
- Improves testability and flexibility
```

## Tips

- Refactor in small, verified steps — not all at once
- Run tests after each change to catch regressions early
- Commit each logical refactoring step separately
- If no tests exist, write them before refactoring
