# ============================================================
# 000037 | LC 0100 --- Same Tree
# Pattern   : Trees (DFS)
# Difficulty : Easy
# ============================================================
# Time Complexity:  O(n) --- where n is the minimum number of nodes in p or q
# Space Complexity: O(h) --- where h is the minimum height of the trees (for the recursion stack)
# ============================================================
# Problem:
#   Given the roots of two binary trees p and q, write a function to
#   check if they are the same or not.
#   Two binary trees are considered the same if they are structurally
#   identical, and the nodes have the same value.
#
# Examples:
#   p = [1,2,3], q = [1,2,3]  ->  True
#   p = [1,2], q = [1,null,2] ->  False
#   p = [1,2,1], q = [1,1,2]  ->  False
#
# Constraints:
#   The number of nodes in both trees is in the range [0, 100].
#   -10^4 <= Node.val <= 10^4
# ============================================================
# Key Insight:
#   Use Depth-First Search (DFS) recursion to traverse both trees
#   simultaneously.
#   - Base Case 1: Both nodes are null -> They match. Return True.
#   - Base Case 2: Only one node is null -> They don't match. Return False.
#   - Base Case 3: Values differ -> They don't match. Return False.
#   - Recursive Step: Return (left branches match) AND (right branches match).
# ============================================================

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # DFS Recursive comparison
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Case 1: If both are None, we reached the end of identical branches
        if not p and not q:
            return True
        
        # Base Case 2: If only one is None, there is a structural imbalance
        if not p or not q:
            return False
        
        # Base Case 3: If the values at the current nodes are different
        if p.val != q.val:
            return False
            
        # Recursive Step: Check both left branches and right branches
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# ── Helpers ──────────────────────────────────────────────────
def build_tree(vals: list) -> Optional[TreeNode]:
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = [root]
    i = 1
    while queue and i < len(vals):
        node = queue.pop(0)
        
        # Left child
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
        
    return root

# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, None, 2], False),
        ([1, 2, 1], [1, 1, 2], False),
        ([], [], True),
        ([1], [1], True),
        ([10, 5, 15], [10, 5, None], False),
        ([10, 5, 15], [10, 5, 15, None, None, 20], False)
    ]

    passed = 0
    for i, (vals_p, vals_q, expected) in enumerate(test_cases, 1):
        p_root = build_tree(vals_p)
        q_root = build_tree(vals_q)
        result = sol.isSameTree(p_root, q_root)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: p={vals_p}, q={vals_q} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
