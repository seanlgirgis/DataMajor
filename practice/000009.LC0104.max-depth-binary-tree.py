# ============================================================
# 000009 | LC 0104 — Maximum Depth of Binary Tree
# Pattern   : Trees / DFS (Recursive)
# Difficulty : Easy
# Time       : O(n)  — visit every node once
# Space      : O(h)  — call stack depth = tree height (O(log n) balanced, O(n) worst)
# ============================================================
# Problem:
#   Given the root of a binary tree, return its maximum depth.
#   Maximum depth = number of nodes along the longest path
#   from root down to the farthest leaf node.
#
# Examples:
#   [3, 9, 20, null, null, 15, 7]  ->  3
#   [1, null, 2]                   ->  2
#   []                             ->  0
# ============================================================
# Key Insight:
#   Classic post-order DFS recursion.
#   Two questions to answer — then it writes itself:
#     1. Base case: what does null return?  -> 0
#     2. Combine:  how do left + right give depth? -> 1 + max(left, right)
# ============================================================

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0                                         # base case: null node
        return 1 + max(self.maxDepth(root.left),
                       self.maxDepth(root.right))           # 1 (current) + deeper child


# ── Helpers ──────────────────────────────────────────────────
def build(vals: list) -> Optional[TreeNode]:
    """Build tree from LeetCode level-order list. None = missing node."""
    if not vals or vals[0] is None:
        return None
    root  = TreeNode(vals[0])
    queue = deque([root])           # deque: popleft() is O(1), list.pop(0) is O(n)
    i = 1
    while queue and i < len(vals):
        node = queue.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root

# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([3, 9, 20, None, None, 15, 7],  3),  # standard 3-level tree
        ([1, None, 2],                   2),  # right-skewed
        ([],                             0),  # empty tree
        ([0],                            1),  # single node
        ([1, 2, 3, 4, 5],               3),  # complete tree
        ([1, 2, None, 3, None, 4, None], 4),  # left-skewed chain: 1->2->3->4
    ]

    passed = 0
    for i, (vals, expected) in enumerate(test_cases, 1):
        root   = build(vals)
        result = sol.maxDepth(root)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: {vals} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
