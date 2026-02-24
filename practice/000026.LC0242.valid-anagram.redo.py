# ============================================================
# 000026 | LC 0242 — Valid Anagram  [REDO]
# Pattern   : Frequency Map (Counter or manual dict)
# Difficulty : Easy
# ============================================================
# Time Complexity:  O(n) — one pass per string, n = len(s)+len(t)
# Space Complexity: O(k) — k = distinct characters (max 26)
# ============================================================
# Problem:
#   Given two strings s and t, return True if t is an anagram
#   of s, and False otherwise.
#   An anagram uses all the original letters exactly once.
#
# Examples:
#   s = "anagram", t = "nagaram"  ->  True
#   s = "rat",     t = "car"      ->  False
#   s = "a",       t = "a"        ->  True
# ============================================================
# Key Insight:
#   Two strings are anagrams iff their character frequency maps
#   are equal. Build a freq map for each and compare.
#   Shortcut: early exit if len(s) != len(t).
#
# Three equivalent approaches:
#   1. Manual dict   — explicit, always works
#   2. Counter       — cleanest, signals Python fluency
#   3. sorted(s)==sorted(t) — O(n log n) but one-liner
# ============================================================
# Interviewer follow-ups:
#   Q: "What if the input contains Unicode / non-ASCII?"
#   A: Both Counter and dict handle it — no alphabet assumption.
#      The sorted() approach also works unchanged.
#
#   Q: "Can you do it in O(1) space?"
#   A: Only if alphabet is fixed (e.g., 26 lowercase letters).
#      Use a single int[26] array. Increment for s, decrement
#      for t. Any non-zero value at end -> not anagram.
#
#   Q: "What's the fastest one-liner?"
#   A: Counter(s) == Counter(t)  — Python stdlib, O(n)
# ============================================================

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):        # fast early exit
            return False
        return Counter(s) == Counter(t)


# ── Manual dict version (same complexity, no import) ─────────
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         def freq(st):
#             d = {}
#             for ch in st:
#                 d[ch] = d.get(ch, 0) + 1
#             return d
#         return freq(s) == freq(t)


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("anagram", "nagaram", True),
        ("rat",     "car",     False),
        ("a",       "a",       True),
        ("ab",      "a",       False),   # different lengths
        ("",        "",        True),    # both empty
        ("aab",     "bba",     False),   # same chars, wrong counts
        ("listen",  "silent",  True),
    ]

    passed = 0
    for i, (s, t, expected) in enumerate(test_cases, 1):
        result = sol.isAnagram(s, t)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: {repr(s)}, {repr(t)} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
