---
pack: task-workflows
summary: Structured process for reproducing issues, finding root cause, and applying fixes.
tags: [workflow, debugging, root-cause]
---

# Debugging

Use a structured approach to diagnosing and fixing issues.

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

Find the root cause, explain it clearly, and apply the fix.
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
Run static analysis on [PROJECT_NAME] and fix all findings
per code-review.md static analysis section.

Rebuild and re-run analysis until zero findings remain.
Watch for cascading findings. Fixing one condition may expose the next redundant condition.
```

### Memory leak audit (Valgrind)
```
Audit [PROJECT_NAME] for memory leaks using Valgrind:

valgrind --leak-check=full --show-leak-kinds=all --error-exitcode=1 ./[BINARY] [ARGS]

For each leak:
1. Read the allocation stack trace and identify which function allocated and which path failed to free it
2. Fix the leak at the earliest error return that skips cleanup
3. Re-run Valgrind until "All heap blocks were freed" on both valid and malformed inputs
4. Test error paths explicitly because many leaks hide in early returns after partial allocation

Test with multiple input classes:
- Valid inputs
- Malformed inputs
- Edge cases such as empty files or oversized inputs
```

### Memory errors (AddressSanitizer)
```
Build [PROJECT_NAME] with AddressSanitizer to detect memory errors at runtime:

cmake -DCMAKE_BUILD_TYPE=Debug -DCMAKE_C_FLAGS="-fsanitize=address -fno-omit-frame-pointer" -DCMAKE_EXE_LINKER_FLAGS="-fsanitize=address" ..

Or for direct compilation:
gcc -fsanitize=address -fno-omit-frame-pointer -g -o [BINARY] [SOURCES]

Run the instrumented binary normally. ASan reports errors to stderr on detection:
./[BINARY] [ARGS]

ASan catches issues Valgrind may miss and vice versa:
- Heap, stack, and global buffer overflows
- Use-after-free and double-free
- Stack use after return
- Memory leaks, with ASAN_OPTIONS=detect_leaks=1

For each ASan finding:
1. Read the error type and the allocation and deallocation stack traces
2. Fix the root cause rather than suppressing it without justification
3. Rebuild and re-run until zero ASan errors remain for all input classes
```

## Tips

- Always include the actual error output. Do not replace it with a summary.
- Specify versions when they matter, such as Python, libraries, compilers, or operating system details.
- Mention recent changes if the code worked before and then started failing.
