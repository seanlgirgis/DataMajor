# Practice: Graph Traversal (BFS & DFS)
# Linked Note: [[01-concepts/python/graph-traversal|Graph Traversal]]

from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            # Reverse for same order as typical recursive
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    return order


def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    order = [node]

    for neighbor in graph[node]:
        if neighbor not in visited:
            order.extend(dfs_recursive(graph, neighbor, visited))
    return order


def num_islands(grid):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols: return
        if grid[r][c] == "0" or (r, c) in visited: return
        
        visited.add((r, c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1
                dfs(r, c)
                
    return islands


def practice_graph_traversal():
    """Small exercise harness for Graph Traversal."""
    
    # 1. Traversal Setup
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": []
    }
    
    # BFS
    bfs_result = bfs(graph, "A")
    assert bfs_result == ['A', 'B', 'C', 'D', 'E', 'F'], "BFS Ordering Failed"
    print("✅ BFS Traversal Passed!")
    
    # DFS (Iterative & Recursive)
    dfs_rec_result = dfs_recursive(graph, "A")
    dfs_iter_result = dfs_iterative(graph, "A")
    # Expected recursive tree plunge: A -> B -> D then E -> F then C -> F (already visited)
    assert dfs_rec_result == ['A', 'B', 'D', 'E', 'F', 'C'], "DFS Recursive Ordering Failed"
    assert dfs_iter_result == dfs_rec_result, "DFS Iterative did not match Recursive ordering"
    print("✅ DFS Traversals Passed!")
    
    # 2. Number of Islands (Grid DFS)
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    islands = num_islands(grid)
    assert islands == 3, f"Expected 3 islands, found {islands}"
    print("✅ Number of Islands (Grid DFS Pattern) Passed!")


if __name__ == "__main__":
    print("Starting Graph Traversal Practice Exercises...\n")
    practice_graph_traversal()
    print("\nAll Graph Traversal tests safely completed!")
