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
        pass


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("A", 0, 1),
        ("ABAA", 0, 1),
        ("ABCCC", 1, 4),   # change B to C -> "ACCCC"
        ("KRSK", 2, 4),    # change two chars to K
        ("", 1, 0)
    ]

    passed = 0
    for i, (s_input, k, expected) in enumerate(test_cases, 1):
        result = sol.characterReplacement(s_input, k)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: '{s_input}', k={k} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
