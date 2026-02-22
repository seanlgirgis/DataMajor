# LeetCode #121 - Best Time to Buy and Sell Stock
# Difficulty: Easy
# Approach: One-pass greedy | Time: O(n) | Space: O(1)

from math import inf

def maxProfit(prices: list[int]) -> int:
    """
    Track the lowest buy price seen so far.
    At each step, compute profit and update the max.
    Returns 0 if no profit is possible.
    """
    profit = 0
    buy_price = inf

    for price in prices:
        profit = max(profit, price - buy_price)
        if price < buy_price:
            buy_price = price

    return profit

# --- Tests ---
print(maxProfit([7, 1, 5, 3, 6, 4]))  # 5
print(maxProfit([7, 6, 4, 3, 1]))     # 0