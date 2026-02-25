import re

md_path = r'C:\DataMajor\practice\001Study\LEC.md'

with open(md_path, 'r', encoding='utf-8') as f:
    content = f.read()

# First, remove all existing mistakenly placed `[↑ Back to Top](#lec-cases)` links to start completely fresh
content = content.replace('\n[↑ Back to Top](#lec-cases)\n', '')
content = content.replace('\n[↑ Back to Top](#lec-cases)', '')
content = content.replace('[↑ Back to Top](#lec-cases)\n', '')
content = content.replace('[↑ Back to Top](#lec-cases)', '')

# A problem section ends with ````\n` followed by `\n---` or `\n---\n# Template`
# The safest way is to split by `\n---\n`
pieces = content.split('\n---\n')

new_pieces = []
for i, piece in enumerate(pieces):
    piece = piece.rstrip()
    if '## ' in piece and '### Problem Description' in piece:
        # It's a problem block. Ensure it ends with the Back to Top link.
        # It should end with the trailing ``` of the python codeblock.
        piece = piece + '\n\n[↑ Back to Top](#lec-cases)\n'
    elif '# Template' in piece:
        # The template also ends with a codeblock
        piece = piece + '\n\n[↑ Back to Top](#lec-cases)\n'
    new_pieces.append(piece)

# Rejoin
new_content = '\n---\n'.join(new_pieces)

with open(md_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Fixed Back to Top links final time!")
