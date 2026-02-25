import openpyxl
wb = openpyxl.load_workbook(r'C:\DataMajor\practice\leetcode_files.xlsx')
ws = wb.active
for i, row in enumerate(ws.iter_rows(max_row=5, values_only=True)):
    print(i, row)