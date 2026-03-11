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

### Memory leak audit (Valgrind)
```
Audit [PROJECT_NAME] for memory leaks using Valgrind:

valgrind --leak-check=full --show-leak-kinds=all --error-exitcode=1 ./[BINARY] [ARGS]

For each leak:
1. Read the allocation stack trace — identify which function allocated and which path failed to free
2. Fix the leak at the earliest error return that skips cleanup
3. Re-run Valgrind until "All heap blocks were freed" on both valid and malformed inputs
4. Test error paths explicitly — most leaks hide in early returns after partial allocation

Test with multiple input classes:
- Valid inputs (happy path)
- Malformed inputs (parser/validation error paths)
- Edge cases (empty files, oversized inputs)
```

### Memory errors (AddressSanitizer)
```
Build [PROJECT_NAME] with AddressSanitizer to detect memory errors at runtime:

cmake -DCMAKE_BUILD_TYPE=Debug -DCMAKE_C_FLAGS="-fsanitize=address -fno-omit-frame-pointer" -DCMAKE_EXE_LINKER_FLAGS="-fsanitize=address" ..

Or for direct compilation:
gcc -fsanitize=address -fno-omit-frame-pointer -g -o [BINARY] [SOURCES]

Run the instrumented binary normally — ASan reports errors to stderr on detection:
./[BINARY] [ARGS]

ASan catches issues Valgrind may miss and vice versa:
- Heap/stack/global buffer overflows
- Use-after-free and double-free
- Stack use after return
- Memory leaks (with ASAN_OPTIONS=detect_leaks=1)

For each ASan finding:
1. Read the error type and allocation/deallocation stack traces
2. Fix the root cause — do not suppress without justification
3. Rebuild and re-run until zero ASan errors on all input classes
```

## Tips

- Always include actual error output - don't summarize
- Specify versions (Python, dependencies) when relevant
- Mention recent changes if the code was working before
