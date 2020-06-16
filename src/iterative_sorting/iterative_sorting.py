# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    pass
    # loop through n-1 elements
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    print(arr)
    place_holder = True
    while place_holder:

        # while the array is not sorted continue

        # make a for loop
        # make it check of the length of the array - index
        # use the index to get the value of the first one and the number beside it as well
        for idx in range(0, len(arr)-1):
            counter = 0
            current_value = idx
            save_current_value = arr[idx]
            neighboring_value = current_value + 1

            if arr[idx] > arr[idx - 1]:
                counter += 1

            if len(arr)-1 == counter:
                place_holder = False

            if arr[current_value] > arr[neighboring_value]:
                arr[current_value] = arr[neighboring_value]
                arr[neighboring_value] = save_current_value

            if arr[current_value] < arr[neighboring_value]:
                continue

        # if the current value is < its neighboring value
        # then switch index location
        # if the current value is > its neighboring value
        # then continue

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
    # Your code here

    return arr
