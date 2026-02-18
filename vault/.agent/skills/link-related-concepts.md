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

## Implementation (for the agent)
- Preconditions: Vault indexes available (scan `01-concepts/` and `02-technologies/`).
- Indexing:
    1. Build a list of candidate titles and their canonical paths from `01-concepts/**` and `02-technologies/**`.
    2. Normalize match keys by lowercasing and trimming punctuation.
- Scanning & linking algorithm:
    1. Read `target_file` content and split into block segments to detect code fences (```), YAML frontmatter, and inline links.
    2. For each candidate title, search only in non-code, non-link sections and ensure the exact phrase is not already linked.
    3. Replace first or relevant occurrences with `[[Canonical Note Title]]`.
    4. Keep replacements conservative: prefer whole-word matches and require length >= 3 characters.
- Backup: Before writing, save a `.bak` copy alongside the target file.
- Reporting: Return the number of new links added and the list of files referenced.

## Safety
- Never modify text inside code blocks, YAML frontmatter, or URLs. Make a backup before writing changes.
