# Production Ready Check

Comprehensive checklist to prepare a software project for public release.

## Overview

This guide consolidates checks from all development guides before making a project public. Work through each phase sequentially — later phases depend on earlier ones being complete.

**Related guides**: [architecture.md](../setup/architecture.md) | [code-review.md](../development/code-review.md) | [error-handling.md](../development/error-handling.md) | [reproducibility.md](../setup/reproducibility.md) | [documentation.md](../setup/documentation.md) | [test-generation.md](../development/test-generation.md) | [git-workflow.md](../development/git-workflow.md)

When an AI agent runs this release check, use [exhaustive-review.md](../development/exhaustive-review.md) to create and maintain the findings artifact. This document is the release gate, not the audit protocol.

---

## Phase 1: Architecture Review

Good architecture makes change easy. Review structural integrity first.

```
Review [PROJECT_NAME] architecture per architecture.md.
Verify all 10 principles: layered separation, dependency direction,
single responsibility, configuration externalization, single entry point,
separation of concerns, fail-fast validation, state minimization,
module size limits, and clear interfaces.
```

See [architecture.md](../setup/architecture.md) for the full principle list and prompts.

---

## Phase 2: Code Quality

Clean, readable code is the foundation.

```
Review [PROJECT_NAME] for code quality before public release.
Run a full code review per code-review.md for the project's language(s).
Apply structural improvements per refactoring.md.
Verify separation of concerns per architecture.md §6.
```

See [code-review.md](../development/code-review.md) | [refactoring.md](../development/refactoring.md) | [architecture.md](../setup/architecture.md)

---

## Phase 3: Robustness

Production code must handle failures gracefully.

### Error Handling
```
Implement production-ready error handling for [PROJECT_NAME]
per error-handling.md.
```

See [error-handling.md](../development/error-handling.md) for custom exceptions, logging levels, and user-facing messages.

### Fail Fast
```
Verify [PROJECT_NAME] validates early at system boundaries
per ../setup/architecture.md §7.
```

### Edge Cases
```
Review [PROJECT_NAME] for edge case handling:
- Empty/null inputs
- Boundary values (0, negative, max values)
- Invalid types and malformed data
- Network/IO failures and timeouts
- Permission and authorization errors
- Configuration errors
```

---

## Phase 4: Testing

Public projects need verifiable correctness.

```
Generate tests for [PROJECT_NAME] before public release
per test-generation.md.
```

See [test-generation.md](../development/test-generation.md) for unit test patterns, edge case coverage, and naming conventions.

### Verification
```
Verify [PROJECT_NAME] works correctly:
- Clone to a fresh directory
- Follow README setup instructions exactly
- Run all tests with warnings enabled — they must pass with zero errors AND zero warnings
- Execute main functionality end-to-end
- Test on a clean environment (not your development machine)
```

For Python projects:
```bash
pytest tests/ -v -W default --tb=short
```

---

## Phase 5: Reproducibility

Anyone should be able to reproduce results.

```
Ensure reproducibility for [PROJECT_NAME] per reproducibility.md.
Verify all items on its checklist.
```

See [reproducibility.md](../setup/reproducibility.md) for dependency pinning, environment documentation, and ML seed management.

---

## Phase 6: Documentation

Documentation is the first thing users see.

### README
```
Generate a production README for [PROJECT_NAME]
following the template in documentation.md.
```

See [documentation.md](../setup/documentation.md) for the full README template and inline comment guidelines.

### Content Integrity
```
Verify documentation accuracy per content-integrity.md.
```

See [content-integrity.md](../development/content-integrity.md).

---

## Phase 7: Release Preparation

Final steps before going public. Apply [git-workflow.md](../development/git-workflow.md).

### Repository Cleanup
```
Prepare [PROJECT_NAME] repository for public release:
- Verify .gitignore excludes build artifacts, caches, secrets
- Verify compiled binaries, packaged outputs, generated archives, and similar artifacts are not committed unless the project explicitly requires them
- Remove or redact any sensitive data from history
- Ensure no API keys, passwords, or credentials in code
- No TODO comments left for critical functionality
- Add appropriate LICENSE file
- Add CONTRIBUTING.md if accepting contributions
```

### Git Hygiene
```
Review git history per git-workflow.md.
```

See [git-workflow.md](../development/git-workflow.md) for commit message format, branch naming, and PR conventions.

### Version and Tag
```
Prepare release v[X.Y.Z] for [PROJECT_NAME]:
- Update version numbers in code/config
- Create git tag: git tag -a v[X.Y.Z] -m "Release v[X.Y.Z]"
- Write release notes summarizing changes
```

Apply semantic versioning when choosing `X.Y.Z`:

- Patch release (`vX.Y.Z+1`) for backward-compatible bug fixes, release hardening, CI updates, documentation corrections, and test-only coverage improvements
- Minor release (`vX.Y+1.0`) for backward-compatible feature additions or meaningful expansion of supported behavior
- Major release (`vX+1.0.0`) for breaking changes, incompatible defaults, removed APIs, or changed compatibility guarantees
- Optional pre-releases may use `vX.Y.Z-alpha.N`, `vX.Y.Z-beta.N`, or `vX.Y.Z-rc.N` before the final `vX.Y.Z` tag

Release naming rules:

- Use the exact same version string for the annotated git tag and the GitHub Release title
- Create releases from the merge commit on the default branch unless the repository explicitly documents a maintenance-branch workflow
- Release notes should group changes under at least: Summary, Changes, and Verification

---

## Final Checklist

Before publishing, verify all items:

### Architecture
- [ ] Clear layered separation (interface → logic → data)
- [ ] Dependencies flow inward, no circular dependencies
- [ ] Each module has single, clear responsibility
- [ ] Configuration externalized (no hardcoded paths/URLs/credentials)
- [ ] Single, clear entry point

### Code Quality
- [ ] Passes language-specific linting
- [ ] Passes static analysis with zero findings (cppcheck, clang-tidy, pylint)
- [ ] No magic numbers or hardcoded values in function calls
- [ ] All constants are named and centralized
- [ ] No ambiguous naming (classes, functions, variables)
- [ ] No shadow variables (locals must not shadow members, parameters, or outer variables)
- [ ] Prefer string methods over regex
- [ ] Prefer STL algorithms over raw loops where intent is clearer
- [ ] Const-correct: read-only references and pointers are const-qualified
- [ ] No dead code or unused imports
- [ ] No dead stub files (TODO-only placeholders with no real logic)
- [ ] No code duplication (3+ occurrences extracted)
- [ ] Monolithic modules split (<500 lines each)
- [ ] Complex logic has comments explaining "why"
- [ ] Copyright years are current

### Robustness
- [ ] Custom exceptions for domain errors
- [ ] All errors have user-friendly messages
- [ ] Logging configured at appropriate levels
- [ ] Inputs validated at entry points
- [ ] Edge cases handled gracefully
- [ ] No bare except: clauses

### Testing
- [ ] Unit tests for all public API
- [ ] Integration tests for module interactions
- [ ] Edge case coverage
- [ ] All tests pass on clean clone with zero warnings
- [ ] No flaky tests

### Reproducibility
- [ ] All dependencies pinned to exact versions
- [ ] Lockfile committed (poetry.lock, package-lock.json, etc.)
- [ ] Language/compiler version documented
- [ ] Default builds avoid compiler optimization flags unless the project explicitly requires them
- [ ] System dependencies documented
- [ ] .env.example provided for environment variables
- [ ] Random seeds set (for ML/stochastic projects)

### Repository Hygiene
- [ ] No compiled binaries, packaged archives, or build artifacts committed unless the project explicitly requires them

### Documentation
- [ ] README with clear one-line description
- [ ] Overview explains purpose and value
- [ ] Quick Start with copy-paste commands
- [ ] All requirements listed with versions
- [ ] Project structure documented
- [ ] License file present
- [ ] No fabricated metrics or placeholder data
- [ ] All links and references valid

### Repository
- [ ] .gitignore properly configured
- [ ] No secrets in code or history
- [ ] No critical TODOs left unresolved
- [ ] Clean commit history with clear messages
- [ ] Version tag created
- [ ] Release notes written

---

## Tips

- Work through phases in order — don't skip ahead
- Each phase should result in a commit
- Get a fresh perspective: have someone else try the Quick Start
- The "works on my machine" problem is real — test on clean environments
- Less is more: remove features that aren't ready rather than shipping incomplete work
- If adding a feature requires modifying many unrelated files, the architecture needs work
- A focused release is better than a feature-complete mess

---

## Mechanical Verification

The checklists above describe *what* to check. This section prescribes *how* — concrete, repeatable steps that eliminate subjectivity and ensure nothing is missed in a single pass. Run every step; do not skip any.

### Build Verification
```
Build [PROJECT_NAME] under ALL supported configurations and flag combinations:
- Release build with all warnings enabled (-Wall -Wextra -Wpedantic or equivalent)
- Debug build (e.g., -DDEBUG=ON) with all warnings enabled
- Every conditional compilation path (#ifdef DEBUG, #ifdef TESTING, etc.)
  MUST be compiled and verified — not just the default configuration
- Build with static analyzer per [code-review.md](../development/code-review.md) static analysis section
- For C++: run cppcheck and resolve every finding (see code-review.md for the
  command and common finding catalog)
- Count: warnings MUST be exactly zero in ALL configurations
- Count: static analysis findings MUST be exactly zero
  (suppress intentional patterns in a suppressions file with justification)
```

### Grep-Based Code Sweep
Run these searches across ALL source files. Each match is a potential issue — verify or fix every one:
```
Perform a mechanical grep sweep of [PROJECT_NAME] source code:

1. GLOBAL STATE: Search for non-static global variables (extern or file-scope
   without static). Every global accessed only within its own .c file MUST be
   static. Every global exposed in a header MUST have a justification.

2. CONST CORRECTNESS:
   a. Every function returning a string literal MUST return const char*, not char*.
   b. Every function parameter that is not modified MUST be declared const.
   c. Every pointer-to-read-only-data MUST be const-qualified.

3. BUFFER SAFETY: Search for ALL fixed-size arrays and every loop/copy that
   writes into them.
   - Every write loop MUST have a bounds check preventing overflow.
   - Every strncpy/snprintf MUST clamp length to buffer_size - 1.
   - Every strdup MUST be wrapped in a null-checked helper (e.g., safe_strdup).

3b. VARIABLE SCOPE: Search for variables declared at a wider scope than
    necessary. Every variable MUST be declared in the narrowest enclosing
    block where it is used — not hoisted to the function or outer block level.
    Move loop-body-only variables inside the loop, branch-only variables
    inside the branch.

4. RETURN VALUE CHECKING: Search for every function call that returns an error
   code or status (e.g., strtol, strtoi, fopen, malloc, strdup). Every call
   site MUST check the return value and handle failure.

5. NULL DEREFERENCE: Trace every pointer dereference back to its source. If the
   pointer came from a function that can return NULL (malloc, find_*, get_*),
   there MUST be a NULL check before the dereference.

6. SIGNED/UNSIGNED SAFETY: Search for bitwise operations (<<, >>, &, |, ^) on
   signed integers. Signed shifts are undefined behavior in C — cast to unsigned
   first. Search for signed/unsigned comparison warnings.

7. UNUSED INCLUDES: For each #include in every source file, verify at least one
   symbol from that header is actually used. Remove any that aren't.

8. TRANSITIVE INCLUDE FRAGILITY: For each header that uses a type (FILE*, size_t,
   etc.), verify it directly includes the header that defines that type. Do not
   rely on transitive includes through other project headers — they can break
   when headers are reorganized.

9. PARAMETER NAME CONSISTENCY: For every function, compare parameter names in the
   header declaration vs the .c definition. They MUST match exactly (unless
   intentionally different for C++ compatibility — document why in a comment).

10. DEAD CODE:
    a. Search for TODO, FIXME, HACK, XXX comments. Each is either a blocker
       (fix it) or stale (remove it).
    b. Search for functions not called from anywhere (use cppcheck unusedFunction
       or equivalent). Remove or justify each one.
    c. Search for unreachable code paths: if a function always calls exit() or
       returns before reaching a code path, that path is dead.
    d. Search for stub files that contain only TODO placeholders and no real
       implementation. Either implement them or remove them entirely —
       including from ALL build targets (CMakeLists.txt, Makefile, test builds).

11. STALE COMMENTS: Search for comments referencing moved, renamed, or deleted
    functions, files, parameters, or patterns. Cross-reference every comment
    that mentions a function or variable name against the actual code.

12. MAGIC NUMBERS: Search for bare numeric literals (integers, floats) in
    function calls, array sizes, and conditionals. Every one MUST be replaced
    with a named constant (#define, enum, or const).

13. DUPLICATE LOGIC: Search for functions with similar structure or identical
    switch/dispatch patterns. If two functions dispatch on the same enum or
    do similar work, consolidate via function pointers or shared helpers.
```

### Error Handling Integrity
```
Verify [PROJECT_NAME] error handling is consistent and complete:

1. ERROR HANDLER BYPASS: Search for direct printf/fprintf/perror calls that
   report errors or warnings. Every diagnostic message MUST go through the
   project's error handler (log_error, log_warning, etc.) — not raw stdio.

2. EXIT IN LIBRARY CODE: Search for exit() calls outside of main().
   Library/module code should return error codes, not terminate the process.
   If exit() is used (acceptable in early-stage projects), document it as a
   known limitation and verify error-counting APIs are not dead code.

3. ERROR RECOVERY REACHABILITY: If the project has error-counting functions
   (get_error_count, has_errors), verify they are actually consulted somewhere.
   If errors always trigger immediate exit(), the counting API is dead code.

4. RESOURCE CLEANUP: For every fopen/malloc/strdup, trace the corresponding
   fclose/free. Verify cleanup happens on both success and error paths.
```

### C/C++ Interoperability (C projects with C++ tests or consumers)
```
Verify [PROJECT_NAME] headers are safe for C++ inclusion:

1. EXTERN C GUARDS: Every C header (.h) that may be included from C++ MUST have:
     #ifdef __cplusplus
     extern "C" {
     #endif
   at the top, and the matching closing block at the bottom.

2. INCLUDE GUARDS: Every header MUST have #ifndef/#define/#endif include guards.
   The guard name MUST match the filename (e.g., TOKEN_H for token.h).

3. C++ RESERVED WORDS: Search all C header declarations for parameter names that
   are C++ reserved words: class, operator, new, delete, template, namespace,
   virtual, override, final, throw, catch, try, explicit, export, register,
   mutable, typename, typeid, const_cast, dynamic_cast, reinterpret_cast,
   static_cast, and, or, not, xor, bitand, bitor, compl.
   If found: use a different name in the declaration, keep the original in the
   .c definition (parameter names need not match between declaration and
   definition in C, but document the reason).
```

### Documentation Cross-Reference
```
Cross-reference [PROJECT_NAME] documentation against actual code:

1. LICENSE CONSISTENCY: Compare the license stated in README, docs/, and the
   actual LICENSE file. All occurrences MUST name the exact same license.

2. FUNCTION SIGNATURES: Search all documentation files (.rst, .md) for function
   signatures or code examples. Compare each one against the actual code.
   Stale signatures (wrong parameter types/names, renamed functions) are errors.

3. MODULE DESCRIPTIONS: For each module described in architecture docs, verify
   the description matches what the code actually does today. Especially after
   refactoring (moving functions between modules, renaming, splitting files).

4. QUICK START: Follow the README Quick Start from scratch in a clean directory.
   Every command MUST work exactly as documented.

5. LINKS AND URLS: Check every URL, cross-reference, and relative link in all
   documentation files. Dead links are errors.

6. YEAR AND ATTRIBUTION: Verify copyright years are current (e.g., if project
   started in 2025 and current year is 2026, use "2025-2026"). Verify
   author/org names are consistent across LICENSE, README, docs/conf.py,
   and any source file headers. Update all occurrences in a single pass.

7. PATH REFERENCES: Search docs and scripts for hardcoded file paths or location
   comments (e.g., "Location: tools/old/path/"). Verify each matches reality.
```

### Dependency Pinning
```
Verify [PROJECT_NAME] dependencies are reproducible:

1. For each external dependency fetched at build time, verify it has a
   pinned version AND an integrity hash (SHA256, lockfile entry, etc.).

2. For each tool mentioned in build docs (compiler, linter, formatter),
   verify the minimum version is documented.

3. Search for any URL in build files (CMakeLists.txt, Makefile, setup.py,
   package.json) — each one MUST have version + hash pinning.
```

### Encapsulation Enforcement
```
Verify [PROJECT_NAME] encapsulation is compiler-enforced, not just convention:

1. For every module that exposes an API (accessor functions, register/reset),
   verify the underlying data is static (file-scope) in the .c file.
   API-only encapsulation without static is not real encapsulation —
   any translation unit can still access the raw global.

2. For every header in the public include directory, verify a non-module
   consumer actually needs it. For every individual symbol in a public header,
   verify external consumers use it — internal-only symbols belong in internal
   headers (src/*/). Headers used only by one module's own .c files belong in
   that module's source directory.

3. For C/C++ projects: verify all internal helper functions are static.
   Non-static functions not declared in any header are linker-visible accidents.

4. For every module with a "reset" or "clear" function, verify it fully resets
   ALL mutable state — not just counters but also arrays/buffers if applicable.
```
