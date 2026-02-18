---
type: skill
skill-name: generate-quiz
version: 1.0
created: 2026-02-18
---

# Skill: generate-quiz

## Purpose
Creates an active recall quiz based on an existing concept note to test understanding.

## Trigger
- User asks "Quiz me on [Topic]".
- User runs `/quiz [Topic]`.

## Arguments
- `note_path`: Path to an existing concept note.

## Steps
1.  **Read Note**: Extract "Quick Facts" and "Deep Dive" sections from the target note.
2.  **Generate Questions**: Create 3-5 questions.
    -   Mix of Multiple Choice and Short Answer.
    -   Include answers (hidden by default).
3.  **Format Output**:
    -   Use Obsidian Callouts (collapsible) for answers to enable self-testing.
    -   Format:
        ```markdown
        > [!QUESTION] Question 1
        > What is...?
        >
        > > [!SUCCESS]- Answer
        > > The answer is...
        ```
4.  **Append**: Add the quiz to the bottom of the original concept note under a `## Practice Quiz` header.
5.  **Notify**: Tell user the quiz has been added to the note.

## Output
- Modified concept note with appended quiz section.
