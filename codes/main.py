# main.py

import numpy as np
from path_search import PathSearcher
from data_generate import DataGenerator
from image_utils import generate_and_store_image

split_line = "============================================"

def build_matrix(x, y, a, b):
	"""
	   generate random 0/1 matrix
	   x * y matrix
	   a/b percent random set 1
	"""
	martix = np.zeros([x, y])

	for i in range(x):
		for j in range(y):
			cur_rand = np.random.randint(b)
			if cur_rand <= a:
				martix[i][j] = 1
	return martix

def moc_run_search():

	image_flag = False

	print "10*10:=================================================="
	matrix = build_matrix(10, 10, 50, 100)
	searcher = PathSearcher(matrix)
	searcher.run(generate_image=image_flag)

	print "100*100:================================================"
	matrix = build_matrix(100, 100, 50, 100)
	searcher = PathSearcher(matrix)
	searcher.run(generate_image=image_flag)

	print "500*500:================================================"
	matrix = build_matrix(500, 500, 50, 100)
	searcher = PathSearcher(matrix)
	searcher.run(generate_image=image_flag)

	print "1000*1000:=============================================="
	matrix = build_matrix(1000, 1000, 10, 100)
	searcher = PathSearcher(matrix)
	searcher.run(generate_image=image_flag)

	print "5000*5000:=============================================="
	matrix = build_matrix(5000, 5000, 10, 100)
	searcher = PathSearcher(matrix)
	searcher.run(generate_image=image_flag)

	print "10000*10000:============================================"
	matrix = build_matrix(10000, 10000, 5, 100)
	searcher = PathSearcher(matrix)
	searcher.run(generate_image=image_flag)

	print "50000*50000:============================================"
	matrix = build_matrix(10000, 10000, 2, 100)
	searcher = PathSearcher(matrix)
	searcher.run(generate_image=image_flag)	


if __name__ == '__main__':

	# row size
	n = 500
	# col size
	m = 500
	# sample size
	x = 150

	# codes run count
	cur_size = 100

	# has path case count
	count = 0
	real_set_x_total = 0
	v_percent_total = 0
	for i in range(cur_size):

		data_generator = DataGenerator(n, m, x)

		real_set_x_total = real_set_x_total + data_generator.real_x
		v_percent_total = v_percent_total + data_generator.v_percent

		print "No.{}/{} run:\nreal set points:{}".format(str(i), str(cur_size), str(data_generator.real_x))
		print "selected set points:{}".format(str(data_generator.all_select))
		print "vPercent:{}".format(str(data_generator.v_percent))

		searcher = PathSearcher(data_generator.matrix)

		if searcher.run() is True:
			count = count + 1
		print split_line

	cur_probability = float(count) / float(cur_size)
	cur_total_v_percent = float(v_percent_total) / float(cur_size)
	cur_total_real_set_avg = float(real_set_x_total) / float(cur_size)

	print "***All codes run over***\nrow:{} \ncol:{} \nsampleSize:{} \npath:{} \ncalCount:{} \nprobability:{}".format(
		str(n), str(m), str(x), str(count), str(cur_size), str(cur_probability)
	)
	print "allSelectedAvg:" + str(cur_total_real_set_avg)
	print "vPercentAvg:" + str(cur_total_v_percent) 
		









