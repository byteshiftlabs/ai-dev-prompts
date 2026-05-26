# AI Development Prompts

Reusable prompt patterns for AI-assisted software development at byteshiftlabs.

## Prompts

| File | Purpose |
|------|---------|
| [ml-project-bootstrap.md](ml-project-bootstrap.md) | Initialize new ML/research projects |
| [code-review.md](code-review.md) | Code quality audits and refactoring |
| [refactoring.md](refactoring.md) | Structural code improvements |
| [test-generation.md](test-generation.md) | Generate comprehensive test suites |
| [debugging.md](debugging.md) | Diagnose and fix issues |
| [git-workflow.md](git-workflow.md) | Commits, branches, and PRs |
| [documentation.md](documentation.md) | Generate thorough code documentation |
| [error-handling.md](error-handling.md) | Exception patterns and logging |
| [content-integrity.md](content-integrity.md) | Constraint to prevent fabricated content |

## Usage

### Basic Usage

Copy the relevant prompt and adapt placeholders (marked with `[brackets]`) to your specific project.

### Efficient Loading

Don't load all prompts at once. Use selective loading based on the task:

**Always active (system prompt or conversation start):**
- `content-integrity.md` — base constraint for all interactions

**Load per task:**
| Task | Prompt to load |
|------|----------------|
| Review code quality | `code-review.md` |
| Write tests | `test-generation.md` |
| Fix a bug | `debugging.md` |
| Restructure code | `refactoring.md` |
| Commit/PR | `git-workflow.md` |
| Write docs | `documentation.md` |
| Design error handling | `error-handling.md` |
| Start new ML project | `ml-project-bootstrap.md` |

### Example Workflow

```
1. Start session with content-integrity.md as context
2. "Review this code" → load code-review.md
3. "Fix the issues" → (already have context)
4. "Commit changes" → load git-workflow.md
5. "Create PR" → (git-workflow.md still active)
```
