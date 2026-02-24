# ============================================================
# 000031 | LC 0070 --- Climbing Stairs
# Pattern   : Dynamic Programming (basic)
# Difficulty : Easy
# ============================================================
# Time Complexity:  O(n) --- each state 1..n is computed once and cached
# Space Complexity: O(n) --- recursion stack is n deep, cache stores n entries
# ============================================================
# Problem:
#   You are climbing a staircase. It takes n steps to reach the top.
#   Each time you can either climb 1 or 2 steps. In how many
#   distinct ways can you climb to the top?
#
# Examples:
#   n = 2  ->  2
#       Explanation: 1 step + 1 step, or 2 steps
#   n = 3  ->  3
#       Explanation: 1+1+1, 1+2, or 2+1
#
# Constraints:
#   1 <= n <= 45
# ============================================================
# Key Insight:
#   Using `@cache` on the recursive function is an elegant way to do
#   Top-Down Dynamic Programming (Memoization). 
#
#   Optimization: Because we only ever need the result of the last
#   two steps (`n-1` and `n-2`), we can optimize the space to O(1)
#   using Bottom-Up DP. Just keep two variables `one_step` and `two_step`
#   and update them in a loop!
# ============================================================
from functools import cache 
class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (10, 89)
    ]

    passed = 0
    for i, (n, expected) in enumerate(test_cases, 1):
        result = sol.climbStairs(n)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: n={n} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
