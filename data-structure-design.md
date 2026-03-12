# Data Structure Design

Design data structures that eliminate special cases and make algorithms obvious.

## Core Philosophy

> "Bad programmers worry about the code. Good programmers worry about data structures and their relationships."  
> — Linus Torvalds

> "Show me your flowcharts and conceal your tables, and I shall continue to be mystified. Show me your tables, and I won't usually need your flowcharts; they'll be obvious."  
> — Fred Brooks

## Prompt

```
Design data structures for [PROBLEM] in [PROJECT_NAME].

[content-integrity constraint]

Principles:
- Design around how data will be accessed, not how you think the code should look
- Choose structures that eliminate special cases and edge conditions
- Prefer simple, direct access patterns over clever indirection
- Make the common case fast, the rare case correct
- Structure relationships should be clear and minimal

Questions to answer:
- What operations will be performed most frequently?
- What invariants must the structure maintain?
- Can a different layout eliminate if-statements for edge cases?
- Is there unnecessary indirection that obscures data flow?
- Will this structure be cache-friendly if performance matters?

The "good taste" test: Does this design make the algorithm obvious, or does it require special-case handling?
```

## Placeholders

- `[PROBLEM]`: The problem domain (e.g., "a symbol table", "an event queue")
- `[PROJECT_NAME]`: Project context
- `[content-integrity constraint]`: See [content-integrity.md](content-integrity.md)

## The "Good Taste" Principle

A classic example: removing an entry from a singly-linked list.

**Bad taste** (special case for head):
```c
void remove_entry(entry *entry_to_remove, list *list) {
    entry *prev = NULL;
    entry *walk = list->head;
    
    while (walk != entry_to_remove) {
        prev = walk;
        walk = walk->next;
    }
    
    // Special case: removing the head
    if (prev == NULL) {
        list->head = entry_to_remove->next;
    } else {
        prev->next = entry_to_remove->next;
    }
}
```

**Good taste** (no special case):
```c
void remove_entry(entry *entry_to_remove, list *list) {
    // Use indirect pointer to eliminate special case
    entry **indirect = &list->head;
    
    while (*indirect != entry_to_remove) {
        indirect = &(*indirect)->next;
    }
    
    *indirect = entry_to_remove->next;
}
```

The second approach **eliminates the edge case entirely** through better structure handling. This is good taste.

## Design Checklist

### 1. Access Patterns
```
How will this data be used?
- Sequential access → array or linked list
- Random access by key → hash table or tree
- Priority-based access → heap
- FIFO/LIFO access → queue/stack

Don't choose a structure based on what you know how to implement.
Choose based on how it will be used.
```

### 2. Eliminate Special Cases
```
Review your design:
- Does the algorithm need if-statements to handle the first/last element?
- Are there "empty" or "null" cases that need special handling?
- Can you use sentinel nodes, indirect pointers, or different layouts to unify cases?

Example: A doubly-linked list with a sentinel node eliminates special cases for empty lists and boundary insertions/deletions.
```

### 3. Memory Layout
```
When performance matters, consider:
- Cache locality: related data should be adjacent in memory
- Alignment: properly aligned data is faster to access
- Padding: unnecessary padding wastes cache lines
- Hot vs cold data: keep frequently-accessed fields together

Example: Struct fields accessed together should be declared together.
```

### 4. Relationships
```
How are structures related?
- One-to-one: embedded struct or single pointer
- One-to-many: array or linked list
- Many-to-many: separate junction table or bidirectional links

Keep relationships minimal and explicit.
Unnecessary indirection obscures data flow.
```

### 5. Invariants
```
What must always be true?
- List size matches actual length
- Parent/child pointers are consistent
- Reference counts are accurate
- Indices are valid

Design the structure to make invariants easy to maintain.
If an invariant is hard to maintain, the structure is wrong.
```

## Variations

### Choosing Between Structures
```
I need to store [DATA_TYPE] and support [OPERATIONS].

Common operations:
- Insert: [frequency]
- Delete: [frequency]
- Search by key: [frequency]
- Iterate all: [frequency]

Constraints:
- Memory limit: [SIZE]
- Performance requirement: [LATENCY]

Recommend a data structure and explain the tradeoffs.
```

### Refactoring Existing Structure
```
Current structure for [PROBLEM]:
[CURRENT_DESIGN]

Issues:
- [ISSUE_1]
- [ISSUE_2]

Redesign to eliminate special cases and improve access patterns.
```

### Cache-Friendly Design
```
Design a cache-friendly structure for [PROBLEM].

Consider:
- Minimize pointer chasing (bad for cache)
- Keep hot data compact
- Align to cache line boundaries when appropriate
- Use array-of-structs vs struct-of-arrays based on access pattern

Explain memory layout and why it's efficient for the common case.
```

## Anti-Patterns

### Don't Do These

**Over-abstraction:**
```c
// Bad: Unnecessary abstraction that hides the data
typedef struct { void *opaque; } handle_t;

// Good: Direct structure access when appropriate
typedef struct { int fd; char *buffer; size_t size; } file_t;
```

**Premature Optimization:**
```
Don't choose a complex structure "because it might be faster later."
Start simple. Profile. Optimize if needed.

Simple array → faster than fancy tree for small datasets.
```

**Ignoring Access Patterns:**
```
// Bad: Linked list when you need random access
// Good: Array when you iterate sequentially with occasional resizes
```

**Clever Hacks:**
```
Don't use bit-packing, pointer tagging, or other tricks unless:
1. You measured and it's a proven bottleneck
2. You documented WHY it's necessary
3. The complexity is worth the gain
```

## Examples

### Symbol Table Design

**Problem:** Store variable names, types, and scopes during compilation.

**Access patterns:**
- Lookup by name (frequent)
- Insert new symbol (frequent)
- Iterate all symbols in scope (occasional)
- Enter/exit scope (frequent)

**Design choice:** Hash table per scope, linked list of scopes.

**Why:** Hash table gives O(1) lookup by name. Linked list of scopes handles enter/exit without copying. Simple and matches usage.

### Event Queue Design

**Problem:** Store events sorted by timestamp for a simulation.

**Access patterns:**
- Insert event with timestamp (very frequent)
- Remove earliest event (very frequent)
- Cancel event by ID (rare)

**Design choice:** Min-heap by timestamp + hash table for ID lookups.

**Why:** Heap gives O(log n) insert/remove-min. Hash table enables O(1) cancellation. Rare operation doesn't dominate common case.

## Tips

- **Start simple.** Array is often enough. Don't use a tree when you have 10 items.
- **Design for the common case.** Make frequent operations fast, rare operations correct.
- **Eliminate special cases.** If your code has `if (first_element)` or `if (empty)`, reconsider the structure.
- **Draw it.** Visualize the structure and walk through operations on paper before coding.
- **Measure if it matters.** Don't guess about performance. Profile actual usage.
- **Document invariants.** Write down what must always be true. If it's hard to maintain, redesign.

## When NOT to Optimize Structure

- **Small datasets:** Simple array beats everything for <100 items
- **One-time use:** If you build it once and iterate once, structure doesn't matter
- **Code clarity:** If a simpler structure is 10% slower but 100% clearer, prefer clarity
- **No evidence:** If you haven't profiled and found a bottleneck, don't optimize

## Related Guides

- [architecture.md](architecture.md) — system-level structure
- [code-review.md](code-review.md) — reviewing implementation
- [performance.md](performance.md) — when and how to optimize
- [refactoring.md](refactoring.md) — restructuring existing code
