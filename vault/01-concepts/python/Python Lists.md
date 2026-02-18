---
type: concept
tags: [concept, python, data-structures]
difficulty: Beginner
domain: python
created: 2026-02-18
---

# Python Lists

**One-liner**: A mutable, ordered sequence of elements capable of holding mixed data types.

## Mental Model
Think of a list as a customizable backpack. You can throw anything in it (books, lunch, laptop), keep them in a specific order, and take things out or swap them whenever you need.

## Quick Facts
- **Syntax**: Defined with square brackets `[]` e.g., `my_list = [1, "two", 3.0]`.
- **Mutable**: You can change items after creation (`my_list[0] = 5`).
- **Ordered**: Items maintain their insertion order.
- **Dynamic**: Can grow or shrink automatically.

## Code Example
```python
# Creating and modifying a list
fruits = ["apple", "banana", "cherry"]
fruits.append("date")        # Add to end
fruits[1] = "blueberry"      # Change item
print(fruits)                # ['apple', 'blueberry', 'cherry', 'date']
```

## Related Links
- [[01-concepts/python/_index|Python Index]]
- [[Python Tuples]] (Immutable cousin)
- [[Python Sets]] (Unordered, unique)

## Deep Dive
Lists are dynamic arrays under the hood. They are optimized for fast fixed-time access and appending additions. However, inserting or deleting from the beginning or middle can be slower (O(n)) because all subsequent elements must be shifted in memory.
