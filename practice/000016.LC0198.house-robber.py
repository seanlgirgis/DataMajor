# ============================================================
# 000016 | LC 0198 — House Robber
# Pattern   : Dynamic Programming — 1D, Adjacent Constraint
# Difficulty : Medium
# ============================================================
# Time Complexity:
#   O(n) — single pass through the array.
#
# Space Complexity:
#   O(1) extra — we reuse the input array as the DP table.
#   If mutating input is forbidden, use two variables (prev2, prev1).
# ============================================================
# Problem:
#   You are a robber planning to rob houses along a street.
#   Each house has a certain amount of money stashed.
#   Adjacent houses have a security system — robbing two
#   adjacent houses triggers an alarm.
#
#   Given an integer array nums where nums[i] is the amount
#   of money in the i-th house, return the maximum amount
#   you can rob WITHOUT robbing two adjacent houses.
#
# Constraints:
#   1 <= nums.length <= 100
#   0 <= nums[i] <= 400
#
# Examples:
#   nums = [1, 2, 3, 1]        ->  4   (rob house 0 + house 2)
#   nums = [2, 7, 9, 3, 1]     ->  12  (rob house 0, 2, 4)
#   nums = [2, 1, 1, 2]        ->  4   (rob house 0 + house 3)
# ============================================================
# Key Insight:
#   At each house i, you face exactly two choices:
#     1. SKIP house i  ->  best you had at i-1 carries forward
#     2. ROB  house i  ->  nums[i] + best you had at i-2 (can't touch i-1)
#   Take the max of the two. Build forward, one house at a time.
#
#   Recurrence:
#     dp[0] = nums[0]
#     dp[1] = max(nums[0], nums[1])
#     dp[i] = max(dp[i-1], nums[i] + dp[i-2])   for i >= 2
#
#   After the sweep, dp[-1] holds the global maximum.
# ============================================================
# Interviewer follow-ups:
#   Q: "Can you avoid mutating the input?"
#   A: Use two variables: prev2, prev1 = 0, 0.
#      Each step: curr = max(prev1, nums[i] + prev2); prev2=prev1; prev1=curr
#      O(1) space, same O(n) time.
#
#   Q: "What if the houses are arranged in a circle?" (LC 0213)
#   A: Run rob() twice — once on nums[:-1], once on nums[1:].
#      Return max of the two (can't rob first AND last simultaneously).
#
#   Q: "Why not greedy (always pick the bigger neighbour)?"
#   A: Greedy fails. [2,1,1,2] — greedy picks index 0 (2), then index 3 (2)
#      = 4, which happens to be right. But [2,10,3,10,2] — greedy picks 10,
#      10 = 20, but correct is 2+3+2=7? No wait — correct is 10+10=20 which
#      IS greedy here. Counter: [1,3,1,3,100] — greedy picks 3+3=6, DP gets
#      3+100=103. Greedy breaks whenever a small house separates two big ones.
# ============================================================


class Solution:
    def rob(self, nums: list[int]) -> int:
        # Re-use nums[] as the DP table in place — O(1) extra space.
        # nums[i] will hold: max loot achievable considering houses 0..i
        for i in range(1, len(nums)):
            if i == 1:
                nums[1] = max(nums[1], nums[0])     # best of first two
            else:
                nums[i] = max(nums[i] + nums[i-2],  # rob this house
                              nums[i-1])             # skip this house
        return nums[-1]                              # global best


# ── Two-variable variant (no mutation, O(1) space) ───────────
# class Solution:
#     def rob(self, nums: list[int]) -> int:
#         prev2 = prev1 = 0
#         for n in nums:
#             curr = max(prev1, n + prev2)
#             prev2, prev1 = prev1, curr
#         return prev1


# ── Tests ────────────────────────────────────────────────────
import copy

if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1, 2, 3, 1],       4),   # rob index 0,2
        ([2, 7, 9, 3, 1],   12),   # rob index 0,2,4
        ([2, 1, 1, 2],       4),   # rob index 0,3
        ([1],                1),   # single house
        ([0],                0),   # single zero house
        ([0, 0],             0),   # all zeros
        ([5, 1, 1, 5],      10),   # rob first and last
        ([1, 3, 1, 3, 100], 103),  # big value at end — greedy would fail
    ]

    passed = 0
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = sol.rob(copy.copy(nums))
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: {nums} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
