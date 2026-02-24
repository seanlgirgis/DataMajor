r"""
That's clean and correct. One dict version is even tighter but this works perfectly for an interview. We're a go.

---

**Problem 5 — LeetCode #20 — Valid Parentheses**

Given a string containing only `(`, `)`, `{`, `}`, `[`, `]`, return `True` if the string is valid.

A string is valid if:
- Every open bracket has a corresponding closing bracket
- Brackets close in the correct order

```
Input:  s = "()"
Output: True

Input:  s = "()[]{}"
Output: True

Input:  s = "(]"
Output: False

Input:  s = "([)]"
Output: False

Input:  s = "{[]}"
Output: True
```

**Hint:** Think stack. This is a classic.

Take your shot.

"""

"""r
Thinking sctachpad
I would store the paranthese into a dict. with a each key and val matching.
.keys are my open.values are my closed

input string is a stack..
take LIFO mode.

If stack is empty you can only insert open .. Other wise go die
if the current is a close to to the top of the stack pop it. 
yo unever store closes.. always storing opens.

if stack length is not zero at the end.. go die
if stack is zero length --> return true 
"""


def is_valid (ss: str)->bool:

    p_map = {"(": ")", "{": "}", "[": "]"}
    stack = []
    

    vs = p_map.values()

    
    for ch in ss:
        #if it is in keys add to stack
        if ch in vs:
            if not stack:
                return False
            elif p_map[stack[-1]] == ch:
                stack.pop()
            else: # There is a stack and its top does nto match a closing 
                return False
        else: # it is an open
            stack.append(ch)
    return not stack  
    
print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(}"))