# ============================================================
# 000023 | LC 0121 — Best Time to Buy and Sell Stock  [REDO]
# Pattern   : Greedy — One Pass (track min price, max profit)
# Difficulty : Easy
# ============================================================
# Time Complexity:  O(n) — single pass through prices
# Space Complexity: O(1) — two variables only
# ============================================================
# Problem:
#   Given an array prices where prices[i] is the price of a
#   stock on day i, return the maximum profit from a single
#   buy-then-sell transaction.
#   You must buy before you sell. Return 0 if no profit possible.
#
# Examples:
#   prices = [7,1,5,3,6,4]  ->  5   (buy day 1 @ 1, sell day 4 @ 6)
#   prices = [7,6,4,3,1]    ->  0   (prices always falling)
#   prices = [1,2]          ->  1
# ============================================================
# Key Insight:
#   Track the lowest buy price seen so far.
#   At each day, ask: "if I sell today, what's my profit?"
#   Keep the max profit seen across all days.
#
#   CRITICAL — order of operations inside the loop:
#     1. Compute profit FIRST  (sell today at current price)
#     2. Update min price SECOND (maybe buy today for tomorrow)
#   Reversed order would allow "sell then buy same day" — wrong.
#
#   Using float('inf') as initial buy price avoids a separate
#   edge case for the first element — first profit is always
#   negative, so max(0, negative) = 0 safely.
# ============================================================
# Interviewer follow-ups:
#   Q: "What if you can buy and sell multiple times?" (LC 0122)
#   A: Greedy — sum all positive consecutive differences.
#      Any day price goes up from previous day, take that gain.
#
#   Q: "What if you can make at most 2 transactions?" (LC 0123)
#   A: DP with states: hold/no-hold × first/second transaction.
#      O(n) time, O(1) space.
#
#   Q: "Why can't we use two pointers (left=buy, right=sell)?"
#   A: You can — it's equivalent. left starts at 0, right at 1.
#      If prices[right] > prices[left]: update max profit.
#      If prices[right] < prices[left]: move left to right (new min).
#      Advance right each step.
# ============================================================

from math import inf

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buy = inf                               # lowest price seen so far

        for price in prices:
            profit = max(profit, price - buy)   # 1. can I profit selling today?
            if price < buy:                     # 2. is today a better buy day?
                buy = price

        return profit


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([7,1,5,3,6,4],  5),   # buy 1, sell 6
        ([7,6,4,3,1],    0),   # always falling — no profit
        ([1,2],          1),   # two elements
        ([2,1],          0),   # two elements, falling
        ([1],            0),   # single element
        ([3,3,3,3],      0),   # flat — no profit
        ([1,4,2,7],      6),   # buy 1, sell 7
        ([2,4,1,7],      6),   # best is not at start
    ]

    passed = 0
    for i, (prices, expected) in enumerate(test_cases, 1):
        result = sol.maxProfit(prices)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: {prices} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
