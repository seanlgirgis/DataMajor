# ============================================================
# 000008 | LC 0704 — Binary Search
# Pattern   : Binary Search (Classic Template)
# Difficulty : Easy
# Time       : O(log n) — search space halved each iteration
# Space      : O(1)     — no extra memory
# ============================================================
# Problem:
#   Given a sorted array of distinct integers and a target,
#   return the index of target. If not found, return -1.
#   You MUST write an O(log n) solution.
#
# Examples:
#   nums = [-1, 0, 3, 5, 9, 12],  target = 9  ->  4
#   nums = [-1, 0, 3, 5, 9, 12],  target = 2  -> -1
#   nums = [5],                    target = 5  ->  0
# ============================================================
# Key Insight:
#   Classic two-pointer binary search. At each step, compare
#   nums[mid] to target and eliminate half the search space.
#   Template: while right >= left  (inclusive both ends)
#     - found:          return mid
#     - target > mid:   left  = mid + 1  (search right half)
#     - target < mid:   right = mid - 1  (search left half)
#   Loop exits when left > right — target not in array.
# ============================================================

import sys

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while right >= left:                    # inclusive: both pointers valid
            mid = (left + right) // 2           # integer midpoint
            if nums[mid] == target:
                return mid                      # found
            elif target > nums[mid]:
                left = mid + 1                  # target in right half
            else:
                right = mid - 1                 # target in left half

        return -1                               # not found


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([-1, 0, 3, 5, 9, 12],  9,   4),   # target in middle-right
        ([-1, 0, 3, 5, 9, 12],  2,  -1),   # target not present
        ([5],                    5,   0),   # single element — found
        ([5],                    3,  -1),   # single element — not found
        ([-1, 0, 3, 5, 9, 12], -1,   0),   # target at index 0 (left boundary)
        ([-1, 0, 3, 5, 9, 12], 12,   5),   # target at last index (right boundary)
        ([1, 2, 3, 4, 5, 6],    1,   0),   # leftmost
        ([1, 2, 3, 4, 5, 6],    6,   5),   # rightmost
        ([2, 5],                 5,   1),   # two elements
        ([1, 3, 5, 7, 9, 11],   7,   3),   # even-length, mid hit
    ]

    passed = 0
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = sol.search(nums, target)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i:2d}: {nums}, target={target} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
