def linear_search(arr, target):
    for index, item in enumerate(arr):
        if item == target:
            return index
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # markers for each end of range that can contain the target
    lowest_index, highest_index = 0, len(arr) - 1
    # index of target in arr (-1 is not found)
    found = -1

    # loop until target found or list exhausted
    while lowest_index <= highest_index and found < 0:
        # marker for center of range that can contain target
        center_index = (lowest_index + highest_index) // 2

        # current center equals target, update found index
        if arr[center_index] == target:
            found = center_index
        # current center greater than target, move highest_index to
        # one less than current center index
        elif arr[center_index] > target:
            highest_index = center_index - 1
        # current center less than target, move lowest_index to
        # one more than current center index
        else:
            lowest_index = center_index + 1

    return found
