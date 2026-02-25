| # | Problem Title | Concepts | Difficulty | 
| :--- | :--- | :--- | :--- | 
| **1** | [Two Sum](#1-two-sum) | `Array`, `Hash Table` | 2/10 |
| **70** | [Climbing Stairs](#70-climbing-stairs) | `Dynamic Programming`, `Memoization`, `Math` | 2/10 |
| **100** | [Same Tree](#100-same-tree) | `Tree`, `Depth-First Search`, `Binary Tree` | 2/10 |
| **217** | [Contains Duplicate](#217-contains-duplicate) | `Array`, `Hash Set` | 1/10 | 
| **704** | [Binary Search](#704-binary-search) | `Binary Search`, `Array` | 3/10 |  









---
# LEC Cases

---


## 217: Contains Duplicate

### Problem Description
> Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

- number: 217
- title: "Contains Duplicate"
- difficulty: 1/10
- concepts: ["Array", "Hash Set", "Lookup"]
- jupyter_path: ".C:\DataMajor\practice\001Study\playground\group1\217.ipynb"
- script_path: "C:\DataMajor\practice\001Study\playground\group1\217.py"

---

### Solution Idea (Pseudo-solution)
* **Approach:** Hash Set for $O(1)$ average time complexity lookups.
* **Logic:**
    1. Initialize an empty set called `seen`.
    2. Iterate through each number `n` in the input array `nums`.
    3. If `n` is already in `seen`, a duplicate exists; return **True**.
    4. Otherwise, add `n` to the `seen` set and continue.
    5. If the loop finishes without finding a duplicate, return **False**.

**Complexity:**
* **Time:** $O(n)$
* **Space:** $O(n)$

---

### Solution Code
```python

from typing import List
def contains_duplicate(nums:List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False
print ("Single Test Success" if contains_duplicate([1, 2, 3, 4]) == False else "Single Test Fail")

    
```

---

## 704: Binary Search

### Problem Description
> Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

- number: 704
- title: "Binary Search"
- difficulty: 3/10
- concepts: ["Binary Search", "Array"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group1\704.ipynb"
- script_path: 

---

### Solution Idea (Pseudo-solution)
* **Approach:** Binary Search + Two Pointers. The sequence is already sorted so we find the target by halving the search space repeatedly.
* **Logic:**
    1. Initialize `left` pointer to `0`, and `right` pointer to `len(nums) - 1`
    2. While `left` is less than or equal to `right`:
    3. Calculate the midpoint `mid` index using `(left + right) // 2`
    4. If the element at `mid` is the target, return `mid`
    5. Else if the element at `mid` is less than target, target must be in the right half, so move `left` to `mid + 1`
    6. Else if the element at `mid` is greater than target, target must be in the left half, so move `right` to `mid - 1`
    7. If loop finishes with no match, return `-1`

**Complexity:**
* **Time:** $O(\log n)$
* **Space:** $O(1)$

---

### Solution Code
```python

from typing import List
def search(nums: List[int], target: int) -> int:
    # as it is sorted; Binary search is easy
    #2 Pointers .. one from left and one from right 
    # mid is right+left // 2
    left, right = 0, len(nums) -1
    while right >= left:        # drr the >= this covers the case when both pointers alight over the target
        mid = (left+right) //2
        if  target == nums[mid] :
            return mid
        # Now if the target is bigger than number in middle
        elif target > nums[mid]:
            #Move left to mid + 1
            left = mid + 1
        else:
            right = mid - 1
    return -1
print("Test1: Odd number of elements:Target exact middle: success" if search([1, 2, 3, 4, 5], 3) == 2 else "Test1: Fail")
print("Test2: search fro trget 4 in [1, 2, 3, 4, 5, 6] : success" if search([1, 2, 3, 4, 5, 6], 4) == 3 else "Test2: Fail")

```

---

## 1: Two Sum

### Problem Description
> Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

- number: 1
- title: "Two Sum"
- difficulty: 2/10
- concepts: ["Array", "Hash Table"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group1\1.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def twoSum(self, nums: List[int], target: int) -> List[int]:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Hash Map for One-Pass Lookups
* **Logic:**
    1. Initialize an empty dictionary `seen` to store numbers and their indices.
    2. Iterate through each number `num` and its `index` in `nums`.
    3. Calculate the `complement` as `target - num`.
    4. If `complement` exists in `seen`, return `[seen[complement], index]`.
    5. Otherwise, store `seen[num] = index`.

**Complexity:**
* **Time:** $O(n)$
* **Space:** $O(n)$

---

### Solution Code
```python

from typing import List
class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Define a seen dict
        seen: dict = {}
        for i, num in enumerate(nums):
            if (target - num) in seen:
                return [seen[(target - num)  ], i]
            else:
                seen[num] = i
        return []


sol = Solution()
print("Test1: [2,7,11,15] target=9 -> [0,1]: success" if sol.twoSum([2,7,11,15], 9) == [0,1] else "Test1: Fail")
print("Test2: [3,2,4] target=6 -> [1,2]: success" if sol.twoSum([3,2,4], 6) == [1,2] else "Test2: Fail")
print("Test3: [3,3] target=6 -> [0,1]: success" if sol.twoSum([3,3], 6) == [0,1] else "Test3: Fail")

```



---

## 70: Climbing Stairs

### Problem Description
> You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

- number: 70
- title: "Climbing Stairs"
- difficulty: 2/10
- concepts: ["Dynamic Programming", "Memoization", "Math"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group1\70.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def climbStairs(self, n: int) -> int:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Bottom-Up Dynamic Programming (Fibonacci Sequence).
* **Logic:**
    1. If `n <= 2`, return `n` directly (1 way for 1 step, 2 ways for 2 steps).
    2. Initialize `two_steps_before = 1` and `one_step_before = 2`.
    3. Loop from step 3 up to `n`.
    4. Calculate the distinct ways to reach the current step as `one_step_before + two_steps_before`.
    5. Update variables for the next iteration: `two_steps_before = one_step_before`, and `one_step_before = current_ways`.
    6. Return `one_step_before`.

**Complexity:**
* **Time:** $O(n)$
* **Space:** $O(1)$

---

### Solution Code
```python
r"""
    To understand this problem let us go through the seq
    number of steps           possible solutions
    1                         1
    2                         2
    3                         3
    4                         5   < 1111 ; 112 ; 121; 211; 22 >
    in short each step is the sum of the two previous steps
    can be done easily in recursion; but Ifeel it is an overkill
    storing all previous values seems to be an overkill
    
"""

class Solution(object):
    def climbStairs(self, n: int) -> int:
        if n <=2: return n
        prev = 2
        prevprev = 1
        for _ in range (3, n):
            cur = prev + prevprev
            prevprev = prev
            prev = cur
        return prevprev + prev
            
sol = Solution()
print("Test1: n=4 -> 5: success" if sol.climbStairs(4) == 5 else "Test1: Fail")
print("Test2: n=3 -> 3: success" if sol.climbStairs(3) == 3 else "Test2: Fail")
print("Test3: n=1 (edge case) -> 1: success" if sol.climbStairs(1) == 1 else "Test3: Fail")
```

---

## 100: Same Tree

### Problem Description
> Given the roots of two binary trees p and q, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

- number: 100
- title: "Same Tree"
- difficulty: 2/10
- concepts: ["Tree", "Depth-First Search", "Binary Tree"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group1\100.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Depth-First Search (DFS) Recursion — check current nodes, then recursively check left and right subtrees.
* **Logic:**
    1. If both `p` and `q` are `None`, return `True` (reached leaves).
    2. If one is `None` but the other is not, or if their values do not match, return `False`.
    3. Recursively call `isSameTree` on `p.left` and `q.left`.
    4. Recursively call `isSameTree` on `p.right` and `q.right`.
    5. Return `True` only if both recursive calls return `True`.

**Complexity:**
* **Time:** $O(n)$
* **Space:** $O(n)$

---

### Solution Code
```python

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None : return True           # we have reached the end of the trees
        if p is None or q is None : return False           # One is exhausted and the other not yet Not matching
        if p.val != q.val :return False                    # Values are not mathcing. Trees are not the same
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))



sol = Solution()
p1 = TreeNode(1, TreeNode(2), TreeNode(3))
q1 = TreeNode(1, TreeNode(2), TreeNode(3))
print("Test1: [1,2,3], [1,2,3] -> True: success" if sol.isSameTree(p1, q1) == True else "Test1: Fail")

p2 = TreeNode(1, TreeNode(2))
q2 = TreeNode(1, None, TreeNode(2))
print("Test2: [1,2], [1,null,2] (edge case) -> False: success" if sol.isSameTree(p2, q2) == False else "Test2: Fail")

p3 = TreeNode(1, TreeNode(2), TreeNode(1))
q3 = TreeNode(1, TreeNode(1), TreeNode(2))
print("Test3: [1,2,1], [1,1,2] -> False: success" if sol.isSameTree(p3, q3) == False else "Test3: Fail")

```

---
# Template

<!-- ═══════════════════════════════════════════════════════
     AGENT INSTRUCTIONS — how to fill this template
     ═══════════════════════════════════════════════════════
     1. Description: fetch from https://leetcode.com/problems/<slug>/
        Fall back to training knowledge if fetch fails.
     2. function_signature: always the exact LeetCode Python signature.
     3. Solution Code: NEVER leave empty.
        Always write class skeleton + pass + sol = Solution() + print tests.
     4. jupyter_path / script_path: leave as placeholder — user fills.
     ═══════════════════════════════════════════════════════ -->

---


## <<NUMBER>>: <<Title>>

### Problem Description
> <<Fetched from leetcode.com/problems/<slug>/ or from training knowledge>>

- number: <<number>>
- title: "<<Title>>"
- difficulty: <<difficulty>>/10
- concepts: ["<<Concept 1>>", "<<Concept 2>>", "<<Concept 3>>"]
- jupyter_path: <<absolute Path... I fill it>>
- script_path: <<absolute Path... I fill it>>
- function_signature: def <<func_name>>(self, <<params>>) -> <<return_type>>:

---

### Solution Idea (Pseudo-solution)
* **Approach:** <<pattern name — key insight>>
* **Logic:**
    1. <<Logic goes here>>
    2. <<Logic goes here>>
    3. <<Logic goes here>>
    4. <<Logic goes here>>
    5. <<Logic goes here>>

**Complexity:**
* **Time:** $O(...)$
* **Space:** $O(...)$

---

### Solution Code
```python
from typing import List   # include only if needed

class Solution(object):
    def <<func_name>>(self, <<params>>) -> <<return_type>>:
        pass




sol = Solution()
print("Test1: <<input>> -> <<expected>>: success" if sol.<<func_name>>(<<args1>>) == <<expected1>> else "Test1: Fail")
print("Test2: <<input>> -> <<expected>>: success" if sol.<<func_name>>(<<args2>>) == <<expected2>> else "Test2: Fail")
print("Test3: <<edge case>> -> <<expected>>: success" if sol.<<func_name>>(<<args3>>) == <<expected3>> else "Test3: Fail")
```
