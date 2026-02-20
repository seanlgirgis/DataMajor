---
type: concept
tags: [python, fundamentals, loops]
difficulty: Beginner
domain: python
created: 2026-02-18
---

# Loops

**One-liner**: Loops allow you to repeat a block of code multiple times, either by iterating over a sequence (`for`) or while a condition remains true (`while`).

## Mental Model
Think of a **factory conveyor belt**.
-   **For Loop**: "For every item on this belt, stamp it." (You know exactly how many items are there).
-   **While Loop**: "Keep the machine running *while* the 'Power On' light is green." (You don't know how long it will run, strictly depends on the condition).

## Quick Facts
-   **`for` loops**: Iterate over sequences (lists, strings, ranges).
    -   `range(start, stop, step)`: Generates numbers. Stop is exclusive.
-   **`while` loops**: Run as long as the condition is `True`.
    -   **Critical Warning**: Infinite loops freeze your program! Ensure the condition eventually becomes `False` or use `break`.
-   **Control Keywords**:
    -   `break`: Exits the loop *immediately*.
    -   `continue`: Skips the rest of the *current* iteration and jumps to the next one.
-   **`enumerate(seq)`**: Returns `(index, item)` tuples.
-   **`range(len(seq))`**: Classic C-style iteration by index.

## Code Example
```python
# For Loop (Sequence)
for char in "Code":
    print(char)

# Range (Start, Stop, Step)
for i in range(0, 10, 2): # 0, 2, 4, 6, 8
    print(i)

# Enumerate (Index + Value)
fruits = ["apple", "banana"]
for i, fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")

# While Loop
count = 5
while count > 0:
    print(count)
    count -= 1  # DECREMENT IS CRITICAL
```

## LeetCode Patterns
-   **Index Iteration**: `for i in range(len(nums)):` allowing access to `i` and `i+1`.
-   **Two Pointers**:
    ```python
    left, right = 0, len(s) - 1
    while left < right:
        # Swap or compare s[left] and s[right]
        left += 1
        right -= 1
    ```

## Practice
- Practice File: [[03-code/python/loops_practice.py]]

## Related Links
-   [[01-concepts/python/_index|Python Index]]
-   [[01-concepts/python/Control Flow|Control Flow]]
-   [[01-concepts/python/Operators|Operators]]

## Deep Dive
`for` loops in Python are actually "for-each" loops; they consume an iterator. `while` loops are lower-level and riskier (infinite loops) but necessary when the number of iterations isn't known upfront. The two-pointer pattern using `while left < right` is fundamental for array/string reversal and searching problems.
