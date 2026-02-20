# Practice: Loops
# Linked Note: [[01-concepts/python/Loops|Loops]]

def practice_loops():
    """
    Small exercise harness for Loops.
    
    1. For Loop: Print odd numbers from 1 to 10 using range().
    2. String Iteration: Count vowels in "Antigravity".
    3. Enumerate: Print ranking 1..n for a list of items.
    4. While Loop: Two-pointer pattern to reverse a list in-place (without ::-1).
    5. Break/Continue: Print 1-10 but skip 5 and stop at 8.
    """
    
    # 1. Range (Odd numbers)
    print("Odds 1-10:")
    # TODO: usage of range(start, stop, step)
    for i in range(1, 11, 2):
        print(i, end=" ")
    print("\n")

    # 2. String Iteration
    word = "Antigravity"
    vowels = "aeiouAEIOU"
    count = 0
    # TODO: iterate char by char
    for char in word:
        if char in vowels:
            count += 1
    print(f"Vowels in {word}: {count}")

    # 3. Enumerate
    racers = ["Mario", "Luigi", "Peach"]
    # TODO: Print "1. Mario", "2. Luigi", etc.
    for i, name in enumerate(racers, start=1):
        print(f"{i}. {name}")

    # 4. While Loop (Two Pointer Reversal)
    nums = [10, 20, 30, 40, 50]
    left = 0
    right = len(nums) - 1
    # TODO: Swap elements moving inward
    while left < right:
        # Swap
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        # Move pointers
        left += 1
        right -= 1
    print(f"Reversed logic: {nums}")

    # 5. Break and Continue
    print("Logic drill:")
    for i in range(1, 11):
        if i == 5:
            continue # Skip 5
        if i == 8:
            break    # Stop before printing 8? Or at 8? Prompt said stop AT 8 (meaning break after 8 or at 8? Usually means terminate loop).
                     # As per quiz: "i == 5 break" stops there. 
                     # Let's stop WHEN i is 8 (so 8 is not processed or 8 triggers break).
            # "Stop at 8" usually implies 8 might be the limit.
            # Let's follow the standard: if i == 8 break (8 won't print if print is after).
        print(i, end=" ")
    print("\n")

if __name__ == "__main__":
    practice_loops()
