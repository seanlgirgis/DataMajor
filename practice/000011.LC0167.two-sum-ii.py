# ============================================================
# 000011 | LC 0167 — Two Sum II (Input Array Is Sorted)
# Pattern   : Two Pointers (squeeze from both ends)
# Difficulty : Medium
# Time       : O(n)  — single pass, each pointer moves at most n steps
# Space      : O(1)  — no extra storage, satisfies problem constraint
# ============================================================
# Problem:
#   Given a 1-indexed sorted array of integers, find two numbers
#   that add up to target. Return their indices as [i, j] (1-indexed).
#   Exactly one solution exists. Must use O(1) extra space.
#
# Examples:
#   nums = [2, 7, 11, 15], target = 9   ->  [1, 2]
#   nums = [2, 3, 4],      target = 6   ->  [1, 3]
#   nums = [-1, 0],        target = -1  ->  [1, 2]
# ============================================================
# Key Insight:
#   Array is SORTED — squeeze two pointers from both ends.
#   sum > target: move right left  (reduce sum)
#   sum < target: move left right  (increase sum)
#   sum == target: found — return 1-indexed positions.
#   Guaranteed one solution so loop always terminates.
# ============================================================

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left  = 0
        right = len(numbers) - 1

        while right > left:
            cursum = numbers[left] + numbers[right]
            if cursum > target:
                right -= 1              # sum too big — shrink from right
            elif cursum < target:
                left  += 1              # sum too small — grow from left
            else:
                break                   # found

        return [left + 1, right + 1]    # convert to 1-indexed


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([2, 7, 11, 15],     9,  [1, 2]),   # standard
        ([2, 3, 4],          6,  [1, 3]),   # skip middle
        ([-1, 0],           -1,  [1, 2]),   # negatives
        ([1, 2, 3, 4, 5],    9,  [4, 5]),   # end of array
        ([1, 2, 3, 4, 5],    3,  [1, 2]),   # start of array
        ([-3, -1, 0, 2, 5],  1,  [2, 4]),   # mixed signs (-1+2=1, unique)
        ([1, 3, 5, 7, 11],  18,  [4, 5]),   # end pair (7+11=18, unique)
    ]

    passed = 0
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = sol.twoSum(nums, target)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: {nums}, target={target} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
