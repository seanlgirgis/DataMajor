---
type: concept
tags: [python, algorithms, graphs, bfs, dfs]
difficulty: intermediate
language: python
created: 2026-02-21
---

# Graph Traversal (BFS & DFS)

## The 30-Second Rule
**BFS** explores level by level using a queue. **DFS** explores as deep as possible using a stack (or recursion). Both algorithms traverse maps, networks, and trees to visit every connected node exactly once.

Think of **BFS** as water flooding outward in ripples from a stone dropped in a pond — it reaches nearby nodes first. Think of **DFS** as exploring a physical maze: you keep your hand on the left wall and follow the path blindly until you hit a dead end, then you backtrack.

## Representing a Graph (Adjacency List)
```python
# The standard representation for LeetCode
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}
```

## Breadth-First Search (BFS)
Uses a **`deque`**. Explores neighbors before going deeper.
```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft() # PULL FROM FRONT
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order
```

## Depth-First Search (DFS)
Can be done iteratively (explicit stack) or recursively (call stack).
```python
# Iterative using a Stack
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop() # PULL FROM BACK
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return order
```

```python
# Recursive 
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    order = [node]

    for neighbor in graph[node]:
        if neighbor not in visited:
            order.extend(dfs_recursive(graph, neighbor, visited))
    return order
```

## BFS vs DFS — The Decision Table

| | BFS | DFS |
|-|-----|-----|
| Data structure | `Queue` (deque) | `Stack` / Recursion |
| Exploration Order | Level by level | Deep first |
| Best used for | Shortest path | Path existence, cycle detection |
| Memory usage| `O(w)` — width of graph | `O(h)` — height/depth of graph |
| LeetCode signal | *"minimum steps"*, *"nearest"* | *"all paths"*, *"islands"* |

## The "Grid/Island" Pattern (LeetCode #200)
This pattern iterating a 2D matrix, finding a `"1"`, and triggering a DFS flood-fill to capture the whole island appears constantly.
```python
def num_islands(grid):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols: return
        if grid[r][c] == "0" or (r, c) in visited: return
        
        visited.add((r, c))
        # Explore orthogonally
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1
                dfs(r, c)
                
    return islands
```

---
## Related Notes
- [[01-concepts/python/index|Python Index]]
- [[01-concepts/python/queue|Queue]]
- [[01-concepts/python/stacks|Stacks]]
- [[01-concepts/python/binary-search|Binary Search]]

## Practice
- Practice File: [[03-code/python/graph_traversal_practice.py]]
