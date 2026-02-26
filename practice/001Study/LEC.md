
---
# LEC Cases
---

| # | Problem Title | Concepts | Difficulty | 
| :--- | :--- | :--- | :--- | 
| **1** | [Two Sum](#1-two-sum) | `Array`, `Hash Table` | 2/10 |
| **3** | [Longest Substring Without Repeating Characters](#3-longest-substring-without-repeating-characters) | `Hash Table`, `String`, `Sliding Window` | 2/10 |
| **20** | [Valid Parentheses](#20-valid-parentheses) | `String`, `Stack` | 1/10 |
| **21** | [Merge Two Sorted Lists](#21-merge-two-sorted-lists) | `Linked List`, `Two Pointers`, `Recursion` | 1/10 |
| **49** | [Group Anagrams](#49-group-anagrams) | `Array`, `Hash Table`, `String`, `Sorting` | 2/10 |
| **53** | [Maximum Subarray](#53-maximum-subarray) | `Array`, `Divide and Conquer`, `Dynamic Programming` | 2/10 |
| **70** | [Climbing Stairs](#70-climbing-stairs) | `Dynamic Programming`, `Memoization`, `Math` | 2/10 |
| **73** | [Set Matrix Zeroes](#73-set-matrix-zeroes) | `Array`, `Hash Table`, `Matrix` | 2/10 |
| **74** | [Search a 2D Matrix](#74-search-a-2d-matrix) | `Array`, `Binary Search`, `Matrix` | 2/10 |
| **83** | [Remove Duplicates from Sorted List](#83-remove-duplicates-from-sorted-list) | `Linked List` | 1/10 |
| **100** | [Same Tree](#100-same-tree) | `Tree`, `Depth-First Search`, `Binary Tree` | 2/10 |
| **102** | [Binary Tree Level Order Traversal](#102-binary-tree-level-order-traversal) | `Tree`, `Breadth-First Search`, `Binary Tree` | 2/10 |
| **104** | [Maximum Depth of Binary Tree](#104-maximum-depth-of-binary-tree) | `Tree`, `Depth-First Search`, `Breadth-First Search` | 2/10 |
| **121** | [Best Time to Buy and Sell Stock](#121-best-time-to-buy-and-sell-stock) | `Array`, `Dynamic Programming` | 1/10 |
| **128** | [Longest Consecutive Sequence](#128-longest-consecutive-sequence) | `Array`, `Hash Table`, `Union Find` | 2/10 |
| **141** | [Linked List Cycle](#141-linked-list-cycle) | `Hash Table`, `Linked List`, `Two Pointers` | 1/10 |
| **142** | [Linked List Cycle II](#142-linked-list-cycle-ii) | `Hash Table`, `Linked List`, `Two Pointers` | 2/10 |
| **143** | [Reorder List](#143-reorder-list) | `Linked List`, `Two Pointers`, `Stack` | 2/10 |
| **155** | [Min Stack](#155-min-stack) | `Stack`, `Design` | 2/10 |
| **167** | [Two Sum II - Input Array Is Sorted](#167-two-sum-ii---input-array-is-sorted) | `Array`, `Two Pointers`, `Binary Search` | 2/10 |
| **198** | [House Robber](#198-house-robber) | `Array`, `Dynamic Programming` | 2/10 |
| **203** | [Remove Linked List Elements](#203-remove-linked-list-elements) | `Linked List`, `Recursion` | 1/10 |
| **206** | [Reverse Linked List](#206-reverse-linked-list) | `Linked List`, `Recursion` | 1/10 |
| **217** | [Contains Duplicate](#217-contains-duplicate) | `Array`, `Hash Set` | 1/10 | 
| **226** | [Invert Binary Tree](#226-invert-binary-tree) | `Tree`, `Depth-First Search`, `Binary Tree` | 1/10 |
| **242** | [Valid Anagram](#242-valid-anagram) | `Hash Table`, `String`, `Sorting` | 1/10 |
| **378** | [Kth Smallest Element in a Sorted Matrix](#378-kth-smallest-element-in-a-sorted-matrix) | `Array`, `Binary Search`, `Matrix`, `Heap (Priority Queue)` | 2/10 |
| **496** | [Next Greater Element I](#496-next-greater-element-i) | `Array`, `Hash Table`, `Monotonic Stack` | 1/10 |
| **674** | [Longest Continuous Increasing Subsequence](#674-longest-continuous-increasing-subsequence) | `Array` | 1/10 |
| **704** | [Binary Search](#704-binary-search) | `Binary Search`, `Array` | 3/10 |
| **876** | [Middle of the Linked List](#876-middle-of-the-linked-list) | `Linked List`, `Two Pointers` | 1/10 |
| **937** | [Reorder Data in Log Files](#937-reorder-data-in-log-files) | `Array`, `String`, `Sorting` | 2/10 |
| **2043** | [Simple Bank System](#2043-simple-bank-system) | `Array`, `Design`, `Simulation` | 2/10 |

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

[↑ Back to Top](#lec-cases)

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

[↑ Back to Top](#lec-cases)

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

[↑ Back to Top](#lec-cases)

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

[↑ Back to Top](#lec-cases)

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

[↑ Back to Top](#lec-cases)

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

[↑ Back to Top](#lec-cases)

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

[↑ Back to Top](#lec-cases)

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
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""r
Reversing   a linked list requires creating an imaginary node (dummy) and use it to traverse
the list while swapping the pointers converting head to tail and vice versa
Obviously hard copying of nodes would require doubling the memory
We want the exotic solution
Consider we are looking at two nodes 
cur and prev  .. in the very beginning prev is just a dummy
Got to cash next_node first thing so you would not lose it
At the bottom of the loop move curr to the saved next_node
in between

"""
class Solution(object):
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev: ListNode = None
        curr = head                                #normal traverse architecture
        while curr:                                #normal traverse architecture
            next_node = curr.next                  # have to save the next node
            curr.next = prev                       # reverse the curr node direction . make it look backward
            prev = curr                            # move prev forward
            curr = next_node                        #normal traverse architecture  -- Move forward
        return prev
            

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

[↑ Back to Top](#lec-cases)

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

[↑ Back to Top](#lec-cases)

---

## 83: Remove Duplicates from Sorted List

### Problem Description
> Given the `head` of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

- number: 83
- title: "Remove Duplicates from Sorted List"
- difficulty: 1/10
- concepts: ["Linked List"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group1\83.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

---

### Solution Idea (Pseudo-solution)
* **Approach:** One Pointer Traversal — Loop through the list and skip over next nodes that share the same value as the current node.
* **Logic:**
    1. Initialize `current` pointer to `head`.
    2. While `current` and `current.next` are not `None`:
    3. If `current.val == current.next.val`, a duplicate is found.
    4. Bypass the duplicate by setting `current.next` to `current.next.next`.
    5. Else, the values are different, so simply advance `current` to `current.next`.
    6. Return the original `head`.

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
r"""
Traverse  the list while curr and curr.next: To avoid erring 
if curr.val = curr.next.val == duplicat.
then curr.next = curr.next.next == advance to next
else .. Just advance once

"""
class Solution(object):
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        while curr and curr.next:
            if (curr.val == curr.next.val): # a duplicat is found
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

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
print("Test1: [1,1,2] -> [1,2]: success" if to_list(sol.deleteDuplicates(to_linked_list([1,1,2]))) == [1,2] else "Test1: Fail")
print('-' * 100)
print("Test2: [1,1,2,3,3] -> [1,2,3]: success" if to_list(sol.deleteDuplicates(to_linked_list([1,1,2,3,3]))) == [1,2,3] else "Test2: Fail")
print('-' * 100)
print("Test3: [] (edge case) -> []: success" if to_list(sol.deleteDuplicates(to_linked_list([]))) == [] else "Test3: Fail")
```

[↑ Back to Top](#lec-cases)

---

## 203: Remove Linked List Elements

### Problem Description
> Given the `head` of a linked list and an integer `val`, remove all the nodes of the linked list that has `Node.val == val`, and return the new head.

- number: 203
- title: "Remove Linked List Elements"
- difficulty: 1/10
- concepts: ["Linked List", "Recursion"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group1\203.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Dummy Head + Traversal — Use a dummy node pointing to the head to cleanly handle edge cases where the head itself needs to be removed.
* **Logic:**
    1. Create a `dummy` node and set its `next` to `head`.
    2. Initialize a `current` pointer starting at `dummy`.
    3. Loop while `current.next` is not `None`:
    4. If `current.next.val == val`, we need to remove it. Update `current.next` to `current.next.next` (bypassing the target node).
    5. Else, advance `current` to `current.next`.
    6. Return `dummy.next` as the new head.

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
    r"""
    If I am deleting any node in the middle. It is standard as moving a pointer.
    I think it is the first and last item that might break something
    """
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        current = dummy
        while current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next
            
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

print("Test1: [1,2,6,3,4,5,6], val=6 -> [1,2,3,4,5]: success" if to_list(sol.removeElements(to_linked_list([1,2,6,3,4,5,6]), 6)) == [1,2,3,4,5] else "Test1: Fail")
print("Test2: [7,7,7,7], val=7 -> []: success" if to_list(sol.removeElements(to_linked_list([7,7,7,7]), 7)) == [] else "Test2: Fail")
print("Test3: [] (edge case), val=1 -> []: success" if to_list(sol.removeElements(to_linked_list([]), 1)) == [] else "Test3: Fail")
```

[↑ Back to Top](#lec-cases)

---

## 141: Linked List Cycle

### Problem Description
> Given `head`, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

- number: 141
- title: "Linked List Cycle"
- difficulty: 1/10
- concepts: ["Hash Table", "Linked List", "Two Pointers"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group1\141.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def hasCycle(self, head: Optional[ListNode]) -> bool:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Floyd's Cycle-Finding Algorithm (Two Pointers: Slow and Fast)
* **Logic:**
    1. Initialize `slow` pointer to `head`, and `fast` pointer to `head`.
    2. Loop while `fast` and `fast.next` are not `None`:
    3. Advance `slow` by 1 step (`slow = slow.next`).
    4. Advance `fast` by 2 steps (`fast = fast.next.next`).
    5. If `slow == fast` at any point, they have met inside a cycle. Return `True`.
    6. If the loop ends naturally (meaning we hit a `None` pointer), there is no cycle. Return `False`.

**Complexity:**
* **Time:** $O(n)$
* **Space:** $O(1)$
---

### Solution Code
```python
from typing import Optional

class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

class Solution(object):
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        

def build_cycle_list(values: list, pos: int) -> Optional[ListNode]:
    if not values:
        return None
    
    head = ListNode(values[0])
    curr = head
    nodes = [head]
    
    # build straight list
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
        nodes.append(curr)
        
    # attach cycle back-pointer if requested
    if pos >= 0 and pos < len(nodes):
        curr.next = nodes[pos]
        
    return head

sol = Solution()
print("Test1: [3,2,0,-4], pos=1 (cycle exists) -> True: success" if sol.hasCycle(build_cycle_list([3,2,0,-4], 1)) == True else "Test1: Fail")
print("Test2: [1,2], pos=0 (cycle exists) -> True: success" if sol.hasCycle(build_cycle_list([1,2], 0)) == True else "Test2: Fail")
print("Test3: [1], pos=-1 (no cycle edge case) -> False: success" if sol.hasCycle(build_cycle_list([1], -1)) == False else "Test3: Fail")
```

[↑ Back to Top](#lec-cases)


# Solution 2 set more human
```python
def hasCycle(self, head: Optional[ListNode]) -> bool:
    seen = set()
    curr = head
    while curr:
        if curr in seen:
            return True
        seen.add(curr)
        curr = curr.next
    return False

```
---

## 142: Linked List Cycle II

### Problem Description
> Given the `head` of a linked list, return the node where the cycle begins. If there is no cycle, return `null`. There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Do NOT modify the linked list.

- number: 142
- title: "Linked List Cycle II"
- difficulty: 2/10
- concepts: ["Hash Table", "Linked List", "Two Pointers"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group1\142.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Floyd's Cycle-Finding Algorithm Phase 1 & 2 (Fast & Slow Pointers)
* **Logic:**
    1. **Phase 1 (Detect Cycle):** Use `slow` (1 step) and `fast` (2 steps) pointers starting from `head` to check if they meet. If they don't meet and reach `None`, return `None` (no cycle).
    2. **Phase 2 (Find Start):** Once they meet, initialize a new pointer `slow2` at `head`.
    3. Move both `slow` and `slow2` by 1 step at a time.
    4. The node where `slow` and `slow2` meet is the exact starting node of the cycle. Return it.

**Complexity:**
* **Time:** $O(n)$
* **Space:** $O(1)$
---

### Solution Code
```python
from typing import Optional

class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

class Solution(object):
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow2 = head
                while slow2 != slow:
                    slow2 = slow2.next
                    slow = slow.next
                return slow  # they met at the cycle entry
        return None
        

def build_cycle_list(values: list, pos: int) -> Optional[ListNode]:
    if not values:
        return None
    
    head = ListNode(values[0])
    curr = head
    nodes = [head]
    
    # build straight list
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
        nodes.append(curr)
        
    # attach cycle back-pointer if requested
    if pos >= 0 and pos < len(nodes):
        curr.next = nodes[pos]
        
    return head

# Test assertion helper for nodes
def check_node(actual, expected_val):
    if actual is None and expected_val is None:
        return True
    if actual is not None and expected_val is not None and actual.val == expected_val:
        return True
    return False

sol = Solution()
print("Test1: [3,2,0,-4], pos=1 -> Node with val 2: success" if check_node(sol.detectCycle(build_cycle_list([3,2,0,-4], 1)), 2) else "Test1: Fail")
print("Test2: [1,2], pos=0 -> Node with val 1: success" if check_node(sol.detectCycle(build_cycle_list([1,2], 0)), 1) else "Test2: Fail")
print("Test3: [1], pos=-1 -> null: success" if check_node(sol.detectCycle(build_cycle_list([1], -1)), None) else "Test3: Fail")
```

[↑ Back to Top](#lec-cases)


# set Solution . More Human

```python
def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    seen = set()
    curr = head
    while curr:
        if curr in seen:
            return curr
        seen.add(curr)
        curr = curr.next
    return None
```
---

## 876: Middle of the Linked List

### Problem Description
> Given the `head` of a singly linked list, return the middle node of the linked list. If there are two middle nodes, return the second middle node.

- number: 876
- title: "Middle of the Linked List"
- difficulty: 1/10
- concepts: ["Linked List", "Two Pointers"]
- jupyter_path: <<absolute Path... I fill it>>
- script_path: <<absolute Path... I fill it>>
- function_signature: def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Fast and Slow Pointers (Tortoise and Hare)
* **Logic:**
    1. Initialize `slow` pointer to `head`, and `fast` pointer to `head`.
    2. Loop while `fast` is not `None` and `fast.next` is not `None`:
    3. Advance `slow` by 1 step (`slow = slow.next`).
    4. Advance `fast` by 2 steps (`fast = fast.next.next`).
    5. When `fast` reaches the end of the list, `slow` will be exactly at the middle.
    6. Return `slow`.

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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
print("Test1: [1,2,3,4,5] (odd length) -> [3,4,5]: success" if to_list(sol.middleNode(to_linked_list([1,2,3,4,5]))) == [3,4,5] else "Test1: Fail")
print("Test2: [1,2,3,4,5,6] (even length) -> [4,5,6]: success" if to_list(sol.middleNode(to_linked_list([1,2,3,4,5,6]))) == [4,5,6] else "Test2: Fail")
print("Test3: [1] (edge case) -> [1]: success" if to_list(sol.middleNode(to_linked_list([1]))) == [1] else "Test3: Fail")
```

[↑ Back to Top](#lec-cases)

---
---

## 143: Reorder List

### Problem Description
> You are given the head of a singly linked-list. The list can be represented as:
> `L0 → L1 → … → Ln - 1 → Ln`
> Reorder the list to be on the following form:
> `L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …`
> You may not modify the values in the list's nodes. Only nodes themselves may be changed.

- number: 143
- title: "Reorder List"
- difficulty: 2/10
- concepts: ["Linked List", "Two Pointers", "Stack"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group1\143.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def reorderList(self, head: Optional[ListNode]) -> None:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Middle of list + Reverse second half + Merge two halves
* **Logic:**
    1. **Find Middle:** Use fast and slow pointers to find the middle of the linked list. 
    2. **Reverse 2nd Half:** Reverse the second half of the linked list starting from `slow.next`. Once reversed, cut the first half off by setting `slow.next = None`.
    3. **Merge:** Set two pointers, `p1` at the beginning of the first half (`head`) and `p2` at the beginning of the reversed second half. Alternatingly connect nodes from `p1` and `p2` to reorder the list in place.

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

r"""
    A) Half the list
    B) reverse the second half
    C) merge the two list

"""
class Solution(object):
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Guard Clause: If list is empty, has 1 node, or 2 nodes, no reorder needed or possible
        if not head or not head.next or not head.next.next:
            return
        """
        Do not return anything, modify head in-place instead.
        """
        #mid
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next        
        mid = slow
        # Now think of two lists
        list1 = head
        list2 = slow.next
        # list2 already have an Null at its tail
        #Now make slow a tail for list1
        slow.next = None
        #reversing list2
        
        prev: ListNode = None
        curr = list2                                #normal traverse architecture
        while curr:                                #normal traverse architecture
            next_node = curr.next                  # have to save the next node
            curr.next = prev                       # reverse the curr node direction . make it look backward
            prev = curr                            # move prev forward
            curr = next_node                        #normal traverse architecture  -- Move forward
        list2 = prev     
        # We'll start with list1 (you can swap if you prefer list2 first)
        head = list1
        curr1 = list1
        curr2 = list2
        
        while curr1 and curr2:
            next1 = curr1.next
            next2 = curr2.next
            
            curr1.next = curr2
            curr2.next = next1
            
            curr1 = next1
            curr2 = next2
        

def to_list(head: Optional[ListNode]) -> list:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

def to_linked_list(lst: list) -> Optional[ListNode]:
    if not lst: return None
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

sol = Solution()

# Test 1
head1 = to_linked_list([1,2,3,4])
sol.reorderList(head1)
print("Test1: [1,2,3,4] -> [1,4,2,3]: success" if to_list(head1) == [1,4,2,3] else "Test1: Fail")

# Test 2
head2 = to_linked_list([1,2,3,4,5])
sol.reorderList(head2)
print("Test2: [1,2,3,4,5] -> [1,5,2,4,3]: success" if to_list(head2) == [1,5,2,4,3] else "Test2: Fail")

# Test 3
head3 = to_linked_list([1])
sol.reorderList(head3)
print("Test3: [1] (edge case) -> [1]: success" if to_list(head3) == [1] else "Test3: Fail")

```

[↑ Back to Top](#lec-cases)

---

---
---

## 226: Invert Binary Tree

### Problem Description
> Given the `root` of a binary tree, invert the tree, and return its root.

- number: 226
- title: "Invert Binary Tree"
- difficulty: 1/10
- concepts: ["Tree", "Depth-First Search", "Binary Tree"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group1\226.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Depth-First Search (DFS) / Recursion
* **Logic:**
    1. If `root` is `None`, return `None` (base case).
    2. Swap the left and right children of the current `root` node (`root.left`, `root.right` = `root.right`, `root.left`).
    3. Recursively call `invertTree` on the new `root.left`.
    4. Recursively call `invertTree` on the new `root.right`.
    5. Return the original `root` node.

**Complexity:**
* **Time:** $O(n)$
* **Space:** $O(h)$ where $h$ is the height of the tree (for the recursion stack).
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None : return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.right)   
        self.invertTree(root.left) 
        return root

def to_level_order(root: Optional[TreeNode]) -> list:
    if not root: return []
    res = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    # Remove trailing Nones for cleaner equality checks
    while res and res[-1] is None:
        res.pop()
    return res

sol = Solution()

# Test 1
root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
inverted1 = sol.invertTree(root1)
print("Test1: [4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]: success" if to_level_order(inverted1) == [4,7,2,9,6,3,1] else "Test1: Fail")

# Test 2
root2 = TreeNode(2, TreeNode(1), TreeNode(3))
inverted2 = sol.invertTree(root2)
print("Test2: [2,1,3] -> [2,3,1]: success" if to_level_order(inverted2) == [2,3,1] else "Test2: Fail")

# Test 3
root3 = None
inverted3 = sol.invertTree(root3)
print("Test3: [] (edge case) -> []: success" if to_level_order(inverted3) == [] else "Test3: Fail")
```

[↑ Back to Top](#lec-cases)

---

## 242: Valid Anagram

### Problem Description
> Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

- number: 242
- title: "Valid Anagram"
- difficulty: 1/10
- concepts: ["Hash Table", "String", "Sorting"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group1\242.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def isAnagram(self, s: str, t: str) -> bool:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Hash Map (Frequency Counter)
* **Logic:**
    1. If the lengths of `s` and `t` are different, they cannot be anagrams (return `False`).
    2. Initialize a dictionary `counts` to store character frequencies.
    3. Iterate through characters in string `s` and increment their count in the dictionary.
    4. Iterate through characters in string `t` and decrement their count in the dictionary.
    5. Iterate through the values in the dictionary. If any value is not exactly `0`, the strings are not anagrams (return `False`).
    6. If all counts are `0`, return `True`.

**Complexity:**
* **Time:** $O(n)$ where $n$ is the length of the string.
* **Space:** $O(1)$ because the hash table is bound by a fixed number of possible characters (e.g., 26 lowercase English letters).
---

### Solution Code
```python
class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        thash = {}
        shash = {}
        for ch in s: shash[ch] = shash.get(ch,0) + 1
        for ch in t: thash[ch] = thash.get(ch,0) + 1
        return shash == thash
            

sol = Solution()
print("Test1: s='anagram', t='nagaram' -> True: success" if sol.isAnagram("anagram", "nagaram") == True else "Test1: Fail")
print("Test2: s='rat', t='car' -> False: success" if sol.isAnagram("rat", "car") == False else "Test2: Fail")
print("Test3: s='a', t='ab' (edge case length mismatch) -> False: success" if sol.isAnagram("a", "ab") == False else "Test3: Fail")

```

[↑ Back to Top](#lec-cases)

---

## 378: Kth Smallest Element in a Sorted Matrix

### Problem Description
> Given an `n x n` `matrix` where each of the rows and columns is sorted in ascending order, return the `kth` smallest element in the matrix. Note that it is the `kth` smallest element in the sorted order, not the `kth` distinct element. You must find a solution with a memory complexity better than $O(n^2)$.

- number: 378
- title: "Kth Smallest Element in a Sorted Matrix"
- difficulty: 2/10
- concepts: ["Array", "Binary Search", "Matrix", "Heap (Priority Queue)"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group1\378.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Min-Heap (Priority Queue)
* **Logic:**
    1. The matrix rows are sorted, so the smallest element overall must be in the first column.
    2. Initialize a min-heap and push the first element of each row into it, along with its row `r` and column `c` coordinates: `(matrix[r][0], r, 0)`.
    3. Loop `k` times:
    4. Pop the minimum element `(val, r, c)` from the heap. This is the current smallest element.
    5. If this is the `kth` iteration (the loop finishes), return `val`.
    6. If the popped element isn't the last column in its row (`c + 1 < len(matrix[0])`), push the next element in that same row into the heap: `(matrix[r][c+1], r, c+1)`.
    7. After `k` pops, we have our answer.

**Complexity:**
* **Time:** $O(X + k \log X)$ where $X = \min(n, k)$ for the initial heap build and popping/pushing.
* **Space:** $O(X)$ for storing up to $X$ elements in the heap.
---

### Solution Code
```python
from typing import List
class Solution(object):
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted(val for row in matrix for val in row)[k-1]
sol = Solution()
print("Test1: matrix=[[1,5,9],[10,11,13],[12,13,15]], k=8 -> 13: success" if sol.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8) == 13 else "Test1: Fail")
print("Test2: matrix=[[-5]], k=1 -> -5: success" if sol.kthSmallest([[-5]], 1) == -5 else "Test2: Fail")
print("Test3: matrix=[[1,2],[1,3]], k=2 -> 1: success" if sol.kthSmallest([[1,2],[1,3]], 2) == 1 else "Test3: Fail")
```

[↑ Back to Top](#lec-cases)


### Heap Solution
```
# later not now. heapq

```
---

## 20: Valid Parentheses

### Problem Description
> Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.
> 
> An input string is valid if:
> 1. Open brackets must be closed by the same type of brackets.
> 2. Open brackets must be closed in the correct order.
> 3. Every close bracket has a corresponding open bracket of the same type.

- number: 20
- title: "Valid Parentheses"
- difficulty: 1/10
- concepts: ["String", "Stack"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group2\20.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def isValid(self, s: str) -> bool:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Stack (LIFO matching)
* **Logic:**
    1. Initialize an empty list `stack` to keep track of opening brackets.
    2. Create a dictionary/hash map mapping closing brackets to their corresponding opening brackets: `)` -> `(`, `}` -> `{`, `]` -> `[`.
    3. Iterate through each character `char` in the string `s`.
    4. If `char` is an opening bracket (i.e., not a key in the map), push it onto the `stack`.
    5. If `char` is a closing bracket (i.e., is a key in the map):
        - If the `stack` is empty (meaning no opening bracket available to match) or the top of the stack does not match the mapped opening bracket, return `False`.
        - Otherwise, pop the matching opening bracket from the stack.
    6. After checking all characters, if the `stack` is empty, return `True` (all matched). Otherwise, return `False`.

**Complexity:**
* **Time:** $O(n)$ where $n$ is the length of the string `s`.
* **Space:** $O(n)$ for the stack in the worst case (all opening brackets).
---

### Solution Code
```python
class Solution(object):
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}   # ← reversed mapping!
        stack = []
        
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            elif ch in ')}]':
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                return False  
        return not stack
sol = Solution()
print("Test1: s='()' -> True: success" if sol.isValid("()") == True else "Test1: Fail")
print("Test2: s='()[]{}' -> True: success" if sol.isValid("()[]{}") == True else "Test2: Fail")
print("Test3: s='(]' -> False: success" if sol.isValid("(]") == False else "Test3: Fail")
print("Test4: s=']' (edge case single close) -> False: success" if sol.isValid("]") == False else "Test4: Fail")
```

[↑ Back to Top](#lec-cases)

---

## 167: Two Sum II - Input Array Is Sorted

### Problem Description
> Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.
> 
> Return the indices of the two numbers, `index1` and `index2`, **added by one** as an integer array `[index1, index2]` of length 2.
> 
> The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.
> 
> Your solution must use only constant extra space.

- number: 167
- title: "Two Sum II - Input Array Is Sorted"
- difficulty: 2/10
- concepts: ["Array", "Two Pointers", "Binary Search"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group2\167.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def twoSum(self, numbers: List[int], target: int) -> List[int]:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Two Pointers (Left and Right)
* **Logic:**
    1. Initialize a `left` pointer to index `0` and a `right` pointer to the last index `len(numbers) - 1`.
    2. Loop while `left < right`:
    3. Calculate the `current_sum = numbers[left] + numbers[right]`.
    4. If `current_sum == target`: return `[left + 1, right + 1]` (since the array is 1-indexed).
    5. If `current_sum < target`: the sum is too small, so increment the `left` pointer to increase the sum.
    6. If `current_sum > target`: the sum is too large, so decrement the `right` pointer to decrease the sum.
    7. Because a solution is guaranteed to exist, the loop will always return before bounds are an issue.

**Complexity:**
* **Time:** $O(n)$ where $n$ is the length of the array.
* **Space:** $O(1)$ since only two pointers are used.
---

### Solution Code
```python
from typing import List
"""r
Because the numbers are sorted
we will use two pointers right, left
if sum  is greater than target move right pointer towards left
if sum is smaller move left pointer to the right
when sum found.. return rigth, left
left is < right in the loop

"""
class Solution(object):
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) -1
        
        while left < right:
            if (numbers[left] + numbers[right]) == target:
                return [left+1, right+1]
            elif (numbers[left] + numbers[right]) > target:
                right -= 1
            else:
                left += 1
sol = Solution()
print("Test1: numbers=[2,7,11,15], target=9 -> [1,2]: success" if sol.twoSum([2,7,11,15], 9) == [1,2] else "Test1: Fail")
print("Test2: numbers=[2,3,4], target=6 -> [1,3]: success" if sol.twoSum([2,3,4], 6) == [1,3] else "Test2: Fail")
print("Test3: numbers=[-1,0], target=-1 (edge case negatives) -> [1,2]: success" if sol.twoSum([-1,0], -1) == [1,2] else "Test3: Fail")
```

[↑ Back to Top](#lec-cases)

---

## 53: Maximum Subarray

### Problem Description
> Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

- number: 53
- title: "Maximum Subarray"
- difficulty: 2/10
- concepts: ["Array", "Divide and Conquer", "Dynamic Programming"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group2\53.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def maxSubArray(self, nums: List[int]) -> int:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Kadane's Algorithm (Dynamic programming / Greedy)
* **Logic:**
    1. Initialize `max_so_far` and `current_max` to the first element in the array `nums[0]`.
    2. Iterate through the array starting from the second element (index 1).
    3. For each element, decide whether it's better to add the current element to the existing sequence of numbers (`current_max + num`), or to start a new sequence from the current element itself (`num`).
    4. Set `current_max = max(num, current_max + num)`.
    5. Update `max_so_far` if `current_max` is strictly greater than `max_so_far`.
    6. Return `max_so_far`.

**Complexity:**
* **Time:** $O(n)$ where $n$ is the length of the array.
* **Space:** $O(1)$ since only variable tracking is used.
---

### Solution Code
```python
from typing import List

class Solution(object):
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far , current_max = nums[0], nums[0]
        for i in range(1, len(nums)):
            if (current_max + nums[i]) > nums[i] :           # keeping the current window condition is about 
                                                            #if adding the current number to the current max
                                                          # is actually bigger than the current number itself
                current_max += nums[i]
            else:
                current_max =  nums[i]
            max_so_far = max(max_so_far, current_max)
        return max_so_far


sol = Solution()
print("Test1: nums=[-2,1,-3,4,-1,2,1,-5,4] -> 6: success" if sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6 else "Test1: Fail")
print("Test2: nums=[1] -> 1: success" if sol.maxSubArray([1]) == 1 else "Test2: Fail")
print("Test3: nums=[5,4,-1,7,8] -> 23: success" if sol.maxSubArray([5,4,-1,7,8]) == 23 else "Test3: Fail")
```

[↑ Back to Top](#lec-cases)

---

## 102: Binary Tree Level Order Traversal

### Problem Description
> Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

- number: 102
- title: "Binary Tree Level Order Traversal"
- difficulty: 2/10
- concepts: ["Tree", "Breadth-First Search", "Binary Tree"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group2\102.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Breadth-First Search (BFS) using a Queue
* **Logic:**
    1. If the `root` is None, return an empty list `[]`.
    2. Initialize a queue (e.g. `collections.deque`) and append the `root`.
    3. Initialize a `result` list to store the levels.
    4. While the queue is not empty:
    5.   Get the current length of the queue (`level_size`). This is the number of nodes at the current level.
    6.   Initialize an empty list `current_level` to store values of this level.
    7.   Loop `level_size` times:
    8.     Pop a node from the left of the queue.
    9.     Append its value to `current_level`.
    10.    If the node has a left child, append it to the queue.
    11.    If the node has a right child, append it to the queue.
    12.  Append `current_level` to the `result` list.
    13. Return `result`.

**Complexity:**
* **Time:** $O(n)$ where $n$ is the number of nodes in the tree.
* **Space:** $O(n)$ to store the nodes in the queue, which can contain at most $n/2$ nodes at the bottom level.
---

### Solution Code
```python

from typing import List, Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []
        q = collections.deque([root])
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level)
        return res

# Helper function to build a tree from list for testing
def build_tree(values):
    if not values: return None
    root = TreeNode(values[0])
    queue = collections.deque([root])
    i = 1
    while queue and i < len(values):
        current = queue.popleft()
        if values[i] is None:
            pass
        else:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values):
            if values[i] is None:
                pass
            else:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1
    return root

sol = Solution()
tree1 = build_tree([3,9,20,None,None,15,7])
print("Test1: root=[3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]: success" if sol.levelOrder(tree1) == [[3],[9,20],[15,7]] else "Test1: Fail")
tree2 = build_tree([1])
print("Test2: root=[1] -> [[1]]: success" if sol.levelOrder(tree2) == [[1]] else "Test2: Fail")
tree3 = build_tree([])
print("Test3: root=[] -> []: success" if sol.levelOrder(tree3) == [] else "Test3: Fail")


```

[↑ Back to Top](#lec-cases)

---

## 155: Min Stack

### Problem Description
> Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
>
> Implement the `MinStack` class:
> - `MinStack()` initializes the stack object.
> - `void push(int val)` pushes the element `val` onto the stack.
> - `void pop()` removes the element on the top of the stack.
> - `int top()` gets the top element of the stack.
> - `int getMin()` retrieves the minimum element in the stack.
>
> You must implement a solution with `O(1)` time complexity for each function.

- number: 155
- title: "Min Stack"
- difficulty: 2/10
- concepts: ["Stack", "Design"]
- jupyter_path: <<absolute Path... I fill it>>
- script_path: <<absolute Path... I fill it>>
- function_signature: class MinStack:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Two Stacks (or Stack of Tuples)
* **Logic:**
    1. A standard stack does not naturally track the historic minimum element efficiently over push/pop operations.
    2. To achieve $O(1)$ for `getMin()`, we can store pairs of `(value, current_minimum)` in our stack instead of just `value`.
    3. `__init__`: Initialize an empty list `stack`.
    4. `push(val)`: If the stack is empty, the `current_minimum` is `val`. If not empty, `current_minimum` is `min(val, stack[-1][1])`. Push `(val, current_minimum)`.
    5. `pop()`: Standard list pop.
    6. `top()`: Return `stack[-1][0]`.
    7. `getMin()`: Return `stack[-1][1]`.

**Complexity:**
* **Time:** $O(1)$ for all operations natively.
* **Space:** $O(n)$ where $n$ is the number of elements in the stack.

---

### Solution Code
```python
from math import inf
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.cur_min = inf

    def push(self, val: int) -> None:
        self.cur_min = min(self.cur_min, val)
        self.stack.append(val)
        self.min_stack.append(self.cur_min)
        
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print("Test1: getMin() -> -3: success" if minStack.getMin() == -3 else "Test1: Fail")
minStack.pop()
print("Test2: top() -> 0: success" if minStack.top() == 0 else "Test2: Fail")
print("Test3: getMin() -> -2: success" if minStack.getMin() == -2 else "Test3: Fail")

```

[↑ Back to Top](#lec-cases)

---

## 198: House Robber

### Problem Description
> You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
>
> Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

- number: 198
- title: "House Robber"
- difficulty: 2/10
- concepts: ["Array", "Dynamic Programming"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group2\198.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def rob(self, nums: List[int]) -> int:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Dynamic Programming (Bottom-Up)
* **Logic:**
    1. If the list of houses is empty, return 0.
    2. If there's only one house, return its value.
    3. The maximum money at any given house `i` depends on the maximum between (robbing house `i` + maximum money up to house `i-2`) and (not robbing house `i` + maximum money up to house `i-1`).
    4. We only need to keep track of the max money from the previous two steps to compute the current step, which optimizes space to $O(1)$.
    5. Initialize two variables, `rob1 = 0` and `rob2 = 0`.
    6. Iterate through each `num` in `nums`. Compute the new max: `temp = max(rob1 + num, rob2)`.
    7. Update `rob1 = rob2` and `rob2 = temp`.
    8. Return `rob2`.

**Complexity:**
* **Time:** $O(n)$ where $n$ is the number of houses.
* **Space:** $O(1)$ since only two variables are used.
---

### Solution Code
```python
#LEC 198
from typing import List

class Solution(object):
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        #The maximum money at any given house i depends on the maximum between 
        #(robbing house i + maximum money up to house i-2) and (not robbing house i + maximum money up to house i-1).
        
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-1], nums[i-2] + nums[i])
        return nums[-1]
sol = Solution()
print("Test1: nums=[1,2,3,1] -> 4: success" if sol.rob([1,2,3,1]) == 4 else "Test1: Fail")
print("Test2: nums=[2,7,9,3,1] -> 12: success" if sol.rob([2,7,9,3,1]) == 12 else "Test2: Fail")
print("Test3: nums=[0] -> 0: success" if sol.rob([0]) == 0 else "Test3: Fail")
```

[↑ Back to Top](#lec-cases)

---

## 674: Longest Continuous Increasing Subsequence

### Problem Description
> Given an unsorted array of integers `nums`, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.
>
> A continuous increasing subsequence is defined by two indices `l` and `r` (`l < r`) such that it is `[nums[l], nums[l + 1], ..., nums[r - 1], nums[r]]` and for each `l <= i < r`, `nums[i] < nums[i + 1]`.

- number: 674
- title: "Longest Continuous Increasing Subsequence"
- difficulty: 1/10
- concepts: ["Array"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group2\674.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def findLengthOfLCIS(self, nums: List[int]) -> int:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Single Pass (Greedy / Sliding Window)
* **Logic:**
    1. If the array is empty, return 0. (Though constraints usually say $\ge 1$).
    2. Initialize `max_len = 1` and `current_len = 1`.
    3. Loop through the array from the second element (index `i = 1`) to the end.
    4. If the current element is greater than the previous element (`nums[i] > nums[i - 1]`), increment `current_len`.
    5. Update `max_len = max(max_len, current_len)`.
    6. If the current element is not strictly greater, the continuous increasing sequence is broken. Reset `current_len = 1`.
    7. Return `max_len`.

**Complexity:**
* **Time:** $O(n)$ where $n$ is the length of the array, as we only need a single pass.
* **Space:** $O(1)$ since only variable counters are used.
---

### Solution Code
```python
# LEC 647
from typing import List

class Solution(object):
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums: return 0
        max_len, current_len = 1 , 1
        for i in range (1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 1
        return max_len
sol = Solution()
print("Test1: nums=[1,3,5,4,7] -> 3: success" if sol.findLengthOfLCIS([1,3,5,4,7]) == 3 else "Test1: Fail")
print("Test2: nums=[2,2,2,2,2] -> 1: success" if sol.findLengthOfLCIS([2,2,2,2,2]) == 1 else "Test2: Fail")
print("Test3: nums=[1] -> 1: success" if sol.findLengthOfLCIS([1]) == 1 else "Test3: Fail")
```

[↑ Back to Top](#lec-cases)

---

## 937: Reorder Data in Log Files

### Problem Description
> You are given an array of `logs`. Each log is a space-delimited string of words, where the first word is the identifier.
>
> There are two types of logs:
> - **Letter-logs**: All words (except the identifier) consist of lowercase English letters.
> - **Digit-logs**: All words (except the identifier) consist of digits.
>
> Reorder these logs so that:
> 1. The letter-logs come before all digit-logs.
> 2. The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
> 3. The digit-logs maintain their relative ordering.
>
> Return the final order of the logs.

- number: 937
- title: "Reorder Data in Log Files"
- difficulty: 2/10
- concepts: ["Array", "String", "Sorting"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group2\937.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def reorderLogFiles(self, logs: List[str]) -> List[str]:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Custom Sorting using Tuples
* **Logic:**
    1. Separate the logs into two lists: `let_logs` and `dig_logs`.
    2. Iterate through each `log` in `logs`.
    3. Split each `log` into two parts maximally: the `identifier` and the `content`.
    4. Check if the first character of the `content` is a digit or a letter.
    5. If it's a digit, append the entire `log` to `dig_logs`.
    6. If it's a letter, append the entire `log` to `let_logs`.
    7. Sort the `let_logs` list.
       * Python's `.sort()` allows a custom `key` function.
       * We want to sort primarily by the `content`, and secondarily by the `identifier`.
       * The key should return a tuple: `(content, identifier)`.
    8. Combine the sorted `let_logs` and the original `dig_logs` (which maintains relative order) and return the combined list.

**Complexity:**
* **Time:** $O(M \log M)$ where $M$ is the number of characters across all logs, because string comparisons take an amount of time proportional to the length of the string.
* **Space:** $O(M)$ to store the separated lists of logs.
---

### Solution Code
```python
#LEC 937
from typing import List

class Solution(object):
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let_logs = []
        dig_logs = []
        for log in logs:
            id, content = log.split(' ',1 )
            if content[0].isdigit():
                dig_logs.append(log)
            else:
                let_logs.append(log)
        let_logs.sort(key=lambda log: (
                log.split(' ', 1)[1],   # primary: content
                log.split(' ', 1)[0]    # secondary: identifier
                ))
        return let_logs+dig_logs
            
                
sol = Solution()
print("Test1: logs=['dig1 8 1 5 1','let1 art can','dig2 3 6','let2 own kit dig','let3 art zero'] -> ['let1 art can','let3 art zero','let2 own kit dig','dig1 8 1 5 1','dig2 3 6']: success" if sol.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]) == ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"] else "Test1: Fail")
print("Test2: logs=['a1 9 2 3 1','g1 act car','zo4 4 7','ab1 off key dog','a8 act zoo'] -> ['g1 act car','a8 act zoo','ab1 off key dog','a1 9 2 3 1','zo4 4 7']: success" if sol.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]) == ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"] else "Test2: Fail")
```

### Solution Code2 More efficient
```python
#LEC 937
from typing import List
class Solution(object):
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let_logs = []
        dig_logs = []
        for log in logs:
            log_id, content = log.split(' ', 1)
            if content[0].isdigit():
                dig_logs.append(log)
            else:
                let_logs.append((log, log_id, content))  # cache the split
                
        let_logs.sort(key=lambda x: (x[2], x[1]))  # sort by content then id
        
        return [log for log, _, _ in let_logs] + dig_logs
sol = Solution()
print("Test1: logs=['dig1 8 1 5 1','let1 art can','dig2 3 6','let2 own kit dig','let3 art zero'] -> ['let1 art can','let3 art zero','let2 own kit dig','dig1 8 1 5 1','dig2 3 6']: success" if sol.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]) == ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"] else "Test1: Fail")
print("Test2: logs=['a1 9 2 3 1','g1 act car','zo4 4 7','ab1 off key dog','a8 act zoo'] -> ['g1 act car','a8 act zoo','ab1 off key dog','a1 9 2 3 1','zo4 4 7']: success" if sol.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]) == ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"] else "Test2: Fail")
```

[↑ Back to Top](#lec-cases)

[↑ Back to Top](#lec-cases)

---

## 2043: Simple Bank System

### Problem Description
> You have been tasked with writing a program for a popular bank that will automate all its incoming transactions (transfer, deposit, and withdraw). The bank has `n` accounts numbered from `1` to `n`. The initial balance of each account is stored in a 0-indexed integer array `balance`, with the `(i + 1)th` account having an initial balance of `balance[i]`.
>
> Execute all the valid transactions. A transaction is valid if:
> - The given account number(s) are between `1` and `n`, and
> - The amount of money withdrawn or transferred from is less than or equal to the balance of the account.
>
> Implement the `Bank` class:
> - `Bank(long[] balance)` Initializes the object with the 0-indexed integer array `balance`.
> - `boolean transfer(int account1, int account2, long money)` Transfers `money` dollars from the account numbered `account1` to the account numbered `account2`. Return `true` if the transaction was successful, `false` otherwise.
> - `boolean deposit(int account, long money)` Deposit `money` dollars into the account numbered `account`. Return `true` if the transaction was successful, `false` otherwise.
> - `boolean withdraw(int account, long money)` Withdraw `money` dollars from the account numbered `account`. Return `true` if the transaction was successful, `false` otherwise.

- number: 2043
- title: "Simple Bank System"
- difficulty: 2/10
- concepts: ["Array", "Design", "Simulation"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group2\2043.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: class Bank:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Array / Object-Oriented Simulation
* **Logic:**
    1. `__init__`: Store the 0-indexed `balance` array as a class variable. We can optionally prepend it with a dummy value (like `0`) so it becomes 1-indexed to match account numbers directly, or just subtract `1` from every account argument in the functions.
    2. Helper `is_valid(account)`: Create a helper function to verify if an account is strictly between `1` and `n` (or length of balance).
    3. `transfer(acc1, acc2, money)`: Check `is_valid(acc1)` and `is_valid(acc2)`. If valid, check if `balance[acc1] >= money`. If so, `-= money` from `acc1` and `+= money` to `acc2` and return `True`. Otherwise return `False`.
    4. `deposit(acc, money)`: Check `is_valid(acc)`. If valid, `+= money` to `acc` and return `True`. Otherwise return `False`.
    5. `withdraw(acc, money)`: Check `is_valid(acc)`. If valid, check if `balance[acc] >= money`. If so, `-= money` from `acc` and return `True`. Otherwise return `False`.

**Complexity:**
* **Time:** $O(1)$ per operation.
* **Space:** $O(n)$ to store the copy of the `balance` array within the class instance.
---

### Solution Code
```python
#LEC 2043
from typing import List

class Bank:
    def __init__(self, balance: List[int]):
        self.balance = [0]                #prepend with 0 for dummy account. from now one you can work safely
        self.balance += balance           # on a 1 base array
        
    def _is_valid (self, account: int)-> bool:
        return 1 <= account <= (len(self.balance) -1)
        
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self._is_valid(account1) and self._is_valid(account2):
            if self.withdraw(account1, money):
                self.deposit(account2, money)
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self._is_valid(account):
            self.balance[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self._is_valid(account) and self.balance[account] >= money:
            self.balance[account] -= money
            return True
        return False


bank = Bank([10, 100, 20, 50, 30])
print("Test1: withdraw(3, 10) -> True: success" if bank.withdraw(3, 10) == True else "Test1: Fail")
print("Test2: transfer(5, 1, 20) -> True: success" if bank.transfer(5, 1, 20) == True else "Test2: Fail")
print("Test3: deposit(5, 20) -> True: success" if bank.deposit(5, 20) == True else "Test3: Fail")
print("Test4: transfer(3, 4, 15) -> False: success" if bank.transfer(3, 4, 15) == False else "Test4: Fail")
print("Test5: withdraw(10, 50) -> False: success" if bank.withdraw(10, 50) == False else "Test5: Fail")
```

[↑ Back to Top](#lec-cases)

---

## 496: Next Greater Element I

### Problem Description
> The next greater element of some element `x` in an array is the first greater element that is to the right of `x` in the same array.
>
> You are given two distinct 0-indexed integer arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.
>
> For each `0 <= i < nums1.length`, find the index `j` such that `nums1[i] == nums2[j]` and determine the next greater element of `nums2[j]` in `nums2`. If there is no next greater element, then the answer for this query is `-1`.
>
> Return an array `ans` of length `nums1.length` such that `ans[i]` is the next greater element as described above.

- number: 496
- title: "Next Greater Element I"
- difficulty: 1/10
- concepts: ["Array", "Hash Table", "Monotonic Stack"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group2\496.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Monotonic Stack + Hash Map
* **Logic:**
    1. We want to find the next greater element for every element in `nums2` efficiently, and then instantly look up the answers for elements in `nums1`.
    2. Initialize a hash map `next_greater` to store answers: `{element: next_greater_element}`.
    3. Initialize an empty `stack` (monotonic decreasing).
    4. Iterate through each `num` in `nums2`:
    5.   While the `stack` is not empty and the current `num` is strictly greater than the element at the top of the `stack` (`stack[-1]`):
    6.     The current `num` is the "next greater element" for the top element.
    7.     Pop the top element off the `stack` and add it to the hash map: `next_greater[popped_element] = num`.
    8.   Push the current `num` onto the `stack`.
    9. After iterating through all of `nums2`, any elements left in the `stack` do not have a next greater element. We can iterate through them and map them to `-1`, or just use `-1` as the default value when looking up the hash map.
    10. Finally, construct the answer array by iterating through `nums1` and looking up their next greater element in the `next_greater` map (defaulting to `-1`).

**Complexity:**
* **Time:** $O(n + m)$ where $n$ is length of `nums1` and $m$ is length of `nums2`. Elements in `nums2` are pushed and popped at most once.
* **Space:** $O(m)$ to store the stack and the map for `nums2`.
---

### Solution Code
```python
#LEC 496
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}           # maps number → its next greater in nums2
        
        for num in nums2:
            # Pop all elements smaller than current num
            while stack and num > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = num
            
            stack.append(num)
        
        # All remaining elements in stack have no greater element
        while stack:
            next_greater[stack.pop()] = -1
        
        # Build result for nums1
        return [next_greater.get(num, -1) for num in nums1]
        

sol = Solution()
print("Test1: nums1=[4,1,2], nums2=[1,3,4,2] -> [-1,3,-1]: success" if sol.nextGreaterElement([4,1,2], [1,3,4,2]) == [-1,3,-1] else "Test1: Fail")
print("Test2: nums1=[2,4], nums2=[1,2,3,4] -> [3,-1]: success" if sol.nextGreaterElement([2,4], [1,2,3,4]) == [3,-1] else "Test2: Fail")
```

[↑ Back to Top](#lec-cases)

---

## 49: Group Anagrams

### Problem Description
> Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.
>
> An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

- number: 49
- title: "Group Anagrams"
- difficulty: 2/10
- concepts: ["Array", "Hash Table", "String", "Sorting"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group2\49.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Hash Map with Sorted String as Key (or Character Count as Key)
* **Logic:**
    1. Two strings are anagrams if and only if their sorted strings are exactly the same (or their character counts are the same).
    2. We can use a hash map `anagrams` mapping a string representation to a list of original strings.
    3. Iterate through each string `s` in `strs`.
    4. Sort the characters of `s` and join them back to form a sorted string (e.g., "eat" -> "aet").
    5. Check if this sorted string exists as a key in `anagrams`.
    6. If it does not exist, create it with an empty list.
    7. Append the original string `s` to the list corresponding to the sorted string key.
    8. Once all strings are processed, return the values of the hash map as a list of lists.
    *(Alternatively, use a tuple of 26 character counts as the key for $O(NK)$ instead of $O(NK \log K)$)*

**Complexity:**
* **Time:** $O(N \cdot K \log K)$ where $N$ is the number of strings and $K$ is the maximum length of a string, due to sorting each string.
* **Space:** $O(N \cdot K)$ to store the strings in the hash map.
---

### Solution Code
```python
import collections
from typing import List
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        data: defaultdict[str, list[str]] = defaultdict(list)
        for s in strs:
            data[''.join(sorted(s))].append(s)
        return list(data.values())
sol = Solution()
print("Test1: strs=['eat','tea','tan','ate','nat','bat'] -> [['bat'],['nat','tan'],['ate','eat','tea']]: success" if sorted([sorted(group) for group in sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])]) == sorted([sorted(group) for group in [["bat"],["nat","tan"],["ate","eat","tea"]]]) else "Test1: Fail")
print("Test2: strs=[''] -> [['']]: success" if sol.groupAnagrams([""]) == [[""]] else "Test2: Fail")
print("Test3: strs=['a'] -> [['a']]: success" if sol.groupAnagrams(["a"]) == [["a"]] else "Test3: Fail")
```

[↑ Back to Top](#lec-cases)

---

## 73: Set Matrix Zeroes

### Problem Description
> Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.
>
> You must do it in place.

- number: 73
- title: "Set Matrix Zeroes"
- difficulty: 2/10
- concepts: ["Array", "Hash Table", "Matrix"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group2\73.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def setZeroes(self, matrix: List[List[int]]) -> None:

---

### Solution Idea (Pseudo-solution)
* **Approach:** In-place State Tracking (using first row and first column)
* **Logic:**
    1. The naive approach is $O(M \cdot N)$ space, keeping a full copy of the matrix. We can improve this to $O(M+N)$ by keeping track of which rows/cols need to be zeroed in two separate arrays.
    2. We can optimize this to $O(1)$ space by using the first row and first column of the matrix itself to store the zero states.
    3. Iterate through the matrix. If `matrix[r][c] == 0`, mark the start of its row `matrix[r][0] = 0` and the start of its column `matrix[0][c] = 0`.
    4. *Crucial Detail:* The element `matrix[0][0]` overlaps for both the first row and first column. We need an extra variable `rowZero = False` to track if the *first row* needs to be zeroed, while `matrix[0][0]` will solely track if the *first column* needs to be zeroed.
    5. Second pass: Iterate from `r = 1` to `M-1` and `c = 1` to `N-1`. If `matrix[r][0] == 0` or `matrix[0][c] == 0`, set `matrix[r][c] = 0`.
    6. Third pass: If `matrix[0][0] == 0`, set the entire first column to `0`.
    7. Fourth pass: If `rowZero == True`, set the entire first row to `0`.

**Complexity:**
* **Time:** $O(m \times n)$ to traverse the matrix a couple of times.
* **Space:** $O(1)$ strictly in-place, relying only on the matrix structure itself and one boolean variable.
---

### Solution Code
```python
#LEC 73
from typing import List

class Solution(object):
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowsMarker: List[int] = [1]* len(matrix)
        colsMarker: List[int] = [1]* len(matrix[0])
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rowsMarker[r] = 0
                    colsMarker[c] = 0
        for i, val in enumerate(rowsMarker):
            if val == 0:
                for c in range(len(matrix[0])):
                    matrix[i][c] = 0
                    
        for i, val in enumerate(colsMarker):
            if val == 0:
                for r in range(len(matrix)):
                    matrix[r][i] = 0        
        return


sol = Solution()

# Test 1
matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
sol.setZeroes(matrix1)
print("Test1: matrix=[[1,1,1],[1,0,1],[1,1,1]] -> [[1,0,1],[0,0,0],[1,0,1]]: success" if matrix1 == [[1,0,1],[0,0,0],[1,0,1]] else "Test1: Fail")

# Test 2
matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
sol.setZeroes(matrix2)
print("Test2: matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]] -> [[0,0,0,0],[0,4,5,0],[0,3,1,0]]: success" if matrix2 == [[0,0,0,0],[0,4,5,0],[0,3,1,0]] else "Test2: Fail")
```

[↑ Back to Top](#lec-cases)

[↑ Back to Top](#lec-cases)

---

## 74: Search a 2D Matrix

### Problem Description
> You are given an `m x n` integer matrix `matrix` with the following two properties:
> - Each row is sorted in non-decreasing order.
> - The first integer of each row is greater than the last integer of the previous row.
>
> Given an integer `target`, return `true` if `target` is in `matrix` or `false` otherwise.
>
> You must write a solution in `O(log(m * n))` time complexity.

- number: 74
- title: "Search a 2D Matrix"
- difficulty: 2/10
- concepts: ["Array", "Binary Search", "Matrix"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group2\74.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Binary Search (treating the 2D matrix as a 1D array)
* **Logic:**
    1. Since the matrix is strictly sorted, we can conceptually flatten it into a 1D array of length `m * n`.
    2. We can perform a standard binary search on this conceptual 1D array.
    3. Initialize `left = 0` and `right = m * n - 1`.
    4. While `left <= right`:
        * Calculate `mid = left + (right - left) // 2`.
        * Map the 1D index `mid` back to 2D coordinates: `r = mid // n` and `c = mid % n`.
        * If `matrix[r][c] == target`, return `True`.
        * If `matrix[r][c] < target`, shrink the search space to the right: `left = mid + 1`.
        * If `matrix[r][c] > target`, shrink the search space to the left: `right = mid - 1`.
    5. If the loop completes and we haven't found the target, return `False`.

**Complexity:**
* **Time:** $O(\log(m \cdot n))$ because we perform standard binary search over `m * n` elements.
* **Space:** $O(1)$ since we are only using a few pointers and variables.
---

### Solution Code
```python
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        rows, cols = len(matrix), len(matrix[0])
        n = rows * cols
        left, right = 0, n - 1
        
        def trans(offset: int) -> tuple[int, int]:
            return (offset // cols, offset % cols)
        
        while left <= right:                  # ← safer condition (includes equality)
            mid = left + (right - left) // 2  # ← avoids potential overflow (good habit)
            r, c = trans(mid)
            mid_val = matrix[r][c]
            
            if mid_val == target:
                return True
            elif target > mid_val:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
                
            


sol = Solution()
print("Test1: matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3 -> True: success" if sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True else "Test1: Fail")
print("Test2: matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=13 -> False: success" if sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) == False else "Test2: Fail")
```

[↑ Back to Top](#lec-cases)

[↑ Back to Top](#lec-cases)

---

## 128: Longest Consecutive Sequence

### Problem Description
> Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.
>
> You must write an algorithm that runs in `O(n)` time.

- number: 128
- title: "Longest Consecutive Sequence"
- difficulty: 2/10
- concepts: ["Array", "Hash Table", "Union Find"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group2\128.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def longestConsecutive(self, nums: List[int]) -> int:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Hash Set (or Union Find)
* **Logic:**
    1. To achieve $O(n)$ time complexity, we cannot sort the array first ($O(n \log n)$). Instead, we can use a Hash Set for $O(1)$ lookups.
    2. Convert `nums` into a `set` named `num_set`.
    3. Initialize a variable `longest_streak = 0`.
    4. Iterate through each `num` in `num_set`.
    5. **Crucial Optimization:** We only want to start counting a sequence from the *beginning* of that sequence. We know a number is the start of a sequence if `num - 1` is *not* in `num_set`.
    6. If `num` is a start:
        * Initialize `current_num = num` and `current_streak = 1`.
        * While `current_num + 1` is in `num_set`, increment both `current_num` and `current_streak`.
        * Update `longest_streak = max(longest_streak, current_streak)`.
    7. Return `longest_streak`.

**Complexity:**
* **Time:** $O(n)$ because we only iterate through the while loop when we find the *start* of a sequence, meaning each number in the array is visited at most twice (once in the outer loop, once in the inner while loop).
* **Space:** $O(n)$ to store the set.
---

### Solution Code
```python
#LEC 128
from typing import List

class Solution(object):
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums:num_set.add(num)
        current_max:int = 0
        max_cons = 0
        for num in nums:
            if (num-1) not in num_set:
                #start of a sequence
                current_streak = 1
                anum = num + 1
                while anum in num_set:
                    current_streak += 1
                    anum += 1
                max_cons = max(max_cons, current_streak)
        return max_cons
                    

sol = Solution()
print("Test1: nums=[100,4,200,1,3,2] -> 4: success" if sol.longestConsecutive([100,4,200,1,3,2]) == 4 else "Test1: Fail")
print("Test2: nums=[0,3,7,2,5,8,4,6,0,1] -> 9: success" if sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9 else "Test2: Fail")
```

[↑ Back to Top](#lec-cases)

[↑ Back to Top](#lec-cases)

---

## 3: Longest Substring Without Repeating Characters

### Problem Description
> Given a string `s`, find the length of the longest substring without repeating characters.

- number: 3
- title: "Longest Substring Without Repeating Characters"
- difficulty: 2/10
- concepts: ["Hash Table", "String", "Sliding Window"]
- jupyter_path: "C:\DataMajor\practice\001Study\playground\group3\LEC3.ipynb"
- script_path: <<absolute Path... I fill it>>
- function_signature: def lengthOfLongestSubstring(self, s: str) -> int:

---

### Solution Idea (Pseudo-solution)
* **Approach:** Sliding Window (with Hash Map/Set for character tracking)
* **Logic:**
    1. Initialize a `left` pointer to `0`, and a variable `max_length` to `0`.
    2. Initialize a dictionary `char_index_map` to store the most recent index of each character.
    3. Iterate through the string `s` with a `right` pointer (from `0` to `len(s)-1`).
    4. If the character `s[right]` is already in `char_index_map` AND its index is $\ge$ `left`, it means we've found a repeat within our current window.
    5. We must shrink the window by moving `left` to `char_index_map[s[right]] + 1`.
    6. Update `char_index_map[s[right]] = right`.
    7. Update `max_length = max(max_length, right - left + 1)`.
    8. Return `max_length`.

**Complexity:**
* **Time:** $O(n)$ where $n$ is the length of the string `s`.
* **Space:** $O(\min(m, n))$ where $m$ is the size of the character set (e.g., 128 or 256 for ASCII).
---

### Solution Code
```python
#LEC03
class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestsub: int = 0
        seen= set()
        left, right = 0, 0
        for right,ch in enumerate(s):
            #if it is a repeating character
            if ch in seen:
                while seen and ( ch in seen):
                    seen.discard(s[left])
                    left+=1 
            seen.add(ch)
            longestsub = max(longestsub, right - left + 1)
        return longestsub
sol = Solution()
print("Test1: s='abcabcbb' -> 3: success" if sol.lengthOfLongestSubstring("abcabcbb") == 3 else "Test1: Fail")
print("Test2: s='bbbbb' -> 1: success" if sol.lengthOfLongestSubstring("bbbbb") == 1 else "Test2: Fail")
print("Test3: s='pwwkew' -> 3: success" if sol.lengthOfLongestSubstring("pwwkew") == 3 else "Test3: Fail")
print("Test4: s='' -> 0: success" if sol.lengthOfLongestSubstring("") == 0 else "Test4: Fail")
```

[↑ Back to Top](#lec-cases)

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

[↑ Back to Top](#lec-cases)


