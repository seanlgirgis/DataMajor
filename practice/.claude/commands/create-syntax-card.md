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

Always generate TWO files:
1. syntax-card-{topic}.md  — Markdown version
2. syntax-card-{topic}.html — Print-ready HTML with monospace font, tight spacing, colored comments, print CSS (@page letter, 0.4in margins)

The HTML must be self-contained: all CSS inline in <style> tag, no external dependencies.
Use <span class="comment"> with color #555 for # comments inside <pre> blocks.

LAYOUT RULE — ALWAYS use a two-column grid layout in the HTML:
  display: grid; grid-template-columns: 1fr 1fr; gap: 0 16px;
  Distribute sections evenly between left and right columns to fill the page.
  Only fall back to single column if the topic genuinely has fewer than 4 sections.

After writing both files, confirm: "Card created: syntax-card-{topic}.md + .html — open HTML in browser and Ctrl+P to print."
