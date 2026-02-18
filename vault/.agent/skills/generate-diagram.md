---
type: skill
skill-name: generate-diagram
version: 1.0
created: 2026-02-18
---

# Skill: generate-diagram

## Purpose
Visualizes complex concepts or flows using Mermaid.js diagrams embedded in notes.

## Trigger
- User asks "Draw a diagram for [Topic]".
- User runs `/diagram [Description]`.

## Arguments
- `description`: What to visualize.
- `type`: (Optional) `flowchart`, `sequence`, `class`, `state`. Default: inferred.

## Steps
1.  **Generate Code**: Create valid Mermaid syntax based on the description.
    -   Ensure standard direction (TD or LR).
    -   Use readable node labels.
2.  **Create File**:
    -   Path: `05-diagrams/{topic_slug}.md`.
    -   Content:
        ```markdown
        ---
        type: diagram
        tags: [mermaid, diagram]
        ---
        \`\`\`mermaid
        [Mermaid Code Here]
        \`\`\`
        ```
3.  **Embed (Optional)**: If triggered from an active note context, embed the diagram:
    -   `![[05-diagrams/{topic_slug}]]`
4.  **Notify**: Show the diagram file path.

## Output
- A new `.md` file in `05-diagrams/`.
