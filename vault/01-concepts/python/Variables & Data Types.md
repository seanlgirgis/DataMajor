---
type: concept
tags: [python, fundamentals, data-types]
difficulty: Beginner
domain: python
created: 2026-02-18
---

# Variables & Data Types

**One-liner**: Variables are labels for data, and data types define the nature and operations applicable to that data.

## Mental Model
Think of variables as **nametags** stuck onto objects, not boxes that contain them. The object (data) exists in memory, and the variable is just a reference pointing to it. Python figures out the type of the object automatically (dynamic typing) based on what you assign.

## Quick Facts
- **Assignment**: Use `=` to assign a value to a variable (e.g., `x = 5`).
- **Dynamic Typing**: You don't declare types (like `int x`); Python infers them at runtime.
- **Core Types**:
    - `int`: Whole numbers (e.g., `10`, `-5`).
    - `float`: Decimal numbers (e.g., `3.14`, `2.0`).
    - `str`: Text (e.g., `"Hello"`, `'Python'`).
    - `bool`: Truth values (`True`, `False`).
- **Type Checking**: Use `type(variable)` to see what data type a variable holds.
- **Reassignment**: You can change a variable's value and even its type later (e.g., `x = 10` then `x = "ten"`).

## Code Example
```python
# Assignment and dynamic typing
count = 10          # int
price = 19.99       # float
name = "Alice"      # str
is_active = True    # bool

# Checking types
print(type(count))  # <class 'int'>

# Re-assigning to a different type
count = "Too many"
print(type(count))  # <class 'str'>
```

## Practice
- Practice File: [[03-code/python/variables_and_types.py]]

## Related Links
- [[01-concepts/python/_index|Python Index]]
- [[01-concepts/python/fundamentals/Python Lists|Python Lists]]

## Deep Dive
Python leads with **dynamic typing**, meaning type checking happens at runtime. This allows for succinct code but requires discipline to avoid type errors. Everything in Python is an object, including simple integers. The `type()` function is a built-in inspector that tells you the class of any object.
