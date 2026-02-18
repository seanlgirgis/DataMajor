---
type: skill
skill-name: scaffold-code-exercise
version: 1.0
created: 2026-02-18
---

# Skill: scaffold-code-exercise

## Purpose
Creates a runnable code file for practice and links it to a corresponding concept note, enforcing the "Theory + Practice" loop.

## Trigger
- User asks "I want to practice [Topic]".
- User runs `/code [Topic]`.

## Arguments
- `filename`: logical name for the script (e.g., `list_comp_practice.py`).
- `language`: programming language (e.g., `python`, `sql`). Defaults to `python` if ambiguous.
- `concept`: The related concept title (e.g., "List Comprehension").

## Steps
1.  **Verify Concept**: Check if `01-concepts/{language}/{concept}.md` exists.
    -   If NO: Trigger `create-concept-note` first for that concept.
2.  **Create Code File**:
    -   Path: `03-code/{language}/{filename}`.
    -   Content:
        ```python
        # Practice: ${concept}
        # Linked Note: [[01-concepts/${language}/${concept}|${concept}]]
        
        def main():
            # TODO: Implement practice logic here
            pass
        
        if __name__ == "__main__":
            main()
        ```
3.  **Link Back**:
    -   Append to `01-concepts/{language}/{concept}.md` under `## Code Example` or a new `## Practice` section:
        -   `Practice File: [[03-code/${language}/${filename}]]`
4.  **Notify**: Confirm both files are ready and linked.

## Output
- A `.py` (or other ext) file in `03-code/`.
- An updated or new `.md` file in `01-concepts/`.
