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

## Implementation (for the agent)
- Preconditions: `concept` exists or user allows creation of the concept note first.
- File naming:
    - Target code folder: `03-code/{language}/` (create if missing).
    - Use `filename_slug` sanitized for filesystem.
- Idempotency: If the code file exists, do not overwrite; suggest a new name or open the existing file.
- Code template (Python example):
    ```python
    # Practice: {concept}
    # Linked Note: [[01-concepts/{language}/{concept}|{concept}]]

    def practice_{filename_var}():
            """Small exercise harness for {concept}."""
            # TODO: implement small example and assert-based tests
            pass


    if __name__ == "__main__":
            practice_{filename_var}()
    ```
- Linking back to the concept note:
    - If the concept note exists, append a single bullet under `## Practice` or create that header.
    - The bullet should be: `- Practice File: [[03-code/{language}/{filename}]]`.

## Example invocation
- `/code "list_comp_practice.py" python "List Comprehension"`

## Safety
- Do not execute or run user code. Only write scaffold files and tests.
