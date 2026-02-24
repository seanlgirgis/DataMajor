# ============================================================
# 000039 | LC 0003 --- Longest Substring Without Repeating Characters [REDO DRILL]
# Pattern   : Sliding Window
# Difficulty : Medium
# ============================================================
# Problem:
#   Given a string s, find the length of the longest substring
#   without repeating characters.
#
# Examples:
#   s = "abcabcbb"  ->  3
#       Explanation: The answer is "abc", with the length of 3.
#   s = "bbbbb"     ->  1
#       Explanation: The answer is "b", with the length of 1.
#   s = "pwwkew"    ->  3
#       Explanation: The answer is "wke", with the length of 3.
#
# Constraints:
#   0 <= s.length <= 5 * 10^4
#   s consists of English letters, digits, symbols and spaces.
# ============================================================

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3)
    ]

    passed = 0
    for i, (s_input, expected) in enumerate(test_cases, 1):
        result = sol.lengthOfLongestSubstring(s_input)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: '{s_input}' -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
