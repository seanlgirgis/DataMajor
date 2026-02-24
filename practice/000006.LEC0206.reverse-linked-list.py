r"""
Problem 6 — LeetCode #206 — Reverse a Linked List
Given the head of a singly linked list, reverse it and return the new head.
Input:  1 -> 2 -> 3 -> 4 -> 5 -> None
Output: 5 -> 4 -> 3 -> 2 -> 1 -> None

Input:  1 -> 2 -> None
Output: 2 -> 1 -> None

Input:  None
Output: None
Constraint: O(n) time, O(1) space. Iterative solution preferred first, recursive is a bonus.
Note: Define the ListNode class yourself — show me you know the structure.
Take your shot.
"""


"""
Thinking Process:
right out they say Linked List.
We need a list node


"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class SingleLinkedList:
    def __init__(self, head: ListNode = None):
        if head:
            self.head = head
            
    def build(self, lst: list)->ListNode:
        if not lst:
            self.head = None
            return None
        # Create the first node
        self.head = ListNode(lst[0])
        current = self.head
        
        # Link in the rest of the nodes
        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        return self.head
        
        
    def represent(self)->str:
        ret = ""
        if not self.head:
            return ret
        current = self.head
        while current:
            ret += str(current.val) + " -> "
            current = current.next
        ret += "None"
        return ret
        
    # In place reverse
    def reverse(self)->None:
        # First traverse structure
        # Imagine you have Null Node in front of the head call it prev
        prev = None
        curr = self.head # start from the head
        
        while curr:
            temp = curr.next     # 1 save the next item in register so that you do not lose it
            curr.next = prev
            prev = curr 
            curr = temp         # 2 before looping back point to saved register
            
        self.head = prev
        
        
        

                


sll = SingleLinkedList()
sll.build([1,2,3,4,5])

print(sll.represent())
sll.reverse()
print(sll.represent())

            
        
        
        
            
            
            

        
            
            