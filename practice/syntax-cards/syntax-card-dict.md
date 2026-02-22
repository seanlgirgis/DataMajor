# DICT — Syntax Card

## Declare
```python
d = {}                          # empty dict
d = {"a": 1, "b": 2}           # literal
d = dict(a=1, b=2)             # from kwargs
d = dict(zip(keys, vals))      # from two lists
```

## Read / Lookup
```python
d["key"]                        # get value; KeyError if missing
d.get("key")                    # safe get; returns None
d.get("key", 0)                 # safe get with default
"key" in d                      # membership check (O(1))
```

## Add / Update
```python
d["key"] = val                  # add or overwrite
d.update({"x": 1, "y": 2})     # merge another dict
d.setdefault("key", 0)         # set only if key absent
```

## Delete
```python
del d["key"]                    # remove; KeyError if missing
d.pop("key")                    # remove + return; KeyError if missing
d.pop("key", None)             # safe remove with default
d.clear()                       # empty the dict
```

## Iterate
```python
for k in d:                     # keys only
for k, v in d.items():         # key-value pairs
for v in d.values():           # values only
for k in sorted(d):            # sorted keys
```

## Common Patterns
```python
# frequency count
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1

# frequency count (cleaner)
from collections import Counter
freq = Counter(s)               # Counter("aab") → {a:2, b:1}
freq.most_common(2)            # top 2 elements

# default dict (avoid KeyError on missing)
from collections import defaultdict
d = defaultdict(int)            # default value = 0
d = defaultdict(list)          # default value = []
d["key"] += 1                  # no KeyError

# invert a dict
inv = {v: k for k, v in d.items()}

# dict comprehension
squares = {x: x**2 for x in range(5)}
```

## Sizes / Info
```python
len(d)                          # number of keys
max(d, key=d.get)              # key with max value
min(d, key=d.get)              # key with min value
```
