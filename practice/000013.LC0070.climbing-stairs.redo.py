# ============================================================
# 000013 | LC 0070 — Climbing Stairs  [REDO DRILL]
# Pattern   : Dynamic Programming (1D) / Fibonacci
# Difficulty : Easy
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
# Goal this time: O(n) time, O(1) space — no naive recursion.
# ============================================================

# ============================================================
# INTERVIEWER MIGHT ASK YOU:
#
# Q1: "What is the time and space complexity of your solution?"
#     A: O(n) time — each subproblem computed once and cached.
#        O(n) space — memo dict stores n entries + O(n) call stack.
#        NOT O(1) space. If they ask for O(1), use the iterative version.
#
# Q2: "Why did you use memo={} as a default argument?"
#     A: Python creates the default dict ONCE at function definition.
#        It persists across calls — acts as a cache automatically.
#        Risk: it's shared state, so in production code this is a bug.
#        In interview context it's a known trick — explain the tradeoff.
#
# Q3: "What's the difference between memoization and dynamic programming?"
#     A: Memoization = top-down DP. You start from the big problem,
#        recurse down, and cache results on the way back up.
#        Bottom-up DP = iterative, build from base cases upward.
#        Both are O(n) time. Bottom-up avoids recursion stack overhead.
#
# Q4: "Can you do this in O(1) space?"
#     A: Yes — two rolling variables, no recursion, no dict:
#        prev2, prev1 = 1, 2
#        for _ in range(3, n+1):
#            prev2, prev1 = prev1, prev1 + prev2
#        return prev1
#
# Q5: "Have you seen this sequence before?"
#     A: Yes — Fibonacci. ways(n) = ways(n-1) + ways(n-2).
#        Classic DP reduction: recognize that the recurrence IS Fibonacci,
#        then apply the appropriate optimization level.
# ============================================================

# MY OPINION (Claude):
# Your instinct to cache was correct and shows good DP awareness.
# memo={} default arg is clever and works — but know its risks cold.
# For CodeSignal tomorrow: if you write recursion + memo you'll score.
# If you write the O(1) iterative version you'll score higher.
# If the interviewer follows up on the mutable default — you now know
# exactly what to say. That's a senior engineer answer.
# ============================================================

class Solution:

    def climbStairs(self, n: int, memo= {}) -> int:
        if n in memo:
            return memo[n]
        if n <= 2:
            ret = n
            memo[n] = ret
            return ret
        ret = self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo)
        memo[n] = ret
        return ret
        


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":


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
        result = Solution().climbStairs(n)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: n={n} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
