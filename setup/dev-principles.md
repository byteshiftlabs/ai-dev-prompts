---
pack: task-workflows
summary: General development principles for shaping project setup and implementation choices.
tags: [setup, principles, standards]
---

# Development Principles

Define project principles before writing code.

---

## Prompt

```
Before starting work on [PROJECT_NAME], establish and follow these development principles:

1. **Clarity over Cleverness** — code must teach, not just execute. Every line should be understandable without deep context.
2. **Incremental Progress** — small, testable commits. Never combine unrelated changes.
3. **Documentation First** — explain WHY before implementing. Design decisions and hardware/domain behavior documented inline.
4. **Test-Driven** — validate with known-good inputs before moving forward.
5. **Educational Value** — treat the codebase as something another developer should be able to learn from.

Apply these principles to every commit, review, and design decision.
```

## Placeholders

- `[PROJECT_NAME]`: The project these principles apply to

## Variations

### Minimalist (3 principles)
```
Development principles for [PROJECT_NAME]:

1. **Simplicity** — the simplest solution that works correctly
2. **Verify before proceeding** — every change tested before the next
3. **Document why, not what** — code shows what, comments show why
```

### Systems programming
```
Development principles for [PROJECT_NAME]:

1. **Clarity over cleverness** — readable code over clever tricks
2. **Data structures over algorithms** — design around the data, not the other way around
3. **Incremental progress** — small, testable, committed steps
4. **Documentation first** — explain WHY before implementing
5. **Test-driven** — validate against known-good references
6. **Zero warnings** — treat warnings as errors; clean builds always
7. **Named constants** — no magic numbers in logic
8. **Backward compatibility** — public APIs and file formats are sacred
```

### Research / ML project
```
Development principles for [PROJECT_NAME]:

1. **Reproducibility first** — pin seeds, versions, and data checksums
2. **Incremental experiments** — change one variable at a time
3. **Log everything** — parameters, metrics, environment
4. **Separate concerns** — data loading, preprocessing, model, evaluation in distinct modules
5. **Document assumptions** — every simplification and approximation noted
6. **No fabricated results** — only report what was actually measured
```

## Tips

- Define principles at the start, not after avoidable problems appear
- Keep the list short (3–8 items). If there are too many principles, people stop using them.
- Principles should be actionable, not aspirational ("test every change" vs "quality matters")
- Review principles when onboarding new contributors
- If a principle is routinely violated, either enforce it or remove it
- Unless the project says otherwise, keep compiler optimization flags out of the default build so debugging and verification stay predictable
- Do not commit compiled binaries, build outputs, packaged archives, or other generated artifacts
- Combine this with [code-review.md](../development/code-review.md) when checking whether the project follows its own standards

---

## License

CC BY 4.0 — Use freely with attribution.
