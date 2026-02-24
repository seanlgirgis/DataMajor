# LINKED LIST (Singly) — Syntax Card

## Node Definition
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next
```

## Build a List
```python
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)    # 1 → 2 → 3 → None

# from array
def build(arr):
    dummy = ListNode(0)
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next
```

## Traverse
```python
cur = head
while cur:
    print(cur.val)
    cur = cur.next
```

## Insert
```python
# at head
node.next = head
head = node

# after a node
node.next = prev.next
prev.next = node
```

## Delete
```python
# delete next node
prev.next = prev.next.next

# delete by value (with dummy head)
dummy = ListNode(0, head)
cur = dummy
while cur.next:
    if cur.next.val == target:
        cur.next = cur.next.next
    else:
        cur = cur.next
return dummy.next
```

## Reverse (Iterative — Three Pointers)
```python
prev, cur = None, head
while cur:
    nxt      = cur.next
    cur.next = prev
    prev     = cur
    cur      = nxt
return prev                     # new head
```

## Find Middle (Slow / Fast)
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
return slow                     # middle node
```

## Detect Cycle (Floyd's)
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True
return False
```
