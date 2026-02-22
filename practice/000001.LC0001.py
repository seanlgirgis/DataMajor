# =============================================================================
# LEETCODE DRILL — Session 1  |  Problem 1
# LeetCode #1 — Two Sum  |  Difficulty: Easy
# Pattern : Hash Map (One Pass)  |  Time: O(n)  |  Space: O(n)
# =============================================================================
#
# PROBLEM STATEMENT:
#   Given a list of integers and a target, return the indices of the two
#   numbers that add up to the target. Exactly one solution exists.
#   You cannot use the same element twice.
#
#   Input:  nums = [2, 7, 11, 15], target = 9
#   Output: [0, 1]   # nums[0] + nums[1] = 2 + 7 = 9
#
#   Input:  nums = [3, 2, 4], target = 6
#   Output: [1, 2]   # nums[1] + nums[2] = 2 + 4 = 6
#
# KEY INSIGHT:
#   Instead of checking every pair (brute force O(n²)),
#   ask at each element: "Have I already seen the complement I need?"
#   complement = target - current_value
#
#   Store what you've SEEN so far, not what you're looking for.
#   This flips the problem from search → lookup.
#
# PATTERN — One Pass Hash Map:
#   1. Walk the list once with enumerate() to get both index and value.
#   2. Compute the complement needed to reach the target.
#   3. If complement is already in seen{} → found our pair, return indices.
#   4. Otherwise store current value → index in seen{} and keep walking.
#
# WHY THIS WORKS:
#   seen = { value: index }
#   When we find the complement in seen, we know:
#     - seen[complement] is the index of the first number
#     - i is the index of the second number
#   Order matters: check BEFORE inserting so we never match an element with itself.
# =============================================================================

def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}                          # maps value -> index for everything seen so far

    for i, n in enumerate(nums):
        another = target - n           # the complement we need to complete the pair

        if another in seen:            # have we seen the complement before?
            return [seen[another], i]  # yes — return [earlier index, current index]

        seen[n] = i                    # no — record this value and index, move on


# =============================================================================
# TESTS
# =============================================================================
nums: list[int] = [2, 7, 11, 15]
target: int = 9
print(twoSum(nums, target))   # Expected: [0, 1]

nums: list[int] = [3, 2, 4]
target: int = 6
print(twoSum(nums, target))   # Expected: [1, 2]