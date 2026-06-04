# API Design

Design stable, user-facing interfaces that minimize breaking changes.

## Core Principle

Once you ship an API, it's a **contract with your users**. Breaking that contract without overwhelming justification is unacceptable. Design carefully from the start—fixing a bad API later is painful for everyone.

## Prompt

```
Design a public API for [FUNCTIONALITY] in [PROJECT_NAME].

[content-integrity constraint]

Requirements:
- Define the minimal interface that solves the problem
- Design for extensibility without breaking existing code
- Follow the principle of least surprise
- Document behavior, edge cases, and error conditions
- Consider versioning strategy from the start

Questions to answer:
- What operations must users perform?
- What flexibility do users need?
- What can change in the future without breaking existing code?
- What invariants and contracts must the API maintain?
- How will errors be handled and communicated?

Guiding principle: "Make the simple case simple and the complex case possible."
```

## Placeholders

- `[FUNCTIONALITY]`: What the API enables (e.g., "file I/O", "network requests")
- `[PROJECT_NAME]`: Project context
- `[content-integrity constraint]`: See [content-integrity.md](content-integrity.md)

## API Design Principles

### 1. Backward Compatibility is Sacred

**Never break existing code without overwhelming justification.**

```
Acceptable changes:
- Adding new functions/methods (with defaults for existing callers)
- Adding new optional parameters (with sensible defaults)
- Adding new error codes (if existing code handles unknown errors gracefully)
- Making constraints looser (e.g., accepting more input formats)
- Improving performance or fixing bugs (if behavior remains correct)

Unacceptable changes:
- Removing functions/methods/parameters
- Changing function signatures
- Changing return types
- Changing error conditions users rely on
- Making constraints stricter (e.g., rejecting previously valid input)
- Changing side effects or observable behavior
```

**If you MUST break compatibility:**
- Major version bump (semantic versioning: v1 → v2)
- Provide migration guide and deprecation period
- Justify why maintaining compatibility is impossible
- Consider keeping old API as wrapper around new implementation

### 2. Minimal Interface

**Expose only what users need. Everything exposed is a maintenance burden.**

```
Good: Small, focused API
- Easy to learn
- Easy to maintain
- Easy to optimize internals without breaking users

Bad: Kitchen-sink API
- Exposes implementation details
- Locks you into specific design choices
- Users depend on things you never intended
```

**Guideline:** If you're not sure whether to expose something, **don't**. It's easier to add later than remove.

### 3. Principle of Least Surprise

**Functions should do what their names suggest, nothing more.**

```
Good names:
- read_file(path) → reads and returns file contents
- calculate_sum(numbers) → returns sum, doesn't modify input
- sort_array(arr) → sorts in-place if name doesn't say otherwise

Surprising behavior (avoid):
- read_file(path) → also caches the file globally
- calculate_sum(numbers) → modifies input array
- validate_input(data) → also sends analytics
```

**Guideline:** If the function name doesn't capture what it does, either rename it or split it into multiple functions.

### 4. Fail Fast and Clearly

**Invalid input should cause immediate, unambiguous errors.**

```
Good error handling:
- Check inputs at API boundary
- Return/throw specific errors with helpful messages
- Document what errors can occur and why

Bad error handling:
- Silently accept invalid input and fail later
- Generic "something went wrong" errors
- Errors that don't indicate how to fix the problem
```

**Guideline:** Users should never have to guess why something failed.

### 5. Consistency

**Similar operations should work similarly.**

```
If you have:
- create_user(name, email)
- create_post(title, body)

Don't suddenly introduce:
- make_new_comment(author_id, comment_body, post_id)
  ^^^^^^^^^ Inconsistent naming and parameter order

Keep it consistent:
- create_comment(post_id, author_id, body)
```

**Guideline:** Similar names → similar behavior. Use the same patterns throughout your API.

## API Design Checklist

### Before You Ship

```
☐ Can users accomplish common tasks easily?
☐ Are function names clear and descriptive?
☐ Is parameter order logical and consistent across similar functions?
☐ Are return types predictable?
☐ Are errors specific and actionable?
☐ Is behavior documented (not just signature)?
☐ Are edge cases handled and documented?
☐ Are defaults sensible?
☐ Can the API evolve without breaking existing code?
☐ Is there a versioning plan?
```

## Versioning Strategy

### Semantic Versioning (Recommended)

```
Version format: MAJOR.MINOR.PATCH (e.g., 2.4.1)

- MAJOR: Breaking changes (increment when you break backward compatibility)
- MINOR: New features (backward-compatible additions)
- PATCH: Bug fixes (backward-compatible fixes)

Examples:
- 1.0.0 → 1.1.0: Added new function (non-breaking)
- 1.1.0 → 1.1.1: Fixed bug in existing function (non-breaking)
- 1.1.1 → 2.0.0: Changed function signature (BREAKING)
```

### Pre-1.0 Development

```
- 0.x.y versions = unstable, API may change
- Users know to expect breaking changes
- Once stable, ship 1.0.0 and commit to compatibility
```

### Deprecation Process

```
1. Mark function as deprecated in version N.x
2. Keep it working, emit deprecation warnings
3. Document replacement in deprecation message
4. Remove in version (N+1).0

Give users at least one major version to migrate.
```

## Variations

### Designing a New API
```
Design a public API for [FUNCTIONALITY] in [PROJECT_NAME].

Core operations users need:
- [OPERATION_1]
- [OPERATION_2]
- [OPERATION_3]

Constraints:
- [CONSTRAINT_1]
- [CONSTRAINT_2]

Provide:
- Function signatures with clear names
- Parameter types and purposes
- Return values and error conditions
- Usage examples for common cases
```

### Reviewing an Existing API
```
Review the following API for [PROJECT_NAME]:

[API_DEFINITION]

Check for:
- Is the interface minimal? Can anything be removed or simplified?
- Is naming consistent and clear?
- Are there hidden side effects or surprising behaviors?
- Can users accomplish common tasks easily?
- Are errors specific and helpful?
- Can this evolve without breaking existing code?
- What would a breaking change look like? How could we avoid it?
```

### Evolving an API Without Breaking Changes
```
Current API: [CURRENT_API]
Desired new functionality: [NEW_FEATURE]

Add the new functionality without breaking existing code.
Options:
- Add new optional parameters with defaults
- Add new functions/methods (don't modify existing)
- Add overloads or variants
- Extend return types (if language allows graceful handling)

Show before/after and verify existing code still works.
```

## Examples

### Good API Design: POSIX open()

```c
int open(const char *path, int flags, mode_t mode);
```

**Why it's good:**
- Clear name: "open" does what it says
- Simple common case: `open("file.txt", O_RDONLY)`
- Flexible: flags allow extensions (O_CREAT, O_APPEND, etc.)
- Consistent with rest of POSIX (read, write, close)
- Backward compatible: new flags added over decades without breaking code
- Clear error handling: returns -1 on error, sets errno

### Bad API Design: Changing Return Type

```python
# Version 1.0
def get_user(id):
    """Returns User object or None if not found."""
    return user_or_none

# Version 1.5 (BREAKS COMPATIBILITY!)
def get_user(id):
    """Returns list of User objects matching query."""
    return [user]  # Now returns list!
```

**Why it's bad:**
- Existing code expecting User/None will break
- `if user:` now checks if list is non-empty (different meaning!)
- Type changed without major version bump

**Better approach:**
```python
# Version 1.0
def get_user(id):
    """Returns User or None."""
    return user_or_none

# Version 1.5 (non-breaking)
def find_users(query):
    """Returns list of Users matching query."""
    return users  # New function, doesn't break old code
```

### Extensible API Design: Configuration Objects

```c
// Version 1.0
typedef struct {
    int timeout_ms;
    bool retry_on_failure;
} http_config;

http_client* http_create(const http_config *config);

// Version 2.0 (backward compatible!)
typedef struct {
    int timeout_ms;
    bool retry_on_failure;
    
    // New fields (existing code leaves these uninitialized or zero)
    int max_redirects;
    bool verify_ssl;
} http_config;

// Existing code still works:
// http_config cfg = { .timeout_ms = 1000, .retry_on_failure = true };
// New fields default to 0/false, which is sensible
```

**Why it's good:**
- Existing code compiles without changes
- New fields have safe defaults (zero-initialized in C)
- Clear migration path for users who want new features

## Common Mistakes

### 1. Exposing Implementation Details

```python
# Bad: Exposes internal cache
class Database:
    def get_cache(self):
        return self._cache  # Now users depend on cache existing!

# Good: Hide implementation
class Database:
    def get_user(self, id):
        return self._fetch(id)  # Cache is internal detail
```

### 2. Boolean Parameters

```python
# Bad: What does True mean?
send_email(user, True, False)

# Good: Use enums or named parameters
send_email(user, include_attachments=True, mark_as_important=False)
```

### 3. Silent Failures

```python
# Bad: Silently returns None on error
def parse_config(path):
    try:
        return load(path)
    except:
        return None  # User can't tell error from missing key!

# Good: Let errors propagate or return Result type
def parse_config(path):
    return load(path)  # Raises FileNotFoundError if missing
```

## Language-Specific Considerations

### C
- Use opaque pointers for encapsulation: `typedef struct client client_t;`
- Explicit context parameters: `client_send(client_t *ctx, ...)`
- Return error codes, don't use exceptions

### Python
- Use keyword arguments for clarity and extensibility
- Type hints for documentation and tooling
- Raise specific exceptions, not generic Exception

### REST APIs
- Use HTTP verbs correctly (GET, POST, PUT, DELETE)
- Version in URL (`/api/v1/users`) or header
- Return appropriate status codes (200, 404, 500)

## Tips

- **Design for your first 3 users, not your next 1000.** Solve real problems, not hypothetical ones.
- **Write usage examples first.** If the API is awkward to use in examples, redesign before implementing.
- **Seek feedback early.** Show the API design to users before implementing.
- **Document behavior, not just signatures.** Users need to know what your function **does**, not just what it takes.
- **Stability over cleverness.** A boring, stable API is better than a clever, unstable one.

## Related Guides

- [architecture.md](architecture.md) — system-level organization
- [documentation.md](documentation.md) — documenting APIs
- [git-workflow.md](git-workflow.md) — versioning and releases
- [data-structure-design.md](data-structure-design.md) — internal structure design
