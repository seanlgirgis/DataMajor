# Practice: Dictionaries
# Linked Note: [[01-concepts/python/Dictionaries|Dictionaries]]

from collections import defaultdict, Counter

def practice_dictionaries():
    """
    Small exercise harness for Dictionaries.
    
    1. Basics: Create, access (safe vs unsafe), update, delete.
    2. Iteration: Loop through keys and values.
    3. Frequency Counter: Count characters in a string manually.
    4. Counter: Use collections.Counter for the same task.
    5. Grouping: Use defaultdict to group words by their starting letter.
    6. Memoization: Implement simple caching for a function.
    """
    
    # 1. Basics
    profile = {"user": "admin", "active": True}
    # TODO: Add "role": "superuser", safely get "email", remove "active" safely.
    profile["role"] = "superuser"
    email = profile.get("email", "Not Found")
    removed_val = profile.pop("active", None)
    print(f"Profile: {profile}, Email: {email}, Active Removed: {removed_val}")

    # 2. Iteration
    # TODO: Print key->value pairs
    for k, v in profile.items():
        print(f"{k} -> {v}")

    # 3. Frequency Counter (Manual)
    text = "banana"
    counts = {}
    # TODO: Count chars
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    print(f"Manual Counts: {counts}")

    # 4. Counter
    # TODO: Use Counter
    auto_counts = Counter(text)
    print(f"Counter: {auto_counts}")

    # 5. Grouping with defaultdict
    words = ["apple", "apricot", "banana", "blueberry", "cherry"]
    # TODO: Group by first letter { 'a': ['apple', 'apricot'] ... }
    by_letter = defaultdict(list)
    for w in words:
        by_letter[w[0]].append(w)
    print(f"Grouped: {dict(by_letter)}")

    # 6. Memoization / Caching
    cache = {}
    def fib(n):
        # TODO: Implement cached Fibonacci
        if n in cache: return cache[n]
        if n <= 1: return n
        res = fib(n-1) + fib(n-2)
        cache[n] = res
        return res
    
    print(f"Fib(10): {fib(10)}")

if __name__ == "__main__":
    practice_dictionaries()
