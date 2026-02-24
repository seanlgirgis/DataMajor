# DOUBLY LINKED LIST — Syntax Card

## Node Definition
```python
class DLNode:
    def __init__(self, val=0):
        self.val  = val
        self.prev = None
        self.next = None
```

## Sentinel (Dummy Head + Tail) Pattern
```python
# eliminates all edge cases for insert/delete
head = DLNode(0)              # dummy head
tail = DLNode(0)              # dummy tail
head.next = tail
tail.prev = head
```

## Insert (after a given node)
```python
def insert_after(node, new_node):
    new_node.prev = node
    new_node.next = node.next
    node.next.prev = new_node  # update successor's prev
    node.next      = new_node  # update node's next
```

## Delete (a given node)
```python
def delete(node):
    node.prev.next = node.next  # bypass node forward
    node.next.prev = node.prev  # bypass node backward
    # node is now garbage collected
```

## Traverse
```python
cur = head.next               # forward (skip dummy head)
while cur != tail:
    print(cur.val)
    cur = cur.next

cur = tail.prev               # backward (skip dummy tail)
while cur != head:
    print(cur.val)
    cur = cur.prev
```

## LRU Cache Pattern (OrderedDict shortcut)
```python
from collections import OrderedDict
cache = OrderedDict()
cache[key] = val              # insert
cache.move_to_end(key)        # mark as recently used
cache.move_to_end(key, last=False)  # move to front
cache.popitem(last=False)     # evict least recently used (front)
cache.popitem(last=True)      # evict most recently used (back)
```

## Python deque (doubly linked list built-in)
```python
from collections import deque
d = deque()
d.append(x)                   # add right
d.appendleft(x)               # add left
d.pop()                       # remove right
d.popleft()                   # remove left  O(1)
d[0]                          # peek left
d[-1]                         # peek right
```
