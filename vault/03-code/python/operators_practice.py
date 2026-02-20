# Practice: Operators
# Linked Note: [[01-concepts/python/Operators|Operators]]

def practice_operators():
    """
    Small exercise harness for Operators.
    
    1. Arithmetic: Calculate the implementation of the Pythagorean theorem (c = sqrt(a^2 + b^2)) using only math operators (hint: sqrt is power of 0.5).
    2. Modulus: Check if a number 'n' is even or odd using %.
    3. Comparison: Create two variables and check if they are NOT equal.
    4. Logical: Verify if a number is strictly between 10 and 20.
    """
    
    # 1. Arithmetic (Pythagorean Theorem)
    a = 3
    b = 4
    # TODO: Calculate c using ** operator
    c = (a**2 + b**2)**0.5
    print(f"Hypotenuse of {a} and {b} is: {c}") # Should be 5.0

    # 2. Modulus
    n = 17
    # TODO: Use % to print "Odd" or "Even"
    is_even = (n % 2) == 0
    print(f"Is {n} even? {is_even}")

    # 3. Comparison
    score1 = 50
    score2 = 100
    # TODO: Check inequality
    print(f"Scores are different: {score1 != score2}")
    
    # 4. Logical
    value = 15
    # TODO: Check if 10 < value < 20 using and
    in_range = (value > 10) and (value < 20)
    print(f"Is {value} between 10 and 20? {in_range}")

if __name__ == "__main__":
    practice_operators()
