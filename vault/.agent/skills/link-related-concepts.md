---
type: skill
skill-name: link-related-concepts
version: 1.0
created: 2026-02-18
---

# Skill: link-related-concepts

## Purpose
Scans a note for keywords that match other existing notes in the vault and converts them into internal links, increasing knowledge connectivity.

## Trigger
- User asks "Link concepts in [Note]".
- User runs `/link [Note]`.

## Arguments
- `target_file`: The note to scan.

## Steps
1.  **Index Vault**: Get a list of all file names in `01-concepts` and `02-technologies`. (e.g., "Python Lists", "AWS Lambda").
2.  **Read Target**: Read the content of `target_file`.
3.  **Scan & Replace**:
    -   Iterate through the index.
    -   If a concept name appears in the text (and isn't already linked), replace it with `[[Concept Name]]`.
    -   *Constraint*: Do not link inside code user blocks or URLs.
4.  **Update File**: Write the modified content back to `target_file`.
5.  **Report**: Tell user how many new links were created.

## Output
- Modified note with more internal `[[links]]`.
