Save the current problem solution to a clean annotated .py file.

Steps:
1. Read the current problem's .py file from C:/DataMajor/practice/
2. Coach the user: assess their solution — correctness, time/space complexity, style
3. Enhance the file IN PLACE:
   - Add time complexity and space complexity to the header
   - Add a "Key Insight" comment above the solution
   - Add inline comments explaining each non-obvious step
   - Keep the user's logic intact — do not rewrite their approach unless it is wrong
   - Ensure all test assertions are present and correct
4. Run the file with Python to confirm all tests pass:
   PYTHONUTF8=1 C:/py_venv/proj_educate/Scripts/python.exe C:/DataMajor/practice/NNNNNN.LCXXXX.descriptive-name.py
5. Ask the user to rate the drill:
   "Rate this drill: 1=Nailed it  2=Slow  3=Struggled  4=Wrong first  5=Needed coaching"
6. After user gives rating, update C:/DataMajor/practice/drill-log.md:
   - Append a new row to the log table: | # | filename | title | pattern | rating | REDO or OK |
   - Set Redo = REDO if rating >= 3, OK if rating <= 2
7. Confirm: "Saved: NNNNNN.LCXXXX.py — log updated."
   Then give a 2-3 line coaching note: what they did well + one thing to watch for.
