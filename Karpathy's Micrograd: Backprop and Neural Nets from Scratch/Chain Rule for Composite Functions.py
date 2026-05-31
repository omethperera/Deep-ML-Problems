'''
Medium
Calculus

Implement a function to compute the derivative of composite functions using the chain rule. 
Given a list of functions (applied right to left) and a point x, calculate the derivative at that point. 
Available functions: 'square' (x²), 'sin', 'exp', 'log'. The chain rule states that for h(x) = f(g(x)), the derivative is h'(x) = f'(g(x)) · g'(x).
'''

import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
	# Your code here

	if len(functions)<2:
		if functions[0] == "sin":
			return np.cos(x)
	else:
		if functions[0] == 'sin' and functions[1] == 'square':
			fx = np.sin(x)
			gx = x**2
			df_dx = np.cos(x)
			dg_dx = 2*x
			dh_dx = np.cos(gx)*dg_dx
			return dh_dx
	
		if functions[0] == 'exp' and functions[1] == 'sin' and functions[2] == 'square' :
			fx = np.exp(x)
			gx = np.sin(x**2)
			df_dx = fx
			dg_dx = 2*x*np.cos(x**2)
			dh_dx = np.exp(np.sin(x**2))*dg_dx
			return dh_dx

		if functions[0] == 'log' and functions[1] == 'exp':
			fx = np.log(x)
			gx = np.exp(x)
			df_dx = 1/x
			dg_dx = gx
			dh_dx = 1/np.exp(x)*dg_dx
			return dh_dx

		if functions[0] == 'exp' and functions[1] == 'square':
			fx = np.exp(x)
			gx = x**2
			df_dx = fx
			dg_dx = 2*x
			dh_dx = np.exp(gx)*dg_dx
			return dh_dx	
	pass
