def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
	
	a = matrix[0][0]
	b = matrix[0][1]
	c = matrix[1][0]
	d = matrix[1][1]

	determinant = a * d - b * c

	if determinant == 0:
		return none
	else:
		inverse  = [[1/determinant * d, 1/determinant * -b],[1/determinant * -c,1/determinant * a]]

		return inverse
