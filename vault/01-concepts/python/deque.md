---
type: concept
tags: [python, data-structures, deque, collections]
difficulty: beginner-intermediate
language: python
created: 2026-02-20
---
# Deque

## The 30-Second Rule
A **deque** (Double-Ended Queue, pronounced "deck") is a list-like data structure that allows fast `O(1)` append and pop operations from *both* ends (left and right). 

By contrast, a standard Python list takes `O(n)` time to insert or pop from the left, because it must shift every other element over. Deques eliminate this performance bottleneck, making them essential for Queue-based algorithms like Breadth-First Search (BFS) and Sliding Windows.

## The Core Problem With Lists
```python
nums = [1, 2, 3, 4, 5]
nums.pop(0)       # O(n) — Python must shift every remaining element left
nums.insert(0, 0) # O(n) — same problem
```

## Creating & Importing
To use a deque, import it from the built-in `collections` module.
```python
from collections import deque

d = deque()              # empty deque
d = deque([1, 2, 3])     # initialize with an iterable
```

## Time Complexity Comparison

| Operation | `list` | `deque` |
|-----------|------|-------|
| Append Right | `O(1)` | `O(1)` |
| Pop Right | `O(1)` | `O(1)` |
| Append Left | `O(n)` | **`O(1)`** |
| Pop Left | `O(n)` | **`O(1)`** |
| Random Access `d[i]` | `O(1)` | `O(n)` |

> [!WARNING]
> **The tradeoff**: You give up fast random access. Deques are implemented as doubly-linked lists under the hood in Python. They are fantastic for pushing and pulling from the ends, but terrible for accessing middle elements like `d[50]`.

## Core Operations

```python
from collections import deque
d = deque([2, 3])

# Right side operations (Same as Lists)
d.append(4)       # deque([2, 3, 4])
d.pop()           # returns 4, deque([2, 3])

# Left side operations (The Deque Superpower)
d.appendleft(1)   # deque([1, 2, 3])
d.popleft()       # returns 1, deque([2, 3])
```

## `maxlen` — The Sliding Window Shortcut
You can bound a deque to a maximum length. When it hits this length, appending a new item automatically evicts the oldest item on the opposite end.
```python
d = deque(maxlen=3)
d.append(1)   # deque([1])
d.append(2)   # deque([1, 2])
d.append(3)   # deque([1, 2, 3])
d.append(4)   # deque([2, 3, 4])  ← '1' was evicted automatically!
```

## LeetCode Patterns
1. **Breadth-First Search (BFS):** Always use a deque for the queue. You will repeatedly run `queue.popleft()` to process nodes level by level.
2. **Sliding Window Minimum/Maximum:** Store indices in a deque, popping from the right to maintain monotonicity, and popping from the left when the index falls out of the window boundary.
3. **Implementing a FIFO Queue:** Simply use `.append()` to enqueue, and `.popleft()` to dequeue.

---
## Related Notes
- [[01-concepts/python/lists|Python Lists]]
- [[01-concepts/python/sets|Sets]]
- [[01-concepts/python/graphs|Graph Traversal (BFS/DFS)]]

## Practice
- Practice File: [[03-code/python/deque_practice.py]]
