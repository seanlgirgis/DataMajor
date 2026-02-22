# Practice: Deque
# Linked Note: [[01-concepts/python/deque|deque]]

from collections import deque

def practice_deque_practice():
    """Small exercise harness for Deque."""
    
    # 1. Initialize empty deque
    d = deque()
    
    # 2. Add elements 1, 2, 3 to the RIGHT (end)
    d.append(1)
    d.append(2)
    d.append(3)
    assert list(d) == [1, 2, 3], "Failed right append"
    
    # 3. Add element 0 to the LEFT (front)  
    d.appendleft(0)
    assert list(d) == [0, 1, 2, 3], "Failed left append"
    
    # 4. Pop an element from the RIGHT
    right_val = d.pop()
    assert right_val == 3, "Failed pulling from right"
    assert list(d) == [0, 1, 2], "Failed updating right"

    # 5. Pop an element from the LEFT 
    left_val = d.popleft()
    assert left_val == 0, "Failed pulling from left"
    assert list(d) == [1, 2], "Failed updating left"

    print("✅ Core Operations Passed!")

    # ---------------------------------------------
    # 6. Test MaxLen (Sliding Window Shortcut)
    # ---------------------------------------------
    bounded_d = deque(maxlen=3)
    bounded_d.extend([10, 20, 30])
    
    # Appending a 4th item should evict '10' automatically
    bounded_d.append(40)
    assert list(bounded_d) == [20, 30, 40], "Failed maxlen auto-eviction"
    
    print("✅ MaxLen Operations Passed!")
    
    # ---------------------------------------------
    # 7. Basic BFS Queue Simulation
    # ---------------------------------------------
    bfs_queue = deque(["Start_Node"])
    processed_order = []
    
    while bfs_queue:
        # Standard BFS pulls from the left!
        current_node = bfs_queue.popleft() 
        processed_order.append(current_node)
        
        # Simulate adding children to the end of the queue
        if current_node == "Start_Node":
            bfs_queue.append("Child_A")
            bfs_queue.append("Child_B")
            
    assert processed_order == ["Start_Node", "Child_A", "Child_B"], "Failed BFS Ordering!"
    print("✅ BFS Queue Simulation Passed!")


if __name__ == "__main__":
    print("Starting Deque Practice Exercises...\n")
    practice_deque_practice()
    print("\nAll tests safely completed!")
