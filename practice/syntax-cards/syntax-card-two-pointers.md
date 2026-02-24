# TWO POINTERS — Syntax Card

## Template — Squeeze from Both Ends (sorted array)
```python
l, r = 0, len(arr) - 1
while l < r:
    # compute something with arr[l] and arr[r]
    if condition_to_move_left:
        l += 1
    else:
        r -= 1
```

## Two Sum II — target sum
```python
while l < r:
    s = nums[l] + nums[r]
    if s == target: return [l+1, r+1]
    elif s < target: l += 1   # need bigger sum
    else:            r -= 1   # need smaller sum
```

## Container With Most Water — max area
```python
while l < r:
    area = max(area, min(height[l], height[r]) * (r - l))
    if height[l] >= height[r]: r -= 1  # move shorter side
    else:                       l += 1
```

## Reverse in Place
```python
while l < r:
    arr[l], arr[r] = arr[r], arr[l]
    l += 1; r -= 1
```

## Fast / Slow Pointer (Linked List cycle)
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast: return True   # cycle detected
return False
```

## Remove Duplicates (sorted, in-place)
```python
k = 1
for i in range(1, len(nums)):
    if nums[i] != nums[i-1]:
        nums[k] = nums[i]
        k += 1
return k
```

## When to Use
```python
# Sorted array + pair/triplet problem       -> squeeze both ends
# Unsorted + fast/slow traversal            -> fast/slow pointers
# In-place write with read pointer          -> slow(write)/fast(read)
# Key: O(n) replaces O(n^2) brute force
```
