def linear_search(arr, target):
    # Your code here
    if target in arr:
        return arr.index(target)

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # get the array and get the lowest and highest index as possible
    # make the highest and lowest a variable
    # calculate the middle of the array by grabbing the highest and lowest
    # variable and dividing it by 2 to find the middle
    if len(arr) < 1:
        return -1
    lowest = 0
    highest = len(arr)-1
    # whole loop - true:
    # if target is > middle:
    # go to the right
    # else go to the left
    # repeat the process
    while True:
        middle = (lowest + highest) // 2
        print(lowest, highest, middle, arr[middle], target)

        if target == arr[middle]:
            return middle

        if target > arr[middle]:
            lowest = middle + 1
        if target < arr[middle]:
            highest = middle - 1

    return -1  # not found
