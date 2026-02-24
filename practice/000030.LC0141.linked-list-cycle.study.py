# ============================================================
# 000030 | LC 0141 --- Linked List Cycle
# Pattern   : Fast/Slow Pointers (Floyd's Tortoise and Hare)
# Difficulty : Easy
# ============================================================
# Time Complexity:  O(n) --- slow pointer travels around cycle at most once
# Space Complexity: O(1) --- only tracking two pointers
# ============================================================
# Problem:
#   Given head, the head of a linked list, determine if the
#   linked list has a cycle in it.
#   There is a cycle in a linked list if there is some node in
#   the list that can be reached again by continuously following
#   the next pointer.
#   Return True if there is a cycle in the linked list. Otherwise, return False.
#
# Examples:
#   head = [3,2,0,-4], pos = 1 (tail connects to node index 1) -> True
#   head = [1,2], pos = 0 (tail connects to node index 0)      -> True
#   head = [1], pos = -1 (no cycle)                            -> False
# ============================================================
# Key Insight:
#   Instead of a HashSet which requires O(n) memory, use two
#   pointers moving at different speeds.
#   `slow` moves 1 step, `fast` moves 2 steps.
#   If there's a cycle, `fast` will eventually lap `slow` and
#   they will point to the same node (`slow == fast`).
#   If the list terminates (`fast` or `fast.next` is None), there's no cycle.
# ============================================================

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next          # moves 1 step
            fast = fast.next.next     # moves 2 steps
            
            if slow == fast:
                return True           # fast lapped slow, cycle found!
                
        return False                  # fast reached end of list, no cycle


# ── Helpers ──────────────────────────────────────────────────
def build_list_with_cycle(vals: list, pos: int) -> Optional[ListNode]:
    if not vals:
        return None
    
    head = ListNode(vals[0])
    curr = head
    nodes = [head]
    
    for val in vals[1:]:
        curr.next = ListNode(val)
        curr = curr.next
        nodes.append(curr)
        
    if pos != -1:
        curr.next = nodes[pos]
        
    return head

# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([3, 2, 0, -4], 1, True),
        ([1, 2],        0, True),
        ([1],          -1, False),
        ([],           -1, False),
        ([1, 2, 3, 4], -1, False),
        ([1, 1, 1, 1],  2, True)
    ]

    passed = 0
    for i, (vals, pos, expected) in enumerate(test_cases, 1):
        head = build_list_with_cycle(vals, pos)
        result = sol.hasCycle(head)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: {vals}, pos={pos} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
