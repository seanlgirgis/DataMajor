# ============================================================
# 000019 | LC 0033 — Search in Rotated Sorted Array
# Pattern   : Binary Search — Pivot-Aware
# Difficulty : Medium
# ============================================================
# Time Complexity:  O(log n) — halve the search space each step
# Space Complexity: O(1)     — two pointers only
# ============================================================
# Problem:
#   An integer array nums was sorted in ascending order, then
#   rotated at some unknown pivot index k.
#   Example: [0,1,2,4,5,6,7] rotated at k=4 -> [4,5,6,7,0,1,2]
#
#   Given nums (all unique) and a target, return the index of
#   target, or -1 if not found. Must be O(log n).
#
# Examples:
#   nums = [4,5,6,7,0,1,2], target = 0  ->  4
#   nums = [4,5,6,7,0,1,2], target = 3  ->  -1
#   nums = [1],              target = 0  ->  -1
# ============================================================
# Key Insight:
#   No matter where the rotation is, when you pick a mid point
#   ONE of the two halves is always fully sorted.
#   Use that guaranteed-sorted half to decide which side to search.
#
#   Decision tree at each step:
#
#   1. Hit target?           -> return mid
#
#   2. Left half sorted?  (nums[l] <= nums[mid])
#        Target inside left? (nums[l] <= target < nums[mid])
#          YES -> r = mid - 1   (search left)
#          NO  -> l = mid + 1   (search right)
#
#   3. Right half sorted  (else)
#        Target inside right? (nums[mid] < target <= nums[r])
#          YES -> l = mid + 1   (search right)
#          NO  -> r = mid - 1   (search left)
#
#   Memory trick: "move TOWARD the half where target must be"
#     - target in left  -> pull r down  (r = mid - 1)
#     - target in right -> push l up    (l = mid + 1)
# ============================================================
# Interviewer follow-ups:
#   Q: "What if there are duplicates?" (LC 0081)
#   A: Add: if nums[l] == nums[mid] == nums[r]: l += 1; r -= 1; continue
#      Worst case degrades to O(n) when all values identical.
#
#   Q: "How do you find the pivot index itself?"
#   A: Binary search for the index where nums[i] > nums[i+1].
#      Or find min element (LC 0153) — that index is the pivot.
#
#   Q: "Why nums[l] <= nums[mid] and not < ?"
#   A: When l == mid (2-element window), left half has one element.
#      Using <= correctly classifies it as "sorted."
# ============================================================


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            # Left half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:   # target in left half
                    r = mid - 1
                else:                               # target in right half
                    l = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[r]:   # target in right half
                    l = mid + 1
                else:                               # target in left half
                    r = mid - 1

        return -1


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([4,5,6,7,0,1,2], 0,   4),   # target in right half
        ([4,5,6,7,0,1,2], 3,  -1),   # not present
        ([1],              0,  -1),   # single element, not found
        ([1],              1,   0),   # single element, found
        ([3,1],            1,   1),   # two elements
        ([3,1],            3,   0),   # two elements, first
        ([5,1,3],          3,   2),   # target at end
        ([1,2,3,4,5],      3,   2),   # no rotation at all
        ([2,3,4,5,1],      1,   4),   # target at very end
        ([6,7,1,2,3,4,5],  3,   4),   # target deep in right
    ]

    passed = 0
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = sol.search(nums, target)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: {nums}, target={target} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
