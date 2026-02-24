# QUEUE & DEQUE — Syntax Card

## Queue — using collections.deque (recommended)
```python
from collections import deque
q = deque()
q.append(x)                   # enqueue (add right)
q.popleft()                   # dequeue (remove left) O(1)
q[0]                          # peek front
len(q) == 0                   # check empty
if not q:                     # check empty (Pythonic)
```

## DO NOT use list as queue
```python
q = []
q.append(x)                   # enqueue — O(1)
q.pop(0)                      # dequeue — O(n) !! SLOW
```

## Deque — double-ended queue
```python
from collections import deque
d = deque()
d.append(x)                   # add right
d.appendleft(x)               # add left
d.pop()                       # remove right  O(1)
d.popleft()                   # remove left   O(1)
d[0]                          # peek left
d[-1]                         # peek right
d.rotate(k)                   # rotate right k steps
d.rotate(-k)                  # rotate left  k steps
deque(iterable, maxlen=k)     # fixed-size sliding window
```

## Deque as Sliding Window (maxlen)
```python
from collections import deque
window = deque(maxlen=k)      # auto-evicts oldest when full
for x in nums:
    window.append(x)          # old element dropped automatically
    if len(window) == k:
        process(window)       # window always has last k elements
```

## Monotonic Deque (Sliding Window Maximum)
```python
from collections import deque
d = deque()                   # stores indices, decreasing values
for i, n in enumerate(nums):
    while d and nums[d[-1]] < n:
        d.pop()               # evict smaller elements from back
    d.append(i)
    if d[0] < i - k + 1:
        d.popleft()           # evict out-of-window index from front
    if i >= k - 1:
        result.append(nums[d[0]])  # front = max of current window
```

## Priority Queue (Min-Heap)
```python
import heapq
h = []
heapq.heappush(h, val)        # push
heapq.heappop(h)              # pop min
h[0]                          # peek min (no pop)
heapq.heapify(lst)            # convert list to heap in-place O(n)
heapq.nlargest(k, lst)        # k largest elements
heapq.nsmallest(k, lst)       # k smallest elements

# max-heap: negate values
heapq.heappush(h, -val)
-heapq.heappop(h)             # negate back on pop

# heap with tuple (priority, value)
heapq.heappush(h, (priority, val))
```

## queue.Queue (thread-safe, rarely needed in interviews)
```python
from queue import Queue
q = Queue()
q.put(x)                      # enqueue
q.get()                       # dequeue (blocks if empty)
q.empty()                     # check empty
q.qsize()                     # size
```
