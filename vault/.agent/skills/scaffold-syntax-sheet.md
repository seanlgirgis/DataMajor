---
type: skill
skill-name: scaffold-syntax-sheet
version: 1.0
created: 2026-02-21
---

# Skill: scaffold-syntax-sheet

## Purpose
Creates the master print sheet `06-reference/syntax-cards/syntax-cards.html` from scratch.
This is a one-time setup step. Run this before using `create-syntax-card` for the first time.

## Trigger
- User says "scaffold-syntax-sheet"
- Automatically triggered by `create-syntax-card` if the master sheet is missing.

## Arguments
None.

## Steps

1. **Check path**: Verify `06-reference/syntax-cards/` exists. Create it if not.
2. **Write file**: Create `syntax-cards.html` using the full HTML template below.
3. **Confirm**: Report "Syntax sheet scaffolded at 06-reference/syntax-cards/syntax-cards.html. Ready for cards."

## Output: Full HTML Template

Write the following file verbatim, replacing only `${YYYY-MM-DD}` with today's date:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>DataMajor — Syntax Cards</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Courier New', Courier, monospace;
      font-size: 11px;
      background: #fff;
      color: #111;
      padding: 10mm;
    }

    h1 {
      font-size: 13px;
      text-align: center;
      margin-bottom: 8mm;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: #333;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 6mm;
    }

    .card {
      border: 1px solid #333;
      padding: 4mm 5mm;
      page-break-inside: avoid;
      break-inside: avoid;
      overflow: visible;
    }

    .card-header {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      border-bottom: 1px solid #333;
      padding-bottom: 2mm;
      margin-bottom: 3mm;
    }

    .card-title {
      font-size: 13px;
      font-weight: bold;
      letter-spacing: 1px;
    }

    .card-badge {
      font-size: 9px;
      color: #555;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .card-body pre {
      font-family: 'Courier New', Courier, monospace;
      font-size: 10px;
      line-height: 1.6;
      white-space: pre;
    }

    @media print {
      body { padding: 8mm; }
      .grid { gap: 5mm; }
      @page { margin: 8mm; size: Letter; }
    }
  </style>
</head>
<body>
  <h1>DataMajor · Syntax Cards · ${YYYY-MM-DD}</h1>
  <div class="grid">

    <!-- CARDS START -->

    <!-- CARDS END -->

  </div>
</body>
</html>
```

## Safety
- If the file already exists, do NOT overwrite. Notify user: "Sheet already exists. Use create-syntax-card to add cards."
