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
