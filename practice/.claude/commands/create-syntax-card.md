Create a syntax card for the topic: $ARGUMENTS

Generate a dense, scannable Markdown cheat sheet and save it to:
C:/DataMajor/practice/syntax-cards/syntax-card-{topic}.md

Rules:
- Filename: lowercase, hyphenated. Example: syntax-card-dict.md, syntax-card-stack.md
- One printed page max
- Code + short comment only — no prose, no paragraphs
- Align # comments to column 28 for readability
- Cover all interview-relevant operations: import (if needed), declare, add, update, delete, lookup, iterate, common patterns, edge cases
- Max 10 rows per section. If topic needs more, split into Part 1 and Part 2 files
- Show safe AND unsafe versions where relevant (e.g., dict.get() vs dict[key])
- Use Python 3 syntax only

Format:
```
# TOPIC — Syntax Card

## Core Operations
snippet                     # what it does

## Patterns
snippet                     # pattern name
```

After writing the file, confirm: "Card created: syntax-card-{topic}.md"
