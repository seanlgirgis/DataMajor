---
type: skill
skill-name: create-syntax-card
version: 1.0
created: 2026-02-21
---

# Skill: create-syntax-card

## Purpose
Generates a single syntax card block (HTML `<div>`) for a given data structure or concept,
and appends it to the master print sheet at `06-reference/syntax-cards/syntax-cards.html`.
Cards are designed to be printed on Letter/A4, cut to index-card size, and kept at the keyboard.

## Trigger
- User says "create-syntax-card — [Topic]"
- User runs `/create-syntax-card [Topic]`

## Arguments
- `topic`: The data structure or concept name (e.g., "List", "Binary Search", "Stack").
- `category`: (Optional) Group label shown in card header. Default: inferred from topic.

## Steps

1. **Load template**: Read `06-reference/syntax-cards/_card-template.html` for the card `<div>` block structure.
2. **Load master sheet**: Open `06-reference/syntax-cards/syntax-cards.html`.
3. **Generate card content**:
   - Title: `topic` in ALL CAPS.
   - Category badge: `category` (e.g., "Python DS", "Algorithm").
   - Syntax rows: each row is `code snippet` + `# comment` explaining what it does.
   - Include only operations that matter for interviews: add, remove, lookup, iterate, edge cases.
   - Max 10 rows per card. If more are needed, split into two cards (e.g., "LIST — Part 1", "LIST — Part 2").
   - Import line (if needed) shown at top of code block, visually distinct.
4. **Append card**: Insert the new card `<div>` inside `<!-- CARDS START -->` / `<!-- CARDS END -->` markers in the master sheet.
5. **Confirm**: Report back: "Card added: [Topic]. Total cards in sheet: [N]."

## Output Format (card HTML block)

```html
<div class="card">
  <div class="card-header">
    <span class="card-title">TOPIC</span>
    <span class="card-badge">Category</span>
  </div>
  <div class="card-body">
    <pre>
import_line_if_needed

snippet_1          # what it does
snippet_2          # what it does
snippet_3          # what it does
    </pre>
  </div>
</div>
```

## Content Rules
- Use monospace font only (handled by CSS in master sheet).
- Comments must be short — max 4 words.
- Align `#` comments to column 20 for readability.
- No explanatory prose. Code + comment only.
- Show the dangerous version AND the safe version where applicable (e.g., `remove` vs `discard`).
- **Max 10 rows per card.** If content exceeds 10 rows, split into two cards: "TOPIC — Part 1", "TOPIC — Part 2".
- **NEVER truncate or hide content.** Every line appended must be fully visible when printed.
- **NEVER set `max-height` or `overflow: hidden` on any card element.**

## Example invocation
- `/create-syntax-card "Linked List" --category "Python DS"`
- `/create-syntax-card "Binary Search"`

## Safety
- Never overwrite the master sheet — only append inside the markers.
- If `syntax-cards.html` does not exist, run `scaffold-syntax-sheet` first and notify user.
- If the card for this topic already exists, notify user and skip (do not duplicate).
