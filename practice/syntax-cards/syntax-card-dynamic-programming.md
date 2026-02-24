# DYNAMIC PROGRAMMING — Syntax Card

## Decision Framework
```python
# 1. Can I define subproblems?
# 2. Do subproblems overlap?  -> cache
# 3. Can I go bottom-up?      -> O(1) space
```

## Climbing Stairs / Fibonacci — bottom-up O(1)
```python
a, b = 1, 1
for _ in range(n - 1):
    a, b = b, a + b
return b
```

## House Robber — adjacent constraint
```python
prev2 = prev1 = 0
for n in nums:
    curr = max(prev1, n + prev2)   # skip or rob
    prev2, prev1 = prev1, curr
return prev1
```

## Maximum Subarray — Kadane's
```python
curr = max_sum = nums[0]
for n in nums[1:]:
    curr = max(n, curr + n)        # restart or extend
    max_sum = max(max_sum, curr)
return max_sum
```

## Best Time to Buy/Sell Stock — running min
```python
min_price = float('inf')
max_profit = 0
for p in prices:
    max_profit = max(max_profit, p - min_price)
    min_price  = min(min_price, p)
return max_profit
```

## 1D DP — in-place table (House Robber variant)
```python
for i in range(1, len(nums)):
    if i == 1: nums[1] = max(nums[0], nums[1])
    else:      nums[i] = max(nums[i] + nums[i-2], nums[i-1])
return nums[-1]
```

## @lru_cache — top-down memoization
```python
from functools import cache

@cache
def dp(i):
    if i <= 1: return i
    return dp(i-1) + dp(i-2)
```

## Patterns by problem shape
```python
# Single sequence, no skip constraint  -> Kadane's / running value
# Single sequence, skip-one constraint -> House Robber (prev2/prev1)
# Count ways                           -> Fibonacci / bottom-up
# 2D grid paths                        -> dp[i][j] = dp[i-1][j] + dp[i][j-1]
```
