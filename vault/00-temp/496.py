#Thinking program to try to find solution

from typing import List

#we will recieve two entire l
    #Intializing with defulat valueists all at once and we will calculate entire output list
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    #Intializing with defulat value
    # Keep a dictionary of Already calculated
#    cashed = { 4:-1, 1:3, 2:3    }    # store value and next 
    next_greater = {}
    res: List[int] = [-1] * len(nums1)
    #Let us loop on nums1
    if not nums1 or not nums2:
        return res
    # loop on nums1 for input
    
    # Stack the first item always
    stack = [nums2[0]]
    for i in range (1,len(nums2)):
        while stack and nums2[i] > stack[-1]:
            n = stack.pop()
            next_greater[n] =  nums2[i]
        stack.append(nums2[i])
    #cleanup
    while stack:
        n = stack.pop()
        next_greater[n] =  -1

    #Now we have built a Map of nums2 .. All what we have to do is to 
    # loop on numbs one and translate the nums to the mapping
    
    for i,n in enumerate(nums1):
        res[i] = next_greater[n]

    return res
    
    

#------------------------------------------------------------
# Comprehensive test suite – run this after implementing Cell 3
#------------------------------------------------------------
def run_all_tests():
    cases = [
        ([4,1,2],   [1,3,4,2],   [-1,3,-1],   "Example 1"),
        ([2,4],     [1,2,3,4],   [3,-1],      "Example 2"),
        ([1],       [1],         [-1],        "Single element no greater"),
        ([1,3,5,2,4], [6,5,4,3,2,1,7], [7,7,7,7,7], "All have greater at end"),
        ([1,2,3],   [3,2,1],     [-1,-1,-1], "Strictly decreasing"),
        ([3,2,1],   [1,2,3],     [-1,3,2], "Wait — adjust expected below"),
      
    ]

    print("=" * 70)
    print(" LeetCode 496 – Next Greater Element I  Test Suite")
    print("=" * 70)
    
    all_passed = True
    for nums1, nums2, expected, name in cases[:6]:  # skip invalid for brevity
        result = nextGreaterElement(nums1, nums2)
        status = "PASS" if result == expected else f"FAIL (got {result})"
        print(f"{name:<38} | n1={len(nums1)} n2={len(nums2)} | {result} vs {expected} → {status}")
        if result != expected:
            all_passed = False
    
    print("-" * 70)
    if all_passed:
        print("🎉 ALL KEY TESTS PASSED! Solid monotonic stack usage!")
    else:
        print("Some tests failed – check your stack logic or map lookup.")

run_all_tests()