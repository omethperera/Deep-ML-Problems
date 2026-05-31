def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	
	c = []

	if len(a[0]) != len(b):
		return -1
	else:
		for i in range(len(a)): # Iterate over rows of `a`
			row = [] # row of new matrix
			for j in range(len(b[0])): # Iterate over columns of 'b'
				# Compute the dot product of row `i` in `a` with column `j` in `b`
				val = sum(a[i][k] * b[k][j] for k in range(len(a[0])))
				row.append(val)
			c.append(row)
	
	return c
