# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # find next smallest element
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


def bubble_sort(arr):
    # initialize swap tracker to True to enter the loop
    swap_happened = True
    # loop until parsed entire input without any swaps
    while swap_happened:
        # no swaps yet this time through
        swap_happened = False
        # Loop through your array
        # start at index 1 and compare with previous neighbor
        for i in range(1, len(arr)):
            # Compare each element to its neighbor
            if arr[i] < arr[i-1]:
                # If elements in wrong position (relative to each other, swap them)
                arr[i], arr[i-1] = arr[i-1], arr[i]
                # swap occurred, set flag
                swap_happened = True
    # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.

    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # input validation
    if len(arr) == 0:
        return arr
    if min(arr) < 0:
        return 'Error, negative numbers not allowed in Count Sort'

    # https://ayada.dev/posts/counting-sort/
    n = len(arr)
    k = max(arr) + 1

    # initialize value counter
    count = [0] * k

    # count occurrences by incrementing index in count array
    for value in arr:
        count[value] = count[value] + 1

    # 2nd step of counting sort, calculate cumulative totals
    total = 0
    for i in range(k):
        count[i], total = total, count[i] + total
    
    # 3rd step of counting sort, building sorted array
    output = [None] * n
    for value in arr:
        output[count[value]] = value
        count[value] = count[value] + 1

    return output
