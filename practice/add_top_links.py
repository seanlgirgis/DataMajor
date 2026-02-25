import re

md_path = r'C:\DataMajor\practice\001Study\LEC.md'

with open(md_path, 'r', encoding='utf-8') as f:
    content = f.read()

# I want to add an anchor to the top table so the links can go back to it.
# Wait, standard markdown `#` usually just jumps to top of page, or we can use the top heading name.
# Let's add an explicit anchor `<a name="top"></a>` right before the table, or use `[Back to Top](#lec-cases)` if there's an `# LEC Cases` heading.
# Looking at line 34, there is a `# LEC Cases` heading. So `#lec-cases` works, or just `#` which often works in Github MD to go top.
# The user wants it "at the bottom of problem section". The problem section ends with the Solution Code block: ` ``` `
# Wait, some end with plain ` ``` ` and some end with ` ``` \n\n ---` or similar.
# The best hook is `sol = Solution()`... wait no.
# Let's look at the structure:
# ### Solution Code
# ```python
# ...
# print(...)
# ```
# <we want link here>
# --- (or next problem)

# Look for ````python\n(.*?)```\n(^---|\n# Template)`
# Actually, let's just use Python's regex to replace ````\n\n---` with ````\n\n[Back to Top](#lec-cases)\n\n---`
# But let's be careful not to double add. Let's do a positive lookbehind and manual replace

# First, ensure there is an anchor at the very top. 
# "LEC Cases" heading is at line 34. Let's use `[Back to Top](<br/>↑ Back to Top) ` or similar.
# I will just write `[↑ Back to Top](#lec-cases)` right before the `---` that separates problems, AND right before `# Template`.

pieces = content.split('\n---\n')

new_pieces = []
for i, piece in enumerate(pieces):
    # Check if piece defines a problem (has "## " and "### Problem Description")
    if '## ' in piece and '### Problem Description' in piece:
        # Check if back to top is already there so we don't duplicate
        if '[↑ Back to Top]' not in piece:
            piece = piece.rstrip() + '\n\n[↑ Back to Top](#lec-cases)\n'
    elif '# Template' in piece:
        if '[↑ Back to Top]' not in piece:
            # The template itself might have instructions.
            # Replace the end of the template code block.
            piece = piece.replace('```\n', '```\n\n[↑ Back to Top](#lec-cases)\n')
    new_pieces.append(piece)

new_content = '\n---\n'.join(new_pieces)

with open(md_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Added Back to Top links!")
