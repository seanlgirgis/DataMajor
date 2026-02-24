# ============================================================
# 000035 | LC 0074 --- Search a 2D Matrix
# Pattern   : Binary Search
# Difficulty : Medium
# ============================================================
# Time Complexity:  O(log(m * n)) --- standard binary search over m*n elements
# Space Complexity: O(1) --- only tracking pointers, no extra array created
# ============================================================
# Problem:
#   You are given an m x n integer matrix matrix with the following two properties:
#     - Each row is sorted in non-decreasing order.
#     - The first integer of each row is greater than the last integer of the previous row.
#   Given an integer target, return true if target is in matrix or false otherwise.
#   You must write a solution in O(log(m * n)) time complexity.
#
# Examples:
#   matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3  ->  True
#   matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13 ->  False
#
# Constraints:
#   m == matrix.length
#   n == matrix[i].length
#   1 <= m, n <= 100
#   -10^4 <= matrix[i][j], target <= 10^4
# ============================================================
# Key Insight:
#   Because the rows are sorted AND the first element of each row
#   is strictly greater than the last element of the previous row,
#   we can treat the entire 2D matrix as one giant sorted 1D array
#   of length `m * n`.
#   
#   To do standard Binary Search without physically transforming it:
#   Map the 1D `mid` index back to 2D coordinates using:
#     row = mid // COLS
#     col = mid % COLS
# ============================================================

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #problem screams binary search
        #Find a way to convert matrix to List
        #Since creating new space is processing and space.. do it on the fly
        #
        rows,cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols -1
        
        while left <= right:
            mid = (left + right) //2
            midv = matrix[mid//cols][mid%cols]
            if midv == target:
                return True
            elif midv < target:
                left = mid + 1
            else:
                right = mid -1
        
        
        #assume the worst. If we found it we would have returned
        #Solution is always at mid in binary search
        return False



# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True),
        ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False),
        ([[1]], 1, True),
        ([[1]], 2, False),
        ([[1,3]], 3, True)
    ]

    passed = 0
    for i, (matrix, target, expected) in enumerate(test_cases, 1):
        result = sol.searchMatrix(matrix, target)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: target={target} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
