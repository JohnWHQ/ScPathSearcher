import numpy as np
import time
import datetime
import multiprocessing
import os

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

def run(seed_size, cal_count, dir_name, pid):

	# length
	a = 500
	# width
	b = 500
	# heigth
	c = 140

	v_percent_total= 0

	# get path pass count
	count = 0

	file_name = dir_name + "/" + str(pid)
	file = open(file_name, "w")

	for i in range(1, cal_count + 1):
		# print "No.{}/{} run:".format(str(i), str(cal_count))
		print "Pid:{} No.{}/{} start...".format(str(pid), str(i), str(cal_count))


		data = DataGenerator(a, b, c, seed_size)
		searcher = PathSearcher(data.matrix)

		v_percent_total = v_percent_total + data.v_percent

		if searcher.run() is True:
			count = count + 1

		# print split_line
		print "Pid:{} No.{}/{} done...".format(str(pid), str(i), str(cal_count))


	cur_probability = float(count) / float(cal_count)
	cur_total_v_percent = float(v_percent_total) / float(cal_count)

	# print "**********All codes run over**********\nrow:{} \ncol:{} \nheight:{} \nsampleSize:{} \npath:{} \ncalCount:{} \nprobability:{}".format(
	# 	str(a), str(b), str(c), str(seed_size), str(count), str(cal_count), str(cur_probability)
	# )
	file.write("**********cur pid run over**********\nrow:{} \ncol:{} \nheight:{} \nsampleSize:{} \npath:{} \ncalCount:{} \nprobability:{}\n".format(
		str(a), str(b), str(c), str(seed_size), str(count), str(cal_count), str(cur_probability)
	))

	# print "vPercentAvg:" + str(cur_total_v_percent) 
	file.write("\n=========summary========")
	file.write("\ncurPidVPercentAvg:" + str(cur_total_v_percent))
	file.write("\ncurPidRunCount:" + str(cal_count))
	file.write("\ncurPidPathCount:" + str(count))


	file.close()

def normal_main():

	# length
	a = 500
	# width
	b = 500
	# heigth
	c = 140

	# ticks seeds size
	seed_size = 20000

	# algrithm run count
	cal_count = 5

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


def parallel_main():

	# ticks seeds size
	seed_size = 20000

	# algrithm run count
	total_run_count = 5

	core_nu = 5

	dt = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
	folder = os.getcwd() + "/result_" + str(dt)
	

	if not os.path.exists(folder):
	    os.makedirs(folder)
	print folder
	dir_name = folder + "/"

	if total_run_count >= core_nu:
	    pid_size = total_run_count / core_nu
	    real_pid_size = core_nu
	else:
		pid_size = 1
		real_pid_size = total_run_count
		total_run_count = 0

	print "=== run start pidNum:{} batchSize:{} mo:{} ===".format(str(real_pid_size), str(pid_size), str((total_run_count % core_nu)))

	ps = []
	for i in range(1, real_pid_size + 1):
		cur_p = multiprocessing.Process(target=run, args=(seed_size, pid_size, dir_name, i,))
		cur_p.start()
		ps.append(cur_p)

	cur_i = 0
	if (total_run_count % core_nu) != 0:
		real_pid_size = real_pid_size + 1
		cur_i = (total_run_count % core_nu)
		cur_p = multiprocessing.Process(target=run, args=(seed_size, cur_i, dir_name, real_pid_size,))
		cur_p.start()
		ps.append(cur_p)
		

	for item in ps:
		item.join()

	total_v_percent = 0
	total_count = 0
	total_path = 0
	for i in range(1, real_pid_size + 1):
		file_name = dir_name + "/" + str(i)
		for line in open(file_name):
			if "curPidVPercentAvg" in line:
				total_v_percent = total_v_percent + float(line.split(":")[1])
			if "curPidRunCount" in line:
				total_count = total_count + float(line.split(":")[1])
			if "curPidPathCount" in line:
				total_path = total_path + float(line.split(":")[1])


	total_v_percent_avg = total_v_percent / float(real_pid_size)
	total_probability = float(total_path) / float(total_count)


	print "\n=== run  completed ==="

	print "\n=== result summary ==="
	print "totalRunCount:{}\n".format(str(total_count))
	print "totalPath:{}\n".format(str(total_path))
	print "totalVpercentAvg:{}\n".format(str(total_v_percent_avg))
	print "totalProbability:{}\n".format(str(total_probability))



if __name__ == '__main__':
	
	# matrix = build_matrix(500, 500, 200, 1, 1000)
	# searcher = PathSearcher(matrix)
	# searcher.run()

	# data = DataGenerator(500, 500, 140, 25000)
	# searcher = PathSearcher(data.matrix)
	# searcher.run()

	trick_welcome()

	start_time = time.time()

	# normal_main()
	
	parallel_main()

	end_time = time.time()
	print "=== cal total cost time:" + str(end_time - start_time)







