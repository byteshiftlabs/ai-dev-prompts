# Code Review

Audit code quality with emphasis on readability and maintainability.

## Core Principle

**Code is read far more often than it is written.** Prioritize clarity over cleverness. Every piece of code should be immediately understandable to a new developer.

---

## Python

```
Review [PROJECT_NAME] for code quality.

[content-integrity constraint]

Check for:
1. PEP8 compliance (except line length)
2. Imports at the top of each file, properly organized (stdlib → third-party → local)
3. Clear, descriptive naming for classes, functions, and variables
4. No monolithic modules — proper separation of concerns
5. No magic numbers — use named constants
6. Readable code structure — logical flow, consistent formatting

For each issue:
- File and location
- Problem description
- Applied fix

After fixes, commit following git-workflow.md.
```

---

## C

```
Review [PROJECT_NAME] for code quality.

[content-integrity constraint]

Check for:
1. GNU coding standards compliance (https://www.gnu.org/prep/standards/)
2. Clear, descriptive naming for structs, functions, and variables
3. No magic numbers — use #define or const
4. Readable code structure — consistent indentation, logical grouping

For each issue:
- File and location
- Problem description
- Applied fix

After fixes, commit following git-workflow.md.
```

---

## C++

```
Review [PROJECT_NAME] for code quality.

[content-integrity constraint]

Check for:
1. C++ Core Guidelines compliance (https://isocpp.github.io/CppCoreGuidelines/)
2. Clear, descriptive naming for classes, methods, and variables
3. No magic numbers — use constexpr or const
4. Readable code structure — consistent style, logical organization

For each issue:
- File and location
- Problem description
- Applied fix

After fixes, commit following git-workflow.md.
```

---

## Placeholders

- `[PROJECT_NAME]`: Target project or directory
- `[content-integrity constraint]`: See [content-integrity.md](content-integrity.md)

## Quick Variations

| Use case | Prompt |
|----------|--------|
| Quick check | `Check [FILE] for PEP8 and magic numbers only.` |
| Naming audit | `Review all identifiers in [PROJECT] for clarity. Rename ambiguous names.` |
| Imports only | `Organize imports in [FILE]: stdlib → third-party → local, at file top.` |

## Tips

- Run after every change, major or minor
- Readable code reduces bugs and speeds up onboarding
- When in doubt, choose the more explicit option
