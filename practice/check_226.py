import openpyxl

file_path = r'c:\DataMajor\practice\leetcode_files.xlsx'
try:
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active

    updated = False
    found = False
    for row in ws.iter_rows(min_row=2):
        prob_num_cell = row[2]
        if str(prob_num_cell.value) == '226':
            found = True
            diff_cell = row[5]
            c1_cell = row[6]
            c2_cell = row[7]
            c3_cell = row[8]
            
            if diff_cell.value != 1:
                diff_cell.value = 1
                updated = True
                
            if c1_cell.value != "Tree":
                c1_cell.value = "Tree"
                updated = True
            if c2_cell.value != "Depth-First Search":
                c2_cell.value = "Depth-First Search"
                updated = True
            if c3_cell.value != "Binary Tree":
                c3_cell.value = "Binary Tree"
                updated = True

    if updated:
        wb.save(file_path)
        print("Updated xlsx file with Difficulty=1, Concept 1=Tree, Concept 2=Depth-First Search, Concept 3=Binary Tree for Problem 226")
    elif found:
        print("xlsx file already has correct data for Problem 226")
    else:
        print("Problem 226 not found in xlsx")
except Exception as e:
    print(f"Error: {e}")
