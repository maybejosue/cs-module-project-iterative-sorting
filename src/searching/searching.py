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
    lowest = 0
    highest = len(arr)-1
    # whole loop - true:
    # if target is > middle:
    # go to the right
    # else go to the left
    # repeat the process
    while True:
        middle = (lowest + highest) // 2
        print(f"{middle} this is the middle")

        if target == middle:
            ind = arr.index(target)
            print(f"{ind} this is the index being returned")
            return ind

        if target > middle:
            lowest = middle + 1
        if target < middle:
            highest = middle - 1

    return -1  # not found
