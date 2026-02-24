# LIST — Syntax Card

## Create & Initialize
```python
a = []                      # empty
a = [0] * n                 # n zeros
a = list(range(n))          # [0,1,...,n-1]
a = [x*2 for x in range(5)] # comprehension
```

## Access & Slice
```python
a[0]        # first
a[-1]       # last
a[1:4]      # index 1,2,3 (end exclusive)
a[::-1]     # reversed copy
a[::2]      # every other element
```

## Add / Remove
```python
a.append(x)         # add to end         O(1)
a.insert(i, x)      # insert at index    O(n)
a.pop()             # remove last        O(1)
a.pop(i)            # remove at index    O(n)
a.remove(x)         # remove first x     O(n)
del a[i]            # delete at index    O(n)
a.extend([1,2,3])   # add multiple       O(k)
a + [4,5]           # concatenate (new list)
```

## Search & Info
```python
x in a              # membership         O(n)
a.index(x)          # first index of x   O(n)
a.count(x)          # occurrences        O(n)
len(a)              # length             O(1)
min(a), max(a)      # min/max            O(n)
sum(a)              # sum                O(n)
```

## Sort & Order
```python
a.sort()                        # in-place, O(n log n)
a.sort(reverse=True)            # descending
a.sort(key=lambda x: x[1])     # by second element
sorted(a)                       # returns new list
sorted(a, key=len)              # sort strings by length
a.reverse()                     # in-place reverse   O(n)
```

## Copy
```python
b = a[:]            # shallow copy (slice)
b = a.copy()        # shallow copy (method)
import copy
b = copy.deepcopy(a)  # deep copy (nested lists)
```

## Stack (use list)
```python
stack = []
stack.append(x)     # push    O(1)
stack.pop()         # pop     O(1)
stack[-1]           # peek    O(1)
```

## 2D List
```python
grid = [[0]*cols for _ in range(rows)]  # correct
# grid = [[0]*cols] * rows  WRONG — shares rows
grid[r][c]          # access cell
len(grid)           # rows
len(grid[0])        # cols
```

## Useful Patterns
```python
# Enumerate (index + value)
for i, v in enumerate(a):
    ...

# Zip two lists
for x, y in zip(a, b):
    ...

# Flatten 2D
flat = [x for row in grid for x in row]

# Unpack
first, *rest = a
*init, last  = a
```
