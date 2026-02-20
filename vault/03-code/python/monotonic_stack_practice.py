# Practice: Monotonic Stack
# Linked Note: [[01-concepts/python/Monotonic Stack]]

def practice_monotonic_stack():
    """
    Exercise harness for Monotonic Stack patterns.
    
    1. Basic Next Greater Element (Indices).
    2. Daily Temperatures (#739) - Distance.
    3. Next Greater Element I (#496) - Subset lookup.
    4. Next Greater Element II (#503) - Circular.
    5. Largest Rectangle in Histogram (#84) - Area/Width formula.
    """
    
    # 1. Basic Next Greater Element
    print("--- 1. Basic Next Greater ---")
    def next_greater(nums):
        res = [-1] * len(nums)
        stack = [] # indices, decreasing
        
        for i, val in enumerate(nums):
            while stack and nums[stack[-1]] < val:
                idx = stack.pop()
                res[idx] = val
            stack.append(i)
        return res

    arr = [2, 1, 3, 2, 4, 3]
    expected = [3, 3, 4, 4, -1, -1]
    res = next_greater(arr)
    print(f"Input: {arr}\nResult: {res}")
    assert res == expected

    # 2. Daily Temperatures (#739)
    print("\n--- 2. Daily Temperatures ---")
    def daily_temperatures(temps):
        res = [0] * len(temps)
        stack = [] # indices, decreasing
        
        for i, t in enumerate(temps):
            while stack and temps[stack[-1]] < t:
                idx = stack.pop()
                res[idx] = i - idx # distance
            stack.append(i)
        return res

    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    t_expected = [1, 1, 4, 2, 1, 1, 0, 0]
    t_res = daily_temperatures(temps)
    print(f"Temps: {temps}\nDistances: {t_res}")
    assert t_res == t_expected

    # 3. Next Greater Element I (#496)
    print("\n--- 3. Next Greater Element I (Subset) ---")
    def next_greater_subset(nums1, nums2):
        # Map next greater for all in nums2
        mapping = {}
        stack = []
        
        for num in nums2:
            while stack and stack[-1] < num:
                prev = stack.pop()
                mapping[prev] = num
            stack.append(num)
        
        # Lookup for nums1
        return [mapping.get(n, -1) for n in nums1]

    n1 = [4, 1, 2]
    n2 = [1, 3, 4, 2]
    n1_expected = [-1, 3, -1]
    n1_res = next_greater_subset(n1, n2)
    print(f"Subset NGE: {n1_res}")
    assert n1_res == n1_expected

    # 4. Next Greater Element II (#503) - Circular
    print("\n--- 4. NGE II (Circular) ---")
    def next_greater_circular(nums):
        n = len(nums)
        res = [-1] * n
        stack = []
        
        for i in range(2 * n):
            idx = i % n
            while stack and nums[stack[-1]] < nums[idx]:
                prev_idx = stack.pop()
                res[prev_idx] = nums[idx]
            
            # Only push during first pass to avoid infinite loop potential
            if i < n:
                stack.append(idx)
        return res

    circ = [1, 2, 1]
    c_expected = [2, -1, 2]
    c_res = next_greater_circular(circ)
    print(f"Circular Input: {circ}\nResult: {c_res}")
    assert c_res == c_expected

    # 5. Largest Rectangle in Histogram (#84)
    print("\n--- 5. Largest Rectangle (Histogram) ---")
    def largest_rectangle_area(heights):
        # Add 0 to end to flush remaining items in stack
        heights = heights + [0]
        stack = [-1] # monotonic increasing, seeded with -1 for left boundary
        max_area = 0
        
        for i, h in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area

    hist = [2, 1, 5, 6, 2, 3]
    h_expected = 10
    h_res = largest_rectangle_area(hist)
    print(f"Histogram: {hist}\nMax Area: {h_res}")
    assert h_res == h_expected

if __name__ == "__main__":
    practice_monotonic_stack()
