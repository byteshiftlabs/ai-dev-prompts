# Test Generation

Generate unit, integration, and platform test suites.

## Prompt

```
Generate tests for [FILE_OR_MODULE] in [PROJECT_NAME].

[content-integrity constraint]

Include:
- Unit tests for each public function/method
- Edge cases (empty inputs, boundary values, invalid types)
- Integration tests for module interactions

Use [pytest/unittest] with descriptive test names following the pattern: test_[function]_[scenario]_[expected_result]

Place tests in [tests/ directory structure].
```

## Placeholders

- `[FILE_OR_MODULE]`: Target code to test
- `[PROJECT_NAME]`: Project context
- `[pytest/unittest]`: Testing framework
- `[tests/ directory structure]`: Where to place test files
- `[content-integrity constraint]`: See [content-integrity.md](content-integrity.md)

## Variations

### Unit tests
```
Generate unit tests for [FILE] covering all public functions. Mock external dependencies.
```

### Integration tests
```
Generate integration tests for [MODULE_A] and [MODULE_B] interaction. Test data flow between components.
```

### Platform tests
```
Generate tests for [MODULE] that verify behavior on real hardware across [PLATFORMS]. Include hardware-specific setup/teardown.
```

## Tips

- Provide sample input/output when testing domain-specific logic
- Specify mocking requirements for external dependencies
- Ask for parameterized tests when testing multiple similar cases

## Verification (Python)

After generating tests, always run them and fix any errors or warnings:

```bash
# Run tests with verbose output and warnings enabled
pytest tests/ -v -W default --tb=short

# Or with unittest
python -m unittest discover -v tests/
```

### Common Issues to Fix

1. **Tests assume non-existent API**: Read the actual source code to verify method signatures and return types before writing tests
2. **ResourceWarning (unclosed files)**: Ensure file handlers are closed in teardown or use context managers
3. **DeprecationWarning**: Update code to use current APIs; add `filterwarnings` in pytest.ini if third-party
4. **Flaky tests**: Avoid time-dependent assertions, use mocks for external resources
5. **Missing test fixtures**: Configure git user in temp repos, ensure proper cleanup in teardown

### pytest.ini Example

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short
filterwarnings =
    ignore::DeprecationWarning
```

Tests must pass with zero warnings before considering them complete.
