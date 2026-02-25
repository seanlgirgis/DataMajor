import openpyxl

file_path = r'c:\DataMajor\practice\leetcode_files.xlsx'
wb = openpyxl.load_workbook(file_path)
ws = wb.active

updated = False
found = False
for row in ws.iter_rows(min_row=2):
    prob_num_cell = row[2]
    if str(prob_num_cell.value) == '70':
        found = True
        diff_cell = row[5]
        c1_cell = row[6]
        c2_cell = row[7]
        c3_cell = row[8]
        
        if diff_cell.value != 2:
            diff_cell.value = 2
            updated = True
        if c1_cell.value != "Dynamic Programming":
            c1_cell.value = "Dynamic Programming"
            updated = True
        if c2_cell.value != "Memoization":
            c2_cell.value = "Memoization"
            updated = True
        if c3_cell.value != "Math":
            c3_cell.value = "Math"
            updated = True

if updated:
    wb.save(file_path)
    print("Updated xlsx file with Difficulty=2, Concept 1=Dynamic Programming, Concept 2=Memoization, Concept 3=Math for Problem 70")
elif found:
    print("xlsx file already has correct data for Problem 70")
else:
    print("Problem 70 not found in xlsx")
