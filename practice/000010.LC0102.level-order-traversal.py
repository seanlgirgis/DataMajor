# ============================================================
# 000010 | LC 0102 — Binary Tree Level Order Traversal
# Pattern   : Trees / BFS (Level by Level)
# Difficulty : Medium
# Time       : O(n)  — every node visited once
# Space      : O(n)  — queue holds at most one full level (widest level)
# ============================================================
# Problem:
#   Given the root of a binary tree, return the level-order
#   traversal of its nodes' values as a list of lists —
#   one inner list per level, left to right.
#
# Examples:
#   [3, 9, 20, null, null, 15, 7]  ->  [[3], [9, 20], [15, 7]]
#   [1]                            ->  [[1]]
#   []                             ->  []
# ============================================================
# Key Insight:
#   Two-list BFS: `stack` = current level nodes, `stack_next` = next level.
#   For each level, drain current → collect values + queue children.
#   Swap lists and repeat until no children remain.
#   Equivalent to the deque + range(len(queue)) approach but avoids deque.
# ============================================================

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        ret = []
        if not root:
            return ret

        stack = [root]                  # current level's nodes

        while True:
            level      = []             # values at this level
            stack_next = []             # nodes for the next level

            for node in stack:
                if node.left:
                    stack_next.append(node.left)    # cache left child
                if node.right:
                    stack_next.append(node.right)   # cache right child
                level.append(node.val)

            ret.append(level)

            if not stack_next:
                break                   # no more levels
            stack = stack_next          # advance to next level

        return ret


# ── Helpers ──────────────────────────────────────────────────
def build(vals: list) -> Optional[TreeNode]:
    if not vals or vals[0] is None: return None
    root  = TreeNode(vals[0])
    queue = deque([root])
    i = 1
    while queue and i < len(vals):
        node = queue.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i]); queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i]); queue.append(node.right)
        i += 1
    return root

# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([3, 9, 20, None, None, 15, 7],  [[3], [9, 20], [15, 7]]),  # standard
        ([1],                            [[1]]),                     # single node
        ([],                             []),                        # empty
        ([1, 2, 3],                      [[1], [2, 3]]),             # 2 levels
        ([1, 2, 3, 4, 5, 6, 7],         [[1], [2, 3], [4, 5, 6, 7]]),  # full 3-level
        ([1, None, 2, None, 3],          [[1], [2], [3]]),           # right-skewed
    ]

    passed = 0
    for i, (vals, expected) in enumerate(test_cases, 1):
        root   = build(vals)
        result = sol.levelOrder(root)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: {vals}")
        print(f"        -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
