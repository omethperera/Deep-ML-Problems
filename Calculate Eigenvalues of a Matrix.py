'''
Medium
Linear Algebra

Write a Python function that calculates the eigenvalues of a 2x2 matrix. The function should return a list containing the eigenvalues, sort values from highest to lowest.
'''
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	
	a,b,c,d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
	
	determinant = a * d - b * c
	trace = a + d
	discriminant = trace ** 2 - 4 * determinant
	lamda_1 = (trace + discriminant ** 0.5) / 2
	lamda_2 = (trace - discriminant ** 0.5) / 2
	
	Eigen_values= [lamda_1,lamda_2]
	
	return Eigen_values
