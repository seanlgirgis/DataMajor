# ============================================================
# 000028 | LC 0238 — Product of Array Except Self  [O(1) Space]
# Pattern   : Prefix / Postfix Products — In-Place
# Difficulty : Medium (follow-up optimisation)
# ============================================================
# Time Complexity:  O(n)
# Space Complexity: O(1) extra — output array not counted
# ============================================================
# Why this is better than the two-array version (000027):
#   000027 used l_mult[] and r_mult[] — two full O(n) arrays.
#   Here we eliminate both by:
#     1. Reusing the output array to hold prefix products
#     2. Multiplying the suffix in-place using one int variable
# ============================================================
# The trick — think of it as two separate sweeps:
#
#   SWEEP 1 (left → right)  builds prefix products INTO answer[]
#   ┌─────┬─────┬─────┬─────┐
#   │  i  │  0  │  1  │  2  │  3  │
#   ├─────┼─────┼─────┼─────┤
#   │nums │  1  │  2  │  3  │  4  │
#   │ans  │  1  │  1  │  2  │  6  │  <- product of everything LEFT of i
#   └─────┴─────┴─────┴─────┘
#   prefix starts at 1; we FIRST store it, THEN multiply it in.
#
#   SWEEP 2 (right → left)  multiplies suffix INTO answer[] in-place
#   suffix starts at 1 (nothing to the right of last element)
#   ┌─────┬─────┬─────┬─────┐
#   │  i  │  3  │  2  │  1  │  0  │
#   ├─────┼─────┼─────┼─────┤
#   │ans  │  6  │  8  │ 12  │ 24  │  <- final answer
#   │sfx  │  1  │  4  │ 12  │ 24  │  <- running suffix after update
#   └─────┴─────┴─────┴─────┘
#   We FIRST multiply ans[i] by suffix, THEN update suffix.
#
# Order matters:
#   Store/multiply BEFORE updating the running variable — same
#   principle in both sweeps.
# ============================================================

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        # ── Sweep 1: fill answer[i] with prefix product ───────
        # After this loop:  answer[i] = product of nums[0..i-1]
        prefix = 1
        for i in range(n):
            answer[i] = prefix      # store BEFORE multiplying in
            prefix *= nums[i]

        # ── Sweep 2: multiply answer[i] by suffix product ─────
        # After this loop:  answer[i] *= product of nums[i+1..n-1]
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix     # multiply in BEFORE updating
            suffix *= nums[i]

        return answer


# ── Side-by-side trace for nums = [1, 2, 3, 4] ───────────────
#
# After Sweep 1:
#   i=0: answer[0]=1,  prefix=1
#   i=1: answer[1]=1,  prefix=2
#   i=2: answer[2]=2,  prefix=6
#   i=3: answer[3]=6,  prefix=24
#   answer = [1, 1, 2, 6]
#
# After Sweep 2:
#   i=3: answer[3]=6*1=6,   suffix=4
#   i=2: answer[2]=2*4=8,   suffix=12
#   i=1: answer[1]=1*12=12, suffix=24
#   i=0: answer[0]=1*24=24, suffix=24
#   answer = [24, 12, 8, 6]  ✓
# ─────────────────────────────────────────────────────────────


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1, 2, 3, 4],         [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3],    [0, 0, 9, 0, 0]),
        ([1, 1],               [1, 1]),
        ([0, 0],               [0, 0]),
        ([2, 3],               [3, 2]),
        ([1, 0, 3, 4],         [0, 12, 0, 0]),
    ]

    passed = 0
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = sol.productExceptSelf(nums)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: {nums} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
