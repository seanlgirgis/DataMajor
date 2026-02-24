# LRU CACHE / MEMOIZATION — Syntax Card

## Basic Usage
```python
from functools import lru_cache

@lru_cache(maxsize=None)        # None = unlimited cache (best for interviews)
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)  # repeated calls hit cache, not recursion
```

## On a Class Method
```python
from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    # WARNING: self is part of the cache key — can cause memory leaks
    # Safe for interviews, not for production
```

## cache (Python 3.9+) — simpler alias
```python
from functools import cache   # equivalent to lru_cache(maxsize=None)

@cache
def solve(n):
    ...
```

## Cache Info / Clear
```python
fib.cache_info()              # hits, misses, maxsize, currsize
fib.cache_clear()             # wipe the cache
```

## Manual Memo dict (interview-safe alternative)
```python
def solve(n, memo={}):        # memo={} created once — persists across calls
    if n in memo: return memo[n]
    # ... compute result ...
    memo[n] = result
    return result

# Safer: pass memo explicitly
def solve(n, memo=None):
    if memo is None: memo = {}
    if n in memo: return memo[n]
    memo[n] = solve(n-1, memo) + solve(n-2, memo)
    return memo[n]
```

## When to Use
```python
# Use @lru_cache when:
# - function is pure (same input → same output, no side effects)
# - subproblems repeat (DP, recursion trees)
# - args are hashable (int, str, tuple — NOT list or dict)

# Unhashable args will raise TypeError:
@lru_cache
def bad(nums: list): ...      # TypeError — list not hashable
def good(nums: tuple): ...    # tuple is hashable — OK
```

## Complexity Impact
```python
# Without cache:  O(2^n) — exponential (recomputes everything)
# With cache:     O(n)   — each unique input computed exactly once
# Space:          O(n)   — cache stores n entries + call stack
```
