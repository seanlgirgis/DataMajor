# ============================================================
# 000034 | LC 0424 --- Longest Repeating Character Replacement
# Pattern   : Sliding Window
# Difficulty : Medium
# ============================================================
# Problem:
#   You are given a string s and an integer k. You can choose any
#   character of the string and change it to any other uppercase
#   English character. You can perform this operation at most k times.
#   Return the length of the longest substring containing the same
#   letter you can get after performing the above operations.
#
# Examples:
#   s = "ABAB", k = 2  ->  4
#       Explanation: Replace the two 'A's with two 'B's or vice versa.
#   s = "AABABBA", k = 1  ->  4
#       Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
#       The substring "BBBB" has the longest repeating letters, which is 4.
# ============================================================

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, n = 0,0, len(s)
        
        
        
        # looks like 2 pointers
        pass



s, k = "AAABBBCCC", 3
print(Solution().characterReplacement(s,k))
import sys
sys.exit()

# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
# Edge cases
("AAAA", 0, 4),        # all same, no changes needed
("AAAA", 2, 4),        # all same, k irrelevant
("ABCD", 0, 1),        # all different, no changes allowed
("ABCD", 1, 2),        # all different, 1 change
("ABCD", 3, 4),        # all different, k covers whole string
("AABB", 1, 3),        # tie between A and B dominance

# k >= len(s)
("ABCD", 4, 4),        # k equals length, whole string
("ABCD", 10, 4),       # k exceeds length

# Longer strings
("ABABABABAB", 2, 6),  # alternating, 2 replacements
("AABBBBAAA", 2, 9),   # nearly uniform
("AAABBBCCC", 3, 6),   # three equal groups

# All same character
("BBBBBB", 0, 6),      # no replacements needed
("BBBBBB", 3, 6),      # k irrelevant

# Single char repeated with noise
("BAAAB", 2, 5),       # surround A island with B replacements
("AABAA", 1, 5),       # one replacement makes whole string A
    ]

    passed = 0
    for i, (s_input, k, expected) in enumerate(test_cases, 1):
        result = sol.characterReplacement(s_input, k)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: '{s_input}', k={k} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
