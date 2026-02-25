# add-lec-entry

You are joining an active LeetCode study project. Read and internalize
everything below before you do anything. Save it all to persistent memory
so it survives across sessions.

═══════════════════════════════════════════════════════════
ENVIRONMENT — DO THIS BEFORE ANY PYTHON COMMAND
═══════════════════════════════════════════════════════════

Before running Python, ALWAYS locate env_setter.ps1.
Search the agent working directory first, then one level up (parent).
Currently at:  c:\DataMajor\env_setter.ps1

It activates the venv at:  C:\py_venv\proj_educate

ALL Python must be run like this:
  powershell -ExecutionPolicy RemoteSigned -Command
    "& 'c:/DataMajor/env_setter.ps1'; python 'path/to/script.py'"

Never use bare `python` without that wrapper. openpyxl is installed.

═══════════════════════════════════════════════════════════
KEY FILE PATHS
═══════════════════════════════════════════════════════════

Problem inventory:   C:\DataMajor\practice\leetcode_files.xlsx
Study notes:         C:\DataMajor\practice\001Study\LEC.md
Skill command:       C:\DataMajor\practice\.claude\commands\add-lec-entry.md
Practice .py files:  C:\DataMajor\practice\  (naming: NNNNNN.LCXXXX.name.py)
Drill log:           C:\DataMajor\practice\drill-log.md
Syntax cards:        C:\DataMajor\practice\syntax-cards\

═══════════════════════════════════════════════════════════
SKILL: /add-lec-entry <number>
═══════════════════════════════════════════════════════════

The full skill instructions live in add-lec-entry.md above. Read that
file at the start of every session. Below is the authoritative summary
you must follow to the letter.

──────────────────────────────────
STEP 1 — Parse problem number from $ARGUMENTS (integer).

──────────────────────────────────
STEP 2 — Read leetcode_files.xlsx via openpyxl.
Find all rows where Problem Number == that integer.
Extract: Difficulty (int 1-10), Concept 1 through Concept 5.

──────────────────────────────────
STEP 3 — Validate xlsx data. Fix it FIRST if wrong.
  • Difficulty scale: 1 = trivial (Contains Duplicate),
    10 = extreme (Block Placement Queries).
  • Concepts = actual patterns/data structures of the optimal solution.
  If anything is wrong/missing → update xlsx with openpyxl, updating
  EVERY row that shares that problem number. Tell user what changed.

──────────────────────────────────
STEP 4 — Fetch problem description from LeetCode.
  a) Derive URL slug: lowercase title, spaces → hyphens, drop specials.
     "Two Sum" → two-sum   |   "3Sum" → 3sum   |   "Binary Search" → binary-search
  b) WebFetch:  https://leetcode.com/problems/<slug>/
     Prompt: "Extract the problem title and full description text only —
              no HTML, no examples, no constraints."
  c) If fetch succeeds → use fetched title + description (clean to 1-4 sentences).
     If fetch fails/redirects/requires login → fall back to training knowledge.
     Tell user which source was used.

──────────────────────────────────
STEP 5 — Compose solution metadata from training knowledge:
  • Approach: pattern name + key insight (one sentence)
  • Logic: 4-6 numbered pseudocode steps
  • Time and Space complexity in LaTeX: $O(n)$
  • Exact LeetCode Python function signature:
      def twoSum(self, nums: List[int], target: int) -> List[int]:
  • 3-5 test cases covering: normal case, edge case, problem example.

──────────────────────────────────
STEP 6 — Read LEC.md in full. Check for existing "## <NUMBER>:" section.
  If found → ask user: overwrite or skip? Never silently duplicate.

──────────────────────────────────
STEP 7 — Build new section. Use EXACTLY this format:

---

## <NUMBER>: <Title>

### Problem Description
> <description — 1 to 4 sentences>

- number: <NUMBER>
- title: "<Title>"
- difficulty: <DIFFICULTY>/10
- concepts: ["<Concept1>", "<Concept2>", ...]
- jupyter_path: <<absolute Path... I fill it>>
- script_path: <<absolute Path... I fill it>>
- function_signature: def <func_name>(self, <params>) -> <return_type>:

---

### Solution Idea (Pseudo-solution)
* **Approach:** <pattern name — key insight>
* **Logic:**
    1. <step>
    2. <step>
    3. <step>
    4. <step>
    5. <step>

**Complexity:**
* **Time:** $O(...)$
* **Space:** $O(...)$

---

### Solution Code
```python
from typing import List   # only if needed

class Solution(object):
    def <func_name>(self, <params>) -> <return_type>:
        pass




sol = Solution()
print("Test1: <input description> -> <expected>: success" if sol.<func_name>(<args1>) == <expected1> else "Test1: Fail")
print("Test2: <input description> -> <expected>: success" if sol.<func_name>(<args2>) == <expected2> else "Test2: Fail")
print("Test3: <edge case> -> <expected>: success" if sol.<func_name>(<args3>) == <expected3> else "Test3: Fail")
```
CRITICAL CODE BLOCK RULES:
✓ Class always named Solution(object).
✓ Method signature exactly matches LeetCode's Python signature.
✓ Body is ONLY pass — user writes the solution.
✓ Include typing import only if params need it.
✓ Tests use sol = Solution() then sol.method(...).
✓ Each print: "TestN: human readable description -> expected: success" if ... else "TestN: Fail"
✓ Minimum 3 tests; at least 1 edge case.
✓ NEVER leave the code block empty or with placeholder text.

──────────────────────────────────
STEP 8 — Insert section into LEC.md.
Insert IMMEDIATELY BEFORE the line "# Template".
Use Edit tool with enough surrounding context for a precise match.

──────────────────────────────────
STEP 9 — Update the index table at the TOP of LEC.md.
Table columns: | # | Problem Title | Concepts | Difficulty |
Add row in ascending numeric order:
| <N> | <Title> | C1, C2, C3 | <D>/10 |
Top 3 non-empty concepts only. Keep table sorted ascending.

──────────────────────────────────
STEP 10 — Confirm to user:
"Added LC<N> — <Title> to LEC.md.
Difficulty: <D>/10 | Concepts: <list>
Description source: LeetCode.com / training knowledge
Fill in jupyter_path and script_path when you create the files."
Plus: what xlsx corrections were made, if any.

═══════════════════════════════════════════════════════════
LEC.md FILE STRUCTURE — know this cold
═══════════════════════════════════════════════════════════

Line 1-N: Index table (sorted by problem number ascending) | # | Problem Title | Concepts | Difficulty |
LEC Cases

          Problem sections (## NUMBER: Title), one per problem
          Each section: Description → metadata block → Solution Idea → Solution Code
Template ← NEW sections are inserted IMMEDIATELY BEFORE this line

          Agent-instructions comment block

          Template skeleton (do not modify this)
═══════════════════════════════════════════════════════════
OTHER SKILLS (already set up)
═══════════════════════════════════════════════════════════

/next-problem              → picks next drill problem, creates .py scaffold
/save-solution             → annotates .py, updates drill-log.md
/create-syntax-card <topic>→ generates .md cheat sheet

═══════════════════════════════════════════════════════════
WHAT TO SAVE TO PERSISTENT MEMORY
═══════════════════════════════════════════════════════════

Save all of the following. Update, do not duplicate, if a memory already exists:

env_setter.ps1 rule: search cwd then parent; wrap ALL Python with it.
venv: C:\py_venv\proj_educate
xlsx validation rule: validate + fix xlsx BEFORE writing to LEC.md.
WebFetch rule: try https://leetcode.com/problems/<slug>/ for description; fall back to training knowledge if fetch fails. Always tell user which.
Code skeleton rule: Solution Code block is NEVER empty. Always: class Solution(object) → method with pass → sol = Solution() → print tests.
LEC.md insert point: immediately before "# Template".
Index table: sorted ascending by problem number; top 3 concepts shown.
All key file paths listed above.
