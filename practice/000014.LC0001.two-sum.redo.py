# ============================================================
# 000014 | LC 0001 — Two Sum  [REDO DRILL]
# Pattern   : Hash Map (One Pass)
# Difficulty : Easy
# Time       : O(n)  — single pass through array
# Space      : O(n)  — hash map stores up to n elements
# ============================================================
# Problem:
#   Given an array of integers and a target, return the indices
#   of the two numbers that add up to target.
#   Each input has exactly one solution. Cannot use same element twice.
#   Return answer in any order.
#
# Examples:
#   nums = [2, 7, 11, 15], target = 9   ->  [0, 1]
#   nums = [3, 2, 4],      target = 6   ->  [1, 2]
#   nums = [3, 3],         target = 6   ->  [0, 1]
# ============================================================
# Key Insight:
#   For each num, the complement is (target - num).
#   Store each number's index in a hash map as you go.
#   If complement already in map — you have your pair.
#   One pass: check first, store second (handles duplicates correctly).
# ============================================================

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}                               # num -> index
        for i, num in enumerate(nums):
            if (target - num) in seen:          # complement already visited
                return [seen[target - num], i]
            seen[num] = i                       # store current for future lookup


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([2, 7, 11, 15],  9,  [0, 1]),   # standard
        ([3, 2, 4],       6,  [1, 2]),   # not index 0
        ([3, 3],          6,  [0, 1]),   # duplicate values
        ([1, 2, 3, 4, 5], 9,  [3, 4]),   # end of array
        ([0, 4, 3, 0],    0,  [0, 3]),   # zeros
        ([-3, 4, 3, 90],  0,  [0, 2]),   # negatives
        ([1, 5, 8, 3],   11,  [2, 3]),   # middle pair
    ]

    passed = 0
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = sol.twoSum(nums, target)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: {nums}, target={target} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
