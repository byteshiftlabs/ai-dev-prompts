# Content Integrity

Constraint to prevent AI-generated fabrications.

## Prompt

```
Don't generate any biased, unfounded, unverified, opinion-based and unnecessarily-fabricated content neither in the source code nor in the docs nor in any other file.

Do not generate performance metrics, benchmarks, or timing results without explicit developer consent and actual measured data.

Do not generate code snippet examples or example commands unless explicitly requested.

Keep documentation sections focused: each section contains only its intended content. Do not mix concerns (e.g., testing details belong in testing sections, not in architecture overviews).

If uncertain about any fact, ask for clarification rather than inventing.
```

## Usage

Append this constraint to any prompt where factual accuracy matters:
- Documentation generation
- Source code implementations
- README files
- Code comments explaining domain logic

## Why This Matters

AI models can hallucinate plausible-sounding but incorrect:
- Citations and references
- API endpoints and URLs
- Statistical claims
- Historical facts
- Technical specifications
- Performance numbers and benchmarks

This constraint forces explicit acknowledgment of uncertainty.
