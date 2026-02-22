# Practice: Sorting Algorithms
# Linked Note: [[01-concepts/python/sorting-algorithms|Sorting Algorithms]]

def bubble_sort(nums):
    """
    Repeatedly swap adjacent elements that are out of order.
    The largest element 'bubbles' to the end each pass.
    """
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def merge_sort(nums):
    """
    Divide the array in half recursively, then merge them back.
    """
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)

def merge(left, right):
    """Helper for merge_sort to combine two sorted arrays."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(nums, low, high):
    """
    Pick a pivot, put everything smaller to the left and everything 
    larger to the right, then recurse. Modifies array in-place.
    """
    if low < high:
        pivot_idx = partition(nums, low, high)
        quick_sort(nums, low, pivot_idx - 1)
        quick_sort(nums, pivot_idx + 1, high)

def partition(nums, low, high):
    """Helper for quick_sort to place the pivot correctly."""
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1


def practice_sorting_algorithms():
    """Small exercise harness for Sorting Algorithms."""
    
    # 1. Bubble Sort
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr1)
    assert arr1 == [11, 12, 22, 25, 34, 64, 90], "Bubble Sort Failed"
    print("✅ Bubble Sort Passed!")
    
    # 2. Merge Sort
    arr2 = [38, 27, 43, 3, 9, 82, 10]
    merged = merge_sort(arr2)
    assert merged == [3, 9, 10, 27, 38, 43, 82], "Merge Sort Failed"
    print("✅ Merge Sort Passed!")
    
    # 3. Quick Sort
    arr3 = [10, 7, 8, 9, 1, 5]
    quick_sort(arr3, 0, len(arr3) - 1)
    assert arr3 == [1, 5, 7, 8, 9, 10], "Quick Sort Failed"
    print("✅ Quick Sort Passed!")
    
    # 4. Built-in with Custom Keys
    words = ["banana", "apple", "cherry"]
    words.sort(key=len)
    assert words == ["apple", "banana", "cherry"], "Built-in Key Sort Failed"
    print("✅ Built-In Lambda/Key Sort Passed!")


if __name__ == "__main__":
    print("Starting Sorting Algorithms Practice Exercises...\n")
    practice_sorting_algorithms()
    print("\nAll Sorting tests safely completed!")
