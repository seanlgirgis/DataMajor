---
type: concept
tags: [python, fundamentals, dictionaries]
difficulty: Beginner
domain: python
created: 2026-02-18
---

# Dictionaries

**One-liner**: Dictionaries are mutable, unordered collections of key-value pairs, optimized for O(1) retrieval using hashing.

## Mental Model
Think of a **real-world dictionary**. You don't read every word to find "Python"; you jump directly to "P", then "y"... It's an indexed lookup. In Python, the "Index" is a **Hash Table**, calculating exactly where the data lives in memory based on the key.

## Quick Facts
-   **Structure**: `{key: value}`. Keys must be **immutable** (hashable) like strings, numbers, or tuples. Values can be anything.
-   **Operations**:
    -   **Read**: `d[key]` (crashes if missing), `d.get(key, default)` (safe).
    -   **Write**: `d[key] = value` (adds or updates).
    -   **Delete**: `del d[key]` (crashes if missing), `d.pop(key, default)` (safe, returns value).
    -   **Check**: `key in d` (Fast O(1) lookup).
-   **Iteration**:
    -   `d.keys()`, `d.values()`, `d.items()` (returns pairs).

## Code Example
```python
person = {"name": "Alice", "age": 30}

# Safe Access
print(person.get("email", "No Email"))  # "No Email"

# Iteration
for k, v in person.items():
    print(f"{k}: {v}")

# Update
person["city"] = "NY"         # Insert
person["age"] += 1            # Modify

# Frequency Counter (Manual)
freq = {}
for char in "apple":
    freq[char] = freq.get(char, 0) + 1
```

## LeetCode Patterns
-   **Frequency Counter**: `collections.Counter(s)` gives `{'a': 1, 'p': 2...}` instantly.
-   **DefaultDict**: `collections.defaultdict(list)` avoids key checking (auto-initializes values).
    -   Pattern: Grouping items (e.g., `groups[len(word)].append(word)`).
-   **Two Sum**: Store `target - num` in a dict to find pairs in O(n).
-   **Memoization**: Use a dict to cache function results (`cache = {}`) to avoid re-calcs (e.g., Fibonacci).

## Practice
-   Practice File: [[03-code/python/dictionaries_practice.py]]

## Related Links
-   [[01-concepts/python/_index|Python Index]]
-   [[01-concepts/python/Lists and Tuples|Lists and Tuples]]
-   [[01-concepts/python/Loops|Loops]]
-   [[01-concepts/python/Control Flow|Control Flow]]

## Deep Dive
Under the hood, Python dicts are **Hash Maps**. A hash function converts the key into an integer index. This is why lists (mutable) cannot be keys—their hash would change if modified, breaking the map. Python 3.7+ guarantees insertion order for dicts, a feature often relied upon now.
