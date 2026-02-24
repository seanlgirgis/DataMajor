# ============================================================
# 000038 | LC 0015 --- 3Sum
# Pattern   : Two Pointers / Sorting
# Difficulty : Medium
# ============================================================
# Problem:
#   Given an integer array nums, return all the triplets
#   [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
#   and nums[i] + nums[j] + nums[k] == 0.
#
#   Notice that the solution set must not contain duplicate triplets.
#
# Examples:
#   nums = [-1,0,1,2,-1,-4]  ->  [[-1,-1,2],[-1,0,1]]
#   nums = [0,1,1]           ->  []
#   nums = [0,0,0]           ->  [[0,0,0]]
#
# Constraints:
#   3 <= nums.length <= 3000
#   -10^5 <= nums[i] <= 10^5
# ============================================================

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()   # In-place sorting is step 1 for two-pointers
        res: List[List[int]] = []   # Place holder for the triplets that add to 0
        
        for i, n in enumerate(nums):
            # FIX 1: Prevent Duplicate Triplets from the same starting number
            # If this number is the same as the previous number we checked, skip it.
            # We already found all unique combinations that start with this number!
            if i > 0 and n == nums[i-1]:
                continue
                
            # FIX 2: Order Enforcement (Replaces the `tr_ind` virtual index)
            # Instead of searching the ENTIRE array and risking finding the exact
            # same triplet in a different order (e.g. [-1, 0, 1] then [0, -1, 1]),
            # we FORCE the result to be ordered: nums[i] <= nums[left] <= nums[right].
            # We do this by only letting `left` search the array AFTER index `i`.
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = n + nums[left] + nums[right]
                
                if current_sum > 0:
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    # We found a valid triplet!
                    res.append([n, nums[left], nums[right]])
                    
                    # Move the left pointer to search for the next distinct combination
                    left += 1
                    
                    # FIX 3: Prevent duplicate second numbers
                    # Keep shifting left if it's the same as the one we just processed
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                    # Note: We don't strictly *need* to deduplicate `right` in a while-loop
                    # because updating `left` to a new distinct number forces `current_sum`
                    # to change anyway, which naturally updates `right` in the next loop!
                    
        return res


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]])
    ]

    passed = 0
    for i, (nums, expected) in enumerate(test_cases, 1):
        # Sort the results so order doesn't fail the test
        result = sol.threeSum(nums)
        if isinstance(result, list):
            result = sorted([sorted(triplet) for triplet in result])
        expected_sorted = sorted([sorted(triplet) for triplet in expected])
        
        status = "PASS" if result == expected_sorted else f"FAIL (expected {expected_sorted})"
        print(f"Test {i}: {nums} -> {result}  {status}")
        if result == expected_sorted:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
