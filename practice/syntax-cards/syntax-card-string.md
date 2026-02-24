# STRING — Syntax Card

## Create & Access
```python
s = "hello"
s[0]            # 'h'
s[-1]           # 'o'
s[1:4]          # 'ell'  (end exclusive)
s[::-1]         # 'olleh' reversed copy
len(s)          # 5
```

## Strings are Immutable
```python
# s[0] = 'H'   -> TypeError!
# To modify: convert to list, then join
a = list(s)
a[0] = 'H'
s = ''.join(a)
```

## Search & Check
```python
"lo" in s               # True
s.find("ll")            # 2  (index, -1 if not found)
s.index("ll")           # 2  (raises ValueError if not found)
s.count("l")            # 2
s.startswith("hel")     # True
s.endswith("lo")        # True
```

## Case & Strip
```python
s.upper()       # "HELLO"
s.lower()       # "hello"
s.strip()       # remove leading/trailing whitespace
s.lstrip()      # left strip
s.rstrip()      # right strip
s.strip("x")    # strip specific char
```

## Split & Join
```python
"a,b,c".split(",")      # ['a','b','c']
"hello world".split()   # ['hello','world'] (any whitespace)
",".join(['a','b','c']) # 'a,b,c'
"".join(['h','i'])      # 'hi'
```

## Replace & Format
```python
s.replace("l", "r")         # 'herro'  (all occurrences)
s.replace("l", "r", 1)      # 'herlo'  (first only)
f"value={x}"                # f-string (fastest)
"value={}".format(x)        # .format
```

## Char & Ord
```python
ord('a')            # 97
chr(97)             # 'a'
ord(c) - ord('a')   # 0-25 index for lowercase letter

# Frequency map pattern
from collections import Counter
freq = Counter(s)           # {'l':2,'e':1,'h':1,'o':1}
```

## Useful Checks
```python
s.isalpha()     # all letters
s.isdigit()     # all digits
s.isalnum()     # letters or digits
s.isspace()     # all whitespace
```

## Sort / Anagram
```python
sorted("eat")           # ['a','e','t']
''.join(sorted("eat"))  # 'aet'  <- anagram key
```

## Multiline / Raw
```python
s = """line1
line2"""
s = r"\n is not newline"    # raw string
```

## Common Patterns
```python
# Palindrome check
s == s[::-1]

# Anagram check
Counter(s) == Counter(t)   # or sorted(s) == sorted(t)

# Character frequency
for ch in set(s):
    print(ch, s.count(ch))

# Build string efficiently (avoid repeated +)
parts = []
parts.append(x)
result = ''.join(parts)    # O(n) vs repeated + which is O(n^2)
```
