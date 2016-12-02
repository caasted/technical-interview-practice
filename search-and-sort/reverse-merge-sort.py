# From Udacity Full Stack Web Developer Nanodegree

"""Implement a sorting algorithm in Python.
Input a list.
Output a sorted list."""

"""After completing this quiz, I realized that the algorithm I had created 
really didn't reflect the quick sort algorithm described in class. This is 
actually closer to a hybrid between quick sort and merge sort, but not 
necessarily better than either."""

def reverseMergeSort(array):
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
        return reverseMergeSort(lower) + array[pivot:] + reverseMergeSort(upper)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print reverseMergeSort(test)
