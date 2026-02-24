# ============================================================
# 000038 | LC 0015 --- 3Sum
# Pattern   : Two Pointers / Sorting
# Difficulty : Medium
# ============================================================
# Problem:
#   Given an integer array nums, return all the triplets
#   [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
#   and nums[i] + nums[j] + nums[k] == 0.
#
#   Notice that the solution set must not contain duplicate triplets.
#
# Examples:
#   nums = [-1,0,1,2,-1,-4]  ->  [[-1,-1,2],[-1,0,1]]
#   nums = [0,1,1]           ->  []
#   nums = [0,0,0]           ->  [[0,0,0]]
#
# Constraints:
#   3 <= nums.length <= 3000
#   -10^5 <= nums[i] <= 10^5
# ============================================================

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]])
    ]

    passed = 0
    for i, (nums, expected) in enumerate(test_cases, 1):
        # Sort the results so order doesn't fail the test
        result = sol.threeSum(nums)
        if isinstance(result, list):
            result = sorted([sorted(triplet) for triplet in result])
        expected_sorted = sorted([sorted(triplet) for triplet in expected])
        
        status = "PASS" if result == expected_sorted else f"FAIL (expected {expected_sorted})"
        print(f"Test {i}: {nums} -> {result}  {status}")
        if result == expected_sorted:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
