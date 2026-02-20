# Practice: Stacks
# Linked Note: [[01-concepts/python/Stacks]]

def practice_stacks():
    """
    Exercise harness for Stacks.
    
    1. Implement Stack class.
    2. Raw list operations.
    3. Valid Parentheses (#20).
    4. Reverse String.
    5. Undo System.
    """
    
    # 1. Stack Class Implementation
    print("--- 1. Stack Class ---")
    class Stack:
        def __init__(self):
            self._items = []
        
        def push(self, item): self._items.append(item)
        
        def pop(self):
            if self.is_empty(): raise IndexError("pop from empty stack")
            return self._items.pop()
        
        def peek(self):
            if self.is_empty(): raise IndexError("peek from empty stack")
            return self._items[-1]
        
        def is_empty(self): return len(self._items) == 0
        def size(self): return len(self._items)
        def __repr__(self): return f"Stack({self._items})"
    
    s = Stack()
    s.push(10)
    s.push(20)
    assert s.pop() == 20
    assert s.peek() == 10
    print("Stack class tests passed.")

    # 2. Raw List Operations
    print("\n--- 2. Raw List Stack ---")
    raw = []
    # Push 5 items
    for i in range(1, 6):
        raw.append(i) # [1, 2, 3, 4, 5]
    
    # Verify LIFO
    popped = []
    while raw:
        popped.append(raw.pop())
    
    print(f"Popped order: {popped}")
    assert popped == [5, 4, 3, 2, 1]

    # 3. Valid Bracket Checker (LeetCode 20)
    print("\n--- 3. Valid Parentheses ---")
    def is_valid(s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping.values(): # Opening bracket
                stack.append(char)
            elif char in mapping.keys(): # Closing bracket
                if not stack or stack.pop() != mapping[char]:
                    return False
            # Ignore other chars if any
        
        return len(stack) == 0

    assert is_valid("()") == True
    assert is_valid("()[]{}") == True
    assert is_valid("(]") == False
    assert is_valid("([)]") == False
    assert is_valid("{[]}") == True
    assert is_valid("") == True
    print("Valid Parentheses tests passed.")

    # 4. Reverse String
    print("\n--- 4. Reverse String ---")
    def reverse_string(text):
        stack = list(text) # Push all characters
        reversed_text = ""
        while stack:
            reversed_text += stack.pop()
        return reversed_text

    original = "hello"
    reversed_str = reverse_string(original)
    print(f"Original: {original}, Reversed: {reversed_str}")
    assert reversed_str == "olleh"

    # 5. Undo System
    print("\n--- 5. Undo Logic ---")
    actions = []
    
    # User types
    actions.append("Type A")
    actions.append("Type B")
    actions.append("Type C")
    print(f"Current State: {actions}")
    
    # Undo twice
    undo1 = actions.pop()
    print(f"Undoing: {undo1}")
    undo2 = actions.pop()
    print(f"Undoing: {undo2}")
    
    print(f"Final State: {actions}")
    assert actions == ["Type A"]

if __name__ == "__main__":
    practice_stacks()
