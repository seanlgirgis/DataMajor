# Practice: iter() and next()
# Linked Notes: 
# - [[02-Python-Fundamentals/iter-and-next-core-concept|iter() and next() — Core Concept]]
# - [[02-Python-Fundamentals/iterator-protocol-support|Iterator Protocol — Which Data Structures Support It]]

def practice_iter_and_next():
    print("--- Exercise 1: First key of a dict ---")
    # Use next(iter()) to grab the first key of this dict without converting to a list
    a = {"A": ["B","C"], "B": ["D"], "C": ["D"], "D": []}
    
    first_key = next(iter(a))
    print(f"First key is: {first_key}")
    assert first_key == "A", "Exercise 1 Failed"

    
    print("\n--- Exercise 2: Manual iteration loop ---")
    # Use iter() and next() with a while/try/except to loop through the same dict
    # Print each key and its value
    dict_iterator = iter(a)
    
    while True:
        try:
            key = next(dict_iterator)
            print(f"Key: {key}, Value: {a[key]}")
        except StopIteration:
            print("Finished iterating!")
            break


    print("\n--- Exercise 3: Identify the StopIteration ---")
    # Create an iterator from a list of 3 items
    # Call next() four times and handle the StopIteration gracefully
    my_list = [10, 20, 30]
    list_iterator = iter(my_list)
    
    for i in range(4):
        try:
            val = next(list_iterator)
            print(f"Pulled item: {val}")
        except StopIteration:
            print(f"StopIteration caught on attempt {i+1}! The iterator is exhausted.")


    print("\n--- Exercise 4: for vs iter/next ---")
    # Rewrite Exercise 2 using a for loop instead
    # Which do you prefer and why? (answer in a comment)
    for key in a:
        print(f"Key: {key}, Value: {a[key]}")
        
    # Answer: The `for` loop is heavily preferred for standard data structures 
    # because it is vastly more readable and handles the `StopIteration` 
    # exception automatically under the hood!


    print("\n--- Exercise 5: Generator ---")
    # Create a simple generator function that yields numbers 1 to 5
    # Use next() manually to pull values one at a time
    def simple_generator():
        for i in range(1, 6):
            yield i
            
    gen = simple_generator()
    
    print(next(gen)) # 1
    print(next(gen)) # 2
    print(next(gen)) # 3
    print(next(gen)) # 4
    print(next(gen)) # 5
    
    print("\n✅ All exercises completed successfully!")

if __name__ == "__main__":
    practice_iter_and_next()
