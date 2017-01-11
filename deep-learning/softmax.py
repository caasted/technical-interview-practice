# softmax(yi) = exp(yi) / sum_j(exp(yj))

import numpy
import math

def softmax(x):
	array = numpy.transpose(x)
	shape = array.shape
	if len(shape) == 1:
		print "1D Array"
		temp = []
		for value in x:
			temp.append(math.exp(value))
		
		sum_of_x = sum(temp)
		
		result = []
		for value in temp:
			result.append(value / sum_of_x)
		
		return result
	elif len(shape) == 2:
		print "2D Array"
		rows = shape[0]
		cols = shape[1]
		result = []
		for row in range(rows):
			temp1 = []
			for col in range(cols):
				temp1.append(math.exp(x[col][row]))

			sum_of_x = sum(temp1)
			
			temp2 = []
			for value in temp1:
				temp2.append(value / sum_of_x)

			result.append(temp2)
		return numpy.transpose(result)
	else:
		return None


# Or using numpy more effectively:
def softmax2(x):
	return numpy.exp(x) / numpy.sum(numpy.exp(x), axis=0)


scores = [1.0, 2.0, 3.0]

print softmax2(scores), "\n"

scores = [[1, 2, 3, 6], [2, 4, 5, 6], [3, 8, 7, 6]]

print softmax2(scores)
