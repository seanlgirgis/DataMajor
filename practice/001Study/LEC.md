| # | Problem Title | Concepts | Difficulty | 
| :--- | :--- | :--- | :--- | 
| **1** | [Two Sum](#1-two-sum) | `Array`, `Hash Table` | 2/10 |
| **21** | [Merge Two Sorted Lists](#21-merge-two-sorted-lists) | `Linked List`, `Two Pointers`, `Recursion` | 1/10 |
| **70** | [Climbing Stairs](#70-climbing-stairs) | `Dynamic Programming`, `Memoization`, `Math` | 2/10 |
| **100** | [Same Tree](#100-same-tree) | `Tree`, `Depth-First Search`, `Binary Tree` | 2/10 |
| **104** | [Maximum Depth of Binary Tree](#104-maximum-depth-of-binary-tree) | `Tree`, `Depth-First Search`, `Breadth-First Search` | 2/10 |
| **121** | [Best Time to Buy and Sell Stock](#121-best-time-to-buy-and-sell-stock) | `Array`, `Dynamic Programming` | 1/10 |
| **206** | [Reverse Linked List](#206-reverse-linked-list) | `Linked List`, `Recursion` | 1/10 |
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

## 104: Maximum Depth of Binary Tree

### Problem Description
> Given the `root` of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

- number: 104
- title: "Maximum Depth of Binary Tree"
- difficulty: 2/10
- concepts: ["Tree", "Depth-First Search", "Breadth-First Search"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group1\104.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def maxDepth(self, root: Optional[TreeNode]) -> int:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Depth-First Search (Recursion) — the max depth of a tree is 1 plus the max depth of its deepest subtree.
* **Logic:**
    1. If `root` is `None`, return `0` (depth is 0).
    2. Recursively call `maxDepth` on `root.left`.
    3. Recursively call `maxDepth` on `root.right`.
    4. Calculate the maximum of the two depths.
    5. Return the maximum depth computed plus `1` (for the current node).

**Complexity:**
* **Time:** $O(n)$
* **Space:** $O(h)$ where h is the height of the tree (for recursion stack). Or $O(n)$ in the worst case (skewed tree).

---

### Solution Code
```python
from typing import Optional
r"""
Thinking: -
    - Recursive wins
    - if object is None .. return 0   (end of a tree)
    - return max (maxDepth (left) and right + 1
    

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #No run forever
        if root is None:
            return 0
        return max(self.maxDepth(root.left) , self.maxDepth(root.right)) + 1


sol = Solution()
root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print("Test1: [3,9,20,null,null,15,7] -> 3: success" if sol.maxDepth(root1) == 3 else "Test1: Fail")

root2 = TreeNode(1, None, TreeNode(2))
print("Test2: [1,null,2] -> 2: success" if sol.maxDepth(root2) == 2 else "Test2: Fail")

root3 = None
print("Test3: [] (edge case) -> 0: success" if sol.maxDepth(root3) == 0 else "Test3: Fail")

```

---

## 121: Best Time to Buy and Sell Stock

### Problem Description
> You are given an array prices where `prices[i]` is the price of a given stock on the `ith` day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

- number: 121
- title: "Best Time to Buy and Sell Stock"
- difficulty: 1/10
- concepts: ["Array", "Dynamic Programming"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group1\121.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def maxProfit(self, prices: List[int]) -> int:

---

### Solution Idea (Pseudo-solution)
* **Approach:** One Pass (Greedy / state tracking) — Keep track of the lowest price seen so far and the maximum profit at each step.
* **Logic:**
    1. Initialize `min_price` to infinity (or a very large number).
    2. Initialize `max_profit` to `0`.
    3. Loop through each `price` in the array `prices`.
    4. If the current `price` is less than `min_price`, update `min_price` to `price`.
    5. Else if `price - min_price` is greater than `max_profit`, update `max_profit` to `price - min_price`.
    6. Return `max_profit`.

**Complexity:**
* **Time:** $O(n)$
* **Space:** $O(1)$

---

### Solution Code
```python
r"""
Thinking:
    - tart by setting buy to infinity so any real price beats it.
    - creat a virtual price of buy at infinity.. can not every buy more expensively
    - initially your profit is 0
    - only buy of you can buy cheaper
    - only sell if you can make more profit
    

"""
from math import inf
from typing import List

class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        buy = inf
        profit = 0
        for p in prices:
            profit = max( profit, p - buy)
            if p < buy: buy = p
        return profit


sol = Solution()
print("Test1: [7,1,5,3,6,4] -> 5: success" if sol.maxProfit([7,1,5,3,6,4]) == 5 else "Test1: Fail")
print("Test2: [7,6,4,3,1] -> 0: success" if sol.maxProfit([7,6,4,3,1]) == 0 else "Test2: Fail")
print("Test3: [2,4,1] (edge case) -> 2: success" if sol.maxProfit([2,4,1]) == 2 else "Test3: Fail")
```

---

## 206: Reverse Linked List

### Problem Description
> Given the `head` of a singly linked list, reverse the list, and return the reversed list.

- number: 206
- title: "Reverse Linked List"
- difficulty: 1/10
- concepts: ["Linked List", "Recursion"]
- jupyter_path: <<absolute Path... I fill it>>
- script_path: <<absolute Path... I fill it>>
- function_signature: def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Iterative Pointers — Keep track of previous node, current node, and next node to reverse the links.
* **Logic:**
    1. Initialize `prev` as `None` and `current` as `head`.
    2. While `current` is not `None`:
    3. Save `next_node` as `current.next` so we don't lose the rest of the list.
    4. Reverse the link: point `current.next` to `prev`.
    5. Move `prev` forward to `current`, and `current` forward to `next_node`.
    6. Return `prev` as the new head.

**Complexity:**
* **Time:** $O(n)$
* **Space:** $O(1)$

---

### Solution Code
```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass


def to_list(head: Optional[ListNode]) -> list:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

def to_linked_list(lst: list) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

sol = Solution()
print("Test1: [1,2,3,4,5] -> [5,4,3,2,1]: success" if to_list(sol.reverseList(to_linked_list([1,2,3,4,5]))) == [5,4,3,2,1] else "Test1: Fail")
print("Test2: [1,2] -> [2,1]: success" if to_list(sol.reverseList(to_linked_list([1,2]))) == [2,1] else "Test2: Fail")
print("Test3: [] (edge case) -> []: success" if to_list(sol.reverseList(to_linked_list([]))) == [] else "Test3: Fail")
```

---

## 21: Merge Two Sorted Lists

### Problem Description
> You are given the heads of two sorted linked lists list1 and list2. Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.

- number: 21
- title: "Merge Two Sorted Lists"
- difficulty: 1/10
- concepts: ["Linked List", "Two Pointers", "Recursion"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group1\21.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Two Pointers with Dummy Node — Iterate through both lists, appending the smaller value to the merged list.
* **Logic:**
    1. Create a `dummy` node to act as the head of the merged list.
    2. Initialize a pointer `current` to `dummy`.
    3. Loop while both `list1` and `list2` are not `None`:
    4. If `list1.val < list2.val`, set `current.next` to `list1`, and advance `list1`.
    5. Else, set `current.next` to `list2`, and advance `list2`.
    6. Advance `current`. After the loop, attach any remaining nodes from `list1` or `list2` and return `dummy.next`.

**Complexity:**
* **Time:** $O(n + m)$
* **Space:** $O(1)$

---

### Solution Code
```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
r"""
Merge Two Sorted Lists
----------------------
Strategy: dummy head + two-pointer traversal

Create a dummy node as a fixed anchor for the result list.
Use curr to build the merged list by advancing through it node by node.

Each iteration, compare the front of list1 vs list2 — attach the smaller
node to curr.next, advance that list forward, then advance curr.

When one list is exhausted, the other is already sorted — attach it whole.

Return dummy.next to skip the empty placeholder and get the real head.

Pattern: dummy/curr is the standard linked list construction pattern.
         dummy stays fixed. curr walks. dummy.next is always your answer.
"""
class Solution(object):
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2 : return None
        if not list1: return list2
        if not list2: return list1
        #Now edge cases are handled. We have two lists to merge
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next        # ← advance curr
        curr.next = list1 or list2  # ← attach remainder
        return dummy.next           # ← skip the dummy        


def to_list(head: Optional[ListNode]) -> list:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

def to_linked_list(lst: list) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

sol = Solution()
l1 = to_linked_list([1,2,4])
l2 = to_linked_list([1,3,4])
print("Test1: [1,2,4], [1,3,4] -> [1,1,2,3,4,4]: success" if to_list(sol.mergeTwoLists(l1, l2)) == [1,1,2,3,4,4] else "Test1: Fail")

l3 = to_linked_list([])
l4 = to_linked_list([])
print("Test2: [], [] (edge case) -> []: success" if to_list(sol.mergeTwoLists(l3, l4)) == [] else "Test2: Fail")

l5 = to_linked_list([])
l6 = to_linked_list([0])
print("Test3: [], [0] -> [0]: success" if to_list(sol.mergeTwoLists(l5, l6)) == [0] else "Test3: Fail")
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
