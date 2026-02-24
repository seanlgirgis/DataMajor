# buy sell stock for max profit
### must buy before you sell.

```python
  buy = inf
  profit = 0
  for price in prices:
    profit = max(profit, (price - buy))
    if price < buy : buy = price
  return profit
```

# Find if a linked list has  a cycle
### Option 1 O(n)  using a set

```python
        if not head:
            return False
        seen = set()
        cur = head
        while True:
            if cur in seen:
                return True        # Found a cycle!
            seen.add(cur)          # Track that we've seen this node
            
            cur = cur.next
            if not cur: break
        return False               # Loop completed naturally, no cycle
```

### Option 2 O(1)  using a fast and slow pointers

```python
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next          # moves 1 step
            fast = fast.next.next     # moves 2 steps
            
            if slow == fast:
                return True           # fast lapped slow, cycle found!
                
        return False                  # fast reached end of list, no cycle

```


# LC0020 Valid Parentheses
# 

```python

    def isValid(self, s: str) -> bool:
        if not s: return True
        if len(s) %2 != 0 : return False  #Odd
        p = {'(': ')', '{': '}', '[' :']'}
        stack = []
        for ch in s:
            if ch in p:  # Open paranthesis
                stack.append(ch)
            elif stack and  p[stack[-1]] == ch:
                stack.pop()
            else:
                return False
        #For isValid stack ought to be empty        
        return True if not stack else False
```


# LC0070 Find  how many distinct ways can you climb to the top?  
## Understand the sequence
```python
1     1
2     2
3     3
4     5
5     8   => 5 + 3
6     13  => 8 + 5 

```
## Solution 1 .. Mine works and expensive in space
## recursive
```python
from functools import cache 
class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

```

## Solution 2 .. Lengthier - Better - Cheaper
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: 
            return n
            
        # Base cases for n = 1 and n = 2
        two_steps_before = 1  # Ways to climb 1 step
        one_step_before = 2   # Ways to climb 2 steps
        
        # Calculate from step 3 up to step n
        for _ in range(3, n + 1):
            current = one_step_before + two_steps_before
            
            # Shift the window forward for the next iteration
            two_steps_before = one_step_before
            one_step_before = current
            
        return one_step_before
```

# LC0424 .. Longest Repeating Character Replacement
## 


