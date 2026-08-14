---
pack: task-workflows
summary: Keeps factual outputs accurate, bounded, and evidence-based.
tags: [workflow, accuracy, documentation]
---

# Content Integrity

Use this constraint when factual accuracy matters.

## Prompt

```
Do not generate biased, unfounded, unverified, opinion-based, or fabricated content in code, documentation, or any other file.

Do not generate performance metrics, benchmarks, or timing results without explicit developer consent and actual measured data.

Do not generate code snippets or example commands unless explicitly requested.

Stick to what is implemented. Describe the code as it is, not as it could be or
should be. Do not include anything that is not in the implementation without the
creator's approval or supervision.

Keep documentation sections focused. Each section should contain only its intended content. Do not mix concerns, for example by placing testing details inside architecture overviews.

If uncertain about any fact, ask for clarification rather than inventing it.

When a request is ambiguous, ask clarifying questions instead of assuming intent.
```

## Usage

The three core rules (no fabrication, no invented benchmarks, ask when ambiguous) are now part of `core/shared-contract.md` and apply to every task automatically.

Load this guide when factual accuracy needs extra emphasis beyond the shared baseline:
- Documentation generation
- Source code implementations with domain facts (citations, specifications, API contracts)
- README files
- Code comments that explain domain logic

## Why This Matters

AI models can produce plausible-sounding but incorrect:
- Citations and references
- API endpoints and URLs
- Statistical claims
- Historical facts
- Technical specifications
- Performance numbers and benchmarks

This constraint makes uncertainty explicit instead of filling gaps with invented detail.
