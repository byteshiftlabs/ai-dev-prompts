---
pack: core-rules
summary: Defines when memory is real, what should be stored, and how to separate memory scopes.
tags: [core, memory, context]
---

# Memory Contract

Define how an agent should use memory when the host really supports it.

## Purpose

This file does not create memory.

It explains how an agent should use memory when the host provides memory tools or built-in storage.

Use this file to keep memory behavior consistent across tasks and model families.

## What Counts As Memory Support

Treat a host as memory-capable only when it provides all of the following:

- a place to store information outside the current prompt window
- a way to read that stored information later
- clear rules or tools for writing, updating, and deleting stored memory
- enough stability that stored preferences are likely to be available later

Examples of hosts with memory support:

- explicit memory tools exposed to the agent
- a built-in saved-memory feature in the host product
- a workspace or user profile store that survives across sessions

Examples of hosts without memory support:

- a long prompt with extra notes pasted into it once
- a one-session chat with no persistence layer
- a system that can summarize the current conversation but cannot retrieve it later

If the host cannot save and later retrieve memory, treat it as a host without memory support.

## Memory Scopes

Separate memory into three categories whenever the host supports it:

1. Session context
   - active task state
   - temporary plans
   - working assumptions that may change during the task
2. User memory
   - stable user preferences
   - repeated workflow instructions
   - stable approval boundaries or tool constraints
3. Repository or workspace memory
   - project-specific facts, conventions, commands, and structure

Do not mix these scopes.

## What To Remember

Remember only information that is stable and likely to help in later work.

Good candidates:

- explicit user requests to remember a preference
- repeated corrections that reveal a stable preference
- stable tool restrictions
- stable communication preferences
- recurring workflow requirements
- clear approval boundaries

## What Not To Remember

Do not store:

- secrets, credentials, tokens, keys, or personal sensitive data
- current task state that will go stale
- speculative guesses about the user
- repo-specific implementation details in user memory
- one-off exceptions that apply only to a single task
- unresolved assumptions or uncertain interpretations

## Before Writing Memory

Before writing user memory, verify all of the following:

1. the information is explicit or strongly confirmed by repeated evidence
2. it is likely to matter in a future task
3. it belongs to user memory rather than session or repository memory
4. it is short enough to stay maintainable

If any of these conditions are not met, keep the information in session context instead.

## First-Use Initialization

On first use in a host with memory support, set up memory behavior before substantial task execution.

Minimum first-use procedure:

1. inspect what memory scopes the host provides
2. review any existing user memory before adding new entries
3. decide what belongs in session memory, user memory, or repository memory
4. avoid writing new user memory until that decision is clear
5. if the user or repository already defines memory rules, apply those rules first

This step is about setting up memory correctly, not filling it quickly.

Good first-use outcomes:

- the agent knows where stable preferences belong
- the agent avoids duplicating or scattering memory entries
- the agent can explain whether memory is actually available in the host

Bad first-use behavior:

- writing guesses into user memory immediately
- treating session summaries as user memory
- storing repository facts in user memory
- ignoring existing memory and creating duplicate entries

## Updating And Removing Memory

- update stored memory when the user corrects or replaces it
- remove stored memory when it is contradicted, outdated, or causing friction
- prefer editing an existing memory entry over creating duplicates
- if uncertain whether a preference is still valid, ask or keep it out of user memory

## Default Operating Rules

```text
When the host supports memory:

- Use memory deliberately, not automatically.
- Store only stable user preferences and stable constraints.
- Keep task state in session context, not in user memory.
- Keep repository facts in repository-scoped memory when available.
- Do not store secrets, guesses, or one-off exceptions.
- Update or remove stored memory when the user changes direction.
```

## When The Host Does Not Support Memory

If the host does not provide memory support:

- do not pretend memory exists
- keep important instructions in the current prompt or session summary
- tell the user that persistence depends on the host environment
- use context-management rules to separate current-task context from future-use preferences, even if they cannot be persisted yet