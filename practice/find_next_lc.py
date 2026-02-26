import openpyxl

file_path = r'c:\DataMajor\practice\leetcode_files.xlsx'
try:
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active

    for row in ws.iter_rows(min_row=2):
        worked_on = str(row[0].value).lower() if row[0].value else ""
        num = row[2].value
        if worked_on != 'x' and num is not None:
            print(f"NEXT_PROBLEM:{num}:{row[3].value}")
            break
except Exception as e:
    print(f"Error: {e}")
