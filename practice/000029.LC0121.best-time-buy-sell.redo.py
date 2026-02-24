# ============================================================
# 000029 | LC 0121 --- Best Time to Buy and Sell Stock  [REDO]
# Pattern   : Greedy / One Pass
# Difficulty : Easy
# ============================================================
# Time Complexity:  O(n) --- single pass through prices
# Space Complexity: O(1) --- only tracking two variables
# ============================================================
# Problem:
#   You are given an array prices where prices[i] is the price of a stock on day i.
#   Return the maximum profit from buying on one day and selling on a later day.
#   If no profit is possible, return 0.
#
# Examples:
#   [7,1,5,3,6,4]  ->  5
#   [7,6,4,3,1]    ->  0
#   Constraints: 1 <= prices.length <= 10^5, 0 <= prices[i] <= 10^4
# ============================================================
# Key Insight:
#   To maximize profit, we want to track the lowest `buy` price seen
#   so far. At each step `i`, the potential profit is `prices[i] - buy`.
#   We keep the maximum profit across all days.
# ============================================================
from math import inf
class Solution:

    def maxProfit(self, prices: list[int]) -> int:
        buy = inf
        profit = 0
        # you musst buy before you sell
        for price in prices:
            profit = max(profit, (price - buy))  # current profit vs best profit seen
            if price < buy : buy = price         # update lowest buy price going forward
        return profit


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2], 1),
        ([2, 1], 0),
        ([3, 2, 6, 5, 0, 3], 4),
        ([2, 4, 1], 2),
    ]

    passed = 0
    for i, (inp, expected) in enumerate(test_cases, 1):
        result = sol.maxProfit(inp)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: {inp} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
