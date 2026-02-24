# ============================================================
# 000007 | LC 0003 — Longest Substring Without Repeating Characters
# Pattern   : Sliding Window + Hash Map
# Difficulty : Medium
# Time       : O(n)  — each char added/removed from window at most once
# Space      : O(min(n, m))  — m = size of charset (26 / 128 / etc.)
# ============================================================
# Problem:
#   Given a string s, find the length of the longest substring
#   that contains no repeating characters.
#
# Examples:
#   "abcabcbb" → 3  ("abc")
#   "bbbbb"    → 1  ("b")
#   "pwwkew"   → 3  ("wke")
# ============================================================
# Key Insight:
#   Maintain a sliding window [left, right].
#   Use a dict to track chars currently in the window.
#   When a duplicate is found at `right`, shrink from `left`
#   until the duplicate is evicted — then expand again.
#   O(n) amortized: every char enters and leaves the window once.
# ============================================================

import sys

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left, max_length = 0, 0
        seen = {}                               # char → present in window (True/False via existence)

        for right, ch in enumerate(s):
            if s[right] in seen:
                # shrink window from left until duplicate is evicted
                while left <= right and s[right] in seen:
                    del seen[s[left]]
                    left += 1

            seen[ch] = right                    # mark char as in window
            max_length = max(max_length, right - left + 1)

        return max_length


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("abcabcbb",        3),     # classic — "abc"
        ("bbbbb",           1),     # all same — "b"
        ("pwwkew",          3),     # "wke"
        ("",                0),     # edge: empty string
        ("a",               1),     # edge: single char
        ("dvdf",            3),     # "vdf" — left must jump past first 'd'
        ("abcabcde",        5),     # "abcde"
        ("geeksforgeeks",   7),     # "eksforg"
        ("abcdefabcbb",     6),     # "abcdef"
        ("tmmzuxt",         5),     # "mzuxt"
        ("au",              2),     # two unique chars
        ("abba",            2),     # "ab" or "ba"
        ("anviaj",          5),     # "anvia" or "nviaj"
        ("ohomm",           3),     # "hom"
        (" !@#$%^&*()",    11),     # spaces + special chars all unique
    ]

    passed = 0
    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = sol.lengthOfLongestSubstring(input_str)
        if result == expected:
            passed += 1
            print(f"Test {i:2d}: '{input_str}' -> {result}  PASS")
        else:
            print(f"Test {i:2d}: '{input_str}' -> {result}  FAIL  (expected {expected})")

    print(f"\n{passed}/{len(test_cases)} tests passed")
