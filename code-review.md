# Code Review

Comprehensive code quality audit with specific checks.

## Prompt (Python)

```
Make sure the following apply to [PROJECT_NAME]:

[content-integrity constraint]

1. PEP8 compliance (except line length)
2. No ambiguous naming neither in classes nor functions nor variables (clear, descriptive identifiers)
3. No monolithic modules (proper separation of concerns)
4. No magic numbers (use named constants)

For each issue found:
- Identify the file and location
- Explain the problem
- Apply the fix

After all fixes, commit with a descriptive message following the existing commit style.
```

## Prompt (C)

```
Make sure the following apply to [PROJECT_NAME]:

[content-integrity constraint]

1. GNU coding standards compliance (https://www.gnu.org/prep/standards/)
2. No ambiguous naming neither in structs nor functions nor variables
3. No magic numbers (use #define or const)

For each issue found:
- Identify the file and location
- Explain the problem
- Apply the fix

After all fixes, commit with a descriptive message following the existing commit style.
```

## Prompt (C++)

```
Make sure the following apply to [PROJECT_NAME]:

[content-integrity constraint]

1. C++ Core Guidelines compliance (https://isocpp.github.io/CppCoreGuidelines/)
2. No ambiguous naming neither in classes nor methods nor variables
3. No magic numbers (use constexpr or const)

For each issue found:
- Identify the file and location
- Explain the problem
- Apply the fix

After all fixes, commit with a descriptive message following the existing commit style.
```

## Placeholders

- `[PROJECT_NAME]`: Target project or directory to review
- `[content-integrity constraint]`: See [content-integrity.md](content-integrity.md)

## Variations

### Quick syntax check
```
Check [FILE] for PEP8 compliance and magic numbers only.
```

### Naming audit
```
Review all variable, function, and class names in [PROJECT] for clarity.
Rename any ambiguous identifiers (single letters, abbreviations, generic names).
```

## Tips

- Run after every kind of addition (whether major or minor)
- Combine with git commit for atomic changes
- Specify "except line length" if your project tolerates longer lines
