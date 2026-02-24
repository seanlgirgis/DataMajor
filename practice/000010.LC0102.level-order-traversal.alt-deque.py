# ============================================================
# 000010 | LC 0102 — Binary Tree Level Order Traversal
# Pattern   : Trees / BFS (deque + level snapshot)
# Difficulty : Medium
# Time       : O(n)  — every node visited once
# Space      : O(n)  — queue holds at most one full level
# ============================================================
# ALTERNATIVE SOLUTION — deque + range(len(queue)) snapshot
# Compare with 000010.LC0102.py (two-list approach)
# ============================================================
# Key Insight:
#   `range(len(queue))` at the START of each while iteration
#   freezes the current level size before children are added.
#   Everything inside that for loop belongs to the same level.
#   Children appended during the loop belong to the next level.
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
        if not root:
            return []

        result = []
        queue  = deque([root])

        while queue:
            level = []

            for _ in range(len(queue)):         # snapshot: freeze level size
                node = queue.popleft()
                level.append(node.val)
                if node.left:  queue.append(node.left)   # next level
                if node.right: queue.append(node.right)  # next level

            result.append(level)

        return result


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
        ([3, 9, 20, None, None, 15, 7],  [[3], [9, 20], [15, 7]]),
        ([1],                            [[1]]),
        ([],                             []),
        ([1, 2, 3],                      [[1], [2, 3]]),
        ([1, 2, 3, 4, 5, 6, 7],         [[1], [2, 3], [4, 5, 6, 7]]),
        ([1, None, 2, None, 3],          [[1], [2], [3]]),
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
