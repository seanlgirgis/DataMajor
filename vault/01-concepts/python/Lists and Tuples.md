---
type: concept
tags: [python, fundamentals, lists, tuples]
difficulty: Beginner
domain: python
created: 2026-02-18
---

# Lists and Tuples

**One-liner**: Lists are mutable, ordered collections of items, while Tuples are immutable ordered collections often used for fixed data.

## Mental Model
-   **List (`[]`)**: A **whiteboard**. You can write things on it, erase them, rearrange them, or wipe it clean. It's designed to be changed.
-   **Tuple (`()`)**: A **stone tablet**. Once engraved, it cannot be changed. If you need it different, you have to carve a brand new tablet.

## Quick Facts
-   **Lists (Mutable)**:
    -   `append(x)`: Add to end.
    -   `insert(i, x)`: Add at index.
    -   `pop()`: Remove/return last item.
    -   `remove(x)`: Remove first occurrence of value.
    -   `sort()` vs `sorted()`: `sort()` modifies in-place (returns `None`), `sorted()` returns a new list.
    -   `extend(seq)`: Adds all elements of seq to list.
-   **Tuples (Immutable)**:
    -   Syntax: `(1, 2, 3)`.
    -   Faster than lists, hashable (can be dict keys).
    -   **Unpacking**: `x, y = (1, 2)`.
-   **Indexing**: Same as strings (`[0]`, `[-1]`, slicing `[::]`).

## Code Example
```python
# List Mutation
fruits = ["apple", "banana"]
fruits.append("cherry")      # ["apple", "banana", "cherry"]
fruits[0] = "mango"          # ["mango", "banana", "cherry"]

# Sorting
nums = [3, 1, 2]
sorted_nums = sorted(nums)   # [1, 2, 3], nums remains [3, 1, 2]
nums.sort()                  # nums becomes [1, 2, 3], returns None

# Tuple Unpacking & Swapping
point = (10, 20)
x, y = point                 # x=10, y=20
x, y = y, x                  # Swap: x=20, y=10
```

## LeetCode Patterns
-   **List Comprehensions**: `[x**2 for x in range(5) if x % 2 == 0]`
-   **Fixed Size Init**: `dp = [0] * n` (Create list of `n` zeros).
-   **2D Grid**: `grid = [[0] * cols for _ in range(rows)]`.
-   **Membership**: `if x in nums:` (O(n) for lists, O(1) for sets).
-   **Stacking**: `list_a + list_b` (New list) vs `list_a.extend(list_b)` (In-place).

## Practice
-   Practice File: [[03-code/python/lists_and_tuples_practice.py]]

## Related Links
-   [[01-concepts/python/_index|Python Index]]
-   [[01-concepts/python/Variables & Data Types|Variables & Data Types]]
-   [[01-concepts/python/String Methods|String Methods]]
-   [[01-concepts/python/Loops|Loops]]

## Deep Dive
Lists are dynamic arrays (pointers to objects). Tuples are static. The immutability of tuples makes them safer for returning multiple values from functions or protecting constant data. NamedTuples (`collections.namedtuple`) give tuples field names, making them lightweight objects.
