import openpyxl

file_path = r'c:\DataMajor\practice\leetcode_files.xlsx'
try:
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active

    updated = False
    found = False
    for row in ws.iter_rows(min_row=2):
        prob_num_cell = row[2]
        if str(prob_num_cell.value) == '20':
            found = True
            row[0].value = 'x' # WorkedOn
            diff_cell = row[5]
            c1_cell = row[6]
            c2_cell = row[7]
            c3_cell = row[8]
            
            if diff_cell.value != 1:
                diff_cell.value = 1
                updated = True
                
            if c1_cell.value != "String":
                c1_cell.value = "String"
                updated = True
            if c2_cell.value != "Stack":
                c2_cell.value = "Stack"
                updated = True

    if not found:
        new_row = [
            'x',                                     # 0: WorkedOn
            "LC0020",                                # 1: LeetCode Number
            "20",                                    # 2: Problem Number
            "Valid Parentheses",                     # 3: File Name (Putting title for now)
            r"C:\DataMajor\practice\001Study\LEC.md",# 4: Full Path
            1,                                       # 5: Difficulty
            "String",                                # 6: Concept 1
            "Stack",                                 # 7: Concept 2
            None,                                    # 8: Concept 3
            None,                                    # 9: Concept 4
            None                                     # 10: Concept 5
        ]
        ws.append(new_row)
        updated = True
        print("Added Problem 20 to xlsx")

    if updated and found:
        wb.save(file_path)
        print("Updated xlsx file with Difficulty=1, Concept 1=String, Concept 2=Stack for Problem 20")
    elif updated and not found:
        wb.save(file_path)
    else:
        print("xlsx file already has correct data for Problem 20")
except Exception as e:
    print(f"Error: {e}")
