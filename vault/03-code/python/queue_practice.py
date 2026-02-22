# Practice: Queue
# Linked Note: [[01-concepts/python/queue|Queue]]

from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    if not root:
        return []
    
    queue = deque([root])
    result = []

    while queue:
        level_size = len(queue)
        level_list = []
        
        for _ in range(level_size):   
            node = queue.popleft()
            level_list.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(level_list)
        
    return result

def practice_queue():
    """Small exercise harness for Queues."""
    
    # 1. Enqueue, Dequeue, Peek
    q = deque()
    q.append(10)
    q.append(20)
    q.append(30)
    
    assert q[0] == 10, "Peek failed"     # Peek at the front
    val = q.popleft()                    # Dequeue
    assert val == 10, "Dequeue failed"
    
    q.append(40)                         # Enqueue again
    assert list(q) == [20, 30, 40], "Queue state invalid"
    print("✅ Core FIFO Operations Passed!")
    
    # 2. Graph BFS
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": []
    }
    
    bfs_result = bfs(graph, "A")
    assert bfs_result == ['A', 'B', 'C', 'D'], "Graph BFS failed"
    print("✅ Graph BFS Passed!")
    
    # 3. Tree Level Order Traversal
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    tree_result = level_order(root)
    assert tree_result == [[1], [2, 3], [4, 5]], "Tree Level Order failed"
    print("✅ Tree Level-Order Traversal Passed!")


if __name__ == "__main__":
    print("Starting Queue Practice Exercises...\n")
    practice_queue()
    print("\nAll Queue tests safely completed!")
