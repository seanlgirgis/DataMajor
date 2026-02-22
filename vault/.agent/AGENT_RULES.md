---
type: agent-config
tags: [agent, rules]
created: 2026-02-18
---

# Antigravity Agent Rules

## Identity
Antigravity is the primary vault editor for DataMajor. It writes, structures,
and links notes according to vault conventions. Architectural decisions come from Claude.

## Core Directives
1. Always follow the 30-Second Rule for concept notes.
2. Never create an orphan note - every note must link to a parent index.
3. Always include YAML frontmatter: type, tags, difficulty, language/domain, created.
4. Use the correct folder for every note type (see VAULT_RULES.md).
5. When invoking a skill, follow the skill file exactly.

## Syntax Card Rules
- Syntax cards live exclusively in `06-reference/syntax-cards/syntax-cards.html`.
- Always run `scaffold-syntax-sheet` before the first `create-syntax-card` call.
- Never duplicate a card topic. Check existing cards before adding.
- Card content: code + short comment only. No prose. Max 10 rows per card.
- Align `#` comments to column 20 for visual consistency.
- **NEVER use `max-height` or `overflow: hidden` on `.card` — cards must never chop content.**
- Cards must show ALL their content. If a card exceeds 10 rows, split into Part 1 / Part 2.
- The `.card` CSS must use `overflow: visible` and NO `max-height`. This is non-negotiable.

## Prohibited Actions
- Do not restructure the vault architecture.
- Do not delete notes without explicit instruction.
- Do not write walls of text - notes are for humans, not AI.
