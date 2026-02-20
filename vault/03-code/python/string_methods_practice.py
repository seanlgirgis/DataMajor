# Practice: String Methods
# Linked Note: [[01-concepts/python/String Methods|String Methods]]

def practice_string_methods():
    """
    Small exercise harness for String Methods.
    
    1. Slicing: Extract "Code" from the string "I Love Code".
    2. Methods: Clean up the messy string "  data__  ", remove underscores and whitespace, then uppercase it.
    3. Replace: Change "I like Java" to "I like Python".
    4. Split/Join: Parse "user:pass:uid:gid", getting just the "user" and keeping the rest? Then join a list back with pipes.
    5. F-String: Create a greeting using variables for name and age.
    """
    
    # 1. Slicing
    sentence = "I Love Code"
    # TODO: Slice "Code" (last 4 chars)
    target_word = sentence[-4:] 
    print(f"Extracted: '{target_word}'")

    # 2. Methods (Chaining)
    messy = "  data__  "
    # TODO: strip whitespace, replace '__' with empty string, then upper()
    clean = messy.strip().replace("__", "").upper()
    print(f"Cleaned: '{clean}'")

    # 3. Replace and Immutability
    opinion = "I like Java"
    # TODO: fixing the opinion
    fact = opinion.replace("Java", "Python")
    print(f"Original: {opinion}") # Shows immutability
    print(f"New: {fact}")

    # 4. Split (maxsplit) & Join
    config = "admin:12345:999:sales"
    # TODO: Split only ONCE at the first colon to get ['admin', '12345:999:sales']
    parts = config.split(":", 1)
    print(f"User: {parts[0]}, Rest: {parts[1]}")
    
    # TODO: Join ['a', 'b', 'c'] with "->"
    arrow_path = "->".join(['a', 'b', 'c'])
    print(f"Path: {arrow_path}")

    # 5. f-Strings
    name = "Agent"
    level = 9000
    # TODO: Print "Agent is level 9000!"
    greeting = f"{name} is level {level}!"
    print(greeting)

if __name__ == "__main__":
    practice_string_methods()
