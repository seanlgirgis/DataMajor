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


# LC0074 Search a 2D Matrix
## matrix is sorted

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #problem screams binary search
        #Find a way to convert matrix to List
        #Since creating new space is processing and space.. do it on the fly
        #
        rows,cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols -1
        
        while left <= right:
            mid = (left + right) //2
            midv = matrix[mid//cols][mid%cols]
            if midv == target:
                return True
            elif midv < target:
                left = mid + 1
            else:
                right = mid -1
        
        
        #assume the worst. If we found it we would have returned
        #Solution is always at mid in binary search
        return False

```
#LEC0206 Reverse Linked List
##  
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head 
        prev = None
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev

```



---
# LC0424 .. Longest Repeating Character Replacement
##  You can replace up to a k characters . get the max possible window with replacements of the same char
### sliding Window Technique

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0                       # Left pointer of our sliding window
        res = 0                     # Stores the maximum length found so far
        count = {}                  # Frequency dictionary for characters in current window
        
        # r is the right pointer expanding the window
        for r in range(len(s)):
            # 1. Add the new character to our window's frequency count
            # you can continue do that until you have exceeded possible replacements
            count[s[r]] = count.get(s[r], 0) + 1
            
            # 2. Check if the current window is VALID.
            # A window is valid if: (Length of window) - (Count of most frequent char) <= k
            # This means the number of characters we need to replace is within our allowance 'k'.
            # Note: `max(count.values())` takes O(26) time. To optimize to O(1), you can just track a `max_f` variable!
            while (r - l + 1) - max(count.values()) > k:
                # If invalid, shrink the window by moving the left pointer
                count[s[l]] -= 1
                l += 1
                
            # 3. The window is now valid, so we update our maximum result length
            res = max(res, r - l + 1)
            
        return res

s, k = "ABABABABAB", 2
print(Solution().characterReplacement(s,k))

```
 

