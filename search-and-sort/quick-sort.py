# From Udacity Full Stack Web Developer Nanodegree

"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    if len(array) == 0:
        return []
    if len(array) == 1:
        return array
    else:
        pivot = len(array) - 1
        lower = []
        upper = []
        for index in range(pivot):
            if array[index] > array[pivot]:
                upper.append(array[index])
            else:
                lower.append(array[index])
        return quicksort(lower) + array[pivot:] + quicksort(upper)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
