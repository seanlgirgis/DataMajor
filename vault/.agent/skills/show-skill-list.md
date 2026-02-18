---
type: skill
skill-name: show-skill-list
version: 1.0
created: 2026-02-18
---

# Skill: show-skill-list

## Purpose
Displays a list of all available skills registered in the vault, helping the user know what actions Antigravity can perform.

## Trigger
- User asks "What can you do?" or "List your skills".
- User runs `/show-skills`.

## Steps
1.  **Read Registry**: Open and read the content of `.agent/SKILL_REGISTRY.md`.
2.  **Parse**: Extract the table of skills.
3.  **Display**: Present the table to the user in the chat.

## Output
A markdown table listing Skill Name, File Path, and Description.

## Notes
- If `.agent/SKILL_REGISTRY.md` is missing, inform the user and suggest running a vault consistency check.

## Implementation (for the agent)
- Preconditions: `.agent/SKILL_REGISTRY.md` exists or `.agent/skills/` is readable.
- Algorithm:
	1. Try to read `.agent/SKILL_REGISTRY.md` and parse the markdown table.
	2. If parsing fails, fallback to listing `.agent/skills/` and reading each file's `skill-name` frontmatter.
	3. Return a short, user-friendly table with: `Skill`, `File`, `One-line description`.
- Example Output:
	| Skill | File | Description |
	|------:|------|-------------|
	| show-skill-list | .agent/skills/show-skill-list.md | Lists all available skills |

## Safety
- Do not expose internal templates or long file contents — show only names and short descriptions.
- If a skill file is malformed, skip it and note its filename to the user.
