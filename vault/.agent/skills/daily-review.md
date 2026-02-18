---
type: skill
skill-name: daily-review
version: 1.0
created: 2026-02-18
---

# Skill: daily-review

## Purpose
Generates a daily journal entry to track learning progress, focus, and achievements.

## Trigger
- User asks "Start daily review".
- User runs `/review`.

## Arguments
- `date`: Defaults to today (YYYY-MM-DD).

## Steps
1.  **Calculate Path**: `08-journal/{YYYY}/{MM}/{YYYY-MM-DD}.md`.
2.  **Ensure Directory**: Create `08-journal/{YYYY}/{MM}` if missing.
3.  **Gather Context**:
    -   **Roadmap Focus**: Read `07-roadmaps/current_focus.md` (if exists).
    -   **Activity**: partial scan of modified files today (optional, if easy).
4.  **Create Content**:
    ```markdown
    ---
    type: daily
    date: {YYYY-MM-DD}
    tags: [journal]
    ---
    # Daily Review: {YYYY-MM-DD}
    
    ## 🎯 Today's Focus
    - [ ] [Focus Item 1]
    
    ## 📝 Notes Created
    - 
    
    ## 💻 Code Written
    - 
    
    ## 🧠 Retrospective
    - **Win**: 
    - **Struggle**: 
    
    ## 🚀 Plan for Tomorrow
    - 
    ```
5.  **Write File**: Save the journal entry.
6.  **Open**: Present to user or open in editor.

## Output
- A new daily note in `08-journal/`.
