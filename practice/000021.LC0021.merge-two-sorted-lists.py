# ============================================================
# 000021 | LC 0021 — Merge Two Sorted Lists
# Pattern   : Linked List — Dummy Head / Two-Pointer Merge
# Difficulty : Easy
# ============================================================
# Time Complexity:  O(m + n) — visit every node exactly once
# Space Complexity: O(1)     — only pointers, no extra allocation
# ============================================================
# Problem:
#   You are given the heads of two sorted linked lists list1 and list2.
#   Merge the two lists into one sorted list by splicing nodes together.
#   Return the head of the merged linked list.
#
# Examples:
#   list1 = [1,2,4], list2 = [1,3,4]  ->  [1,1,2,3,4,4]
#   list1 = [],       list2 = []       ->  []
#   list1 = [],       list2 = [0]      ->  [0]
# ============================================================
# Key Insight:
#   Use a dummy head node to avoid special-casing the first node.
#   Maintain a curr pointer at the tail of the merged list.
#   At each step: compare l1.val vs l2.val, attach the smaller,
#   advance that list's pointer.
#   When one list is exhausted, splice the remainder directly —
#   it's already sorted, no need to loop.
# ============================================================
# Interviewer follow-ups:
#   Q: "Can you do it recursively?"
#   A: Yes. Base case: if either is None, return the other.
#      Recursive case: pick the smaller head, set its .next to
#      the recursive merge of the rest. O(m+n) time, O(m+n) space
#      (call stack). Iterative is O(1) space — preferred.
#
#   Q: "What if the lists are not sorted?"
#   A: Can't use this approach. Would need to collect all nodes,
#      sort them, rebuild — O((m+n) log(m+n)).
#
#   Q: "Why use a dummy head?"
#   A: Avoids an if/else to handle "what is the head of the merged
#      list?" before the loop. dummy.next always holds the answer.
# ============================================================


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()           # dummy head — simplifies start-of-list logic
        curr = head                 # tail pointer of the merged list so far

        while l1 or l2:
            if l1 is None:          # l1 exhausted — splice remaining l2
                curr.next = l2
                return head.next
            if l2 is None:          # l2 exhausted — splice remaining l1
                curr.next = l1
                return head.next
            if l1.val < l2.val:     # l1 is smaller — attach it
                curr.next = l1
                l1 = l1.next
            else:                   # l2 is smaller or equal — attach it
                curr.next = l2
                l2 = l2.next
            curr = curr.next        # advance tail

        return head.next            # dummy.next = true head of merged list


# ── Helpers ──────────────────────────────────────────────────
def to_list(head: ListNode) -> list:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def to_linked(vals: list) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1,2,4],  [1,3,4],  [1,1,2,3,4,4]),   # standard merge
        ([],       [],        []),               # both empty
        ([],       [0],       [0]),              # one empty
        ([0],      [],        [0]),              # other empty
        ([1,3,5],  [2,4,6],  [1,2,3,4,5,6]),   # perfectly interleaved
        ([1,1,1],  [1,1,1],  [1,1,1,1,1,1]),   # all same values
        ([5],      [1,2,3],  [1,2,3,5]),        # single vs multi
    ]

    passed = 0
    for i, (l1_vals, l2_vals, expected) in enumerate(test_cases, 1):
        l1 = to_linked(l1_vals)
        l2 = to_linked(l2_vals)
        result = to_list(sol.mergeTwoLists(l1, l2))
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: {l1_vals} + {l2_vals} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
