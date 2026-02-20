---
type: concept
tags: [python, fundamentals, strings]
difficulty: Beginner
domain: python
created: 2026-02-18
---

# String Methods

**One-liner**: String methods are built-in functions to manipulate text, but since strings are immutable, they always return **new** strings rather than changing the original.

## Mental Model
Think of a string as a **sealed letter**. You can't erase or write over it. If you want to change it (e.g., uppercase it), you have to photocopy it, modify the copy, and use that new sheet. The original remains untouched.

## Quick Facts
- **Immutability**: `s.upper()` returns a *new* string; `s` stays the same unless you reassign it (`s = s.upper()`).
- **Common Methods**:
    - `.upper()`, `.lower()`: Case conversion.
    - `.strip()`: Removes leading/trailing whitespace.
    - `.replace(old, new)`: Swaps substrings.
    - `.split(delimiter, maxsplit)`: Breaks string into a list. `maxsplit` limits the number of splits.
    - `.join(iterable)`: Joins a list of strings into one string using the separator (reverse of split).
- **Indexing & Slicing**:
    - `s[0]`: First character.
    - `s[-1]`: Last character.
    - `s[start:end]`: Slice from `start` up to (but not including) `end`.
- **f-Strings**: Use `f"Hello {name}"` to embed variables directly into strings.

## Code Example
```python
text = "  Python rules  "

# Methods
clean = text.strip().upper()  # "PYTHON RULES"

# Split & Join
csv = "a,b,c,d"
parts = csv.split(",", 2)     # ['a', 'b', 'c,d'] (maxsplit=2)
joined = "-".join(parts)      # "a-b-c,d"

# Slicing
print(clean[0:6])   # "PYTHON"
print(clean[::-1])  # "SELUR NOHTYP" (Reverse)

# f-Strings
score = 95
msg = f"Score: {score}%" # "Score: 95%"
```

## Practice
- Practice File: [[03-code/python/string_methods_practice.py]]

## LeetCode Patterns
- **Membership**: `"x" in "string"` (True/False).
- **Length**: `len(s)` for loops and bounds.
- **ASCII Math**:
    - `ord("a")` -> 97, `chr(97)` -> "a".
    - Useful for alphabet indexing: `ord(char) - ord("a")`.
- **Classification**:
    - `.isalpha()`, `.isdigit()`, `.isalnum()` for filtering characters.
- **Frequency**: `s.count("sub")` counts occurrences.
- **Search**:
    - `.find("x")`: Returns index or `-1` (Safe).
    - `.index("x")`: Returns index or raises `ValueError` (Rigid).
- **Multiplication**: `"a" * 3` -> `"aaa"`.
- **Palindrome Check**: `s == s[::-1]`.

## Related Links
- [[01-concepts/python/_index|Python Index]]
- [[01-concepts/python/Variables & Data Types|Variables & Data Types]]
- [[01-concepts/python/Operators|Operators]]

## Deep Dive
Strings in Python are sequences of Unicode characters. Indexing starts at 0. Negative indexing (`-1`) allows easy access from the end. The `str` class is highly optimized, and f-strings (formatted string literals) are the modern, preferred way to format strings due to readability and performance.
