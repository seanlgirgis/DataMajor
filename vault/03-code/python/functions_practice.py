# Practice: Functions
# Linked Note: [[01-concepts/python/Functions|Functions]]

from functools import lru_cache

def practice_functions():
    """
    Small exercise harness for Functions.
    
    1. Basics: Define with default params.
    2. Unpacking: Return multiple values.
    3. Args/Kwargs: Flexible function.
    4. Lambda: Sort a list of tuples by 2nd value.
    5. Inner Function / Helper: Encapsulate logic.
    6. Recursion: Factorial with base case.
    """
    
    # 1. Basics
    # TODO: write greet(name, greeting="Hello")
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}"
    
    print(greet("Antigravity"))
    print(greet("User", "Welcome"))

    # 2. Unpacking
    def stats(nums):
        # TODO: return min, max, sum
        return min(nums), max(nums), sum(nums)
    
    data = [10, 20, 30]
    mn, mx, sm = stats(data)
    print(f"Stats: Min={mn}, Max={mx}, Sum={sm}")

    # 3. Flexible Args
    def flexible(*args, **kwargs):
        # TODO: print sum of args and keys of kwargs
        print(f"Sum args: {sum(args)}")
        print(f"Kwargs keys: {list(kwargs.keys())}")
    
    flexible(1, 2, 3, a=10, b=20)

    # 4. Lambda Sort
    pairs = [(1, "one"), (3, "three"), (2, "two")]
    # TODO: Sort by the string (2nd element)
    pairs.sort(key=lambda x: x[1])
    print(f"Sorted by name: {pairs}")

    # 5. Inner Function (Closure/Helper)
    def clean_process(words):
        def clean(w):
            return w.strip().lower()
        return [clean(w) for w in words]
    
    dirty = ["  Python ", "RC ", " Rust"]
    print(f"Cleaned: {clean_process(dirty)}")

    # 6. Recursion with lru_cache
    @lru_cache(None)
    def fib(n):
        if n < 2: return n
        return fib(n-1) + fib(n-2)
    
    print(f"Fib(10): {fib(10)}")

    # 7. Pass by Reference check
    def modify_list(lst):
        lst.append(999) # Modifies original
    
    nums = [1, 2]
    modify_list(nums)
    print(f"Modified external list: {nums}") 

if __name__ == "__main__":
    practice_functions()
