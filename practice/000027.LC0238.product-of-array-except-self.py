# ============================================================
# 000027 | LC 0238 — Product of Array Except Self
# Pattern   : Prefix / Postfix Products
# Difficulty : Medium
# ============================================================
# Time Complexity:  O(n)
# Space Complexity: O(n) — two extra arrays (l_mult, r_mult)
#                   O(1) possible — see optimised version below
# ============================================================
# Problem:
#   Given integer array nums, return array answer where
#   answer[i] = product of all nums EXCEPT nums[i].
#   No division allowed. Must be O(n).
#
# Examples:
#   [1, 2, 3, 4]      ->  [24, 12,  8,  6]
#   [-1, 1, 0, -3, 3] ->  [ 0,  0,  9,  0,  0]
# ============================================================
# Key Insight:
#   answer[i] = (product of everything LEFT of i)
#             * (product of everything RIGHT of i)
#
#   Build two arrays:
#     l_mult[i] = product of nums[0..i-1]  (1 if nothing to left)
#     r_mult[i] = product of nums[i+1..n-1] (1 if nothing to right)
#   answer[i] = l_mult[i] * r_mult[i]
#
# Visual for [1, 2, 3, 4]:
#   Index:    0    1    2    3
#   l_mult:   1    1    2    6     <- prefix products
#   r_mult:  24   12    4    1     <- suffix products
#   answer:  24   12    8    6     <- element-wise product
# ============================================================
# Interviewer follow-up:
#   Q: "Can you do it in O(1) extra space?"
#   A: Yes — fill answer[] with prefix products first, then
#      multiply suffix in-place with a running variable.
#      See optimised version below.
# ============================================================

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        l_mult = [1] * n
        r_mult = [1] * n

        # l_mult[i] = product of everything to the LEFT of i
        for i in range(1, n):
            l_mult[i] = l_mult[i-1] * nums[i-1]

        # r_mult[i] = product of everything to the RIGHT of i
        for i in range(n - 2, -1, -1):
            r_mult[i] = r_mult[i+1] * nums[i+1]

        return [a * b for a, b in zip(l_mult, r_mult)]


# ── O(1) space optimised version ─────────────────────────────
# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         n = len(nums)
#         answer = [1] * n
#         prefix = 1
#         for i in range(n):              # pass 1: fill prefix
#             answer[i] = prefix
#             prefix *= nums[i]
#         suffix = 1
#         for i in range(n - 1, -1, -1): # pass 2: multiply suffix
#             answer[i] *= suffix
#             suffix *= nums[i]
#         return answer


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1, 2, 3, 4],         [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3],    [0, 0, 9, 0, 0]),
        ([1, 1],               [1, 1]),
        ([0, 0],               [0, 0]),
        ([2, 3],               [3, 2]),
        ([1, 0, 3, 4],         [0, 12, 0, 0]),
    ]

    passed = 0
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = sol.productExceptSelf(nums)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: {nums} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
