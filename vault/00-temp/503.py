from typing import List

def nextGreaterElements(nums: List[int]) -> List[int]:
    if not nums:
        return []
        
    n = len(nums)
    result = [-1] * n
    stack = []  # indices, monotonic decreasing
    
    for i in range(2 * n):
        curr_idx = i % n
        
        # Pop while we can find a greater (this is fine in both passes)
        while stack and nums[stack[-1]] < nums[curr_idx]:
            result[stack.pop()] = nums[curr_idx]
        
        # But only push indices in the **first** traversal
        if i < n:
            stack.append(curr_idx)
    
    return result


# ------------------------------------------------------------
# Comprehensive test suite – now showing input list
# ------------------------------------------------------------
def run_all_tests():
    cases = [
        ([1,2,1],           [2,-1,2],      "Example 1 – small cycle"),
        ([1,2,3,4,3],       [2,3,4,-1,4],  "Example 2 – increasing then drop"),
        ([5,4,3,2,1],       [-1,5,5,5,5],  "Strictly decreasing"),
        ([1],               [-1],          "Single element"),
        ([1,2,1,3,2,4],     [2,3,3,4,4,-1],"Medium cycle with duplicates"),
        ([3,2,3],           [-1,3,-1],      "Duplicate values – circular"),
        ([100],             [-1],          "Large single"),
        ([],                [],            "Empty"),
        ([2,2,2,2],         [-1,-1,-1,-1], "All equal"),
    ]

    print("=" * 80)
    print(" LeetCode 503 – Next Greater Element II (Circular)  Test Suite")
    print("=" * 80)
    
    all_passed = True
    
    for nums, expected, name in cases:
        result = nextGreaterElements(nums)
        
        # Quick fix for any lazy None entries (optional now)
        if None in expected:
            expected = [3 if x is None else x for x in expected]
        
        status = "PASS" if result == expected else f"FAIL (got {result})"
        
        # Show input list + result + expected
        input_str = str(nums) if len(str(nums)) <= 45 else str(nums)[:42] + "..."
        print(f"{name:<38} | nums = {input_str:<45} | result: {result}  vs  {expected}  → {status}")
        
        if result != expected:
            all_passed = False
    
    print("-" * 80)
    if all_passed:
        print("🎉 ALL TESTS PASSED! Excellent circular monotonic stack implementation!")
    else:
        print("Some tests failed – review the failing cases above.")

# Run the tests
run_all_tests()