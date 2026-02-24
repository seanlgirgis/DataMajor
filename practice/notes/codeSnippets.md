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

