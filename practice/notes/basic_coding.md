# math and inf

```python
from math import inf
var = inf         #now yo uhave a veriable that is stet to inf
```


# Stack Operations

## Basic stack management using Python lists for efficient push, pop, and search

```python
stack = []

# Add (Push)
stack.append(10)

# Delete/Pop (Safe removal)
top = stack.pop() if stack else None

# Search (Check existence or find index)
is_present = 10 in stack
index = stack.index(10) if 10 in stack else -1

```




# Recursion Optimization

## Using functools.cache to store results of recursive calls and prevent redundant calculations

```python
from functools import cache

@cache
def solve(n):
    # functools.cache enhances performance by implementing memoization,
    # ensuring each unique input is calculated only once.
    if n <= 1:
        return n
    return solve(n - 1) + solve(n - 2)

```
