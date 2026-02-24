# SLIDING WINDOW — Syntax Card

## Fixed-Size Window
```python
# Sum of every window of size k
window_sum = sum(nums[:k])
result = [window_sum]
for i in range(k, len(nums)):
    window_sum += nums[i] - nums[i - k]   # add right, drop left
    result.append(window_sum)
```

## Variable-Size Window — longest valid window
```python
# Longest substring with at most k distinct chars
l = 0
window = {}   # or Counter
best = 0
for r, ch in enumerate(s):
    window[ch] = window.get(ch, 0) + 1
    while len(window) > k:              # shrink until valid
        window[s[l]] -= 1
        if window[s[l]] == 0: del window[s[l]]
        l += 1
    best = max(best, r - l + 1)        # window size = r - l + 1
```

## Longest Substring Without Repeating (LC 0003)
```python
l = 0
seen = {}   # char -> last index
best = 0
for r, ch in enumerate(s):
    if ch in seen and seen[ch] >= l:
        l = seen[ch] + 1               # jump l past last occurrence
    seen[ch] = r
    best = max(best, r - l + 1)
```

## Minimum Window — shortest valid window
```python
# Shrink right side as soon as window is valid
l = 0
need = Counter(t)
have, total = 0, len(need)
result = ""
for r, ch in enumerate(s):
    if ch in need:
        need[ch] -= 1
        if need[ch] == 0: have += 1
    while have == total:               # window is valid — try shrinking
        if not result or r-l+1 < len(result):
            result = s[l:r+1]
        if s[l] in need:
            need[s[l]] += 1
            if need[s[l]] > 0: have -= 1
        l += 1
```

## Key Formulas
```python
window_size  = r - l + 1
drop_element = nums[i - k]      # fixed window: element leaving
r - l        = current width    # variable window
```

## When to Use
```python
# Contiguous subarray/substring problem
# "longest / shortest / maximum / minimum" over a window
# O(n) replaces O(n^2) nested loop
```
