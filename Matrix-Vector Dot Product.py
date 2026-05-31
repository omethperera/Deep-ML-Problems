'''
**Easy
Write a Python function that computes the dot product of a matrix and a vector. 
The function should return a list representing the resulting vector if the operation is valid, or -1 if the matrix and vector dimensions are incompatible. A matrix (a list of lists) can be dotted with a vector (a list) only if the number of columns in the matrix equals the length of the vector. For example, an n x m matrix requires a vector of length m.
You may assume the input matrix is a valid (non-jagged) list of lists and the vector is a non-empty list.
'''
# U can adress all elements of the matrix and vector with two variables i,j

def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	# Check if the number of columns in the matrix matches the size of the vector
	ans = []

	if len(a) != len(b):
		return -1
	else:
		for i in range(len(a)):
			val = 0
			# Multiply each element in the row of the matrix with the corresponding element in the vector
			for j in range(len(b)):
				val += a[i][j] * b[j]
			# Store the dot product of the current row and the vector
			ans.append(val)				
	return ans
		
