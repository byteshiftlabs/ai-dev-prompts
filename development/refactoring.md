---
pack: task-workflows
summary: Guidance for restructuring code while preserving behavior.
tags: [workflow, refactoring, structure]
---

# Refactoring

Improve code structure without changing external behavior.

## Prompt

```
Refactor [FILE_OR_MODULE] in [PROJECT_NAME].

Goals:
- Improve code organization and readability
- Reduce complexity and duplication
- Apply appropriate design patterns
- Maintain all existing functionality

Before any changes:
1. Identify current issues (coupling, duplication, complexity)
2. Propose the refactoring approach
3. Confirm the approach before proceeding when the user asked for review first or the change is large

After refactoring, verify behavior is unchanged.
```

## Placeholders

- `[FILE_OR_MODULE]`: Target code to refactor
- `[PROJECT_NAME]`: Project context

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
- In sequential if-blocks where each block returns, remove redundant lower-bound checks
  (e.g., if prior block handles x <= 0x07 and returns, the next block's x >= 0x08 is always true)
```

### Remove dead stubs
```
Find and remove dead stub files/code in [PROJECT_OR_MODULE]:
- Search for files containing only TODO placeholders and no real logic
- Search for private/static functions never called from anywhere
- Verify no build targets (CMakeLists.txt, Makefile) reference removed files
- When removing source files, update ALL build targets (main build AND test builds)
```

### Dependency injection
```
Refactor [MODULE] to use dependency injection:
- Identify hardcoded dependencies
- Convert to constructor/parameter injection
- Improves testability and flexibility
```

## Tips

- Refactor in small, verified steps instead of one large rewrite
- Run tests after each change to catch regressions early
- Keep each logical refactoring step separate
- If no tests exist and behavior must stay stable, add them before refactoring
