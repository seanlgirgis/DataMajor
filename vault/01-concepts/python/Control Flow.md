---
type: concept
tags: [python, fundamentals, control-flow]
difficulty: Beginner
domain: python
created: 2026-02-18
---

# Control Flow

**One-liner**: Control flow dictates the order in which code executes, using conditional logic to make decisions and branch execution paths.

## Mental Model
Think of control flow as a **railway switch**. The train (execution) comes down the track, encounters a switch (`if`), and depending on the signal (True/False), it either continues straight or diverts to a different track. In an `if/elif/else` chain, the train takes the **first** open track it finds and ignores the rest.

## Quick Facts
- **Structure**: `if` checks a condition. `elif` (else if) checks another *only if* the previous failed. `else` catches everything effectively "otherwise".
- **Indentation**: Python uses whitespace (indentation) to define blocks of code. No curly braces `{}`.
- **First Match Wins**: In an `if/elif` chain, Python stops at the **first** True condition.
- **Independent Checks**: Multiple `if` statements run independently; all are checked.
- **Ternary Operator**: `value_if_true if condition else value_if_false` (One-line conditional).
- **Guard Clauses**: Checking for failure conditions at the start of a function and returning early (`if error: return`) to avoid deep nesting ("arrow code").

## Code Example
```python
x = 42

# Chain (Exclusive)
if x > 50:
    print("Big")
elif x > 40:
    print("Medium") # Prints this and STOPS.
elif x > 10:
    print("Small")  # Skipped, even though 42 > 10 is True.
else:
    print("Tiny")

# Independent (Inclusive)
if x > 40: print("Medium") # Prints
if x > 10: print("Small")  # Also prints

# Ternary
status = "Adult" if x >= 18 else "Minor"

# Nested
if x > 0:
    if x % 2 == 0:
        print("Positive Even")
```

## Practice
- Practice File: [[03-code/python/control_flow_practice.py]]

## Related Links
- [[01-concepts/python/_index|Python Index]]
- [[01-concepts/python/Variables & Data Types|Variables & Data Types]]
- [[01-concepts/python/Operators|Operators]]

## Deep Dive
Deeply nested code is hard to read. Prefer **Guard Clauses**: handle edge cases/errors first and `return`, leaving the "happy path" unindented at the bottom. The difference between `if/elif` and `if/if` is a common logic bug source.
