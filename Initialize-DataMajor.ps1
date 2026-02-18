# Initialize-DataMajor.ps1
# Run from: C:\DataaMajor
# Usage: .\Initialize-DataMajor.ps1

param(
    [string]$VaultRoot = ".\vault"
)

$ErrorActionPreference = "Stop"
$today = Get-Date -Format "yyyy-MM-dd"

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  DataMajor Vault Initialization Script"    -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

function New-Dir {
    param([string]$Path)
    if (-not (Test-Path $Path)) {
        New-Item -ItemType Directory -Path $Path -Force | Out-Null
        Write-Host "  [+] $Path" -ForegroundColor Green
    } else {
        Write-Host "  [~] $Path (exists)" -ForegroundColor DarkGray
    }
}

function New-File {
    param([string]$Path, [string]$Content)
    if (-not (Test-Path $Path)) {
        $Content | Set-Content -Path $Path -Encoding UTF8
        Write-Host "  [f] $Path" -ForegroundColor Yellow
    } else {
        Write-Host "  [~] $Path (exists)" -ForegroundColor DarkGray
    }
}

# ─────────────────────────────────────────────
# ROOT LEVEL FILES
# ─────────────────────────────────────────────

Write-Host ">> Root project files" -ForegroundColor White

New-File ".\README.md" "# DataMajor

Personal knowledge operating system for data engineering career mastery.

## Stack
- Vault editor: Obsidian (vault lives in /vault)
- AI Agent: Antigravity (Gemini) - primary vault writer
- Strategic advisor: Claude - architecture, planning, skill design

## Getting Started
Open /vault as your Obsidian vault root."

New-File ".\.gitignore" "# Obsidian workspace (local only)
vault/.obsidian/workspace.json
vault/.obsidian/workspace-mobile.json

# OS
.DS_Store
Thumbs.db
desktop.ini

# Jupyter
**/.ipynb_checkpoints/

# Python
__pycache__/
*.pyc
*.pyo

# Secrets
.env
*.env
secrets/

# Large diagram exports
vault/05-diagrams/exports/*.png
vault/05-diagrams/exports/*.svg"

New-File ".\CHANGELOG.md" "# Changelog

## [Unreleased]
- Vault initialization"

# ─────────────────────────────────────────────
# VAULT ROOT
# ─────────────────────────────────────────────

Write-Host ""
Write-Host ">> Vault root" -ForegroundColor White
New-Dir $VaultRoot

# ─────────────────────────────────────────────
# .obsidian config
# ─────────────────────────────────────────────

Write-Host ""
Write-Host ">> .obsidian config" -ForegroundColor White
New-Dir "$VaultRoot\.obsidian"

New-File "$VaultRoot\.obsidian\app.json" '{
  "newFileLocation": "folder",
  "newFileFolderPath": "00-inbox",
  "useMarkdownLinks": true,
  "strictLineBreaks": false,
  "showFrontmatter": true
}'

New-File "$VaultRoot\.obsidian\appearance.json" '{
  "theme": "moonstone"
}'

# ─────────────────────────────────────────────
# .agent
# ─────────────────────────────────────────────

Write-Host ""
Write-Host ">> .agent - Antigravity config" -ForegroundColor White

New-Dir "$VaultRoot\.agent"
New-Dir "$VaultRoot\.agent\skills"
New-Dir "$VaultRoot\.agent\templates"
New-Dir "$VaultRoot\.agent\logs"

New-File "$VaultRoot\.agent\AGENT_RULES.md" "---
type: agent-config
tags: [agent, rules]
created: $today
---

# Antigravity Agent Rules

## Identity
Antigravity is the primary vault editor for DataMajor. It writes, structures,
and links notes according to vault conventions. Architectural decisions come from Claude.

## Core Directives
1. Always follow the 30-Second Rule for concept notes.
2. Never create an orphan note - every note must link to a parent index.
3. Always include YAML frontmatter: type, tags, difficulty, language/domain, created.
4. Use the correct folder for every note type (see VAULT_RULES.md).
5. When invoking a skill, follow the skill file exactly.

## Prohibited Actions
- Do not restructure the vault architecture.
- Do not delete notes without explicit instruction.
- Do not write walls of text - notes are for humans, not AI."

New-File "$VaultRoot\.agent\SKILL_REGISTRY.md" "---
type: agent-config
tags: [agent, skills]
created: $today
---

# Skill Registry

| Skill | File | Description |
|-------|------|-------------|
| show-skill-list | skills/show-skill-list.md | Lists all available skills |
| create-concept-note | skills/create-concept-note.md | Creates a structured concept note |
| scaffold-code-exercise | skills/scaffold-code-exercise.md | Creates paired .py + concept note |
| generate-quiz | skills/generate-quiz.md | Builds a quiz from a concept note |
| link-related-concepts | skills/link-related-concepts.md | Finds and links related concepts |
| generate-diagram | skills/generate-diagram.md | Creates a Mermaid diagram |
| daily-review | skills/daily-review.md | Generates a journal review entry |"

# Skill stub files
$skills = @("show-skill-list","create-concept-note","scaffold-code-exercise","generate-quiz","link-related-concepts","generate-diagram","daily-review")
foreach ($skill in $skills) {
    New-File "$VaultRoot\.agent\skills\$skill.md" "---
type: skill
skill-name: $skill
version: 0.1
created: $today
---

# Skill: $skill

## Purpose
[Define what this skill does]

## Trigger
[How to invoke this skill]

## Steps
1. [Step 1]
2. [Step 2]

## Output
[What this skill produces]

## Notes
[Any edge cases or caveats]"
}

# Templates
New-File "$VaultRoot\.agent\templates\concept-note.md" "---
type: concept
tags: []
difficulty: beginner
language:
domain:
created: {{date}}
---

# {{title}}

> One-liner: what this is in one sentence.

## Mental Model
[The intuition. How to think about this.]

## Quick Facts
- Fact 1
- Fact 2

## Code Example
\`\`\`python
# example
\`\`\`

## Related
- [[link-1]]
- [[link-2]]

## Deep Dive
[Optional: longer explanation or external links]"

New-File "$VaultRoot\.agent\templates\code-exercise.md" "---
type: code-exercise
tags: []
difficulty: beginner
language:
linked-concept:
created: {{date}}
---

# Exercise: {{title}}

## Goal
[What this exercise teaches]

## File
03-code/python/exercises/{{filename}}.py

## Instructions
1. Step 1
2. Step 2

## Expected Output
[expected output here]"

New-File "$VaultRoot\.agent\templates\daily-review.md" "---
type: journal
tags: [daily-review]
date: {{date}}
focus:
created: {{date}}
---

# Daily Review - {{date}}

## What I Worked On
-

## What Clicked
-

## What's Still Fuzzy
-

## Tomorrow's Focus
-"

# ─────────────────────────────────────────────
# 00-inbox
# ─────────────────────────────────────────────

Write-Host ""
Write-Host ">> 00-inbox" -ForegroundColor White
New-Dir "$VaultRoot\00-inbox"
New-File "$VaultRoot\00-inbox\README.md" "# Inbox

Drop unprocessed notes here. Antigravity will file them."

# ─────────────────────────────────────────────
# 01-concepts
# ─────────────────────────────────────────────

Write-Host ""
Write-Host ">> 01-concepts" -ForegroundColor White

$conceptDirs = @(
    "01-concepts",
    "01-concepts\python",
    "01-concepts\python\fundamentals",
    "01-concepts\python\data-structures",
    "01-concepts\python\functions",
    "01-concepts\python\oop",
    "01-concepts\python\modules-and-packages",
    "01-concepts\python\file-io",
    "01-concepts\python\error-handling",
    "01-concepts\python\comprehensions",
    "01-concepts\python\decorators",
    "01-concepts\python\async",
    "01-concepts\sql",
    "01-concepts\sql\basics",
    "01-concepts\sql\joins",
    "01-concepts\sql\aggregations",
    "01-concepts\sql\window-functions",
    "01-concepts\sql\indexes",
    "01-concepts\sql\query-optimization",
    "01-concepts\data-engineering",
    "01-concepts\data-engineering\pipelines",
    "01-concepts\data-engineering\batch-vs-streaming",
    "01-concepts\data-engineering\data-modeling",
    "01-concepts\data-engineering\orchestration",
    "01-concepts\data-engineering\data-quality",
    "01-concepts\data-engineering\storage-formats",
    "01-concepts\r",
    "01-concepts\java",
    "01-concepts\scala"
)
foreach ($d in $conceptDirs) { New-Dir "$VaultRoot\$d" }

New-File "$VaultRoot\01-concepts\_INDEX.md" "---
type: index
tags: [index, concepts]
created: $today
---

# Concepts Index

## Python
- [[01-concepts/python/fundamentals/_INDEX]]

## SQL
- [[01-concepts/sql/_INDEX]]

## Data Engineering
- [[01-concepts/data-engineering/_INDEX]]

## R | Java | Scala
- (coming in later phases)"

# ─────────────────────────────────────────────
# 02-technologies
# ─────────────────────────────────────────────

Write-Host ""
Write-Host ">> 02-technologies" -ForegroundColor White

$techDirs = @(
    "02-technologies",
    "02-technologies\aws",
    "02-technologies\aws\s3",
    "02-technologies\aws\ec2",
    "02-technologies\aws\glue",
    "02-technologies\aws\redshift",
    "02-technologies\aws\lambda",
    "02-technologies\aws\athena",
    "02-technologies\gcp",
    "02-technologies\gcp\bigquery",
    "02-technologies\gcp\dataflow",
    "02-technologies\azure",
    "02-technologies\snowflake",
    "02-technologies\kafka",
    "02-technologies\spark",
    "02-technologies\dbt",
    "02-technologies\airflow",
    "02-technologies\docker",
    "02-technologies\git"
)
foreach ($d in $techDirs) { New-Dir "$VaultRoot\$d" }

New-File "$VaultRoot\02-technologies\_INDEX.md" "---
type: index
tags: [index, technologies]
created: $today
---

# Technologies Index

## Cloud
- AWS | GCP | Azure

## Data Warehouses
- Snowflake | Redshift | BigQuery

## Streaming
- Kafka

## Processing + Orchestration
- Spark | dbt | Airflow

## DevOps
- Docker | Git"

# ─────────────────────────────────────────────
# 03-code
# ─────────────────────────────────────────────

Write-Host ""
Write-Host ">> 03-code" -ForegroundColor White

$codeDirs = @(
    "03-code",
    "03-code\python",
    "03-code\python\snippets",
    "03-code\python\exercises",
    "03-code\python\projects",
    "03-code\sql",
    "03-code\sql\queries",
    "03-code\notebooks",
    "03-code\notebooks\python",
    "03-code\notebooks\exploratory",
    "03-code\r",
    "03-code\scala",
    "03-code\java"
)
foreach ($d in $codeDirs) { New-Dir "$VaultRoot\$d" }

New-File "$VaultRoot\03-code\python\snippets\README.md" "# Python Snippets

Runnable terminal scripts. Each snippet should have a paired concept note."

New-File "$VaultRoot\03-code\notebooks\README.md" "# Notebooks

Jupyter notebooks for visual and exploratory learning.
Start Jupyter with: jupyter lab"

# ─────────────────────────────────────────────
# 04-leetcode
# ─────────────────────────────────────────────

Write-Host ""
Write-Host ">> 04-leetcode" -ForegroundColor White

$leetDirs = @(
    "04-leetcode",
    "04-leetcode\arrays",
    "04-leetcode\strings",
    "04-leetcode\hashmaps",
    "04-leetcode\two-pointers",
    "04-leetcode\sliding-window",
    "04-leetcode\binary-search",
    "04-leetcode\trees",
    "04-leetcode\graphs",
    "04-leetcode\dynamic-programming",
    "04-leetcode\sorting"
)
foreach ($d in $leetDirs) { New-Dir "$VaultRoot\$d" }

New-File "$VaultRoot\04-leetcode\PROGRESS.md" "---
type: tracker
tags: [leetcode, progress]
created: $today
---

# LeetCode Progress

| Problem | Difficulty | Pattern | Status | Date |
|---------|------------|---------|--------|------|
| | | | | |"

# ─────────────────────────────────────────────
# 05-diagrams
# ─────────────────────────────────────────────

Write-Host ""
Write-Host ">> 05-diagrams" -ForegroundColor White
New-Dir "$VaultRoot\05-diagrams"
New-Dir "$VaultRoot\05-diagrams\source"
New-Dir "$VaultRoot\05-diagrams\exports"
New-File "$VaultRoot\05-diagrams\README.md" "# Diagrams

Mermaid/PlantUML source lives in source/.
Exported images go in exports/ (gitignored for size)."

# ─────────────────────────────────────────────
# 06-cheatsheets
# ─────────────────────────────────────────────

Write-Host ""
Write-Host ">> 06-cheatsheets" -ForegroundColor White

$cheatDirs = @(
    "06-cheatsheets",
    "06-cheatsheets\python",
    "06-cheatsheets\sql",
    "06-cheatsheets\aws",
    "06-cheatsheets\git",
    "06-cheatsheets\terminal"
)
foreach ($d in $cheatDirs) { New-Dir "$VaultRoot\$d" }

# ─────────────────────────────────────────────
# 07-roadmaps
# ─────────────────────────────────────────────

Write-Host ""
Write-Host ">> 07-roadmaps" -ForegroundColor White
New-Dir "$VaultRoot\07-roadmaps"

New-File "$VaultRoot\07-roadmaps\MASTER_ROADMAP.md" "---
type: roadmap
tags: [roadmap, planning]
created: $today
---

# Master Roadmap

## Phase 1 - Foundation (Current)
- [ ] Python fundamentals
- [ ] SQL core (joins, aggregations, window functions)
- [ ] Data Engineering concepts (pipelines, batch vs streaming)

## Phase 2 - Cloud and Warehousing
- [ ] AWS core (S3, Glue, Redshift, Athena, Lambda)
- [ ] Snowflake
- [ ] BigQuery
- [ ] Kafka basics

## Phase 3 - Advanced Engineering
- [ ] Spark
- [ ] dbt
- [ ] Airflow
- [ ] R
- [ ] Java / Scala

## Phase 4 - Mastery and Portfolio
- [ ] End-to-end pipeline projects
- [ ] LeetCode pattern coverage
- [ ] Full GCP + Azure"

New-File "$VaultRoot\07-roadmaps\CURRENT_FOCUS.md" "---
type: roadmap
tags: [roadmap, focus]
created: $today
---

# Current Focus

Phase: 1 - Foundation
Active topics: Python fundamentals, SQL basics
This week: Vault initialization + first concept notes

## Active Skills Being Built
- [ ] create-concept-note
- [ ] scaffold-code-exercise"

# ─────────────────────────────────────────────
# 08-journal
# ─────────────────────────────────────────────

Write-Host ""
Write-Host ">> 08-journal" -ForegroundColor White
New-Dir "$VaultRoot\08-journal"
New-File "$VaultRoot\08-journal\README.md" "# Learning Journal

Daily review entries generated by Antigravity using the daily-review skill."

# ─────────────────────────────────────────────
# _meta
# ─────────────────────────────────────────────

Write-Host ""
Write-Host ">> _meta" -ForegroundColor White
New-Dir "$VaultRoot\_meta"

New-File "$VaultRoot\_meta\VAULT_RULES.md" "---
type: meta
tags: [vault, rules]
created: $today
---

# Vault Rules

## The 30-Second Rule
Every concept note must be useful in 30 seconds.
Structure: One-liner > Mental Model > Quick Facts > Code Example > Related Links > Deep Dive

## Frontmatter
All notes require YAML frontmatter with at minimum:
- type
- tags
- difficulty
- language or domain
- created (YYYY-MM-DD)

## No Orphan Notes
Every note must link to a parent index.

## Folder Conventions
| Folder | Contents |
|--------|----------|
| 00-inbox | Unprocessed drops |
| 01-concepts | Knowledge by language/domain |
| 02-technologies | Tools, platforms, cloud |
| 03-code | Runnable scripts and notebooks |
| 04-leetcode | Algorithm practice |
| 05-diagrams | Mermaid/PlantUML source |
| 06-cheatsheets | Quick reference |
| 07-roadmaps | Learning paths |
| 08-journal | Daily learning log |
| _meta | Glossary, rules, master index |"

New-File "$VaultRoot\_meta\GLOSSARY.md" "---
type: meta
tags: [glossary]
created: $today
---

# Glossary

| Term | Definition |
|------|-----------|
| | |"

New-File "$VaultRoot\_meta\MASTER_INDEX.md" "---
type: meta
tags: [index, master]
created: $today
---

# Master Index

## Concepts
- [[01-concepts/_INDEX]]

## Technologies
- [[02-technologies/_INDEX]]

## LeetCode
- [[04-leetcode/PROGRESS]]

## Roadmaps
- [[07-roadmaps/MASTER_ROADMAP]]
- [[07-roadmaps/CURRENT_FOCUS]]"

# ─────────────────────────────────────────────
# DONE
# ─────────────────────────────────────────────

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  Done! Vault scaffolded successfully."     -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor White
Write-Host "  1. Open Obsidian > Open folder as vault > select your vault folder" -ForegroundColor Gray
Write-Host "  2. Review vault\_meta\VAULT_RULES.md" -ForegroundColor Gray
Write-Host "  3. Fill in .agent\skills\ with Claude" -ForegroundColor Gray
Write-Host ""