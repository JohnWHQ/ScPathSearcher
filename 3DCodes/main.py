import numpy as np
import time

from path_search import PathSearcher
from data_generate import DataGenerator

split_line = "============================================"

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

def trick_welcome():
	print('\n'.join([''.join([('life is a fucking movie~ '[(x-y) % len('life is a fucking movie~ ')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else' ') \
		for x in range(-30, 30)]) for y in range(30, -30, -1)]))

if __name__ == '__main__':
	
	# matrix = build_matrix(500, 500, 200, 1, 1000)
	# searcher = PathSearcher(matrix)
	# searcher.run()

	# data = DataGenerator(500, 500, 140, 25000)
	# searcher = PathSearcher(data.matrix)
	# searcher.run()

	
	trick_welcome()

	# length
	a = 500
	# width
	b = 500
	# heigth
	c = 140

	# ticks seeds size
	seed_size = 20000

	# algrithm run count
	cal_count = 10

	# get path pass count
	count = 0

	v_percent_total= 0

	for i in range(1, cal_count + 1):
		print "No.{}/{} run:".format(str(i), str(cal_count))

		data = DataGenerator(a, b, c, seed_size)
		searcher = PathSearcher(data.matrix)

		v_percent_total = v_percent_total + data.v_percent

		if searcher.run() is True:
			count = count + 1

		print split_line

	cur_probability = float(count) / float(cal_count)
	cur_total_v_percent = float(v_percent_total) / float(cal_count)

	print "**********All codes run over**********\nrow:{} \ncol:{} \nheight:{} \nsampleSize:{} \npath:{} \ncalCount:{} \nprobability:{}".format(
		str(a), str(b), str(c), str(seed_size), str(count), str(cal_count), str(cur_probability)
	)
	print "vPercentAvg:" + str(cur_total_v_percent) 




