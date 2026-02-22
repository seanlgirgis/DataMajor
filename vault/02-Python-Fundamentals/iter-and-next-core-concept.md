---
type: concept
tags: [concept, python, iterators, fundamentals]
difficulty: Beginner
domain: python
created: 2026-02-21
---

# iter() and next() — Core Concept

**One-liner**: `iter()` creates an iterator from any iterable; `next()` pulls the next item one at a time.

## Mental Model
Imagine watching TV: `iter()` is when you pick up the remote control and point it at the TV. `next()` is when you physically press the "Channel Up" button to grab the next station.

## Quick Facts
- **Built-in:** No imports needed — both are standard Python built-ins.
- **Universal:** Any object usable in a `for` loop supports iter/next.
- **Exhaustion:** `StopIteration` is raised when the iterator has no more items to yield.
- **Safe:** It is strictly read-only — it does not mutate the underlying data structure.
- **Under the Hood:** Standard `for` loops are just syntactic sugar over `iter()` + `next()` — they have the exact same computational cost.

## Code Example
```python
# Grabbing the first key of a dictionary efficiently without converting the whole thing to a list first
my_dict = {"a": 1, "b": 2, "c": 3}

first_key = next(iter(my_dict))
print(first_key) # Outputs: 'a'
```

## When to Use (and When NOT To)
- **Best use cases**: Extracting the first key of a dict, consuming Generators, reading files line-by-line, and infinite `itertools` iterators.
- **When NOT to use**: Looping through entire lists, tuples, strings, or sets — just use a standard `for` loop instead for readability.

## Related Links
- [[02-Python-Fundamentals/_index|Python Fundamentals Index]]
- [[01-concepts/python/deque|Deque]]
- [[Dictionary]]
- [[01-concepts/python/graphs|Graph Traversal (BFS/DFS)]]
- [[Generators]]

## Practice
- Practice File: [[03-Code-Exercises/python-fundamentals/iter-and-next-practice.py]]
