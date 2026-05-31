'''
Easy
Statistics


Write a Python function to calculate the covariance matrix for a given set of vectors. 
The function should take a list of lists, where each inner list represents a feature with its observations, and return a covariance matrix as a list of lists.
'''
import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	n_features = len(vectors)
	n_observations = len(vectors[0])
	covariance_matrix = [[0 for i in range(n_features)] for i in range(n_features)]
	means = [sum(feature) / n_observations for feature in vectors]

	for i in range(n_features):
		for j in range(i, n_features):

			covariance = sum((vectors[i][k] - means[i]) * (vectors[j][k] - means[i]) for k in range(n_observations))/(n_observations-1)
			
			covariance_matrix[i][j] = covariance_matrix[j][i] = covariance
	
	return covariance_matrix
		
