# Practice: Binary Search
# Linked Note: [[01-concepts/python/binary-search|Binary Search]]

def binary_search(nums, target):
    """Core standard binary search template."""
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def search_left(nums, target):
    """Finds the leftmost (first) occurrence of the target."""
    left, right = 0, len(nums) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid
            right = mid - 1   # aggressively seek left
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def search_right(nums, target):
    """Finds the rightmost (last) occurrence of the target."""
    left, right = 0, len(nums) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid
            left = mid + 1    # aggressively seek right
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def practice_binary_search():
    """Small exercise harness for Binary Search."""
    
    nums = [1, 3, 5, 7, 9, 11, 13]
    
    # 1. Standard Search
    assert binary_search(nums, 7) == 3, "Failed to find existing target"
    assert binary_search(nums, 14) == -1, "Failed to reject missing target"
    print("✅ Core Binary Search Passed!")

    # 2. Duplicate Occurrences
    dup_nums = [2, 4, 4, 4, 4, 6, 8]
    
    # Left Boundary
    assert search_left(dup_nums, 4) == 1, "Failed leftmost search"
    assert search_left(dup_nums, 5) == -1, "Failed leftmost missing search"
    print("✅ Leftmost Binary Search Passed!")
    
    # Right Boundary
    assert search_right(dup_nums, 4) == 4, "Failed rightmost search"
    assert search_right(dup_nums, 5) == -1, "Failed rightmost missing search"
    print("✅ Rightmost Binary Search Passed!")


if __name__ == "__main__":
    print("Starting Binary Search Practice Exercises...\n")
    practice_binary_search()
    print("\nAll Binary Search tests safely completed!")
