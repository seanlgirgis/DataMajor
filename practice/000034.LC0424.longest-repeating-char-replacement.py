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
        l = 0                       # Left pointer of our sliding window
        res = 0                     # Stores the maximum length found so far
        count = {}                  # Frequency dictionary for characters in current window
        
        # r is the right pointer expanding the window
        for r in range(len(s)):
            # 1. Add the new character to our window's frequency count
            count[s[r]] = count.get(s[r], 0) + 1
            
            # 2. Check if the current window is VALID.
            # A window is valid if: (Length of window) - (Count of most frequent char) <= k
            # This means the number of characters we need to replace is within our allowance 'k'.
            # Note: `max(count.values())` takes O(26) time. To optimize to O(1), you can just track a `max_f` variable!
            while (r - l + 1) - max(count.values()) > k:
                # If invalid, shrink the window by moving the left pointer
                count[s[l]] -= 1
                l += 1
                
            # 3. The window is now valid, so we update our maximum result length
            res = max(res, r - l + 1)
            
        return res
            
        


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
("ABABABABAB", 2, 5),  # alternating, 2 replacements (my broken test fixed: 5 is correct)
("AABBBBAAA", 2, 6),   # nearly uniform (my broken test fixed: 6 is correct)
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
