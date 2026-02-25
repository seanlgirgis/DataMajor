import openpyxl

file_path = r'c:\DataMajor\practice\leetcode_files.xlsx'
try:
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active

    updated = False
    found = False
    for row in ws.iter_rows(min_row=2):
        prob_num_cell = row[2]
        if str(prob_num_cell.value) == '102':
            found = True
            row[0].value = 'x' # WorkedOn
            diff_cell = row[5]
            c1_cell = row[6]
            c2_cell = row[7]
            c3_cell = row[8]
            
            if diff_cell.value != 2:
                diff_cell.value = 2
                updated = True
                
            if c1_cell.value != "Tree":
                c1_cell.value = "Tree"
                updated = True
            if c2_cell.value != "Breadth-First Search":
                c2_cell.value = "Breadth-First Search"
                updated = True
            if c3_cell.value != "Binary Tree":
                c3_cell.value = "Binary Tree"
                updated = True

    if not found:
        new_row = [
            'x',                                     # 0: WorkedOn
            "LC0102",                                # 1: LeetCode Number
            "102",                                   # 2: Problem Number
            "Binary Tree Level Order Traversal",     # 3: File Name
            r"C:\DataMajor\practice\001Study\LEC.md",# 4: Full Path
            2,                                       # 5: Difficulty
            "Tree",                                  # 6: Concept 1
            "Breadth-First Search",                  # 7: Concept 2
            "Binary Tree",                           # 8: Concept 3
            None,                                    # 9: Concept 4
            None                                     # 10: Concept 5
        ]
        ws.append(new_row)
        updated = True
        print("Added Problem 102 to xlsx")

    if updated and found:
        wb.save(file_path)
        print("Updated xlsx file with Difficulty=2, Concept 1=Tree, Concept 2=BFS, Concept 3=Binary Tree for Problem 102")
    elif updated and not found:
        wb.save(file_path)
    else:
        print("xlsx file already has correct data for Problem 102")
except Exception as e:
    print(f"Error: {e}")
