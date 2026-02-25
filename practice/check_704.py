import openpyxl

file_path = r'c:\DataMajor\practice\leetcode_files.xlsx'
wb = openpyxl.load_workbook(file_path)
ws = wb.active

updated = False
for row in ws.iter_rows(min_row=2):
    prob_num_cell = row[2]
    if str(prob_num_cell.value) == '704':
        diff_cell = row[5]
        c1_cell = row[6]
        c2_cell = row[7]
        
        if diff_cell.value != 3:
            diff_cell.value = 3
            updated = True
        if c1_cell.value != "Binary Search":
            c1_cell.value = "Binary Search"
            updated = True
        if c2_cell.value != "Array":
            c2_cell.value = "Array"
            updated = True

if updated:
    wb.save(file_path)
    print("Updated xlsx file with Difficulty=3, Concept 1=Binary Search, Concept 2=Array")
else:
    print("xlsx file already has correct data for 704")
