# Practice: Lists and Tuples
# Linked Note: [[01-concepts/python/Lists and Tuples|Lists and Tuples]]

from collections import namedtuple

def practice_lists_and_tuples():
    """
    Small exercise harness for Lists and Tuples.
    
    1. List Mutation: Create a list, add items, remove items, popping.
    2. Sorting: Demonstrate sort() in-place vs sorted().
    3. Comprehensions: Create a list of squares for even numbers 0-9.
    4. Tuples: Swap variables using tuple unpacking.
    5. NamedTuple: Create a 'Point' and access fields.
    """
    
    # 1. List Mutation
    inventory = ["sword", "shield"]
    # TODO: Add "potion" to end, insert "helmet" at start, remove "shield"
    inventory.append("potion")
    inventory.insert(0, "helmet")
    inventory.remove("shield")
    print(f"Inventory: {inventory}")
    
    # 2. Sorting
    scores = [5, 1, 9, 3]
    # TODO: Use sorted() to print a new list, then score.sort() to modify original
    print(f"Sorted copy: {sorted(scores)}")
    print(f"Original before sort: {scores}")
    scores.sort()
    print(f"Original after sort: {scores}")

    # 3. List Comprehensions
    # TODO: [x^2 for x in 0..9 if x is even]
    squares = [x**2 for x in range(10) if x % 2 == 0]
    print(f"Even squares: {squares}")

    # 4. Tuple Unpacking & Swapping
    a, b = "Left", "Right"
    print(f"Before: {a}, {b}")
    # TODO: Swap
    a, b = b, a
    print(f"After: {a}, {b}")

    # 5. NamedTuple
    # TODO: Define Person(name, age) and create an instance
    Person = namedtuple("Person", ["name", "age"])
    p = Person(name="Alice", age=30)
    print(f"Person: {p.name} is {p.age}")

if __name__ == "__main__":
    practice_lists_and_tuples()
