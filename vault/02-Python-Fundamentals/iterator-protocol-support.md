---
type: concept
tags: [concept, python, iterators, fundamentals]
difficulty: Beginner
domain: python
created: 2026-02-21
---

# Iterator Protocol — Which Data Structures Support It

**One-liner**: Any Data Structure implementing the `__iter__` dunder method can use the `iter()` and `next()` protocol.

## Data Structure Support Table

| Data Structure | Iterable? | Ordered Guarantee? | Notes |
| :--- | :---: | :---: | :--- |
| **List (`[]`)** | Yes | Yes | Iterates sequentially by index. |
| **Tuple (`()`)** | Yes | Yes | Iterates sequentially by index. |
| **String (`""`)** | Yes | Yes | Iterates character by character. |
| **Set (`{}`)** | Yes | **NO** | Elements yield in a pseudo-random, non-guaranteed order based on hashes. |
| **Dict (`{k:v}`)** | Yes | Yes (Python 3.7+) | Iterates over *keys* in insertion order. |
| **Deque** | Yes | Yes | Iterates sequentially from left to right. |
| **Files** | Yes | Yes | Yields one line at a time. Extremely memory efficient. |
| **Generators** | Yes | Yes | Produces items lazily, one by one. |

> [!WARNING]
> **Key Insight:** The order you insert things into a `set` is not the order they will come out when you iterate over them. Never rely on sequence order with a set!

## Related Links
- [[02-Python-Fundamentals/_index|Python Fundamentals Index]]
- [[02-Python-Fundamentals/iter-and-next-core-concept|iter() and next() — Core Concept]]
