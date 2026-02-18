# Practice: Variables & Data Types
# Linked Note: [[01-concepts/python/Variables & Data Types|Variables & Data Types]]

def practice_variables_and_types():
    """
    Small exercise harness for Variables & Data Types.
    
    1. Create variables for an item's name (str), price (float), and quantity (int).
    2. vivid_name = "Magic Sword"
    3. Check the type of the price variable.
    4. Calculate total cost and print it.
    """
    
    # TODO: Implement practice logic here
    item_name = "Magic Sword"
    item_price = 150.50
    item_quantity = 2
    is_available = True
    
    print(f"Item: {item_name}, Type: {type(item_name)}")
    print(f"Price: {item_price}, Type: {type(item_price)}")
    print(f"Quantity: {item_quantity}, Type: {type(item_quantity)}")
    print(f"Available: {is_available}, Type: {type(is_available)}")
    
    total_cost = item_price * item_quantity
    print(f"Total Cost: {total_cost}")

if __name__ == "__main__":
    practice_variables_and_types()
