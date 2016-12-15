import numbers

def findElements(array, k):
	if ([isinstance(x, numbers.Number) for x in array] and 
		isinstance(k, numbers.Number)):
		partner = {}
		for element in array:
			if element in partner:
				return element, partner[element]
			else:
				partner[k - element] = element
	return None

# Edge Cases:
print findElements([], None)
# Returns "None"
print findElements(['a', 'b', 'c'], 'ac')
# Returns "None"

# Test Cases:
print findElements([2, 4, 7, 9], 11)
# Returns "7, 4"
print findElements([9, 5, 7, 2], 11)
# Returns "2, 9"
print findElements([1, 2, 3], 42)
# Returns "None"
