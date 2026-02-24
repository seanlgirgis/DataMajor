# ============================================================
# 000020 | LC 0704 — Binary Search  [REDO]
# Pattern   : Binary Search — Classic Template
# Difficulty : Easy
# ============================================================
# Time Complexity:  O(log n) — halve search space each step
# Space Complexity: O(1)     — two pointers only
# ============================================================
# Problem:
#   Given a sorted array of distinct integers and a target,
#   return the index of target, or -1 if not found.
#   Must be O(log n).
#
# Examples:
#   nums = [-1,0,3,5,9,12], target = 9   ->  4
#   nums = [-1,0,3,5,9,12], target = 2   ->  -1
# ============================================================
# Key Insight:
#   Array is sorted. At each mid, target is either:
#     - equal to mid   -> found, return
#     - less than mid  -> must be in left half  -> r = mid - 1
#     - greater        -> must be in right half -> l = mid + 1
#   Loop ends when l > r (search space exhausted) -> return -1.
#
# Template (memorise this exactly):
#   l, r = 0, len(nums) - 1
#   while l <= r:
#       mid = (l + r) // 2
#       if nums[mid] == target: return mid
#       if target < nums[mid]:  r = mid - 1
#       else:                   l = mid + 1
#   return -1
# ============================================================
# CRITICAL — do NOT confuse with rotated array (LC 0033):
#
#   Plain binary search:     compare TARGET vs nums[mid]
#     if target < nums[mid]: r = mid - 1
#
#   Rotated array search:    compare nums[l] vs nums[mid] FIRST
#     if nums[l] <= nums[mid]: ...  <- identifies sorted half
#
#   The difference: plain search never touches nums[l] or nums[r]
#   in the condition. Rotated search does.
# ============================================================
# Interviewer follow-ups:
#   Q: "Why (l + r) // 2 and not just l + r // 2?"
#   A: Operator precedence — l + r // 2 = l + (r // 2), wrong.
#      Use (l + r) // 2. In very large arrays also use
#      l + (r - l) // 2 to avoid integer overflow (Python is immune,
#      but important in Java/C++).
#
#   Q: "Why while l <= r and not l < r?"
#   A: The = handles the single-element window correctly.
#      If l == r and that element is the target, l < r would skip it.
# ============================================================


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:      # target is in left half
                r = mid - 1
            else:                       # target is in right half
                l = mid + 1

        return -1


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([-1,0,3,5,9,12], 9,   4),
        ([-1,0,3,5,9,12], 2,  -1),
        ([5],              5,   0),   # single element, found
        ([5],              3,  -1),   # single element, not found
        ([1,2,3,4,5],      1,   0),   # target at left edge
        ([1,2,3,4,5],      5,   4),   # target at right edge
        ([1,2,3,4,5],      3,   2),   # target in middle
    ]

    passed = 0
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = sol.search(nums, target)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: {nums}, target={target} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
