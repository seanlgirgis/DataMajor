# Practice: Try Except
# Linked Note: [[01-concepts/python/Try Except|Try Except]]

def practice_try_except():
    """
    Small exercise harness for Try Except.
    
    1. Basic: Handle ZeroDivisionError.
    2. Multiple: Handle ValueError vs TypeError.
    3. Else/Finally: Show the flow of execution.
    4. Raise: Validate input and raise ValueError.
    5. Patterns: Implement safe_get for a list (IndexError).
    """
    
    # 1. Basic ZeroDivision
    print("--- 1. Division ---")
    denominators = [5, 0, 2]
    for d in denominators:
        # TODO: Wrap in try/except
        try:
            res = 10 / d
            print(f"10/{d} = {res}")
        except ZeroDivisionError:
            print(f"Skipping 10/{d}: Cannot divide by zero")

    # 2. Multiple Exceptions
    print("\n--- 2. Parsing ---")
    inputs = ["10", "five", [1, 2]]
    for i in inputs:
        # TODO: Try converting to int
        try:
            val = int(i)
            print(f"Converted: {val}")
        except ValueError:
            print(f"ValueError: '{i}' is a string but not a number")
        except TypeError:
            print(f"TypeError: '{i}' is the wrong type entirely")

    # 3. Else / Finally
    print("\n--- 3. Flow Control ---")
    try:
        # Change this to trigger different paths
        x = 10
        # x = 10 / 0
    except ZeroDivisionError:
        print("Caught Error")
    else:
        print("No Error (Else)")
    finally:
        print("Cleanup (Finally)")

    # 4. Custom Raise
    print("\n--- 4. Validation ---")
    def register_user(age):
        # TODO: Raise ValueError if age < 0
        if age < 0:
            raise ValueError("Age must be positive")
        return f"User age {age} registered"

    try:
        print(register_user(-5))
    except ValueError as e:
        print(f"Registration failed: {e}")

    # 5. List Safe Get
    print("\n--- 5. Safe List pattern ---")
    nums = [10, 20, 30]
    # Like dict.get() but for lists using try/except
    def get_safe(lst, index):
        try:
            return lst[index]
        except IndexError:
            return None
            
    print(f"Index 1: {get_safe(nums, 1)}")
    print(f"Index 99: {get_safe(nums, 99)}")

if __name__ == "__main__":
    practice_try_except()
