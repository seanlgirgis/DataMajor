import openpyxl

file_path = r'c:\DataMajor\practice\leetcode_files.xlsx'
try:
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active

    updated = False
    found = False
    for row in ws.iter_rows(min_row=2):
        prob_num_cell = row[2]
        if str(prob_num_cell.value) == '674':
            found = True
            row[0].value = 'x' # WorkedOn
            diff_cell = row[5]
            c1_cell = row[6]
            c2_cell = row[7]
            c3_cell = row[8]
            
            if diff_cell.value != 1:
                diff_cell.value = 1
                updated = True
                
            if c1_cell.value != "Array":
                c1_cell.value = "Array"
                updated = True

    if not found:
        new_row = [
            'x',                                     # 0: WorkedOn
            "LC0674",                                # 1: LeetCode Number
            "674",                                   # 2: Problem Number
            "Longest Continuous Increasing Subsequence", # 3: File Name
            r"C:\DataMajor\practice\001Study\LEC.md",# 4: Full Path
            1,                                       # 5: Difficulty
            "Array",                                 # 6: Concept 1
            None,                                    # 7: Concept 2
            None,                                    # 8: Concept 3
            None,                                    # 9: Concept 4
            None                                     # 10: Concept 5
        ]
        ws.append(new_row)
        updated = True
        print("Added Problem 674 to xlsx")

    if updated and found:
        wb.save(file_path)
        print("Updated xlsx file with Difficulty=1, Concept 1=Array for Problem 674")
    elif updated and not found:
        wb.save(file_path)
    else:
        print("xlsx file already has correct data for Problem 674")
except Exception as e:
    print(f"Error: {e}")
