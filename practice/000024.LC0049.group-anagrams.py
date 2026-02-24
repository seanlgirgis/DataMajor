# ============================================================
# 000024 | LC 0049 — Group Anagrams
# Pattern   : Hash Map — Sorted Key Grouping
# Difficulty : Medium
# ============================================================
# Time Complexity:  O(n * k log k)
#   n = number of strings, k = max string length
#   Sorting each string costs O(k log k); done n times.
#
# Space Complexity: O(n * k)
#   Storing all strings in the map.
# ============================================================
# Problem:
#   Given an array of strings strs, group the anagrams together.
#   Return the answer in any order.
#   Two strings are anagrams if one is a rearrangement of the other.
#
# Examples:
#   strs = ["eat","tea","tan","ate","nat","bat"]
#     ->  [["bat"],["nat","tan"],["ate","eat","tea"]]
#   strs = [""]   ->  [[""]]
#   strs = ["a"]  ->  [["a"]]
# ============================================================
# Key Insight:
#   All anagrams produce the SAME string when their characters
#   are sorted. Use that sorted string as the hash map key.
#   Group original strings under their key → values() = answer.
#
#   "eat" -> "aet"
#   "tea" -> "aet"   (same key -> same group)
#   "tan" -> "ant"   (different key -> different group)
#
#   Use defaultdict(list) so d[key].append() works without
#   checking if key exists. NEVER use d.get(key, []).append() —
#   that creates a throwaway list that is NOT stored in the dict.
# ============================================================
# Interviewer follow-ups:
#   Q: "Can you avoid sorting?" (faster key generation)
#   A: Yes — use a tuple of 26 letter counts as the key.
#      count = [0]*26; for c in s: count[ord(c)-ord('a')] += 1
#      key = tuple(count)  — O(k) per string vs O(k log k)
#
#   Q: "Why return d.values() and not list(d.values())?"
#   A: LeetCode accepts dict_values; in an interview both are
#      fine. list() makes the type explicit.
#
#   Q: "What's the space complexity?"
#   A: O(n * k) — all characters of all strings stored once.
# ============================================================

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = defaultdict(list)               # key: sorted string -> value: list of originals

        for s in strs:
            key = ''.join(sorted(s))        # anagrams share the same sorted form
            d[key].append(s)                # use d[key], NOT d.get(key, [])

        return list(d.values())


# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    def normalize(result):
        """Sort inner lists and outer list for order-independent comparison."""
        return sorted([sorted(g) for g in result])

    test_cases = [
        (["eat","tea","tan","ate","nat","bat"],
         [["ate","eat","tea"],["bat"],["nat","tan"]]),
        ([""],        [[""]]),
        (["a"],       [["a"]]),
        (["ab","ba"], [["ab","ba"]]),
        (["abc","bca","cab","xyz","zyx"],
         [["abc","bca","cab"],["xyz","zyx"]]),
        (["a","b","c"], [["a"],["b"],["c"]]),   # no anagrams
    ]

    passed = 0
    for i, (strs, expected) in enumerate(test_cases, 1):
        result = sol.groupAnagrams(strs)
        norm_result = normalize(result)
        norm_expected = normalize(expected)
        status = "PASS" if norm_result == norm_expected else f"FAIL (expected {norm_expected})"
        print(f"Test {i}: {strs} -> {norm_result}  {status}")
        if norm_result == norm_expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
