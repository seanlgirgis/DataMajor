---
type: concept
tags: [python, algorithms, sorting]
difficulty: intermediate
language: python
created: 2026-02-21
---

# Sorting Algorithms

## The 30-Second Rule
Sorting algorithms arrange elements in order. While in production you will always use Python's highly optimized built-in `Timsort`, understanding Bubble, Merge, and Quick Sort is required for algorithmic interviews and grasping Time/Space complexity tradeoffs.

## Python's Built-In (Timsort)
Always use these in practical coding:
```python
nums = [3, 1, 4, 1, 5, 9]
nums.sort()                 # In-place, returns None
sorted_nums = sorted(nums)  # Returns a NEW sorted list

# Custom Sorts
words = ["banana", "apple", "cherry"]
words.sort(key=len)         # Sort by length
pairs = [(1, 'b'), (2, 'a')]
pairs.sort(key=lambda x: x[1]) # Sort by second element
```

## The "Big Three" Algorithms

### 1. Bubble Sort (The Simple One)
**Idea:** Repeatedly swap adjacent elements that are out of order. The largest element "bubbles" to the end each pass.
- **When to use:** Never in practice. Exists purely to teach comparison-based sorting concepts.
- **Time Complexity:** `O(n^2)` average/worst.

### 2. Merge Sort (The Reliable One)
**Idea:** Divide the array in half recursively until you have single elements, then merge them back in sorted order using two pointers.
- **When to use:** When stability matters (equal elements maintain original relative order), or when you must guarantee `O(n log n)` even in the worst case (e.g., sorting linked lists).
- **Time Complexity:** `O(n log n)` in all cases.
- **Space Complexity:** `O(n)` because it requires new arrays for the `merge` step.

### 3. Quick Sort (The Fast One)
**Idea:** Pick a "pivot", partition everything smaller to the left and larger to the right, then recursively call on both halves.
- **When to use:** Very fast in practice for primitive types in memory.
- **Time Complexity:** `O(n log n)` average, but `O(n^2)` absolute worst case (e.g., already sorted array with a terrible pivot choice).
- **Space Complexity:** `O(log n)` call stack space (in-place partitioning!). Unstable by default.

## The Comparison Table

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| **Bubble** | `O(n)` | `O(n²)` | `O(n²)` | `O(1)` | ✅ Yes |
| **Merge** | `O(n log n)` | `O(n log n)` | `O(n log n)` | `O(n)` | ✅ Yes |
| **Quick** | `O(n log n)` | `O(n log n)` | `O(n²)` | `O(log n)` | ❌ No |
| **Python Timsort** | `O(n)` | `O(n log n)` | `O(n log n)` | `O(n)` | ✅ Yes |

---
## Related Notes
- [[01-concepts/python/index|Python Index]]
- [[01-concepts/python/binary-search|Binary Search]]

## Practice
- Practice File: [[03-code/python/sorting_algorithms_practice.py]]
