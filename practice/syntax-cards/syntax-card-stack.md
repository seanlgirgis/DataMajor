# STACK — Syntax Card

## Declare
```python
stack = []                      # Python list as stack
```

## Core Operations
```python
stack.append(x)                 # push
stack.pop()                     # pop + return; IndexError if empty
stack[-1]                       # peek top; IndexError if empty
len(stack) == 0                 # check empty
if not stack:                   # check empty (Pythonic)
len(stack)                      # size
```

## Safe Operations
```python
val = stack.pop() if stack else None   # safe pop
top = stack[-1]  if stack else None   # safe peek
```

## Iterate (non-destructive)
```python
for item in stack:              # bottom → top
for item in reversed(stack):   # top → bottom
```

## Common Patterns

### Valid Parentheses
```python
stack = []
pairs = {")": "(", "]": "[", "}": "{"}
for c in s:
    if c in "([{":
        stack.append(c)
    elif not stack or stack[-1] != pairs[c]:
        return False
    else:
        stack.pop()
return not stack
```

### Monotonic Stack (Next Greater Element)
```python
stack = []                      # stores indices
res = [-1] * len(nums)
for i, n in enumerate(nums):
    while stack and nums[stack[-1]] < n:
        res[stack.pop()] = n   # found next greater
    stack.append(i)
```

### Min Stack (track min alongside values)
```python
stack = []                      # stores (val, current_min)
stack.append((val, min(val, stack[-1][1] if stack else val)))
cur_min = stack[-1][1]         # O(1) min
```
