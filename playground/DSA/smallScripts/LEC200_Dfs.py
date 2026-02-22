from collections import deque

class Solution:

    def dfs(self, r, c):
        stack = [(r, c)]                              # ← list as stack
        self.visited.add((r, c))
        while stack:
            row, col = stack.pop()                    # ← pop from TOP (LIFO)
            for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
                x, y = row + dr, col + dc
                if (0 <= x < self.rows and
                    0 <= y < self.cols and
                    self.grid[x][y] == '1' and
                    (x, y) not in self.visited):
                    stack.append((x, y))              # ← push to TOP
                    self.visited.add((x, y))

    def numIslands(self, grid) -> int:
        self.visited = set()
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        islands = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == '1' and (r, c) not in self.visited:
                    islands += 1
                    self.dfs(r, c)                    # ← just renamed
        return islands


grid2 = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]

print(Solution().numIslands(grid2)) 