# ============================================================
# 000025 | LC 0011 — Container With Most Water
# Pattern   : Two Pointers — Squeeze from Both Ends
# Difficulty : Medium
# ============================================================
# Time Complexity:  O(n) — single pass, each pointer moves at most n times
# Space Complexity: O(1) — two pointers only
# ============================================================
# Problem:
#   Given an integer array height of length n representing
#   vertical lines drawn at each index, find two lines that
#   together with the x-axis form a container holding the most water.
#   Return the maximum amount of water.
#
#   Water = min(height[l], height[r]) * (r - l)
#
# Examples:
#   height = [1,8,6,2,5,4,8,3,7]  ->  49
#   height = [1,1]                 ->  1
#   height = [4,3,2,1,4]          ->  16
# ============================================================
# Key Insight:
#   Start with the widest possible container (l=0, r=end).
#   Width shrinks as pointers move inward — the only way to
#   compensate is to find a taller line.
#   The shorter side limits the water height — moving the
#   TALLER pointer inward can only make things worse (shorter
#   width, same or smaller height). So always move the SHORTER
#   pointer — it's the only chance to improve.
#
#   Greedy proof: any pair we skip by moving the shorter pointer
#   would produce less area than what we already recorded.
# ============================================================
# Interviewer follow-ups:
#   Q: "Why not brute force O(n^2)?"
#   A: Check all pairs. Correct but too slow for n=100,000.
#
#   Q: "Does it matter which pointer we move when heights are equal?"
#   A: No — if height[l] == height[r], moving either is safe.
#      Moving both simultaneously is also valid.
#
#   Q: "Is this the same two-pointer pattern as Two Sum II?"
#   A: Similar squeeze from both ends, but the move decision differs.
#      Two Sum II: move based on sum vs target.
#      Container: move the shorter pointer.
# ============================================================


class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0

        while l < r:
            area = max(area, min(height[l], height[r]) * (r - l))  # water this pair holds
            if height[l] >= height[r]:  # right is shorter (or equal) — move it inward
                r -= 1
            else:                       # left is shorter — move it inward
                l += 1

        return area


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1,8,6,2,5,4,8,3,7],  49),   # classic example
        ([1,1],                  1),   # two equal short lines
        ([4,3,2,1,4],           16),   # symmetric — both ends
        ([1,2,1],                2),   # middle is tallest but doesn't help
        ([2,3,4,5,18,17,6],    17),   # big values near center
        ([1,2,3,4,5],           6),    # increasing heights
    ]

    passed = 0
    for i, (height, expected) in enumerate(test_cases, 1):
        result = sol.maxArea(height)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: {height} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
