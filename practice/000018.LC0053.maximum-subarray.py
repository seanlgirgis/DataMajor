# ============================================================
# 000018 | LC 0053 — Maximum Subarray
# Pattern   : Dynamic Programming — Kadane's Algorithm
# Difficulty : Medium
# ============================================================
# Time Complexity:
#   O(n) — single pass through the array.
#
# Space Complexity:
#   O(1) — two variables (curr_sum, max_sum), no extra storage.
# ============================================================
# Problem:
#   Given an integer array nums, find the subarray with the
#   largest sum and return its sum.
#   A subarray is a contiguous part of the array.
#
# Constraints:
#   1 <= nums.length <= 100,000
#   -10,000 <= nums[i] <= 10,000
#
# Examples:
#   nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  ->  6  ([4,-1,2,1])
#   nums = [1]                                ->  1
#   nums = [5, 4, -1, 7, 8]                  ->  23 (entire array)
# ============================================================
# Key Insight — Kadane's Algorithm:
#   At each position, two choices:
#     1. EXTEND: add num to current running sum (curr_sum + num)
#     2. RESTART: begin a fresh subarray at this element (num)
#   Take the max. A negative curr_sum is a liability — restart.
#   Track the global best seen so far in max_sum.
#
#   Recurrence:
#     curr_sum = max(curr_sum + num, num)
#     max_sum  = max(max_sum, curr_sum)
#
#   Initialize:
#     max_sum  = nums[0]   — handles all-negative arrays correctly
#     curr_sum = 0         — neutral start before first element
# ============================================================
# Why max_sum starts at nums[0], not -infinity or 0:
#   If all numbers are negative, the answer is the least-negative
#   single element. Starting at 0 would wrongly return 0.
#   Starting at nums[0] guarantees we return an actual element.
# ============================================================
# Interviewer follow-ups:
#   Q: "What if you also need to return the subarray indices?"
#   A: Track start, end, temp_start. When restarting (num > curr+num),
#      set temp_start = i. When updating max_sum, save temp_start as start,
#      i as end. O(n) time, O(1) extra space.
#
#   Q: "Divide and conquer approach?"
#   A: Split array in half. Answer is max of:
#      left half max, right half max, or cross-middle max.
#      O(n log n) — worse than Kadane's, but demonstrates D&C thinking.
#
#   Q: "Is this greedy or DP?"
#   A: Both labels apply. It's DP (optimal substructure, overlapping
#      subproblems). It's also greedy (locally optimal choice at each step
#      = globally optimal). Kadane's is the overlap.
# ============================================================


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum  = nums[0]      # best subarray sum seen; init to first element
        curr_sum = 0            # running sum of current subarray

        for num in nums:
            curr_sum = max(curr_sum + num, num)     # extend or restart
            max_sum  = max(max_sum, curr_sum)       # update global best

        return max_sum


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4],  6),   # [4,-1,2,1]
        ([1],                                1),   # single element
        ([5, 4, -1, 7, 8],                 23),   # whole array
        ([-1],                             -1),   # single negative
        ([-2, -1],                         -1),   # all negative — best is -1
        ([1, 2, 3, 4, 5],                  15),   # all positive
        ([-2, 1],                           1),   # skip first
        ([2, -1, 2, -1, 3],                 5),   # alternating
    ]

    passed = 0
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = sol.maxSubArray(nums)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: {nums} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
