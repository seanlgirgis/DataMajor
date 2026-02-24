# GRAPH BFS / DFS — Syntax Card

## Build Adjacency List
```python
# undirected
graph = {}
for u, v in edges:
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

# directed
from collections import defaultdict
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
```

## BFS — Shortest Path / Level Order
```python
from collections import deque
def bfs(graph, start):
    visited = {start}
    queue   = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

## BFS — With Distance Tracking
```python
queue   = deque([(start, 0)])   # (node, distance)
visited = {start}
while queue:
    node, dist = queue.popleft()
    for nb in graph[node]:
        if nb not in visited:
            visited.add(nb)
            queue.append((nb, dist + 1))
```

## DFS — Recursive
```python
def dfs(node, visited, graph):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited, graph)
```

## DFS — Iterative (Stack)
```python
def dfs(graph, start):
    visited = set()
    stack   = [start]
    while stack:
        node = stack.pop()
        if node in visited: continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
```

## Count Connected Components
```python
visited = set()
count   = 0
for node in graph:
    if node not in visited:
        dfs(node, visited, graph)   # marks whole component
        count += 1
return count
```

## Detect Cycle (Directed — DFS with rec_stack)
```python
def has_cycle(graph, node, visited, rec_stack):
    visited.add(node); rec_stack.add(node)
    for nb in graph[node]:
        if nb not in visited:
            if has_cycle(graph, nb, visited, rec_stack): return True
        elif nb in rec_stack:
            return True             # back edge = cycle
    rec_stack.remove(node)
    return False
```

## Topological Sort (BFS — Kahn's Algorithm)
```python
from collections import deque, defaultdict
in_degree = defaultdict(int)
for u in graph:
    for v in graph[u]: in_degree[v] += 1
queue = deque([n for n in graph if in_degree[n] == 0])
order = []
while queue:
    node = queue.popleft(); order.append(node)
    for nb in graph[node]:
        in_degree[nb] -= 1
        if in_degree[nb] == 0: queue.append(nb)
return order if len(order) == len(graph) else []  # [] = cycle
```
