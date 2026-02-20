---
type: concept
tags: [python, fundamentals, error-handling, control-flow]
difficulty: Beginner
domain: python
created: 2026-02-18
---

# Try Except

**One-liner**: `try/except` blocks allow you to handle runtime errors gracefully preventing program crashes by "catching" exceptions.

## Mental Model
Think of it as a **Trapeze Artist with a Safety Net**.
-   **`try`**: The artist performing the stunt (the risky code).
-   **`except`**: The safety net. If the artist falls (error), the net catches them so they can walk away safely instead of crashing.
-   **`else`**: The applause after a successful stunt (runs only if *no* fall occurred).
-   **`finally`**: The cleanup crew sweeping the stage (runs *always*, fall or no fall).

## Quick Facts
-   **Structure**:
    ```python
    try:
        # Risky code
    except SpecificError:
        # Handle specific failure
    except Exception as e:
        # Catch-all (use sparingly)
    else:
        # Runs if NO error
    finally:
        # ALWAYS runs (cleanup)
    ```
-   **Common Exceptions**:
    -   `ValueError`: Right type, wrong value (e.g., `int("abc")`).
    -   `TypeError`: Wrong type operation (e.g., `"1" + 2`).
    -   `KeyError`: Dictionary key missing.
    -   `IndexError`: List index out of bounds.
    -   `ZeroDivisionError`: Dividing by zero.
-   **Raising**: Use `raise ValueError("Reason")` to trigger your own errors.

## Code Example
```python
# Multiple Catch Blocks
try:
    val = int("abc")
except ValueError:
    print("Not a number")
except Exception as e:
    print(f"Unknown error: {e}")

# Flow Control (Safe Divide)
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

# Dictionary Access Pattern
try:
    print(data["missing"])
except KeyError:
    print("Key not found")

# Custom Error
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
```

## LeetCode Patterns
-   **Input Parsing**: When converting raw string input to numbers where format isn't guaranteed.
-   **Safe Parsing**:
    ```python
    def safe_int(x):
        try:
            return int(x)
        except (ValueError, TypeError):
            return 0
    ```

## Practice
-   Practice File: [[03-code/python/try_except_practice.py]]

## Related Links
-   [[01-concepts/python/_index|Python Index]]
-   [[01-concepts/python/Control Flow|Control Flow]]
-   [[01-concepts/python/Dictionaries|Dictionaries]]

## Deep Dive
`try/except` is not just for errors; it's a valid flow control mechanism in Python ("EAFP: It's Easier to Ask Forgiveness than Permission"). This contrasts with "LBYL" (Look Before You Leap), like checking `if key in dict` before accessing. EAFP is often faster and considered more "Pythonic" for conditions that happen rarely.
