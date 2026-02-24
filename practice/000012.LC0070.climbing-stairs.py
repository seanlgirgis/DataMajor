# ============================================================
# 000012 | LC 0070 — Climbing Stairs
# Pattern   : Dynamic Programming (1D) / Fibonacci
# Difficulty : Easy
# Time       : O(n)   — one pass
# Space      : O(1)   — two rolling variables
# ============================================================
# Problem:
#   You are climbing a staircase with n steps.
#   Each time you can climb 1 or 2 steps.
#   In how many distinct ways can you climb to the top?
#
# Examples:
#   n = 2  ->  2   (1+1, 2)
#   n = 3  ->  3   (1+1+1, 1+2, 2+1)
#   n = 5  ->  8
# ============================================================
# Key Insight:
#   To reach step n you came from step n-1 (one step) or n-2 (two steps).
#   So: ways(n) = ways(n-1) + ways(n-2)  — pure Fibonacci.
#   Base cases: ways(1) = 1, ways(2) = 2.
#   DP bottom-up with two rolling variables avoids recursion stack
#   and memoization overhead. O(n) time, O(1) space.
# ============================================================

# User's notes (correct reasoning):
# n=1 -> 1,  n=2 -> 2,  n=3 -> 3,  n=4 -> 5,  n=5 -> 8 ...  Fibonacci!
# func(n) = func(n-1) + func(n-2)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev2, prev1 = 1, 2             # ways(1), ways(2)
        for _ in range(3, n + 1):
            curr  = prev1 + prev2       # ways(i) = ways(i-1) + ways(i-2)
            prev2 = prev1
            prev1 = curr

        return prev1


# ============================================================
# USER'S ORIGINAL — Naive Recursion (correct but O(2^n) time)
# Works for small n, times out on LeetCode for large n.
# On CodeSignal this would TLE — always use DP.
# ============================================================
class SolutionRecursive:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

# Fix: add memoization to make recursive O(n)
from functools import lru_cache
class SolutionMemo:
    @lru_cache(maxsize=None)
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol      = Solution()
    sol_rec  = SolutionRecursive()
    sol_memo = SolutionMemo()

    test_cases = [
        (1,   1),
        (2,   2),
        (3,   3),
        (4,   5),
        (5,   8),
        (6,  13),
        (10, 89),
        (38, 63245986),
    ]

    passed = 0
    for i, (n, expected) in enumerate(test_cases, 1):
        r1 = sol.climbStairs(n)
        r2 = sol_rec.climbStairs(n)
        r3 = sol_memo.climbStairs(n)
        ok = r1 == r2 == r3 == expected
        status = "PASS" if ok else f"FAIL (expected {expected})"
        print(f"Test {i}: n={n} -> dp={r1} rec={r2} memo={r3}  {status}")
        if ok:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
