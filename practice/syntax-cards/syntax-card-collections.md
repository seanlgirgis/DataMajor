# PYTHON COLLECTIONS — Syntax Card
# defaultdict, Counter, deque — interview essentials

## defaultdict
```python
from collections import defaultdict

d = defaultdict(list)    # missing key -> []
d = defaultdict(int)     # missing key -> 0
d = defaultdict(set)     # missing key -> set()

d["key"].append(1)       # no KeyError — list auto-created
d["count"] += 1          # no KeyError — int auto-created

# WARNING: d.get("key", []).append(x) does NOT store in d
# CORRECT: d["key"].append(x)
```

## Counter
```python
from collections import Counter

c = Counter("aabbbc")        # {'b':3,'a':2,'c':1}
c = Counter([1,1,2,3])       # {1:2, 2:1, 3:1}

c["x"]                       # 0 — no KeyError for missing
c.most_common(2)             # [('b',3),('a',2)]
c.most_common()[-1]          # least common

# Arithmetic
c1 + c2   # combine counts
c1 - c2   # subtract (drops zeros/negatives)
c1 & c2   # min of each count
c1 | c2   # max of each count

# Frequency map pattern
freq = Counter(s)
for ch, count in freq.items():
    ...
```

## deque
```python
from collections import deque

dq = deque([1, 2, 3])
dq.append(4)        # add right   O(1)
dq.appendleft(0)    # add left    O(1)
dq.pop()            # remove right O(1)
dq.popleft()        # remove left  O(1)  <-- use this, NOT list.pop(0)

# BFS queue pattern
queue = deque([root])
while queue:
    node = queue.popleft()
    if node.left:  queue.append(node.left)
    if node.right: queue.append(node.right)

# Level-order BFS — snapshot size
for _ in range(len(queue)):   # process one level at a time
    node = queue.popleft()
```

## OrderedDict (LRU Cache pattern)
```python
from collections import OrderedDict

od = OrderedDict()
od.move_to_end("key")        # move to most-recently-used end
od.move_to_end("key", last=False)  # move to front
od.popitem(last=False)       # remove least-recently-used (front)
```

## Quick picks
```python
# Need auto-default value?          -> defaultdict
# Need frequency count fast?        -> Counter
# Need O(1) both-end queue?         -> deque
# Need insertion-order + eviction?  -> OrderedDict
```
