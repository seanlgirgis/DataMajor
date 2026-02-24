# ============================================================
# 000021 | LC 0021 — Merge Two Sorted Lists
# Pattern   : Linked List — Dummy Head / Two-Pointer Merge
# Difficulty : Easy
# ============================================================
# Problem:
#   You are given the heads of two sorted linked lists list1 and list2.
#   Merge the two lists into one sorted list.
#   The list should be made by splicing together the nodes of list1 and list2.
#   Return the head of the merged linked list.
#
# Examples:
#   list1 = [1,2,4], list2 = [1,3,4]  ->  [1,1,2,3,4,4]
#   list1 = [],       list2 = []       ->  []
#   list1 = [],       list2 = [0]      ->  [0]
# ============================================================


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
def to_linked(vals: list) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next
    
    
l1 = [1,2,4]
head = to_linked(l1)

def traverse(head)->None:
    if not head :
        return
    node = head
    while True:
        print (node.val)
        if not node.next:
            break
        node = node.next
traverse(head)