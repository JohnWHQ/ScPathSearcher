import numpy as np

from path_search import PathSearcher


def build_matrix(x, y, z, a, b):
	"""
	   generate random 0/1 matrix
	   x * y matrix
	   a/b percent random set 1
	"""
	matrix = np.zeros((x, y, z))

	for i in range(x):
		for j in range(y):
			for k in range(z):
				cur_rand = np.random.randint(b)
				if cur_rand <= a:
					matrix[i][j][k] = 1
	return matrix


if __name__ == '__main__':
	
	matrix = build_matrix(500, 500, 100, 10, 100)
	searcher = PathSearcher(matrix)
	searcher.run()