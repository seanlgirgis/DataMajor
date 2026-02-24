# ============================================================
# 000022 | LC 0226 — Invert Binary Tree
# Pattern   : Tree — DFS Recursive (swap at every node)
# Difficulty : Easy
# ============================================================
# Time Complexity:  O(n) — visit every node exactly once
# Space Complexity: O(h) — recursion stack, h = tree height
#                   O(log n) average, O(n) worst (skewed tree)
# ============================================================
# Problem:
#   Given the root of a binary tree, invert the tree
#   (mirror it), and return its root.
#
# Examples:
#   Input:       4              Output:      4
#               / \                         / \
#              2   7                       7   2
#             / \ / \                     / \ / \
#            1  3 6  9                   9  6 3  1
#
#   root = [4,2,7,1,3,6,9]  ->  [4,7,2,9,6,3,1]
#   root = [2,1,3]          ->  [2,3,1]
#   root = []               ->  []
# ============================================================
# Key Insight:
#   Mirror = swap left and right at EVERY node, recursively.
#   Post-order (or pre-order) both work:
#     1. Recurse into children to get their inverted subtrees
#     2. Assign them swapped: root.left, root.right = right, left
#   Python evaluates the entire right-hand side before assigning,
#   so no temp variable needed — the one-liner is safe and correct.
# ============================================================
# Interviewer follow-ups:
#   Q: "Can you do it iteratively?"
#   A: Yes — BFS with a queue. For each node dequeued, swap its
#      children, then enqueue both children. O(n) time, O(n) space.
#
#   Q: "Pre-order vs post-order — does it matter?"
#   A: No. Swapping top-down (pre) or bottom-up (post) both produce
#      the same result. The swap at each node is independent.
#
#   Q: "What is the base case?"
#   A: root is None — return None. Handles empty tree and leaf
#      children without extra checks.
# ============================================================


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:                            # base case: empty / leaf child
            return None
        root.left, root.right = (                  # swap children (RHS evaluated first)
            self.invertTree(root.right),
            self.invertTree(root.left)
        )
        return root


# ── Helpers ──────────────────────────────────────────────────
def build(vals: list) -> TreeNode:
    """Build tree from level-order list. None = missing node."""
    if not vals:
        return None
    from collections import deque
    root = TreeNode(vals[0])
    queue = deque([root])
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

def level_order(root: TreeNode) -> list:
    """Return level-order values, skipping None nodes."""
    if not root:
        return []
    from collections import deque
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:  queue.append(node.left)
        if node.right: queue.append(node.right)
    return result


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([4,2,7,1,3,6,9],  [4,7,2,9,6,3,1]),   # full tree
        ([2,1,3],          [2,3,1]),             # 3-node tree
        ([],               []),                  # empty tree
        ([1],              [1]),                 # single node
        ([1,2],            [1,2]),               # left-only -> right-only (level_order skips Nones)
        ([3,1,2],          [3,2,1]),             # swap two children
    ]

    passed = 0
    for i, (vals, expected) in enumerate(test_cases, 1):
        root = build(vals)
        result_root = sol.invertTree(root)
        result = level_order(result_root)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: {vals} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
