# From Udacity Full Stack Web Developer Nanodegree

"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    def processPivot(lower, upper):
        if lower >= upper:
            return
        pivot = upper
        element = lower
        while element < pivot:
            if array[element] > array[pivot]:
                temp = array[pivot-1]
                if element == pivot - 1:
                    array[element] = array[pivot]
                    array[pivot] = temp
                else:
                    array[pivot-1] = array[pivot]
                    array[pivot] = array[element]
                    array[element] = temp
                pivot -= 1
            else:
                element += 1
        processPivot(lower, pivot - 1)
        processPivot(pivot + 1, upper)

    processPivot(0, len(array) - 1)
    return array
        

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
