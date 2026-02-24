# ============================================================
# 000033 | LC 0070 --- Climbing Stairs (Study File)
# Pattern   : Dynamic Programming (Bottom-Up)
# Difficulty : Easy
# ============================================================
# Time Complexity:  O(n) --- single loop from 3 to n
# Space Complexity: O(1) --- only tracking two variables
# ============================================================
# Problem:
#   You are climbing a staircase. It takes n steps to reach the top.
#   Each time you can either climb 1 or 2 steps. In how many
#   distinct ways can you climb to the top?
#
# Examples:
#   n = 2  ->  2
#   n = 3  ->  3
# ============================================================
# Key Insight (O(1) Space Optimization):
#   Instead of a recursion stack mapping all the way down, OR
#   an array storing all `n` answers, we realize that step `i`
#   ONLY ever needs the answers from step `i-1` and step `i-2`.
#   
#   Therefore, we can just maintain two variables and update
#   them in a loop as we climb from step 3 up to step n.
# ============================================================

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: 
            return n
            
        # Base cases for n = 1 and n = 2
        two_steps_before = 1  # Ways to climb 1 step
        one_step_before = 2   # Ways to climb 2 steps
        
        # Calculate from step 3 up to step n
        for _ in range(3, n + 1):
            current = one_step_before + two_steps_before
            
            # Shift the window forward for the next iteration
            two_steps_before = one_step_before
            one_step_before = current
            
        return one_step_before


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (10, 89)
    ]

    passed = 0
    for i, (n, expected) in enumerate(test_cases, 1):
        result = sol.climbStairs(n)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: n={n} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
