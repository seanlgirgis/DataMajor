---
type: concept
tags: [python, algorithms, binary-search]
difficulty: intermediate
language: python
created: 2026-02-21
---

# Binary Search

## The 30-Second Rule
**Binary search** cuts a *sorted* array in half on every step, finding a target in logarithmic time `O(log n)` instead of linear time `O(n)`. 

Think of opening a physical dictionary to find a word: you break it open to the middle, decide if your word is in the left or right half based on alphabetical order, and discard the other half instantly. You can easily find any word in a 10,000-page book in under 14 steps.

## The Core Template
There are three things to memorize here: `left <= right`, `mid = (left + right) // 2`, and how to move each pointer.

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1     # Throw away the left half
        else:
            right = mid - 1    # Throw away the right half

    return -1  # Target not found
```

## Complexity

| | Linear Search | Binary Search |
|-|---------------|---------------|
| **Time** | `O(n)` | **`O(log n)`** |
| **Requirement** | Any array | **Sorted array** |

> [!TIP]
> `O(log n)` is extraordinarily fast. Searching through 1 billion elements takes only ~30 steps using Binary Search!

---

## Boundaries: Finding the First or Last Occurrence
Standard binary search just finds *a* match. LeetCode normally asks for the leftmost or rightmost occurrence when there are duplicates.

### Leftmost Position (First Occurrence)
When we find the target, aggressively try to keep looking to the left.
```python
def search_left(nums, target):
    left, right = 0, len(nums) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid
            right = mid - 1   # Keep going left!
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result
```

### Rightmost Position (Last Occurrence)
When we find the target, aggressively try to keep looking to the right.
```python
def search_right(nums, target):
    left, right = 0, len(nums) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid
            left = mid + 1    # Keep going right!
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result
```

---

## The Disguised Pattern: Binary Search on the Answer
Sometimes LeetCode gives you a problem where there is no array to search! If there is a definitive range of possible answers, and a function that explicitly says "Yes/No, this answer is possible", then we can perform Binary Search *on the answer itself*.

**Example**: "What's the minimum capacity to ship packages in D days?"
```python
def ship_within_days(weights, days):
    left = max(weights)       # minimum possible capacity
    right = sum(weights)      # maximum possible capacity

    while left < right:
        mid = (left + right) // 2
        if can_ship(weights, days, mid): # A helper boolean function
            right = mid       # It works! But try even smaller capacity.
        else:
            left = mid + 1    # It failed. Need more capacity!

    return left
```


---
## Related Notes
- [[01-concepts/python/index|Python Index]]
- Sorting
- [[01-concepts/python/linked-list|Linked List]]

## Practice
- Practice File: [[03-code/python/binary_search_practice.py]]
