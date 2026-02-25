import openpyxl

file_path = r'c:\DataMajor\practice\leetcode_files.xlsx'
try:
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active

    updated = False
    found = False
    for row in ws.iter_rows(min_row=2):
        prob_num_cell = row[2]
        if str(prob_num_cell.value) == '121':
            found = True
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
            if c2_cell.value != "Dynamic Programming":
                c2_cell.value = "Dynamic Programming"
                updated = True
            if c3_cell.value is not None:
                c3_cell.value = None
                updated = True

    if updated:
        wb.save(file_path)
        print("Updated xlsx file with Difficulty=1, Concept 1=Array, Concept 2=Dynamic Programming for Problem 121")
    elif found:
        print("xlsx file already has correct data for Problem 121")
    else:
        print("Problem 121 not found in xlsx")
except Exception as e:
    print(f"Error: {e}")
