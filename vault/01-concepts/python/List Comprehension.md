---
type: concept
tags: [concept, python, lists]
difficulty: Beginner
domain: python
created: 2026-02-18
---

# List Comprehension

**One-liner**: A concise syntax for creating lists from iterables using an expression and optional filtering.

## Mental Model
Think of a list comprehension as a compact `for` loop that builds a new list by applying an expression to each item.

## Quick Facts
- Syntax: `[expr for item in iterable if condition]`
- More readable and often faster than equivalent `for`-loop append patterns for simple transformations.
- Supports nested comprehensions for multi-dimensional data.

## Code Example
```python
# Basic example
nums = [1, 2, 3, 4]
squares = [n*n for n in nums]
# With condition
evens = [n for n in nums if n % 2 == 0]
```

## Related Links
- [[01-concepts/python/_index|Python Index]]
- [[Python Lists]]

## Deep Dive
List comprehensions are syntactic sugar over loops; for complex logic prefer `for` loops or generator functions to keep readability.

## Practice
- (Add a practice file via the `scaffold-code-exercise` skill)
