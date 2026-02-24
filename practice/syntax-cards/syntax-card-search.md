# BINARY SEARCH — Syntax Card

## Template A — Exact Search (inclusive both ends)
```python
left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid              # found
    elif target > nums[mid]:
        left = mid + 1          # search right half
    else:
        right = mid - 1         # search left half
return -1                       # not found
```

## Template B — Find Boundary (exclusive right)
```python
left, right = 0, len(nums)     # note: right = len, not len-1
while left < right:
    mid = (left + right) // 2
    if nums[mid] < target:
        left = mid + 1          # boundary is right of mid
    else:
        right = mid             # boundary is mid or left of mid
return left                     # insertion point / first >= target
```

## Find First Position of Target
```python
left, right = 0, len(nums)
while left < right:
    mid = (left + right) // 2
    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid
return left if left < len(nums) and nums[left] == target else -1
```

## Find Last Position of Target
```python
left, right = 0, len(nums)
while left < right:
    mid = (left + right) // 2
    if nums[mid] <= target:
        left = mid + 1
    else:
        right = mid
pos = left - 1
return pos if pos >= 0 and nums[pos] == target else -1
```

## Search in Rotated Sorted Array (LC 33)
```python
left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    if nums[left] <= nums[mid]:         # left half is sorted
        if nums[left] <= target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:                               # right half is sorted
        if nums[mid] < target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1
return -1
```

## bisect (stdlib shortcut)
```python
import bisect
bisect.bisect_left(nums, target)   # first index >= target
bisect.bisect_right(nums, target)  # first index >  target
bisect.insort(nums, val)           # insert in sorted order
```
