# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop thru the array and get the index of the current value
    for i in range(len(arr)):
        # create variable that sets the current value as the minimum
        current_value = i
        current_minimum = i

        # loop thru the rest of the array
        for j in range(current_value, len(arr)):
            # if the current is lower than the minimun value than
            if arr[j] < arr[current_minimum]:
                # override the minimun value
                current_minimum = j

        # switch the current place with the minimum
        arr[current_value], arr[current_minimum] = arr[current_minimum], arr[current_value]
    # return the ordered array
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # if len of arr == zero
    if len(arr) == 0:
        return arr
        # then return arr

    # swapped set to true
    swapped = True

    # while loop (statement: swapped is truthy)
    while swapped:
        swapped = False
    # set swapped to false

    # for loop (i)
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    return arr

    # if arr[i] is greater than arr[i+1]
    # then arr[i], arr[i+1] = arr[i+1], arr[i] swap values
    # set swapped to true to prevent while loop from ending

    # return arr


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
