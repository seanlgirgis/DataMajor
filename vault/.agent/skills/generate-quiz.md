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

## Implementation (for the agent)
- Preconditions: `note_path` exists and contains `Quick Facts` or `Deep Dive` sections.
- Extraction heuristics:
    - Prefer `Quick Facts` bullets as direct fact->question sources.
    - For each bullet, generate a short question; for compound bullets, split into multiple questions.
    - Use `Deep Dive` for 1-2 higher-difficulty short-answer questions.
- Question types:
    - Multiple Choice (3 options) for factual bullets.
    - Short Answer for deeper concepts.
- Idempotency: If `## Practice Quiz` already exists, append with a timestamped subheading instead of duplicating.
- Output formatting: Use Obsidian callouts for questions and collapsible answers (keep answers visible only on user request).

## Example output snippet
> [!QUESTION] What is the time complexity of list append in Python?
>
> A) O(1)
>
> B) O(n)
>
> C) O(log n)
>
> > [!SUCCESS] - Answer
> > A) O(1)

## Safety
- Do not infer facts that are not present in the source note. When uncertain, ask the user for clarification.
