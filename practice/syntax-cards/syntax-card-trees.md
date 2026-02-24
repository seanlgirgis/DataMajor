# BINARY TREES — Syntax Card

## Node Definition
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right
```

## DFS — Recursive Templates
```python
# pre-order:  root → left → right
def dfs(node):
    if not node: return
    process(node.val)
    dfs(node.left)
    dfs(node.right)

# post-order: left → right → root
def dfs(node):
    if not node: return 0
    left  = dfs(node.left)
    right = dfs(node.right)
    return combine(left, right, node.val)

# in-order:   left → root → right  (gives sorted order for BST)
def dfs(node):
    if not node: return
    dfs(node.left)
    process(node.val)
    dfs(node.right)
```

## DFS — Iterative (Stack)
```python
stack = [root]
while stack:
    node = stack.pop()
    if not node: continue
    process(node.val)
    stack.append(node.right)    # right pushed first
    stack.append(node.left)     # left processed first
```

## BFS — Level Order (Queue)
```python
from collections import deque
queue = deque([root])
while queue:
    node = queue.popleft()
    if not node: continue
    process(node.val)
    queue.append(node.left)
    queue.append(node.right)
```

## BFS — Level by Level
```python
from collections import deque
queue = deque([root])
result = []
while queue:
    level = []
    for _ in range(len(queue)):     # process one level at a time
        node = queue.popleft()
        level.append(node.val)
        if node.left:  queue.append(node.left)
        if node.right: queue.append(node.right)
    result.append(level)
return result
```

## Common One-Liners
```python
# max depth
1 + max(dfs(root.left), dfs(root.right))   # post-order combine

# diameter (longest path through any node)
self.res = max(self.res, left + right)      # update global at each node

# is symmetric
mirror(left.left, right.right) and mirror(left.right, right.left)

# BST valid range
def valid(node, lo, hi):
    if not node: return True
    if not (lo < node.val < hi): return False
    return valid(node.left, lo, node.val) and valid(node.right, node.val, hi)
```

## Build from Level-Order List
```python
from collections import deque
def build(vals):
    if not vals or vals[0] is None: return None
    root  = TreeNode(vals[0])
    queue = deque([root])
    i = 1
    while queue and i < len(vals):
        node = queue.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i]); queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i]); queue.append(node.right)
        i += 1
    return root
```
