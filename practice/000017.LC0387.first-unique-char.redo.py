# ============================================================
# 000017 | LC 0387 — First Unique Character in a String [REDO]
# Pattern   : Frequency Count (Two-Pass Hash Map)
# Difficulty : Easy
# ============================================================
# Time Complexity:
#   O(n) — two passes through s, each O(n).
#   Hash map ops are O(1) average.
#
# Space Complexity:
#   O(1) — at most 26 lowercase letter keys in the map.
#   Technically O(alphabet size), not O(n).
# ============================================================
# Problem:
#   Given a string s, find the first non-repeating character
#   and return its index. Return -1 if no such character exists.
#
# Examples:
#   s = "leetcode"      ->  0   ('l' appears once, index 0)
#   s = "loveleetcode"  ->  2   ('v' appears once, index 2)
#   s = "aabb"          ->  -1  (no unique character)
# ============================================================
# Key Insight:
#   Two-pass strategy:
#     Pass 1 — build a frequency map: char -> count
#     Pass 2 — scan s left to right; first char with count==1
#              is the answer (preserves original order).
#   We cannot do it in one pass because we need the full
#   frequency before we can judge any single character.
# ============================================================
# Interviewer follow-ups:
#   Q: "Can you do it in one pass?"
#   A: Not strictly — you need full frequency info before
#      judging. You could use an OrderedDict to track insertion
#      order, but you still scan all chars before concluding.
#
#   Q: "What's the space complexity?"
#   A: O(1) — bounded by alphabet size (26 lowercase letters),
#      not by length of s.
#
#   Q: "What if the string contains unicode / uppercase?"
#   A: Same approach — map still works; space becomes O(k)
#      where k is the number of distinct characters.
# ============================================================


class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for ch in s:                        # pass 1 — build frequency map
            seen[ch] = seen.get(ch, 0) + 1

        for i, ch in enumerate(s):          # pass 2 — find first unique
            if seen[ch] == 1:
                return i

        return -1                           # no unique character found


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("leetcode",      0),
        ("loveleetcode",  2),
        ("aabb",         -1),
        ("z",             0),   # single char
        ("aabbcc",       -1),   # all repeated
        ("aabbc",         4),   # unique at end
        ("abcabc",       -1),   # all repeat
    ]

    passed = 0
    for i, (s, expected) in enumerate(test_cases, 1):
        result = sol.firstUniqChar(s)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: {repr(s)} -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
