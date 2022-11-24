import numpy as np
import time

from path_search import PathSearcher
from data_generate import DataGenerator


def build_matrix(x, y, z, a, b):
	"""
	   generate random 0/1 matrix
	   x * y * z matrix
	   a/b percent random set 1
	"""
	start_time = time.time()

	matrix = np.zeros((x, y, z))
	for i in range(x):
		for j in range(y):
			for k in range(z):
				cur_rand = np.random.randint(b)
				if cur_rand <= a:
					matrix[i][j][k] = 1
					
	end_time = time.time()
	print str(end_time - start_time)
	return matrix


if __name__ == '__main__':
	
	# matrix = build_matrix(500, 500, 200, 1, 1000)
	# searcher = PathSearcher(matrix)
	# searcher.run()

	data = DataGenerator(500, 500, 200, 500000)
	searcher = PathSearcher(data.matrix)
	searcher.run()


