import openpyxl
import re

excel_path = r'C:\DataMajor\practice\leetcode_files.xlsx'
md_path = r'C:\DataMajor\practice\001Study\LEC.md'

try:
    wb = openpyxl.load_workbook(excel_path)
    ws = wb.active
    
    # Get column headers
    headers = [cell.value for cell in next(ws.iter_rows(min_row=1, max_row=1))]
    print("Headers:", headers)
    
except Exception as e:
    print(f"Error: {e}")
