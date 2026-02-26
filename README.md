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
| [incremental-development.md](incremental-development.md) | Build in small, verified steps |
| [reproducibility.md](reproducibility.md) | Ensure reproducible results |
| [scope-control.md](scope-control.md) | Stay focused, avoid scope creep |
| [chain-of-thought.md](chain-of-thought.md) | Step-by-step reasoning |
| [context-management.md](context-management.md) | Control session context |
| [task-decomposition.md](task-decomposition.md) | Break complex tasks into steps |
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
| Complex problem solving | `chain-of-thought.md` |
| Break down large task | `task-decomposition.md` |
| Build feature step-by-step | `incremental-development.md` |
| Ensure reproducibility | `reproducibility.md` |
| Keep focus | `scope-control.md` |
| Manage session context | `context-management.md` |

### Example Workflow

```
1. Start session with content-integrity.md as context
2. "I need to add feature X" → load task-decomposition.md, break it down
3. "Let's start" → load incremental-development.md, build step by step
4. "Review this code" → load code-review.md
5. "Fix the issues" → (already have context)
6. "Write tests" → load test-generation.md
7. "Commit changes" → load git-workflow.md
8. "Create PR" → (git-workflow.md still active)
```
