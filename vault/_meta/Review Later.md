---
type: tracker
tags: [moc, review, tracker]
created: 2026-02-18
---

# Review Later

## Concepts to Revisit
- [ ] Named tuples 
- [ ] A tuple is exactly like a list but immutable 
- [ ] sort() vs sorted() on a List 
- [ ] reverse List or string using [::-1] 
- [ ] String processing in functions — never mutate strings, build new via list buffer + "".join(), or character by character. list(s) converts string to mutable char list. 
- [ ] Dictionary = Hashmap — same concept. hash() converts key to memory address, enables O(1) lookup and insert. Core reason dicts dominate LeetCode solutions.
- [ ] Two Sum pattern — hashmap stores seen values, complement lookup replaces nested loops. O(n) vs O(n²).
- [ ] dict KeyError — direct access [] and del crash on missing keys. Always use .get(key, default) and .pop(key, default) when key existence is uncertain. 

## Questions Unresolved
- [ ] 

## LeetCode Patterns to Practice
- [ ] 

## Related Links
- [[01-concepts/python/_index|Python Index]]
