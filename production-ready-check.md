# Production Ready Check

Comprehensive checklist to prepare a software project for public release.

## Overview

This guide consolidates the prompts and checks needed before making a project public. Work through each phase sequentially — later phases depend on earlier ones being complete.

---

## Phase 1: Code Quality

Clean, readable code is the foundation. A public project will be scrutinized.

### Code Review
Apply [code-review.md](code-review.md) to audit the entire codebase:
```
Review [PROJECT_NAME] for code quality before public release.

Check for:
- Language-specific style compliance
- Clear, descriptive naming throughout
- No ambiguous naming in classes, functions, or variables
- No magic numbers — use named constants
- Prefer string methods over regular expressions where possible
- Proper separation of concerns
- Consistent formatting and structure

Fix all issues before proceeding.
```

### Refactoring
Apply [refactoring.md](refactoring.md) to address structural issues:
```
Identify and fix structural issues in [PROJECT_NAME]:
- Extract duplicated code into reusable functions
- Break up any monolithic modules (>500 lines)
- Simplify complex conditionals
- Remove dead code and unused imports
```

---

## Phase 2: Robustness

Production code must handle failures gracefully.

### Error Handling
Apply [error-handling.md](error-handling.md) to ensure proper error management:
```
Implement production-ready error handling for [PROJECT_NAME]:
- Custom exception classes for domain-specific errors
- Descriptive error messages that help diagnose issues
- User-friendly messages separate from technical logs
- Logging at appropriate levels
- Graceful degradation where possible
```

### Edge Cases
Identify and handle edge cases:
```
Review [PROJECT_NAME] for edge case handling:
- Empty/null inputs
- Boundary values (0, negative, max values)
- Invalid types and malformed data
- Network/IO failures
- Permission errors
```

---

## Phase 3: Testing

Public projects need verifiable correctness.

### Test Coverage
Apply [test-generation.md](test-generation.md) to create a comprehensive test suite:
```
Generate tests for [PROJECT_NAME] before public release:
- Unit tests for all public functions
- Integration tests for module interactions
- Edge case coverage
- Tests should pass on a clean clone
```

### Verification
```
Verify [PROJECT_NAME] works correctly:
- Clone to a fresh directory
- Follow README setup instructions exactly
- Run all tests
- Execute main functionality end-to-end
```

---

## Phase 4: Documentation

Documentation is often the first thing users see.

### README
Apply [documentation.md](documentation.md) to create user-facing docs:
```
Generate a production README for [PROJECT_NAME]:
- Clear one-line description
- Overview explaining purpose and value
- Quick Start with copy-paste commands
- Installation requirements
- Usage examples
- License information
```

### Code Documentation
```
Document [PROJECT_NAME] for contributors:
- Module/file docstrings explaining purpose
- Public API documentation
- Inline comments for complex logic only
- Architecture overview for larger projects
```

---

## Phase 5: Release Preparation

Final steps before going public.

### Repository Cleanup
```
Prepare [PROJECT_NAME] repository for public release:
- Verify .gitignore excludes build artifacts, caches, secrets
- Remove or redact any sensitive data from history
- Ensure no API keys, passwords, or credentials in code
- Add appropriate LICENSE file
- Add CONTRIBUTING.md if accepting contributions
```

### Version and Tag
Apply [git-workflow.md](git-workflow.md) for release tagging:
```
Prepare release v[X.Y.Z] for [PROJECT_NAME]:
- Update version numbers in code/config
- Create git tag: git tag -a v[X.Y.Z] -m "Release v[X.Y.Z]"
- Write release notes summarizing changes
```

---

## Final Checklist

Before publishing, verify all items:

### Code
- [ ] Passes language-specific linting
- [ ] No magic numbers or hardcoded values
- [ ] No ambiguous naming (classes, functions, variables)
- [ ] Prefer string methods over regex
- [ ] No dead code or unused imports
- [ ] Consistent naming and formatting
- [ ] Complex logic has comments

### Robustness
- [ ] Custom exceptions for domain errors
- [ ] All errors have user-friendly messages
- [ ] Logging configured appropriately
- [ ] Edge cases handled gracefully

### Testing
- [ ] Unit tests for public API
- [ ] Integration tests pass
- [ ] Tests run on clean clone
- [ ] No flaky tests

### Documentation
- [ ] README with clear Quick Start
- [ ] Installation requirements listed
- [ ] Usage examples provided
- [ ] License file present

### Repository
- [ ] .gitignore properly configured
- [ ] No secrets in code or history
- [ ] Version tag created
- [ ] Release notes written

---

## Tips

- Work through phases in order — don't skip ahead
- Each phase should result in a commit
- Get a fresh perspective: have someone else try the Quick Start
- The "works on my machine" problem is real — test on clean environments
- Less is more: remove features that aren't ready rather than shipping incomplete work
