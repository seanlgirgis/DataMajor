# ============================================================
# 000032 | LC 0020 --- Valid Parentheses [REDO DRILL]
# Pattern   : Stack
# Difficulty : Easy
# ============================================================
# Time Complexity:  O(n) --- single pass through the string
# Space Complexity: O(n) --- stack can grow up to n in worst case (all opens)
# ============================================================
# Problem:
#   Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
#   determine if the input string is valid.
#   An input string is valid if:
#     1. Open brackets must be closed by the same type of brackets.
#     2. Open brackets must be closed in the correct order.
#     3. Every close bracket has a corresponding open bracket of the same type.
#
# Examples:
#   s = "()"      -> True
#   s = "()[]{}"  -> True
#   s = "(]"      -> False
#   s = "([)]"    -> False
#   s = "{[]}"    -> True
# ============================================================
# Key Insight:
#   Use a dictionary to map open brackets to their corresponding
#   close brackets. Iterate through the string: if it's an open
#   bracket, push it onto the stack. If it's a close bracket,
#   check if the stack is not empty and the top of the stack matches.
#   If so, pop the stack. If not, the string is invalid.
#   At the end, the stack MUST be empty for it to be valid.
# ============================================================

class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        if len(s) %2 != 0 : return False  #Odd
        p = {'(': ')', '{': '}', '[' :']'}
        stack = []
        for ch in s:
            if ch in p:  # Open paranthesis
                stack.append(ch)
            elif stack and  p[stack[-1]] == ch:
                stack.pop()
            else:
                return False
        #For isValid stack ought to be empty        
        return True if not stack else False



# ── Tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("]", False),          # extra closing
        ("((", False),         # extra opening
        ("", True)             # empty string
    ]

    passed = 0
    for i, (s, expected) in enumerate(test_cases, 1):
        result = sol.isValid(s)
        status = "PASS" if result == expected else f"FAIL (expected {expected})"
        print(f"Test {i}: '{s}' -> {result}  {status}")
        if result == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed")
