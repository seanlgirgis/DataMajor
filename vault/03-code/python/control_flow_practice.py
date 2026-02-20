# Practice: Control Flow
# Linked Note: [[01-concepts/python/Control Flow|Control Flow]]

def check_access(age, has_id):
    """
    Guard clause practice.
    Return "Denied" if no ID or age < 18.
    Return "Granted" otherwise.
    """
    # TODO: Implement with guard clauses (early return)
    if not has_id:
        return "Denied"
    if age < 18:
        return "Denied"
    return "Granted"

def practice_control_flow():
    """
    Small exercise harness for Control Flow.
    
    1. if/elif/else: Grading system (90+ A, 80+ B, 70+ C, else F).
    2. Independent ifs: FizzBuzz logic check (Divisible by 3? Divisible by 5?).
    3. Ternary: Assign "Even" or "Odd" to a variable based on a number.
    4. Nested: Check if a number is positive, and if so, checks if it's > 100.
    """
    
    # 1. Chain (Grades)
    score = 85
    # TODO: Print grade based on score (First match wins)
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")  # Should print this
    elif score >= 70:
        print("C")
    else:
        print("F")

    # 2. Independent vs Chain
    num = 15
    print(f"Checking {num}:")
    # TODO: Check for div by 3, then SEPARATELY check for div by 5
    if num % 3 == 0:
        print("Fizz")
    if num % 5 == 0:
        print("Buzz")
    
    # 3. Ternary
    val = 7
    # TODO: One-line assignment
    parity = "Even" if val % 2 == 0 else "Odd"
    print(f"{val} is {parity}")

    # 4. Guard Clause test
    print(f"Access: {check_access(20, True)}")   # Granted
    print(f"Access: {check_access(17, True)}")   # Denied
    print(f"Access: {check_access(25, False)}")  # Denied

if __name__ == "__main__":
    practice_control_flow()
