# Memory Contract

Define how an agent should use memory when the host runtime actually supports persistent or session memory.

## Purpose

This file does not create memory capability.

It defines the policy an agent should follow when the host provides memory tools or built-in persistent storage.

Use this file to keep memory behavior consistent across tasks and model families.

## What Counts As A Memory-Capable Host

A host is memory-capable when it provides all of the following:

- a place to store information outside the current prompt window
- a way to read that stored information in later turns or later sessions
- clear rules or tools for writing, updating, and deleting stored memory
- enough stability that stored user preferences are likely to be available next time

Examples of memory-capable behavior:

- explicit memory tools exposed to the agent
- a built-in saved-memory feature in the host product
- a workspace or user profile store that survives across sessions

Examples of non-memory-capable behavior:

- a long prompt with extra notes pasted into it once
- a one-session chat with no persistence layer
- a system that can summarize the current conversation but cannot retrieve it later

If the host cannot write and later retrieve durable memory, treat it as not memory-capable.

## Memory Scope Rules

Separate memory into three categories whenever the host supports it:

1. Session context
   - active task state
   - temporary plans
   - working assumptions that may change during the task
2. Durable user memory
   - stable user preferences
   - repeated workflow instructions
   - clear approval boundaries or tool constraints that should persist across tasks
3. Repository or workspace memory
   - project-specific facts, conventions, commands, and structure

Do not mix these scopes.

## What To Remember

Remember only information that is both stable and likely to improve future work.

Good candidates:

- explicit user requests to remember a preference
- repeated corrections that reveal a durable preference
- stable tool restrictions
- stable communication preferences
- recurring workflow requirements
- durable approval boundaries

## What Not To Remember

Do not store:

- secrets, credentials, tokens, keys, or personal sensitive data
- current task state that will go stale
- speculative guesses about the user
- repo-specific implementation details in durable user memory
- one-off exceptions that apply only to a single task
- unresolved assumptions or uncertain interpretations

## Write Rules

Before writing durable memory, verify all of the following:

1. the information is explicit or strongly confirmed by repeated evidence
2. it is likely to matter in a future task
3. it belongs to user memory rather than session or repository memory
4. it is short enough to stay maintainable

If any of these conditions are not met, keep the information in session context instead.

## Update And Removal Rules

- update stored memory when the user corrects or replaces it
- remove stored memory when it is contradicted, outdated, or causing friction
- prefer editing an existing memory entry over creating duplicates
- if uncertain whether a preference is still valid, ask or keep it out of durable memory

## Default Operating Rules

```text
When the host supports durable memory:

- Use memory deliberately, not automatically.
- Store only stable user preferences and durable constraints.
- Keep task state in session context, not in durable memory.
- Keep repository facts in repository-scoped memory when available.
- Do not store secrets, guesses, or one-off exceptions.
- Update or remove stored memory when the user changes direction.
```

## When The Host Is Not Memory-Capable

If the host does not provide durable memory:

- do not pretend memory exists
- keep important instructions in the current prompt or session summary
- tell the user that persistence depends on the host environment
- use context-management rules to separate current-task context from future-use preferences, even if they cannot be persisted yet