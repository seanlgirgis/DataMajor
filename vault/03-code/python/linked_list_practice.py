# Practice: Linked List
# Linked Note: [[01-concepts/python/linked-list|Linked List]]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def traverse_to_list(head):
    """Helper to convert linked list to python list for easy assertions"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def find_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def practice_linked_list():
    """Small exercise harness for Linked List."""
    
    # 1. Build a chain: 1 -> 2 -> 3 -> 4 -> 5 -> None
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    
    # Verify traversal
    assert traverse_to_list(a) == [1, 2, 3, 4, 5], "Traversal failed"
    print("✅ Build & Traversal Passed!")
    
    # 2. Find Middle
    middle_node = find_middle(a)
    assert middle_node.val == 3, "Middle pointer failed"
    print("✅ Find Middle Passed!")
    
    # 3. Detect Cycle (Currently False)
    assert has_cycle(a) is False, "False cycle detected"
    
    # Create a cycle: 5 points back to 3
    e.next = c
    assert has_cycle(a) is True, "Cycle detection failed"
    
    # Break the cycle so we can test reverse next!
    e.next = None
    print("✅ Cycle Detection Passed!")

    # 4. Reverse Linked List
    new_head = reverse_list(a)
    assert traverse_to_list(new_head) == [5, 4, 3, 2, 1], "Reverse list failed"
    print("✅ Reverse Linked List Passed!")


if __name__ == "__main__":
    print("Starting Linked List Practice Exercises...\n")
    practice_linked_list()
    print("\nAll tests safely completed!")
