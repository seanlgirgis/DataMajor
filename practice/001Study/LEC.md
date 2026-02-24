| # | Problem Title | Concepts | Difficulty | Links |
| :--- | :--- | :--- | :--- | :--- |
| **217** | [Contains Duplicate](#217-contains-duplicate) | `Array`, `Hash Set` | 1/10 | [Jupyter](./217.ipynb) / [Script](./217.py) |
| **704** | [Binary Search](#704-binary-search) | `Binary Search`, `Array` | 3/10 | [Jupyter](./704.ipynb) / [Script](./704.py) |









---
# LEC Cases

---


## 217: Contains Duplicate

### Problem Description
> Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

##### number: 217
##### title: "Contains Duplicate"
##### difficulty: 1/10
##### concepts: ["Array", "Hash Set", "Lookup"]
##### jupyter_path: ".C:\DataMajor\practice\001Study\playground\group1\217.ipynb"
##### script_path: "C:\DataMajor\practice\001Study\playground\group1\217.py"

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
def containsDuplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False
```

---
# Template

---
number: [ID_NUMBER]
title: "[PROBLEM_TITLE]"
difficulty: [1-10]/10
concepts: ["Concept 1", "Concept 2", "Concept 3"]
jupyter_path: "[PATH_TO_JUPYTER_NOTEBOOK]"
script_path: "[PATH_TO_SCRIPT]"
---

## [ID_NUMBER]: [PROBLEM_TITLE]

### Problem Description
> [Paste the description from LeetCode here.]

section 1  
section 2  
section 3  

---

### Solution Idea (Pseudo-solution)
* **Approach:** [e.g., Two Pointers, Sliding Window, Greedy]
* **Logic:**
    1. [Step 1]
    2. [Step 2]
    3. [Step 3]

**Complexity:**
* **Time:** $O(\dots)$
* **Space:** $O(\dots)$

---

### Solution Code
```python
# [Insert Python Code Here]
def solution():
    pass
```