# Error Handling

Use consistent error handling patterns across projects.

## Prompt

```
Implement error handling for [FILE_OR_MODULE] in [PROJECT_NAME].

[content-integrity constraint]

Include:
- Custom exception classes for domain-specific errors
- An appropriate exception hierarchy
- Descriptive error messages that help diagnose the issue
- Logging at appropriate levels (debug, info, warning, error)
- Graceful degradation where possible
- User-friendly messages that are separate from technical logs

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
- Permission or authorization errors
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

- Catch specific exceptions instead of using a bare `except:`
- If you catch an exception only to add context and then re-raise it, log that added context there because higher layers may not have access to the same local state
- Include relevant state in error messages, such as IDs or values that caused the failure
- Fail fast for unrecoverable errors and retry only for genuinely transient failures
