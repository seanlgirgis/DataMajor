| # | Problem Title | Concepts | Difficulty | 
| :--- | :--- | :--- | :--- | 
| **1** | [Two Sum](#1-two-sum) | `Array`, `Hash Table` | 2/10 |
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
> Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

- number: 1
- title: "Two Sum"
- difficulty: 2/10
- concepts: ["Array", "Hash Table"]
- jupyter_path: <<absolute Path... I fill it>>
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

<<I fill the code here>>

```

---
# Template



---


## 217: Contains Duplicate

### Problem Description
> <<Description of the problem>>

- number: <<number>>
- title: "<<Title>>"
- difficulty: <<difficulty>>
- concepts: ["<<Concept 1>>", "<<Concept 2>>", "<<Concept 3>>"]
- jupyter_path: <<absolute Path... I fill it>>
- script_path: <<absolute Path... I fill it>>
- function_signature: <<suggested by agent always>>:

---

### Solution Idea (Pseudo-solution)
* **Approach:** <<approach goes here>>
* **Logic:**
    1. <<Logic goes here>>
    2. <<Logic goes here>>
    3. <<Logic goes here>>
    4. <<Logic goes here>>
    5. <<Logic goes here>>

**Complexity:**
* **Time:** <<Time Complexity>>
* **Space:** <<Space Complexity>>

---

### Solution Code
```python

<<I fill the code here >>

    
```
