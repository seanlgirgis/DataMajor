# First, let's define a simple Tree Node class
from __future__ import annotations       #Python 3.10



from collections import deque

class TreeNode:
    def __init__(self, val=0, left:TreeNode=None, right:TreeNode=None):
        self.val = val
        self.left:TreeNode  = left
        self.right:TreeNode = right

# Let's build a simple tree:
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print("Tree built successfully!")


def bfs_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root]) # 1. Start the queue with the root
    
    while queue:
        # 2. Pop from the FRONT of the line (left side)
        current_node = queue.popleft()
        result.append(current_node.val)
        
        # 3. Add children to the BACK of the line (right side)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
            
    return result

print("BFS Order:", bfs_traversal(root))