---
type: skill
skill-name: create-concept-note
version: 1.0
created: 2026-02-18
---

# Skill: create-concept-note

## Purpose
Creates a new structured concept note in the appropriate domain folder, ensuring adherence to the **30-Second Rule**.

## Trigger
- User asks "Create a note for [Topic] in [Domain]".
- User runs `/create-note [Topic] [Domain]`.

## Arguments
- `title`: The name of the concept (e.g., "List Comprehension").
- `domain`: The subject area (e.g., "python", "sql", "aws"). Use lowercase kebab-case.
- `difficulty`: (Optional) "Beginner", "Intermediate", "Advanced". Default: "Beginner".
- `tags`: (Optional) List of tags. Default: `[concept, {domain}]`.

## Steps
1.  **Validate Domain**: Check if `01-concepts/{domain}/` exists. If not, create it.
2.  **Check Index**: Check if `01-concepts/{domain}/_index.md` exists. If not, create a basic index file linking to `01-concepts/_master_index.md`.
3.  **Construct Path**: Target file is `01-concepts/{domain}/{title}.md`.
4.  **Content Generation**:
    -   Generate **YAML Frontmatter**:
        ```yaml
        ---
        type: concept
        tags: ${tags}
        difficulty: ${difficulty}
        domain: ${domain}
        created: ${YYYY-MM-DD}
        ---
        ```
    -   Generate **Body** (30-Second Rule):
        ```markdown
        # ${title}
        
        **One-liner**: [One sentence definition]
        
        ## Mental Model
        [Analogy or diagram description]
        
        ## Quick Facts
        - [Fact 1]
        - [Fact 2]
        - [Fact 3]
        
        ## Code Example
        \`\`\`python
        # minimal example
        \`\`\`
        
        ## Related Links
        - [[01-concepts/${domain}/_index|${domain} Index]]
        
        ## Deep Dive
        [Detailed explanation]
        ```
5.  **Write File**: Save the file.
6.  **Confirmation**: Notify the user with a link to the new note.

## Output
A new `.md` file in `01-concepts/{domain}/`.
