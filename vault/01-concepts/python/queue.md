---
type: concept
tags: [python, data-structures, queue, collections]
difficulty: beginner-intermediate
language: python
created: 2026-02-21
---

# Queue

## The 30-Second Rule
A **Queue** is a FIFO (First In, First Out) structure — the first item added is the first item removed. Think of a line at a grocery store or an amusement park ride. 

It is the opposite of a Stack (which is Last-In, First-Out, like a stack of plates).

## Three Implementations in Python

### 1. `deque` (The Right Way)
Always use double-ended queues for algorithmic queues to guarantee `O(1)` performance.
```python
from collections import deque
queue = deque()
queue.append("a")      # enqueue
queue.popleft()        # dequeue → returns 'a'  (FIFO)
```

### 2. `list` (The Wrong Way)
Lists look like queues, but removing from the front forces the entire array to physically shift left in memory.
```python
queue = []
queue.append("a")      # enqueue — O(1)
queue.pop(0)           # dequeue — O(n) ← Highly inefficient!
```

### 3. `queue.Queue` (For Threading)
This is strictly for multi-threaded production applications. It adds heavy thread-locking overhead. Never use this for LeetCode.
```python
from queue import Queue
q = Queue()
q.put("a")             # enqueue
q.get()                # dequeue
```

## Complexity (Using `deque`)
| Operation | Time Complexity |
|-----------|-------------|
| Enqueue (append) | `O(1)` |
| Dequeue (popleft) | `O(1)` |
| Peek front (`q[0]`) | `O(1)` |
| Search | `O(n)` |

## Stack vs Queue: Mental Anchor
| | Stack | Queue |
|-|-------|-------|
| **Order** | LIFO | FIFO |
| **Add** | push (`append`) | enqueue (`append`) |
| **Remove** | pop (`pop`) | dequeue (`popleft`) |
| **Used for** | DFS, Undo arrays, Backtracking | BFS, Task scheduling, Data buffers |

## LeetCode Patterns
The #1 use case for a Queue is **Breadth-First Search (BFS)** (including Level-Order Tree Traversals).

```python
# Standard Adjacency List BFS
def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    order = []

    while queue:
        node = queue.popleft() # PULL from the front
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor) # PUSH to the back
    return order
```

---
## Related Notes
- [[01-concepts/python/index|Python Index]]
- [[01-concepts/python/stacks|Stacks]]
- [[01-concepts/python/deque|Deque]]

## Practice
- Practice File: [[03-code/python/queue_practice.py]]
