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
