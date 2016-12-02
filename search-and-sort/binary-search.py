# From Udacity Full Stack Web Developer Nanodegree

"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    index = int(len(input_array) / 2)
    range = index
    steps = 0
    while steps < len(input_array) and value != input_array[index]:
        steps += 1
        range = int(range / 2)
        if range < 1:
            range = 1
        if value > input_array[-1]:
            return -1
        elif value > input_array[index] and value < input_array[index + 1]:
            return -1
        elif value > input_array[index]:
            index += range
        else:
            index -= range
    return index

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)


# Recommended Solution from https://www.cs.usfca.edu/~galles/visualization/Search.html
def binarySearch(listData, value):
    low = 0
    high = len(listData) - 1
    while low <= high:
        mid = (low + high) / 2
        if listData[mid] == value:
            return mid
        elif listData[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1