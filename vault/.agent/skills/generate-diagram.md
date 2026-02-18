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

## Implementation (for the agent)
- Preconditions: `description` provided; optional `context_note` path if embedding is requested.
- Filename: `topic_slug` derived from description, lowercase hyphenated; ensure uniqueness by appending a numeric suffix when collision occurs.
- Mermaid generation:
    - Produce minimal, readable node names and directions (default `TD`).
    - Prefer simple subgraphs for multi-part systems.
- File content template:
    ```markdown
    ---
    type: diagram
    tags: [mermaid, diagram]
    created: {YYYY-MM-DD}
    ---

    ```mermaid
    %% Mermaid code here
    ```
    ```
- Embedding: If a `context_note` is supplied, insert `![[05-diagrams/{topic_slug}]]` under a `## Diagram` header (idempotent).

## Example invocation
- `/diagram "ETL flow: source -> transform -> warehouse" --type flowchart --embed 01-concepts/data-engineering/etl.md`

## Safety
- Keep diagrams small (prefer multiple focused diagrams over one huge diagram). Do not overwrite existing diagrams without confirmation.
