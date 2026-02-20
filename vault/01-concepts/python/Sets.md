---
type: concept
tags: [python, fundamentals, sets]
difficulty: Beginner
domain: python
created: 2026-02-18
---

# Sets

**One-liner**: Sets are mutable, unordered collections of **unique** elements, optimized for O(1) membership testing and mathematical operations.

## Mental Model
-   **Dictionary with Keys Only**: Think of a set as a dictionary where you threw away the values and kept the keys. It has the same super-fast O(1) lookup speed.
-   **Club Guest List**: The bouncer only cares *if* you are on the list, not *where* you are on the list or how many times you wrote your name (duplicates are ignored).

## Quick Facts
-   **Structure**: `{1, 2, 3}`. No duplicates allowed.
-   **Creation**: `set()` for empty set (Critical: `{}` creates an empty *dictionary*).
-   **Operations**:
    -   `add(x)`: Adds element.
    -   `remove(x)`: Crashes if missing.
    -   `discard(x)`: Safe removal (no error if missing).
    -   `pop()`: Removes arbitrary element.
-   **Set Math**:
    -   `a | b` (Union): All unique items in both.
    -   `a & b` (Intersection): Items common to both.
    -   `a - b` (Difference): Items in `a` but not `b`.
    -   `a ^ b` (Symmetric Diff): Items in one or the other, but not both.

## Code Example
```python
# Creation
nums = {1, 2, 2, 3}  # {1, 2, 3} (Deduplicated)
empty = set()        # Not {}

# Membership (The Superpower)
if 3 in nums:        # O(1) - Instant
    print("Found")

# Math
a = {1, 2, 3}
b = {3, 4, 5}

print(a & b)  # {3} (Intersection)
print(a - b)  # {1, 2} (Difference)
print(a | b)  # {1, 2, 3, 4, 5} (Union)
```

## LeetCode Patterns
-   **Deduplication**: `unique = list(set(nums))` (One-liner to remove duplicates).
-   **Has Duplicate**: `len(nums) != len(set(nums))`.
-   **O(1) Lookup**: Replacing a list with a set for membership checks turns an O(n^2) algorithm into O(n).
-   **Intersection**: Finding common elements between arrays efficiently.

## Practice
-   Practice File: [[03-code/python/sets_practice.py]]

## Related Links
-   [[01-concepts/python/_index|Python Index]]
-   [[01-concepts/python/Lists and Tuples|Lists and Tuples]]
-   [[01-concepts/python/Dictionaries|Dictionaries]]

## Deep Dive
Implemented as a hash table (like dicts). Because they rely on hashing, set elements must be **immutable** (hashable). You can have a tuple in a set, but not a list.
