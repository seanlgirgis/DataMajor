Give me the next LeetCode problem to drill for my CodeSignal interview prep.

Priority order for new topics:
1. Sliding Window
2. Binary Search
3. Trees (BFS / DFS)
4. Two Pointers
5. Dynamic Programming (basic)
6. Graph traversal

Steps:
1. Check C:/DataMajor/practice/ for existing files to determine which problems are done and next sequence number
2. Check C:/DataMajor/practice/drill-log.md for any problems marked REDO
3. Decide what to serve next using this rule:
   - Every 2 new problems, inject 1 REDO problem (pick the oldest REDO not yet redone)
   - If no REDO problems are pending, serve next new topic
   - If serving a REDO: say "REDO DRILL — you struggled with this before. Solve it fresh."
   - If serving a new problem: pick next topic from priority list
4. State: problem number, title, topic/pattern, difficulty, and NEW or REDO
5. Show the problem statement with 2-3 examples
6. CREATE the .py file immediately using naming schema:
   NNNNNN.LCXXXX.descriptive-name.py  (new)
   NNNNNN.LCXXXX.descriptive-name.redo.py  (redo)
   Examples: 000021.LC0021.merge-two-sorted-lists.py
             000014.LC0001.two-sum.redo.py
   File contents:
   - Header comment block (number, title, pattern, difficulty)
   - "# REDO DRILL" in the header if it is a redo
   - Problem statement + examples as comments
   - Empty Solution class with the correct method signature
   - Test assertions in __main__ block (at least 5, including edge cases)
   - pass placeholder inside the method body
7. Then STOP — user will write the solution directly in the file

Do not show hints, approach, or solution. File creation is mandatory.
