# LeetCode #387 - First Unique Character in a String
# Difficulty: Easy
# Approach: Two-pass hash map | Time: O(n) | Space: O(1) (max 26 keys)

def firstUniqChar(s: str) -> int:
    """
    Returns the index of the first non-repeating character in s.
    Returns -1 if no unique character exists.
    
    Pass 1: Count frequency of each character.
    Pass 2: Return index of first character with count == 1.
    """
    cnt = {}
    for ch in s:
        cnt[ch] = cnt.get(ch, 0) + 1

    for i, ch in enumerate(s):
        if cnt[ch] == 1:
            return i

    return -1

# --- Tests ---
print(firstUniqChar("leetcode"))      # 0
print(firstUniqChar("loveleetcode"))  # 2
print(firstUniqChar("aabb"))          # -1