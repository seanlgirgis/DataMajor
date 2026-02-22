---
type: skill
skill-name: export-syntax-sheet
version: 1.0
created: 2026-02-21
---

# Skill: export-syntax-sheet

## Purpose
Confirms the master syntax sheet is print-ready and gives the user instructions to print and cut.

## Trigger
- User says "export-syntax-sheet" or "print syntax cards"

## Arguments
None.

## Steps

1. **Verify file**: Check `06-reference/syntax-cards/syntax-cards.html` exists.
2. **Count cards**: Count the number of `<div class="card">` blocks between the markers.
3. **Report layout**:
   - Cards fit 2 per row.
   - Each page holds ~4 cards (2×2 grid).
   - Estimated pages = ceil(card_count / 4).
4. **Print instructions**: Output the following message to the user:

```
✅ Syntax sheet ready.
Cards: [N] | Est. pages: [P]

To print:
1. Open: 06-reference/syntax-cards/syntax-cards.html in any browser.
2. File → Print (or Ctrl+P / Cmd+P).
3. Set: Paper = Letter, Margins = Minimum, Scale = 100%.
4. Print and cut along card borders.

Tip: Print double-sided if you want concept notes on the back.
```

## Safety
- If file is missing, tell user to run `scaffold-syntax-sheet` first.
