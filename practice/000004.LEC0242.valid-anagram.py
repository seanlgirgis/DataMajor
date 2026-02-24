r"""
Problem 4 — LeetCode #242 — Valid Anagram
Given two strings s and t, return True if t is an anagram of s, otherwise return False.
An anagram uses the same characters the same number of times, just in a different order.
Input:  s = "anagram", t = "nagaram"
Output: True

Input:  s = "rat", t = "car"
Output: False

Input:  s = "ab", t = "a"
Output: False
Constraint: O(n) solution. No sorting allowed.
Take your shot.

"""

r"""
Thinking

It seems to be count problem
use hasmap (ch, count)
Compare two hashmaps ->equal ; ret True -> else ret False

Early checks. are they the sme length

second check  .. Can be useful or not .. Depends on the length of input. early check on hashmap 2 .. while inserting of key not in 1 .. break

"""

def is_anagram (s1: str, s2:str)->bool:
    if len(s1) != len(s2):
        return False
    s1_map = {}
    s2_map = {}
    #s1 full path 
    for ch in s1:
        s1_map[ch] = s1_map.get(ch, 0) + 1
    for ch in s2:
        if not ch in s1_map:
            return False
        
        s2_map[ch] = s2_map.get(ch, 0) + 1
    return (s1_map == s2_map)
        
print(is_anagram("rat","tar"))
print(is_anagram("ab","a"))
print(is_anagram("rat","car"))
print(is_anagram("anagram","nagaram"))
