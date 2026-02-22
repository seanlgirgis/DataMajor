---
type: syntax-card
tags: [python, dict, hashmap, syntax]
difficulty: beginner
domain: python
created: 2026-02-21
---

# Python Dictionaries (Hash Maps)

**One-liner**: A dictionary is a mutable collection of key-value pairs that provides `O(1)` average time complexity for lookups, insertions, and deletions.

## Mental Model
Think of a real-world dictionary or a phone book. You don't read it front-to-back (like a List); instead, you look up a specific unique "Word" (Key) to instantly find its "Definition" (Value).

## Quick Facts
- **Keys must be hashable**: Strings, integers, and tuples can be keys. Lists and dictionaries cannot.
- **Values can be anything**: You can store lists, other dicts, integers, functions, etc.
- **Fast**: Backed by a hash table, making `add`, `update`, `delete`, and `search` effectively `O(1)`.
- **Order**: As of Python 3.7+, dictionaries officially remember the insertion order of their keys.

## Base Operations: Add, Update, Delete
```python
# 1. Declaration / Initialization
empty_dict = {}
my_dict = {1: "one", 2: "two"}  # Integer keys are common in LeetCode

# 2. Add / Update (Same syntax)
my_dict[3] = "three"    # Adds new entry
my_dict[2] = "DOS"      # Updates existing entry

# 3. Delete
del my_dict[1]          # Throws KeyError if key doesn't exist
val = my_dict.pop(3)    # Removes key and returns its value
```

## Search / Lookup
```python
# Check if key exists (O(1) time)
if 2 in my_dict:
    print("Key 2 exists!")

# Get value (safe way)
# .get() returns None (or a specified default) if key is missing
val = my_dict.get(99, "Not Found") 
```

## Iteration
```python
scores = {1: 10, 2: 20, 3: 30}

# Iterate Keys (Default)
for key in scores:           # equivalent to scores.keys()
    print(key)

# Iterate Values
for val in scores.values():
    print(val)

# Iterate Both (Items)
for key, val in scores.items():
    print(f"Key {key} -> Val {val}")
```

## Common Patterns for LeetCode
```python
# 1. Frequency Counting with .get()
nums = [1, 1, 2, 3, 3, 3]
freq = {}
for n in nums:
    freq[n] = freq.get(n, 0) + 1  # Default to 0 if missing, then add 1

# 2. defaultdict
# Automatically initializes missing keys with a default factory (e.g., list or int)
from collections import defaultdict

adj_list = defaultdict(list)
adj_list[1].append(2)     # No KeyError! Key 1 was auto-initialized to []

counts = defaultdict(int) 
counts[5] += 1            # No KeyError! Key 5 was auto-initialized to 0
```

## Related Links
- [[02-Python-Fundamentals/_index|Python Fundamentals Index]]
- [[01-concepts/python/iter-and-next-core-concept|iter() and next()]]
