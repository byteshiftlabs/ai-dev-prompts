# Error Handling

Design patterns for consistent error handling across projects.

## Prompt

```
Implement error handling for [FILE_OR_MODULE] in [PROJECT_NAME].

[content-integrity constraint]

Include:
- Custom exception classes for domain-specific errors
- Appropriate exception hierarchy (inherit from base exceptions)
- Descriptive error messages that help diagnose the issue
- Logging at appropriate levels (debug, info, warning, error)
- Graceful degradation where possible
- User-friendly messages (separate from technical logs)

Follow the project's existing error handling patterns if present.
```

## Placeholders

- `[FILE_OR_MODULE]`: Target code
- `[PROJECT_NAME]`: Project context
- `[content-integrity constraint]`: See [content-integrity.md](content-integrity.md)

## Variations

### Exception hierarchy
```
Design an exception hierarchy for [PROJECT_NAME].
Create a base exception class and specific exceptions for:
- Input validation errors
- External service failures
- Resource not found
- Permission/authorization errors
- Configuration errors
```

### Logging setup
```
Set up logging for [PROJECT_NAME]:
- Configure log levels (DEBUG, INFO, WARNING, ERROR)
- Format: timestamp, level, module, message
- File and console output
- Rotation policy for log files
```

### User-facing errors
```
Convert technical errors in [MODULE] to user-friendly messages.
Map exception types to clear, actionable messages without exposing internals.
```

## Tips

- Catch specific exceptions, not bare `except:`
- Log before re-raising if adding context: when you catch an exception to add information but need to propagate it, log the enriched context at that point since higher-level handlers may not have access to that local state
- Include relevant state in error messages (IDs, values that caused failure)
- Fail fast for unrecoverable errors, retry for transient failures
