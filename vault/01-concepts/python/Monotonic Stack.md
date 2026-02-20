---
type: concept
tags: [python, data-structures, stacks, monotonic-stack, algorithms]
difficulty: Intermediate
domain: python
created: 2026-02-19
---

# Monotonic Stack

**One-liner**: A monotonic stack is a stack that maintains elements in **strictly increasing** or **strictly decreasing** order — used to find the "next greater" or "next smaller" element for every item in an array in **O(n)** time.

## Mental Model
**The Waiting Room**: Indices sit in the waiting room (the stack) until a "resolver" arrives.
-   **Example (Next Greater)**: Elements wait in the stack. When a larger number comes along, it "resolves" the smaller elements waiting at the top of the stack. They are popped, and the larger number becomes their "Next Greater Element".
-   **Efficiency**: Each element is pushed once and popped once. Total time is **O(n)**, instead of the O(n²) required by nested loops.

## Quick Facts
-   **Content**: Usually stores **indices**, not values (allows calculating distance `i - stack[-1]`).
-   **Decreasing Stack**: Keeps elements in decreasing order -> determines **Next Greater Element**.
-   **Increasing Stack**: Keeps elements in increasing order -> determines **Next Smaller Element**.
-   **Triggers**: "Next greater", "Next smaller", "How many days until", "Stock span", "Histogram area".
-   **Complexity**: **O(n)** time, **O(n)** space.

## The Core Template
```python
def solve(arr):
    n = len(arr)
    result = [-1] * n
    stack = []  # indices

    for i, val in enumerate(arr):
        # monotonic decreasing -> finds next GREATER
        # use > for monotonic increasing -> finds next SMALLER
        while stack and val > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = val # or i - idx for distance
        stack.append(i)
    
    return result
```

## Problems Solved
-   **#739 Daily Temperatures**: Distance to next warmer day. Store indices, result is `i - idx`.
-   **#496 Next Greater Element I**: Basic pattern. Store value-to-next-greater mapping.
-   **#503 Next Greater Element II**: Circular array. Loop `2*n` (modulo `n`).
-   **#901 Online Stock Span**: Consecutive days price <= current.
-   **#84 Largest Rectangle in Histogram**: The "Boss Level". Uses monotonic increasing stack to find *both* left and right boundaries where a bar can extend. Width = `right - left - 1`.

## Practice
-   Practice File: [[03-code/python/monotonic_stack_practice.py]]

## Related Links
-   [[01-concepts/python/Stacks|Stacks]]
-   [[04-leetcode/739-daily-temperatures|Daily Temperatures]]
-   [[04-leetcode/496-next-greater-element-i|Next Greater Element I]]
-   [[04-leetcode/503-next-greater-element-ii|Next Greater Element II]]
-   [[04-leetcode/84-largest-rectangle-histogram|Largest Rectangle in Histogram]]

## Deep Dive
For circular problems (#503), iterate up to `2*n` using `i % n`. But **only push** to the stack during the first pass (`i < n`) to avoid infinite loops or duplicates, while allowing the look-ahead to wrap around.
