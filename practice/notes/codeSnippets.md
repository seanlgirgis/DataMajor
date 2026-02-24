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

