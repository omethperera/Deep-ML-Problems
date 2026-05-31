'''
**Easy
Linear Algebra
Write a Python function that computes the transpose of a given 2D matrix. The transpose of a matrix is formed by turning its rows into columns and columns into rows. For an mÃn matrix, the transpose will be an nÃm matrix.
'''

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	
	trans = []
	
	for i in range(len(a[0])): # Loop through rows of the transposed matrix (columns of the original matrix)
		new_row = []
		for j in range(len(a)): # Loop through columns of the transposed matrix (rows of the original matrix)
			new_row.append(a[j][i])
		trans.append(new_row) # Add the new row to the transposed matrix
	
	return trans
