import re

md_path = r'C:\DataMajor\practice\001Study\LEC.md'

with open(md_path, 'r', encoding='utf-8') as f:
    content = f.read()

# I noticed the previous script placed the link prematurely for problems that didn't have a trailing empty line.
# Let's remove all existing `[↑ Back to Top](#lec-cases)` to start clean.
content = content.replace('\n[↑ Back to Top](#lec-cases)\n', '')
content = content.replace('[↑ Back to Top](#lec-cases)', '')

pieces = content.split('\n---\n')

new_pieces = []
for i, piece in enumerate(pieces):
    stripped_piece = piece.rstrip()
    if '## ' in stripped_piece and '### Problem Description' in stripped_piece:
        # Append strictly after the last codeblock/content before the next `---`
        piece = stripped_piece + '\n\n[↑ Back to Top](#lec-cases)\n'
    elif '# Template' in stripped_piece:
        # For template, it usually ends in ````
        piece = stripped_piece.replace('```', '```\n\n[↑ Back to Top](#lec-cases)')
    new_pieces.append(piece)

new_content = '\n---\n'.join(new_pieces)

with open(md_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Fixed Back to Top links!")
