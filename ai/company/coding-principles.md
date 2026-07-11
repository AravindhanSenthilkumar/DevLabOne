# Coding Principles

## Core Rules
- Write clear code first, clever code last.
- Keep functions small and focused.
- Name things by business meaning, not implementation detail.
- Validate inputs at system boundaries.
- Fail safely with useful errors.
- Keep duplicated logic low, but do not abstract too early.

## AI-Assisted Coding
- Ask the agent to explain assumptions before large changes.
- Review generated code like code written by a junior developer.
- Never accept AI output that changes security, data, or money flows without human review.
- Prefer small patches that are easy to inspect.

## Maintainability
- Use consistent project structure.
- Keep dependencies necessary and current.
- Add comments only for non-obvious decisions.
- Remove dead code when replacing behavior.
- Write tests for important business rules.
