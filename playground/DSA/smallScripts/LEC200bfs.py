
# First solution
# use a set as a very fast seatch datastructure and store Tuples of visited 
# in a cell.. 
#   If it is a land ("1") and not visited ... 
#       then we have found an island (increment islamds) and we can start a bf search
# use bfs
#   - Instantiate a queue with the current cell (r, c) and mark it as visited
#   - While the queue is not empty:
#       - Pop the first cell (row, col) from the queue
#       - For each of the four possible directions (up, down, left, right):
#           - Each cell is represented by  a delta  [[-1, 0], [1, 0], [0, -1], [0, 1]]
#           - for a delta tuple calculate x, y of tje cell
#           - Check if the cell (x, y) is within the grid boundaries, is land ("1"), and has not been visited:
#            - If so, add the cell (x, y) to the queue and mark it as visited
#         

from collections import deque

class Solution:
    def bfs(self, r, c):
        queue = deque([(r, c)])
        self.visited.add((r, c))
        while queue:
            row, col = queue.popleft()           # O(1) now ✅
            for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
                x, y = row + dr, col + dc
                if (0 <= x < self.rows and        # cleaner bounds ✅
                    0 <= y < self.cols and
                    self.grid[x][y] == '1' and
                    (x, y) not in self.visited):
                    queue.append((x, y))
                    self.visited.add((x, y))

    def numIslands(self, grid) -> int:
        self.visited = set()                      # reset here ✅
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        islands = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == '1' and (r, c) not in self.visited:
                    islands += 1
                    self.bfs(r, c)
        return islands
    

# Test Case 2: 3 islands
grid2 = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]

print(Solution().numIslands(grid2))