# ============================================================
# 000036 | LEC 0206 --- Reverse Linked List [REDO DRILL]
# Pattern   : Three-Pointer
# Difficulty : Easy
# ============================================================
# Time Complexity:  O(n) --- single pass through the list
# Space Complexity: O(1) --- only three pointers used
# ============================================================
# Problem:
#   Given the head of a singly linked list, reverse the list,
#   and return the reversed list.
#
# Examples:
#   head = [1,2,3,4,5]  ->  [5,4,3,2,1]
#   head = [1,2]        ->  [2,1]
#   head = []           ->  []
#   head = []           ->  []
# ============================================================
# Key Insight:
#   To reverse a linked list in place, you need three pointers:
#   1. `prev`: initialized to None (what the new tail will point to).
#   2. `cur` : the current node we are processing.
#   3. `next_node`: temp variable to hold the rest of the list
#      before we break `cur`'s connection.
#   Operation at each step: save next_node, point cur backwards
#   to prev, shift prev to cur, shift cur to next_node.
# ============================================================

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head 
        prev = None
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev


# ── Helpers ──────────────────────────────────────────────────
def build_list(vals: list) -> Optional[ListNode]:
    if not vals:
        return None
    head = ListNode(vals[0])
    curr = head
    for val in vals[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def to_list(head: Optional[ListNode]) -> list:
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res

# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2],          [2, 1]),
        ([],              []),
        ([1],             [1])
    ]

    passed = 0
    for i, (vals, expected) in enumerate(test_cases, 1):
        head = build_list(vals)
        reversed_head = sol.reverseList(head)
        result = to_list(reversed_head)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: {vals} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
