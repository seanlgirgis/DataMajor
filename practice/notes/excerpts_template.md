# MAin topic 
## Extra info

```python
<the code except goes here>
```


#Example

# Singley Linked List
## just traverse from head to end

```python
# given head
cur = head
while cur:
  print(cur.val)
  cur = cur.next
```


# Matrix Indexing

## Converting a 1D offset to 2D coordinates to access matrix elements on the fly

```python
# rows, cols = len(matrix), len(matrix[0])
# left, right = 0, rows * cols - 1

mid = (left + right) // 2
row = mid // cols
col = mid % cols

val = matrix[row][col]

```

