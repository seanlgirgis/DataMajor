# Techniques
# Sliding Window

## Using two pointers to process a contiguous subsegment of a list or string

```python
def sliding_window(data):
    left = 0
    n = len(data)
    current_sum = 0
    
    for right in range(n):
        # Expand the window
        current_sum += data[right]
        
        # Shrink the window based on a condition
        while left <= right and current_sum > target:
            current_sum -= data[left]
            left += 1

```


## Sliding window using a single while loop with manual pointer increments and exit condition

```python
left = 0
right = 0
n = len(data)

while right < n:
    # Process current element at right
    current_sum += data[right]
    
    # Shrink window from the left
    while left <= right and current_sum > target:
        current_sum -= data[left]
        left += 1
        
    # Expand window to the right
    right += 1

```

# Data Structs


# Python Set Operations

## Create / add / remove / check existence

```python
s = set()

# Add element
s.add(42)
s.add(7)

# Remove element (KeyError if not present)
s.remove(42)

# Remove element (no error if not present)
s.discard(999)

# Check if element exists
if 7 in s:
    print("found")

# Alternative check
exists = 7 in s
```

# Parity Check

## Determining if an integer is odd or even using the modulo operator

```python
is_even = n % 2 == 0
is_odd = n % 2 != 0

```


































# Linked Lists

# Singly Linked List
## Traverse & print values with empty list check

```python
if not head:
    print("Empty list")
    return

cur = head
while cur:
    print(cur.val)
    cur = cur.next
```

## Find middle node (slow & fast pointers)

```python
slow = fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

# slow is now at the middle (for odd length) or second middle (even)
```


## Detect cycle (Floyd's tortoise and hare / slow-fast pointer)

```python
slow, fast = head, head

while fast and fast.next:
    slow = slow.next          # moves 1 step
    fast = fast.next.next     # moves 2 steps
    
    if slow == fast:
        return True           # cycle found

return False                  # no cycle
```



## Reversing a singly linked list in-place using three pointers

```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        
    return prev

```




# Doubly linked lists

## DFS Traverse

# Binary Tree DFS (In-order)

## Depth-First Search explores as far as possible along each branch before backtracking; ideal for sorted traversal and low memory usage

```python
def inorder(root):
    # Advantages: Simple recursive implementation; uses O(h) space (height of tree).
    # In-order on a BST yields elements in non-decreasing order.
    if not root:
        return
    
    inorder(root.left)
    print(root.val)
    inorder(root.right)

```

## BFS Traverse

# Binary Tree BFS (Level-order)

## Breadth-First Search visits nodes level-by-level using a queue; ideal for finding the shortest path or level boundaries

```python
from collections import deque

def level_order(root):
    # Advantages: Guarantees finding the shortest path to a node; visits nodes level by level.
    # Uses O(w) space where w is the maximum width of the tree.
    if not root:
        return
    
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)
        
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)

```


## Binary Tree comparison using DFS
Yes, the value comparison `p.val != q.val` handles the roots of the current subtrees in each call.

# Tree Comparison

## Recursive DFS implicitly compares the current root nodes before proceeding to children

```python
def is_same_tree(p, q):
    # Base cases: both null (True) or one null (False)
    if not p and not q:
        return True
    if not p or not q:
        return False
    
    # Root value comparison (Head of the current subtree)
    if p.val != q.val:
        return False
    
    # Recursive calls for branches
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

```

---
# Two Sum (Sorted)

## Using two pointers starting at both ends to find a target sum in O(n) time and O(1) space

```python
def two_sum_sorted(numbers, target):
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1] # 1-indexed example
        elif current_sum < target:
            left += 1
        else:
            right -= 1
            
    return []

```

