# ============================================================
# 000015 | LC 0200 — Number of Islands
# Pattern   : Graph Traversal — DFS on Grid (Sink / Flood-Fill)
# Difficulty : Medium
# ============================================================
# Time Complexity:
#   O(m * n) — every cell visited at most once.
#   Outer loop: O(m*n). DFS from each new island visits remaining cells.
#   Total work across ALL dfs calls combined = O(m*n), not O(m*n) per island.
#
# Space Complexity:
#   O(m * n) WORST CASE — recursion call stack depth.
#   Worst case: entire grid is one snake-shaped island.
#   The DFS recurses m*n levels deep → stack frame per cell.
#   Average case on sparse grids: O(min(m,n)).
#   NOTE: Sinking eliminates the need for a visited set (O(1) extra space
#   beyond the call stack). Tradeoff: mutates the input grid.
# ============================================================
# Problem:
#   Given an m x n grid of '1's (land) and '0's (water),
#   return the number of islands.
#   An island is surrounded by water and formed by connecting
#   adjacent land cells horizontally or vertically.
#
# Examples:
#   grid = [["1","1","1","1","0"],
#           ["1","1","0","1","0"],
#           ["1","1","0","0","0"],
#           ["0","0","0","0","0"]]  ->  1
#
#   grid = [["1","1","0","0","0"],
#           ["1","1","0","0","0"],
#           ["0","0","1","0","0"],
#           ["0","0","0","1","1"]]  ->  3
# ============================================================
# Key Insight:
#   "Sinking" pattern — when you find land, flood-fill the whole island
#   by converting all connected "1"s to "0"s. This marks them visited
#   without a separate set. Each new "1" encountered after sinking
#   must be a NEW island — increment counter and sink again.
# ============================================================
# Interviewer follow-ups:
#   Q: "What if you can't modify the input grid?"
#   A: Use a visited set() of (r,c) tuples instead of sinking.
#      Space becomes O(m*n) for the set (same asymptotic, explicit).
#
#   Q: "Can you do this iteratively?"
#   A: Yes — replace recursive dfs with a stack (DFS) or deque (BFS).
#      Avoids Python recursion limit for huge grids (sys.setrecursionlimit).
#
#   Q: "What is the recursion limit risk?"
#   A: Python default recursion limit is 1000. A 1000x1000 all-land grid
#      would hit RecursionError. Fix: iterative BFS/DFS or increase limit.
# ============================================================

import copy

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def in_boundary(x, y) -> bool:
            return 0 <= x < rows and 0 <= y < cols

        def dfs(r, c) -> None:
            if not in_boundary(r, c) or grid[r][c] != "1":
                return                          # out of bounds or water/already sunk
            grid[r][c] = "0"                    # sink — mark visited by converting to water
            dfs(r - 1, c)                       # explore up
            dfs(r + 1, c)                       # explore down
            dfs(r, c - 1)                       # explore left
            dfs(r, c + 1)                       # explore right

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":           # new unvisited land = new island
                    islands += 1
                    dfs(i, j)                   # sink the entire island

        return islands


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]], 1),          # one big island

        ([["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]], 3),          # three islands

        ([["1","1","1"],
          ["0","1","0"],
          ["1","1","1"]], 1),                  # ring shape — still 1

        ([["1","0","1","0","1"]], 3),           # single row

        ([["0","0","0"],
          ["0","0","0"]], 0),                  # all water

        ([["1"]], 1),                           # single cell land
        ([["0"]], 0),                           # single cell water

        ([["1","0"],
          ["0","1"]], 2),                      # diagonal — not connected
    ]

    passed = 0
    for i, (grid, expected) in enumerate(test_cases, 1):
        result = sol.numIslands(copy.deepcopy(grid))
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: {len(grid)}x{len(grid[0])} grid -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
