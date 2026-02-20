---
type: concept
tags: [python, fundamentals, operators]
difficulty: Beginner
domain: python
created: 2026-02-18
---

# Operators

**One-liner**: Operators are special symbols that perform computations on values and variables, acting as the "verbs" of the language.

## Mental Model
If variables are **nouns** (subjects), operators are the **verbs** that dictate how they interact. 
`a + b` is a sentence: "Subject `a` performs action `plus` with object `b`."

## Quick Facts
- **Arithmetic**:
    - `+`, `-`, `*`, `/` (Standard math).
    - `//` (Floor Division): Drops the decimal (e.g., `5 // 2` is `2`).
    - `%` (Modulus): Returns the remainder (e.g., `5 % 2` is `1`).
    - `**` (Exponentiation): Power (e.g., `2 ** 3` is `8`).
- **Comparison**:
    - `==` vs `=`: `==` checks **equality** ("Are these the same?"), while `=` performs **assignment** ("Make this equal to that").
    - `!=` (Not equal), `>`, `<`, `>=`, `<=`.
- **Logical**:
    - `and`: True if **both** are True.
    - `or`: True if **at least one** is True.
    - `not`: Inverts the boolean value.

## Code Example
```python
x = 10
y = 3

# Arithmetic
print(x // y)   # 3 (Floor division)
print(x % y)    # 1 (Remainder)
print(x ** y)   # 1000 (Power)

# Comparison
is_same = (x == 10)  # True
is_assigned = (x = 10) # SyntaxError!

# Logical
result = (x > 5) and (y < 2) # True and False -> False
```

## Practice
- Practice File: [[03-code/python/operators_practice.py]]

## Related Links
- [[01-concepts/python/_index|Python Index]]
- [[01-concepts/python/Variables & Data Types|Variables & Data Types]]

## Deep Dive
Operators usually map to "dunder" (double underscore) methods in Python classes (e.g., `+` calls `__add__`). 
The distinction between `=` (assignment statement) and `==` (equality expression) is the most common beginner bug. 
Logical operators short-circuit: in `A or B`, if `A` is True, `B` is never evaluated.
