---
type: concept
tags: [python, data-structures, linked-list]
difficulty: intermediate
language: python
created: 2026-02-20
---

# Linked List

## The 30-Second Rule
A **linked list** is a chain of nodes where each node holds a value and a pointer to the next node — there's no indexing, you navigate by following pointers.

Think of an elaborate treasure hunt where each clue tells you where the next clue is hidden. You can't jump directly to clue #5 — you absolutely have to follow the chain from the very start.

## The Node — The Fundamental Building Block
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```
*This is the exact class LeetCode gives you in almost every linked list problem. Memorize it.*

**Building a chain manually:**
```python
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

a.next = b
b.next = c
# Chain: 1 -> 2 -> 3 -> None
```

## Traversal — The Core Pattern
```python
def traverse(head):
    current = head
    while current:
        print(current.val)
        current = current.next
```
`while current:` — this is the linked list loop. It naturally stops when `current` becomes `None` (the end of the chain).

## Time Complexity Comparison

| Operation | `array` | `Linked List` |
|-----------|-------|-------------|
| Access by index | `O(1)` | `O(n)` |
| Insert at front | `O(n)` | **`O(1)`** |
| Insert at back | `O(1)` | `O(n)`* |
| Delete at front | `O(n)` | **`O(1)`** |
| Search | `O(n)` | `O(n)` |

*\*O(1) if you explicitly track a tail pointer.*

## The Two-Pointer Pattern (LeetCode's Favorite)

### 1. Find the Middle
Slow moves one step, fast moves two. When fast hits the end, slow is at the middle.
```python
def find_middle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow  # slow is exactly at the middle
```

### 2. Detect a Cycle (Floyd's Tortoise and Hare)
If there's a loop, the fast pointer will eventually lap the slow pointer, and they will meet.
```python
def has_cycle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

## Reversing a Linked List — The Classic Interview Question
Draw this out step-by-step with `1 -> 2 -> 3`. Walking through it manually makes the pointer logic click perfectly.
```python
def reverse_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next   # save next
        current.next = prev        # reverse the pointer
        prev = current             # move prev forward
        current = next_node        # move current forward
    
    return prev  # prev is now the new head!
```

---
## Related Notes
- [[01-concepts/python/index|Python Index]]
- [[01-concepts/python/stacks|Stacks]]
- [[01-concepts/python/deque|Deque]]

## Practice
- Practice File: [[03-code/python/linked_list_practice.py]]
