import re

md_path = r'C:\DataMajor\practice\001Study\LEC.md'

with open(md_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Clean up existing links
text = text.replace('[↑ Back to Top](#lec-cases)', '')
# Clean up any leftover blank lines that might have been created
text = re.sub(r'\n{3,}', '\n\n', text)

lines = text.split('\n')
new_lines = []

in_solution_code = False
in_code_block = False
in_template = False

for i, line in enumerate(lines):
    new_lines.append(line)
    
    if line.strip() == '### Solution Code':
        in_solution_code = True
    elif line.strip() == '# Template':
        in_template = True
        
    if in_solution_code or in_template:
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            if not in_code_block:
                # We just closed the code block for the Solution Code or Template
                # Add the back to top link right after
                new_lines.append('')
                new_lines.append('[↑ Back to Top](#lec-cases)')
                new_lines.append('')
                in_solution_code = False
                in_template = False

new_text = '\n'.join(new_lines)
# Clean up any excessive newlines again just in case
new_text = re.sub(r'\n{4,}', '\n\n\n', new_text)

with open(md_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Parsed and fixed Back to Top links correctly!")
