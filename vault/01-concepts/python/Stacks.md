---
type: concept
tags: [python, data-structures, stacks, LIFO]
difficulty: Beginner
domain: python
created: 2026-02-19
---

# Stacks

**One-liner**: A stack is a LIFO (Last In First Out) collection — you add and remove only from the top, like a stack of plates.

## Mental Model
Think of a stack of plates. You always add to the top and take from the top. You never touch the bottom. There is no built-in Stack class in Python — it is just a list used with discipline: only `append()` and `pop()` from the end.

## Quick Facts
-   **Structure**: Python uses a plain list as a stack.
-   **Operations**:
    -   `append(item)` = push (adds to top) — **O(1)**
    -   `pop()` = remove from top — **O(1)**
    -   `list[-1]` = peek (look at top without removing) — **O(1)**
-   **Constraints**: Never use `pop(0)` or `insert(0)` — that turns it into a Queue and is **O(n)** (slow).
-   **Safety**: Use `discard()` style safety checks (`if stack:`) before popping to avoid `IndexError`.
-   **Wrapper**: A class wrapper makes intent explicit and prevents misuse.

## Code Example
```python
# Raw List Stack
stack = []
stack.append("a")    # push -> ["a"]
stack.append("b")    # push -> ["a", "b"]
top = stack.pop()    # pop  -> "b" (LIFO)
peek = stack[-1]     # peek -> "a"

# Stack Class (Explicit)
class Stack:
    def __init__(self):
        self._items = []
    
    def push(self, item): 
        self._items.append(item)
    
    def pop(self):
        if not self._items: raise IndexError("pop from empty stack")
        return self._items.pop()
    
    def peek(self):
        if not self._items: raise IndexError("peek from empty stack")
        return self._items[-1]
        
    def is_empty(self): return not self._items
```

## When to use a Stack
-   **Bracket/Parenthesis Matching**: Ensure every `(` has a matching `)`.
-   **Undo/Redo**: Store previous states to revert actions.
-   **Browser History**: Back button logic.
-   **Depth-First Search (DFS)**: Exploring graph/tree paths.
-   **Monotonic Problems**: Finding "next greater element" or "previous smaller element".

## LeetCode Patterns
-   **Valid Parentheses** (#20): Push opening brackets, match and pop on closing.
-   **Monotonic Stack** (#739, #496, #503): Maintain a sorted order in the stack to solve "next greater" queries efficiently.

## Practice
-   Practice File: [[03-code/python/stacks_practice.py]]

## Related Links
-   [[01-concepts/python/Lists and Tuples|Lists and Tuples]]
-   [[01-concepts/python/Monotonic Stack|Monotonic Stack]]
-   [[04-leetcode/739-daily-temperatures|Daily Temperatures]]
-   [[04-leetcode/20-valid-parentheses|Valid Parentheses]]
