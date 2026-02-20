---
type: concept
tags: [python, fundamentals, functions]
difficulty: Beginner
domain: python
created: 2026-02-19
---

# Functions

**One-liner**: Functions are reusable, named blocks of code that accept inputs (parameters), perform logic, and typically return outputs.

## Mental Model
Think of a function as a **Black Box Machine**. You feed raw materials (arguments) into the top funnel, the machine whirs and clanks (logic), and a finished product (return value) slides out the bottom. You don't need to rebuild the machine every time; just feed it different materials.

## Quick Facts
-   **Syntax**: `def name(params):`.
-   **Return**: `return value`. If missing, returns `None` implicitly.
-   **Parameters**:
    -   **Positional**: Order matters (`f(a, b)`).
    -   **Keyword**: Explicit names (`f(b=2, a=1)`).
    -   **Defaults**: `def f(a=1)` (Must come after non-defaults).
    -   **`*args`**: Tuple of variable positional arguments.
    -   **`**kwargs`**: Dictionary of variable keyword arguments.
-   **Scope**: Variables inside functions are **local**. They die when the function ends. They cannot be seen globally unless returned.
-   **First-Class Objects**: Functions can be passed as arguments (`sort(key=len)`), returned from other functions, and assigned to variables.

## Code Example
```python
# Basic & Default Params
def greet(name, msg="Hello"):
    return f"{msg}, {name}!"

print(greet("Alice"))          # "Hello, Alice!"
print(greet("Bob", "Hi"))      # "Hi, Bob!"

# Multiple Return (Tuple Unpacking)
def get_stats(nums):
    return min(nums), max(nums)

low, high = get_stats([1, 5, 10]) # low=1, high=10

# *args and **kwargs
def echo(*args, **kwargs):
    print(f"Args: {args}")     # Tuple
    print(f"Kwargs: {kwargs}") # Dict

echo(1, 2, mode="debug")
# Args: (1, 2)
# Kwargs: {'mode': 'debug'}

# Lambda (Anonymous Function)
squared = lambda x: x**2
print(squared(5)) # 25
```

## LeetCode Patterns
-   **Helper Functions**: Define `def dfs(node):` *inside* the main solution function to encapsulate recursion logic and access outer variables.
-   **Two Pointers**: Encapsulated in a function like `is_palindrome(s)` to clean up main logic.
-   **Sorting**: `nums.sort(key=lambda x: x[1])` to sort by specific element.
-   **Recursion**: Functions calling themselves (Must have a **Base Case**!).
    -   `@functools.lru_cache(None)` auto-memoizes recursive functions.

## Practice
-   Practice File: [[03-code/python/functions_practice.py]]

## Related Links
-   [[01-concepts/python/_index|Python Index]]
-   [[01-concepts/python/Control Flow|Control Flow]]
-   [[01-concepts/python/Lists and Tuples|Lists and Tuples]]
-   [[01-concepts/python/Dictionaries|Dictionaries]]

## Deep Dive
Python passes arguments by **assignment** (object reference).
-   **Immutable** args (int, str, tuple) act like "pass by value" (changing local `x` doesn't change global `x`).
-   **Mutable** args (lists, dicts) act like "pass by reference" (modifying the list inside the function changes the original list outside).
