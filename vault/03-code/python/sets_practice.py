# Practice: Sets
# Linked Note: [[01-concepts/python/Sets|Sets]]

def practice_sets():
    """
    Small exercise harness for Sets.
    
    1. Basics: Create set, add, remove vs discard, empty set trap.
    2. Deduplication: Remove duplicates from a list.
    3. Set Math: Union, Intersection, Difference.
    4. Performance: Logic check (O(1) vs O(n)).
    """
    
    # 1. Basics
    # TODO: Create set from list [1, 2, 2, 3], add 4, discard 5 (safe), remove 5 (unsafe check)
    nums = set([1, 2, 2, 3])
    nums.add(4)
    nums.discard(99) # Safe
    print(f"Set: {nums}")
    
    # TRAP: Create an empty set
    empty = set() 
    print(f"Type of empty: {type(empty)}") # <class 'set'>
    not_empty = {} 
    print(f"Type of {{}}: {type(not_empty)}") # <class 'dict'>

    # 2. Deduplication
    raw_data = ["apple", "banana", "apple", "cherry"]
    # TODO: Get unique items
    unique = list(set(raw_data))
    print(f"Unique: {unique}")

    # 3. Set Math
    skills_a = {"python", "sql", "git"}
    skills_b = {"java", "sql", "linux"}
    
    # TODO: Find common skills, unique to A, and all skills combined
    common = skills_a & skills_b
    only_a = skills_a - skills_b
    all_skills = skills_a | skills_b
    
    print(f"Common: {common}")
    print(f"Only A: {only_a}")
    print(f"Total: {all_skills}")

    # 4. Logic Check
    # Why use set over list for 'if x in collection'?
    # List: Scans one by one (O(n)). Slow for big data.
    # Set: Hashes x and jumps to spot (O(1)). Instant.

if __name__ == "__main__":
    practice_sets()
