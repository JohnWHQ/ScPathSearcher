# data generate codes

import numpy as np
import time
import node


class DataGenerator:
	_selected = 1
	_sp_point = 2

	def __init__(self, n, m, l, x=None):

		start_time = time.time()

		self.row = n
		self.col = m
		self.height = l

		self.real_set_ponts = set()
		self.fill_set_ponts = set()

		# expect set point counts if x is none, means generate all size points
		self.x = x if x is not None else (n * m * l) 

		self.total = n * m * l

		# build matrix and set selected point with x / row * col * height probability
		self.matrix, self.real_x = self._init_matrix()

		self._generate_rule_shape_by_probability()
		self.all_select = len(self.real_set_ponts) + len(self.fill_set_ponts)

		self.v_percent = float(self.all_select) / float(self.total)

		end_time = time.time()
		print "DataGenrateDone:size={}x{}x{}\nsampleSetPoints={}\nrealSetPoints={}\nallSelectPoints={}\nvPercent={}\ndata cost seconds={}"\
		.format(str(n), str(m), str(l), str(x), str(self.real_x), str(self.all_select), str(self.v_percent), str(end_time - start_time))

	def _check_valid(self, x, y, z, cur):
		return (x < self.row) and (y < self.col) and (z < self.height) and (cur not in self.real_set_ponts) and (cur not in self.fill_set_ponts)


	def _init_matrix(self):

		matrix = np.zeros((self.row, self.col, self.height))

		for i in range(self.row):
			for j in range(self.col):
				for k in range(self.height):
					# equiprobability generate rand from 1 ~ total 
					cur_rand = np.random.randint(self.total) + 1
					if cur_rand <= self.x:
						matrix[i][j][k] = DataGenerator._selected
						self.real_set_ponts.add(node.Node(i, j, k))

		return matrix, len(self.real_set_ponts)	


	def _generate_rule_shape_by_probability(self):

		for cur_node in self.real_set_ponts:
			i = cur_node.x
			j = cur_node.y
			k = cur_node.z

			# equiprobability generate rand from 1 ~ total 
			cur_rand = np.random.randint(100) + 1

			# 2% probability to generate 208 (147)
			if cur_rand >= 1 and cur_rand <= 2:
				if k <= 34:
					self._case_1_8(i, j, k)

				if k >= 35 and k <= 69:
					self._case_2_8(i, j, k)

				if k >= 70 and k <= 104:
					self._case_3_8(i, j, k)

				if k >= 105 and k <= 139:
					self._case_4_8(i, j, k)


			# 3% probability to generate 188 (133)
			if cur_rand >= 3 and cur_rand <= 5:
				if k <= 34:
					self._case_1_7(i, j, k)

				if k >= 35 and k <= 69:
					self._case_2_7(i, j, k)

				if k >= 70 and k <= 104:
					self._case_3_7(i, j, k)

				if k >= 105 and k <= 139:
					self._case_4_7(i, j, k)


			# 7% probability to generate 146 (103)
			if cur_rand >= 6 and cur_rand <= 12:
				if k <= 34:
					self._case_1_6(i, j, k)

				if k >= 35 and k <= 69:
					self._case_2_6(i, j, k)

				if k >= 70 and k <= 104:
					self._case_3_6(i, j, k)

				if k >= 105 and k <= 139:
					self._case_4_6(i, j, k)


			# 10% probability to generate 125 (88)
			if cur_rand >= 13 and cur_rand <= 22:
				if k <= 34:
					self._case_1_5(i, j, k)

				if k >= 35 and k <= 69:
					self._case_2_5(i, j, k)

				if k >= 70 and k <= 104:
					self._case_3_5(i, j, k)

				if k >= 105 and k <= 139:
					self._case_4_5(i, j, k)


			# 16% probability to generate 104 (74)
			if cur_rand >= 23 and cur_rand <= 38:
				if k <= 34:
					self._case_1_4(i, j, k)

				if k >= 35 and k <= 69:
					self._case_2_4(i, j, k)

				if k >= 70 and k <= 104:
					self._case_3_4(i, j, k)

				if k >= 105 and k <= 139:
					self._case_4_4(i, j, k)


			# 17% probability to generate 63 (45)
			if cur_rand >= 39 and cur_rand <= 55:
				if k <= 34:
					self._case_1_3(i, j, k)

				if k >= 35 and k <= 69:
					self._case_2_3(i, j, k)

				if k >= 70 and k <= 104:
					self._case_3_3(i, j, k)

				if k >= 105 and k <= 139:
					self._case_4_3(i, j, k)


			# 30% probability to generate 42 (30)
			if cur_rand >= 56 and cur_rand <= 85:
				if k <= 34:
					self._case_1_2(i, j, k)

				if k >= 35 and k <= 69:
					self._case_2_2(i, j, k)

				if k >= 70 and k <= 104:
					self._case_3_2(i, j, k)

				if k >= 105 and k <= 139:
					self._case_4_2(i, j, k)


			# 15% probability to generate 21 (15)
			if cur_rand >= 86 and cur_rand <= 100:
				if k <= 34:
					self._case_1_1(i, j, k)

				if k >= 35 and k <= 69:
					self._case_2_1(i, j, k)

				if k >= 70 and k <= 104:
					self._case_3_1(i, j, k)

				if k >= 105 and k <= 139:
					self._case_4_1(i, j, k)


	def _case_1_1(self, x, y, z):

		# (x, y, z) -> (x + 10, y, z)
		for delt in range(11):
			cur = node.Node(x + delt, y, z)
			if self._check_valid(x + delt, y, z, cur):
				self.matrix[x + delt][y][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 10, y, z + 1) -> (x + 19, y, z + 1)
		for delt in range(10, 20):
			cur = node.Node(x + delt, y, z + 1)
			if self._check_valid(x + delt, y, z + 1, cur):
				self.matrix[x + delt][y][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)


	def _case_1_2(self, x, y, z):

		# (x, y, z) -> (x + 11, y, z)
		for delt in range(12):
			cur = node.Node(x + delt, y, z)
			if self._check_valid(x + delt, y, z, cur):
				self.matrix[x + delt][y][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 11, y, z + 1) -> (x + 23, y, z + 1)
		for delt in range(11, 24):
			cur = node.Node(x + delt, y, z + 1)
			if self._check_valid(x + delt, y, z + 1, cur):
				self.matrix[x + delt][y][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)


		# (x + 23, y, z + 2) -> (x + 35, y, z + 2)
		for delt in range(23, 36):
			cur = node.Node(x + delt, y, z + 2)
			if self._check_valid(x + delt, y, z + 2, cur):
				self.matrix[x + delt][y][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 35, y, z + 3) -> (x + 47, y, z + 3)
		for delt in range(35, 48):
			cur = node.Node(x + delt, y, z + 3)
			if self._check_valid(x + delt, y, z + 3, cur):
				self.matrix[x + delt][y][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)


	def _case_1_3(self, x, y, z):

		# (x, y, z) -> (x + 11, y, z)
		for delt in range(12):
			cur = node.Node(x + delt, y, z)
			if self._check_valid(x + delt, y, z, cur):
				self.matrix[x + delt][y][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 11, y, z + 1) -> (x + 23, y, z + 1)
		for delt in range(11, 24):
			cur = node.Node(x + delt, y, z + 1)
			if self._check_valid(x + delt, y, z + 1, cur):
				self.matrix[x + delt][y][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)


		# (x + 23, y, z + 2) -> (x + 35, y, z + 2)
		for delt in range(23, 36):
			cur = node.Node(x + delt, y, z + 2)
			if self._check_valid(x + delt, y, z + 2, cur):
				self.matrix[x + delt][y][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 35, y, z + 3) -> (x + 47, y, z + 3)
		for delt in range(35, 48):
			cur = node.Node(x + delt, y, z + 3)
			if self._check_valid(x + delt, y, z + 3, cur):
				self.matrix[x + delt][y][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 47, y, z + 4) -> (x + 58, y, z + 4)
		for delt in range(47, 59):
			cur = node.Node(x + delt, y, z + 4)
			if self._check_valid(x + delt, y, z + 4, cur):
				self.matrix[x + delt][y][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 58, y, z + 5) -> (x + 62, y, z + 5)
		for delt in range(58, 63):
			cur = node.Node(x + delt, y, z + 5)
			if self._check_valid(x + delt, y, z + 5, cur):
				self.matrix[x + delt][y][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)				


	def _case_1_4(self, x, y, z):

		# (x, y, z) -> (x + 11, y, z)
		for delt in range(12):
			cur = node.Node(x + delt, y, z)
			if self._check_valid(x + delt, y, z, cur):
				self.matrix[x + delt][y][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 11, y, z + 1) -> (x + 23, y, z + 1)
		for delt in range(11, 24):
			cur = node.Node(x + delt, y, z + 1)
			if self._check_valid(x + delt, y, z + 1, cur):
				self.matrix[x + delt][y][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)


		# (x + 23, y, z + 2) -> (x + 35, y, z + 2)
		for delt in range(23, 36):
			cur = node.Node(x + delt, y, z + 2)
			if self._check_valid(x + delt, y, z + 2, cur):
				self.matrix[x + delt][y][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 35, y, z + 3) -> (x + 47, y, z + 3)
		for delt in range(35, 48):
			cur = node.Node(x + delt, y, z + 3)
			if self._check_valid(x + delt, y, z + 3, cur):
				self.matrix[x + delt][y][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 47, y, z + 4) -> (x + 58, y, z + 4)
		for delt in range(47, 59):
			cur = node.Node(x + delt, y, z + 4)
			if self._check_valid(x + delt, y, z + 4, cur):
				self.matrix[x + delt][y][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 58, y, z + 5) -> (x + 69, y, z + 5)
		for delt in range(58, 70):
			cur = node.Node(x + delt, y, z + 5)
			if self._check_valid(x + delt, y, z + 5, cur):
				self.matrix[x + delt][y][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 69, y, z + 6) -> (x + 81, y, z + 6)
		for delt in range(69, 82):
			cur = node.Node(x + delt, y, z + 6)
			if self._check_valid(x + delt, y, z + 6, cur):
				self.matrix[x + delt][y][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 81, y, z + 7) -> (x + 92, y, z + 7)
		for delt in range(81, 93):
			cur = node.Node(x + delt, y, z + 7)
			if self._check_valid(x + delt, y, z + 7, cur):
				self.matrix[x + delt][y][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)			

		# (x + 92, y, z + 8) -> (x + 103, y, z + 8)
		for delt in range(92, 104):
			cur = node.Node(x + delt, y, z + 8)
			if self._check_valid(x + delt, y, z + 8, cur):
				self.matrix[x + delt][y][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 103, y, z + 9)
		for delt in range(103, 104):
			cur = node.Node(x + delt, y, z + 9)
			if self._check_valid(x + delt, y, z + 9, cur):
				self.matrix[x + delt][y][z + 9] = DataGenerator._selected
				self.fill_set_ponts.add(cur)


	def _case_1_5(self, x, y, z):

		# (x, y, z) -> (x + 11, y, z)
		for delt in range(12):
			cur = node.Node(x + delt, y, z)
			if self._check_valid(x + delt, y, z, cur):
				self.matrix[x + delt][y][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 11, y, z + 1) -> (x + 23, y, z + 1)
		for delt in range(11, 24):
			cur = node.Node(x + delt, y, z + 1)
			if self._check_valid(x + delt, y, z + 1, cur):
				self.matrix[x + delt][y][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)


		# (x + 23, y, z + 2) -> (x + 35, y, z + 2)
		for delt in range(23, 36):
			cur = node.Node(x + delt, y, z + 2)
			if self._check_valid(x + delt, y, z + 2, cur):
				self.matrix[x + delt][y][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 35, y, z + 3) -> (x + 47, y, z + 3)
		for delt in range(35, 48):
			cur = node.Node(x + delt, y, z + 3)
			if self._check_valid(x + delt, y, z + 3, cur):
				self.matrix[x + delt][y][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 47, y, z + 4) -> (x + 58, y, z + 4)
		for delt in range(47, 59):
			cur = node.Node(x + delt, y, z + 4)
			if self._check_valid(x + delt, y, z + 4, cur):
				self.matrix[x + delt][y][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 58, y, z + 5) -> (x + 69, y, z + 5)
		for delt in range(58, 70):
			cur = node.Node(x + delt, y, z + 5)
			if self._check_valid(x + delt, y, z + 5, cur):
				self.matrix[x + delt][y][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 69, y, z + 6) -> (x + 81, y, z + 6)
		for delt in range(69, 82):
			cur = node.Node(x + delt, y, z + 6)
			if self._check_valid(x + delt, y, z + 6, cur):
				self.matrix[x + delt][y][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 81, y, z + 7) -> (x + 92, y, z + 7)
		for delt in range(81, 93):
			cur = node.Node(x + delt, y, z + 7)
			if self._check_valid(x + delt, y, z + 7, cur):
				self.matrix[x + delt][y][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)			

		# (x + 92, y, z + 8) -> (x + 103, y, z + 8)
		for delt in range(92, 104):
			cur = node.Node(x + delt, y, z + 8)
			if self._check_valid(x + delt, y, z + 8, cur):
				self.matrix[x + delt][y][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 103, y, z + 9) -> (x + 114, y, z + 9)
		for delt in range(103, 115):
			cur = node.Node(x + delt, y, z + 9)
			if self._check_valid(x + delt, y, z + 9, cur):
				self.matrix[x + delt][y][z + 9] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 114, y, z + 10) -> (x + 125, y, z + 10)
		for delt in range(114, 126):
			cur = node.Node(x + delt, y, z + 10)
			if self._check_valid(x + delt, y, z + 10, cur):
				self.matrix[x + delt][y][z + 10] = DataGenerator._selected
				self.fill_set_ponts.add(cur)				

		# (x + 125, y, z + 10)
		for delt in range(125, 126):
			cur = node.Node(x + delt, y, z + 10)
			if self._check_valid(x + delt, y, z + 10, cur):
				self.matrix[x + delt][y][z + 10] = DataGenerator._selected
				self.fill_set_ponts.add(cur)


	def _case_1_6(self, x, y, z):

		# (x, y, z) -> (x + 11, y, z)
		for delt in range(12):
			cur = node.Node(x + delt, y, z)
			if self._check_valid(x + delt, y, z, cur):
				self.matrix[x + delt][y][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 11, y, z + 1) -> (x + 23, y, z + 1)
		for delt in range(11, 24):
			cur = node.Node(x + delt, y, z + 1)
			if self._check_valid(x + delt, y, z + 1, cur):
				self.matrix[x + delt][y][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)


		# (x + 23, y, z + 2) -> (x + 35, y, z + 2)
		for delt in range(23, 36):
			cur = node.Node(x + delt, y, z + 2)
			if self._check_valid(x + delt, y, z + 2, cur):
				self.matrix[x + delt][y][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 35, y, z + 3) -> (x + 47, y, z + 3)
		for delt in range(35, 48):
			cur = node.Node(x + delt, y, z + 3)
			if self._check_valid(x + delt, y, z + 3, cur):
				self.matrix[x + delt][y][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 47, y, z + 4) -> (x + 58, y, z + 4)
		for delt in range(47, 59):
			cur = node.Node(x + delt, y, z + 4)
			if self._check_valid(x + delt, y, z + 4, cur):
				self.matrix[x + delt][y][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 58, y, z + 5) -> (x + 69, y, z + 5)
		for delt in range(58, 70):
			cur = node.Node(x + delt, y, z + 5)
			if self._check_valid(x + delt, y, z + 5, cur):
				self.matrix[x + delt][y][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 69, y, z + 6) -> (x + 81, y, z + 6)
		for delt in range(69, 82):
			cur = node.Node(x + delt, y, z + 6)
			if self._check_valid(x + delt, y, z + 6, cur):
				self.matrix[x + delt][y][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 81, y, z + 7) -> (x + 92, y, z + 7)
		for delt in range(81, 93):
			cur = node.Node(x + delt, y, z + 7)
			if self._check_valid(x + delt, y, z + 7, cur):
				self.matrix[x + delt][y][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)			

		# (x + 92, y, z + 8) -> (x + 103, y, z + 8)
		for delt in range(92, 104):
			cur = node.Node(x + delt, y, z + 8)
			if self._check_valid(x + delt, y, z + 8, cur):
				self.matrix[x + delt][y][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 103, y, z + 9) -> (x + 114, y, z + 9)
		for delt in range(103, 115):
			cur = node.Node(x + delt, y, z + 9)
			if self._check_valid(x + delt, y, z + 9, cur):
				self.matrix[x + delt][y][z + 9] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 114, y, z + 10) -> (x + 125, y, z + 10)
		for delt in range(114, 126):
			cur = node.Node(x + delt, y, z + 10)
			if self._check_valid(x + delt, y, z + 10, cur):
				self.matrix[x + delt][y][z + 10] = DataGenerator._selected
				self.fill_set_ponts.add(cur)				

		# (x + 125, y, z + 11) -> (x + 137, y, z + 11)
		for delt in range(125, 138):
			cur = node.Node(x + delt, y, z + 11)
			if self._check_valid(x + delt, y, z + 11, cur):
				self.matrix[x + delt][y][z + 11] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 137, y, z + 12) -> (x + 146, y, z + 12)
		for delt in range(137, 147):
			cur = node.Node(x + delt, y, z + 12)
			if self._check_valid(x + delt, y, z + 12, cur):
				self.matrix[x + delt][y][z + 12] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	


	def _case_1_7(self, x, y, z):

		# (x, y, z) -> (x + 11, y, z)
		for delt in range(12):
			cur = node.Node(x + delt, y, z)
			if self._check_valid(x + delt, y, z, cur):
				self.matrix[x + delt][y][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 11, y, z + 1) -> (x + 23, y, z + 1)
		for delt in range(11, 24):
			cur = node.Node(x + delt, y, z + 1)
			if self._check_valid(x + delt, y, z + 1, cur):
				self.matrix[x + delt][y][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)


		# (x + 23, y, z + 2) -> (x + 35, y, z + 2)
		for delt in range(23, 36):
			cur = node.Node(x + delt, y, z + 2)
			if self._check_valid(x + delt, y, z + 2, cur):
				self.matrix[x + delt][y][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 35, y, z + 3) -> (x + 47, y, z + 3)
		for delt in range(35, 48):
			cur = node.Node(x + delt, y, z + 3)
			if self._check_valid(x + delt, y, z + 3, cur):
				self.matrix[x + delt][y][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 47, y, z + 4) -> (x + 58, y, z + 4)
		for delt in range(47, 59):
			cur = node.Node(x + delt, y, z + 4)
			if self._check_valid(x + delt, y, z + 4, cur):
				self.matrix[x + delt][y][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 58, y, z + 5) -> (x + 69, y, z + 5)
		for delt in range(58, 70):
			cur = node.Node(x + delt, y, z + 5)
			if self._check_valid(x + delt, y, z + 5, cur):
				self.matrix[x + delt][y][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 69, y, z + 6) -> (x + 81, y, z + 6)
		for delt in range(69, 82):
			cur = node.Node(x + delt, y, z + 6)
			if self._check_valid(x + delt, y, z + 6, cur):
				self.matrix[x + delt][y][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 81, y, z + 7) -> (x + 92, y, z + 7)
		for delt in range(81, 93):
			cur = node.Node(x + delt, y, z + 7)
			if self._check_valid(x + delt, y, z + 7, cur):
				self.matrix[x + delt][y][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)			

		# (x + 92, y, z + 8) -> (x + 103, y, z + 8)
		for delt in range(92, 104):
			cur = node.Node(x + delt, y, z + 8)
			if self._check_valid(x + delt, y, z + 8, cur):
				self.matrix[x + delt][y][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 103, y, z + 9) -> (x + 114, y, z + 9)
		for delt in range(103, 115):
			cur = node.Node(x + delt, y, z + 9)
			if self._check_valid(x + delt, y, z + 9, cur):
				self.matrix[x + delt][y][z + 9] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 114, y, z + 10) -> (x + 125, y, z + 10)
		for delt in range(114, 126):
			cur = node.Node(x + delt, y, z + 10)
			if self._check_valid(x + delt, y, z + 10, cur):
				self.matrix[x + delt][y][z + 10] = DataGenerator._selected
				self.fill_set_ponts.add(cur)				


		# (x + 125, y, z + 11) -> (x + 137, y, z + 11)
		for delt in range(125, 138):
			cur = node.Node(x + delt, y, z + 11)
			if self._check_valid(x + delt, y, z + 11, cur):
				self.matrix[x + delt][y][z + 11] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 137, y, z + 12) -> (x + 148, y, z + 12)
		for delt in range(137, 149):
			cur = node.Node(x + delt, y, z + 12)
			if self._check_valid(x + delt, y, z + 12, cur):
				self.matrix[x + delt][y][z + 12] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 148, y, z + 13) -> (x + 160, y, z + 13)
		for delt in range(148, 161):
			cur = node.Node(x + delt, y, z + 13)
			if self._check_valid(x + delt, y, z + 13, cur):
				self.matrix[x + delt][y][z + 13] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 160, y, z + 14) -> (x + 171, y, z + 14)
		for delt in range(160, 172):
			cur = node.Node(x + delt, y, z + 14)
			if self._check_valid(x + delt, y, z + 14, cur):
				self.matrix[x + delt][y][z + 14] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 171, y, z + 15) -> (x + 183, y, z + 15)
		for delt in range(171, 184):
			cur = node.Node(x + delt, y, z + 15)
			if self._check_valid(x + delt, y, z + 15, cur):
				self.matrix[x + delt][y][z + 15] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 183, y, z + 16) -> (x + 187, y, z + 16)
		for delt in range(183, 188):
			cur = node.Node(x + delt, y, z + 16)
			if self._check_valid(x + delt, y, z + 16, cur):
				self.matrix[x + delt][y][z + 16] = DataGenerator._selected
				self.fill_set_ponts.add(cur)


	def _case_1_8(self, x, y, z):

		# (x, y, z) -> (x + 11, y, z)
		for delt in range(12):
			cur = node.Node(x + delt, y, z)
			if self._check_valid(x + delt, y, z, cur):
				self.matrix[x + delt][y][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 11, y, z + 1) -> (x + 23, y, z + 1)
		for delt in range(11, 24):
			cur = node.Node(x + delt, y, z + 1)
			if self._check_valid(x + delt, y, z + 1, cur):
				self.matrix[x + delt][y][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)


		# (x + 23, y, z + 2) -> (x + 35, y, z + 2)
		for delt in range(23, 36):
			cur = node.Node(x + delt, y, z + 2)
			if self._check_valid(x + delt, y, z + 2, cur):
				self.matrix[x + delt][y][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 35, y, z + 3) -> (x + 47, y, z + 3)
		for delt in range(35, 48):
			cur = node.Node(x + delt, y, z + 3)
			if self._check_valid(x + delt, y, z + 3, cur):
				self.matrix[x + delt][y][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 47, y, z + 4) -> (x + 58, y, z + 4)
		for delt in range(47, 59):
			cur = node.Node(x + delt, y, z + 4)
			if self._check_valid(x + delt, y, z + 4, cur):
				self.matrix[x + delt][y][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 58, y, z + 5) -> (x + 69, y, z + 5)
		for delt in range(58, 70):
			cur = node.Node(x + delt, y, z + 5)
			if self._check_valid(x + delt, y, z + 5, cur):
				self.matrix[x + delt][y][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 69, y, z + 6) -> (x + 81, y, z + 6)
		for delt in range(69, 82):
			cur = node.Node(x + delt, y, z + 6)
			if self._check_valid(x + delt, y, z + 6, cur):
				self.matrix[x + delt][y][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 81, y, z + 7) -> (x + 92, y, z + 7)
		for delt in range(81, 93):
			cur = node.Node(x + delt, y, z + 7)
			if self._check_valid(x + delt, y, z + 7, cur):
				self.matrix[x + delt][y][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)			

		# (x + 92, y, z + 8) -> (x + 103, y, z + 8)
		for delt in range(92, 104):
			cur = node.Node(x + delt, y, z + 8)
			if self._check_valid(x + delt, y, z + 8, cur):
				self.matrix[x + delt][y][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 103, y, z + 9) -> (x + 114, y, z + 9)
		for delt in range(103, 115):
			cur = node.Node(x + delt, y, z + 9)
			if self._check_valid(x + delt, y, z + 9, cur):
				self.matrix[x + delt][y][z + 9] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 114, y, z + 10) -> (x + 125, y, z + 10)
		for delt in range(114, 126):
			cur = node.Node(x + delt, y, z + 10)
			if self._check_valid(x + delt, y, z + 10, cur):
				self.matrix[x + delt][y][z + 10] = DataGenerator._selected
				self.fill_set_ponts.add(cur)				


		# (x + 125, y, z + 11) -> (x + 137, y, z + 11)
		for delt in range(125, 138):
			cur = node.Node(x + delt, y, z + 11)
			if self._check_valid(x + delt, y, z + 11, cur):
				self.matrix[x + delt][y][z + 11] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 137, y, z + 12) -> (x + 148, y, z + 12)
		for delt in range(137, 149):
			cur = node.Node(x + delt, y, z + 12)
			if self._check_valid(x + delt, y, z + 12, cur):
				self.matrix[x + delt][y][z + 12] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 148, y, z + 13) -> (x + 160, y, z + 13)
		for delt in range(148, 161):
			cur = node.Node(x + delt, y, z + 13)
			if self._check_valid(x + delt, y, z + 13, cur):
				self.matrix[x + delt][y][z + 13] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 160, y, z + 14) -> (x + 171, y, z + 14)
		for delt in range(160, 172):
			cur = node.Node(x + delt, y, z + 14)
			if self._check_valid(x + delt, y, z + 14, cur):
				self.matrix[x + delt][y][z + 14] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 171, y, z + 15) -> (x + 183, y, z + 15)
		for delt in range(171, 184):
			cur = node.Node(x + delt, y, z + 15)
			if self._check_valid(x + delt, y, z + 15, cur):
				self.matrix[x + delt][y][z + 15] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 183, y, z + 16) -> (x + 195, y, z + 16)
		for delt in range(183, 196):
			cur = node.Node(x + delt, y, z + 16)
			if self._check_valid(x + delt, y, z + 16, cur):
				self.matrix[x + delt][y][z + 16] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 195, y, z + 17) -> (x + 207, y, z + 17)
		for delt in range(195, 208):
			cur = node.Node(x + delt, y, z + 17)
			if self._check_valid(x + delt, y, z + 17, cur):
				self.matrix[x + delt][y][z + 17] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 208, y, z + 18)
		for delt in range(208, 209):
			cur = node.Node(x + delt, y, z + 18)
			if self._check_valid(x + delt, y, z + 18, cur):
				self.matrix[x + delt][y][z + 18] = DataGenerator._selected
				self.fill_set_ponts.add(cur)


	def _case_2_1(self, x, y, z):

		# (x, y, z) -> (x + 4, y, z)
		for delt in range(5):
			cur = node.Node(x + delt, y, z)
			if self._check_valid(x + delt, y, z, cur):
				self.matrix[x + delt][y][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 4, y + 1, z) -> (x + 7, y + 1, z)
		for delt in range(4, 8):
			cur = node.Node(x + delt, y + 1, z)
			if self._check_valid(x + delt, y + 1, z, cur):
				self.matrix[x + delt][y + 1][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 7, y + 2, z) -> (x + 11, y + 2, z)
		for delt in range(7, 12):
			cur = node.Node(x + delt, y + 2, z)
			if self._check_valid(x + delt, y + 2, z, cur):
				self.matrix[x + delt][y + 2][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 11, y + 2, z + 1)
		for delt in range(11, 12):
			cur = node.Node(x + delt, y + 2, z + 1)
			if self._check_valid(x + delt, y + 2, z + 1, cur):
				self.matrix[x + delt][y + 2][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 11, y + 3, z + 1) -> (x + 14, y + 3, z + 1)
		for delt in range(11, 15):
			cur = node.Node(x + delt, y + 3, z + 1)
			if self._check_valid(x + delt, y + 3, z + 1, cur):
				self.matrix[x + delt][y + 3][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 14, y + 4, z + 1) -> (x + 18, y + 4, z + 1)
		for delt in range(14, 19):
			cur = node.Node(x + delt, y + 4, z + 1)
			if self._check_valid(x + delt, y + 4, z + 1, cur):
				self.matrix[x + delt][y + 4][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 18, y + 5, z + 1) -> (x + 20, y + 5, z + 1)
		for delt in range(18, 21):
			cur = node.Node(x + delt, y + 5, z + 1)
			if self._check_valid(x + delt, y + 5, z + 1, cur):
				self.matrix[x + delt][y + 5][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)


	def _case_2_2(self, x, y, z):

		# (x, y, z) -> (x + 4, y, z)
		for delt in range(5):
			cur = node.Node(x + delt, y, z)
			if self._check_valid(x + delt, y, z, cur):
				self.matrix[x + delt][y][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 4, y + 1, z) -> (x + 7, y + 1, z)
		for delt in range(4, 8):
			cur = node.Node(x + delt, y + 1, z)
			if self._check_valid(x + delt, y + 1, z, cur):
				self.matrix[x + delt][y + 1][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 7, y + 2, z) -> (x + 11, y + 2, z)
		for delt in range(7, 12):
			cur = node.Node(x + delt, y + 2, z)
			if self._check_valid(x + delt, y + 2, z, cur):
				self.matrix[x + delt][y + 2][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 11, y + 2, z + 1)
		for delt in range(11, 12):
			cur = node.Node(x + delt, y + 2, z + 1)
			if self._check_valid(x + delt, y + 2, z + 1, cur):
				self.matrix[x + delt][y + 2][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 11, y + 3, z + 1) -> (x + 14, y + 3, z + 1)
		for delt in range(11, 15):
			cur = node.Node(x + delt, y + 3, z + 1)
			if self._check_valid(x + delt, y + 3, z + 1, cur):
				self.matrix[x + delt][y + 3][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 14, y + 4, z + 1) -> (x + 18, y + 4, z + 1)
		for delt in range(14, 19):
			cur = node.Node(x + delt, y + 4, z + 1)
			if self._check_valid(x + delt, y + 4, z + 1, cur):
				self.matrix[x + delt][y + 4][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 18, y + 5, z + 1) -> (x + 22, y + 5, z + 1)
		for delt in range(18, 23):
			cur = node.Node(x + delt, y + 5, z + 1)
			if self._check_valid(x + delt, y + 5, z + 1, cur):
				self.matrix[x + delt][y + 5][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 22, y + 5, z + 2)
		for delt in range(22, 23):
			cur = node.Node(x + delt, y + 5, z + 2)
			if self._check_valid(x + delt, y + 5, z + 2, cur):
				self.matrix[x + delt][y + 5][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 22, y + 6, z + 2) -> (x + 25, y + 6, z + 2)
		for delt in range(22, 26):
			cur = node.Node(x + delt, y + 6, z + 2)
			if self._check_valid(x + delt, y + 6, z + 2, cur):
				self.matrix[x + delt][y + 6][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 25, y + 7, z + 2) -> (x + 29, y + 7, z + 2)
		for delt in range(25, 30):
			cur = node.Node(x + delt, y + 7, z + 2)
			if self._check_valid(x + delt, y + 7, z + 2, cur):
				self.matrix[x + delt][y + 7][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 29, y + 8, z + 2) -> (x + 33, y + 8, z + 2)
		for delt in range(29, 34):
			cur = node.Node(x + delt, y + 8, z + 2)
			if self._check_valid(x + delt, y + 8, z + 2, cur):
				self.matrix[x + delt][y + 8][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 33, y + 8, z + 3)
		for delt in range(33, 34):
			cur = node.Node(x + delt, y + 8, z + 3)
			if self._check_valid(x + delt, y + 8, z + 3, cur):
				self.matrix[x + delt][y + 8][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 33, y + 9, z + 3) -> (x + 37, y + 9, z + 3) 
		for delt in range(33, 38):
			cur = node.Node(x + delt, y + 9, z + 3)
			if self._check_valid(x + delt, y + 9, z + 3, cur):
				self.matrix[x + delt][y + 9][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 37, y + 10, z + 3) -> (x + 42, y + 10, z + 3) 
		for delt in range(37, 43):
			cur = node.Node(x + delt, y + 10, z + 3)
			if self._check_valid(x + delt, y + 10, z + 3, cur):
				self.matrix[x + delt][y + 10][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)


	def _case_2_3(self, x, y, z):

		# (x, y, z) -> (x + 4, y, z)
		for delt in range(5):
			cur = node.Node(x + delt, y, z)
			if self._check_valid(x + delt, y, z, cur):
				self.matrix[x + delt][y][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 4, y + 1, z) -> (x + 7, y + 1, z)
		for delt in range(4, 8):
			cur = node.Node(x + delt, y + 1, z)
			if self._check_valid(x + delt, y + 1, z, cur):
				self.matrix[x + delt][y + 1][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 7, y + 2, z) -> (x + 11, y + 2, z)
		for delt in range(7, 12):
			cur = node.Node(x + delt, y + 2, z)
			if self._check_valid(x + delt, y + 2, z, cur):
				self.matrix[x + delt][y + 2][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 11, y + 2, z + 1)
		for delt in range(11, 12):
			cur = node.Node(x + delt, y + 2, z + 1)
			if self._check_valid(x + delt, y + 2, z + 1, cur):
				self.matrix[x + delt][y + 2][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 11, y + 3, z + 1) -> (x + 14, y + 3, z + 1)
		for delt in range(11, 15):
			cur = node.Node(x + delt, y + 3, z + 1)
			if self._check_valid(x + delt, y + 3, z + 1, cur):
				self.matrix[x + delt][y + 3][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 14, y + 4, z + 1) -> (x + 18, y + 4, z + 1)
		for delt in range(14, 19):
			cur = node.Node(x + delt, y + 4, z + 1)
			if self._check_valid(x + delt, y + 4, z + 1, cur):
				self.matrix[x + delt][y + 4][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 18, y + 5, z + 1) -> (x + 22, y + 5, z + 1)
		for delt in range(18, 23):
			cur = node.Node(x + delt, y + 5, z + 1)
			if self._check_valid(x + delt, y + 5, z + 1, cur):
				self.matrix[x + delt][y + 5][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 22, y + 5, z + 2)
		for delt in range(22, 23):
			cur = node.Node(x + delt, y + 5, z + 2)
			if self._check_valid(x + delt, y + 5, z + 2, cur):
				self.matrix[x + delt][y + 5][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 22, y + 6, z + 2) -> (x + 25, y + 6, z + 2)
		for delt in range(22, 26):
			cur = node.Node(x + delt, y + 6, z + 2)
			if self._check_valid(x + delt, y + 6, z + 2, cur):
				self.matrix[x + delt][y + 6][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 25, y + 7, z + 2) -> (x + 29, y + 7, z + 2)
		for delt in range(25, 30):
			cur = node.Node(x + delt, y + 7, z + 2)
			if self._check_valid(x + delt, y + 7, z + 2, cur):
				self.matrix[x + delt][y + 7][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 29, y + 8, z + 2) -> (x + 33, y + 8, z + 2)
		for delt in range(29, 34):
			cur = node.Node(x + delt, y + 8, z + 2)
			if self._check_valid(x + delt, y + 8, z + 2, cur):
				self.matrix[x + delt][y + 8][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 33, y + 8, z + 3)
		for delt in range(33, 34):
			cur = node.Node(x + delt, y + 8, z + 3)
			if self._check_valid(x + delt, y + 8, z + 3, cur):
				self.matrix[x + delt][y + 8][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 33, y + 9, z + 3) -> (x + 37, y + 9, z + 3) 
		for delt in range(33, 38):
			cur = node.Node(x + delt, y + 9, z + 3)
			if self._check_valid(x + delt, y + 9, z + 3, cur):
				self.matrix[x + delt][y + 9][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 37, y + 10, z + 3) -> (x + 40, y + 10, z + 3) 
		for delt in range(37, 41):
			cur = node.Node(x + delt, y + 10, z + 3)
			if self._check_valid(x + delt, y + 10, z + 3, cur):
				self.matrix[x + delt][y + 10][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 40, y + 11, z + 3) -> (x + 44, y + 11, z + 3) 
		for delt in range(40, 45):
			cur = node.Node(x + delt, y + 11, z + 3)
			if self._check_valid(x + delt, y + 11, z + 3, cur):
				self.matrix[x + delt][y + 11][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 44, y + 11, z + 4) -> (x + 44, y + 11, z + 4) 
		for delt in range(44, 45):
			cur = node.Node(x + delt, y + 11, z + 4)
			if self._check_valid(x + delt, y + 11, z + 4, cur):
				self.matrix[x + delt][y + 11][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 44, y + 12, z + 4) -> (x + 48, y + 12, z + 4) 
		for delt in range(44, 49):
			cur = node.Node(x + delt, y + 12, z + 4)
			if self._check_valid(x + delt, y + 12, z + 4, cur):
				self.matrix[x + delt][y + 12][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 48, y + 13, z + 4) -> (x + 52, y + 13, z + 4) 
		for delt in range(48, 53):
			cur = node.Node(x + delt, y + 13, z + 4)
			if self._check_valid(x + delt, y + 13, z + 4, cur):
				self.matrix[x + delt][y + 13][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 52, y + 14, z + 4) -> (x + 56, y + 14, z + 4) 
		for delt in range(52, 57):
			cur = node.Node(x + delt, y + 14, z + 4)
			if self._check_valid(x + delt, y + 14, z + 4, cur):
				self.matrix[x + delt][y + 14][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 56, y + 14, z + 5) -> (x + 56, y + 14, z + 5) 
		for delt in range(56, 57):
			cur = node.Node(x + delt, y + 14, z + 5)
			if self._check_valid(x + delt, y + 14, z + 5, cur):
				self.matrix[x + delt][y + 14][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 56, y + 15, z + 5) -> (x + 59, y + 15, z + 5) 
		for delt in range(56, 60):
			cur = node.Node(x + delt, y + 15, z + 5)
			if self._check_valid(x + delt, y + 15, z + 5, cur):
				self.matrix[x + delt][y + 15][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 59, y + 16, z + 5) -> (x + 60, y + 16, z + 5) 
		for delt in range(59, 61):
			cur = node.Node(x + delt, y + 16, z + 5)
			if self._check_valid(x + delt, y + 16, z + 5, cur):
				self.matrix[x + delt][y + 16][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)


	def _case_2_4(self, x, y, z):

		# (x, y, z) -> (x + 4, y, z)
		for delt in range(5):
			cur = node.Node(x + delt, y, z)
			if self._check_valid(x + delt, y, z, cur):
				self.matrix[x + delt][y][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 4, y + 1, z) -> (x + 7, y + 1, z)
		for delt in range(4, 8):
			cur = node.Node(x + delt, y + 1, z)
			if self._check_valid(x + delt, y + 1, z, cur):
				self.matrix[x + delt][y + 1][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 7, y + 2, z) -> (x + 11, y + 2, z)
		for delt in range(7, 12):
			cur = node.Node(x + delt, y + 2, z)
			if self._check_valid(x + delt, y + 2, z, cur):
				self.matrix[x + delt][y + 2][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 11, y + 2, z + 1)
		for delt in range(11, 12):
			cur = node.Node(x + delt, y + 2, z + 1)
			if self._check_valid(x + delt, y + 2, z + 1, cur):
				self.matrix[x + delt][y + 2][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 11, y + 3, z + 1) -> (x + 14, y + 3, z + 1)
		for delt in range(11, 15):
			cur = node.Node(x + delt, y + 3, z + 1)
			if self._check_valid(x + delt, y + 3, z + 1, cur):
				self.matrix[x + delt][y + 3][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 14, y + 4, z + 1) -> (x + 18, y + 4, z + 1)
		for delt in range(14, 19):
			cur = node.Node(x + delt, y + 4, z + 1)
			if self._check_valid(x + delt, y + 4, z + 1, cur):
				self.matrix[x + delt][y + 4][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 18, y + 5, z + 1) -> (x + 22, y + 5, z + 1)
		for delt in range(18, 23):
			cur = node.Node(x + delt, y + 5, z + 1)
			if self._check_valid(x + delt, y + 5, z + 1, cur):
				self.matrix[x + delt][y + 5][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 22, y + 5, z + 2)
		for delt in range(22, 23):
			cur = node.Node(x + delt, y + 5, z + 2)
			if self._check_valid(x + delt, y + 5, z + 2, cur):
				self.matrix[x + delt][y + 5][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 22, y + 6, z + 2) -> (x + 25, y + 6, z + 2)
		for delt in range(22, 26):
			cur = node.Node(x + delt, y + 6, z + 2)
			if self._check_valid(x + delt, y + 6, z + 2, cur):
				self.matrix[x + delt][y + 6][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 25, y + 7, z + 2) -> (x + 29, y + 7, z + 2)
		for delt in range(25, 30):
			cur = node.Node(x + delt, y + 7, z + 2)
			if self._check_valid(x + delt, y + 7, z + 2, cur):
				self.matrix[x + delt][y + 7][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 29, y + 8, z + 2) -> (x + 33, y + 8, z + 2)
		for delt in range(29, 34):
			cur = node.Node(x + delt, y + 8, z + 2)
			if self._check_valid(x + delt, y + 8, z + 2, cur):
				self.matrix[x + delt][y + 8][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 33, y + 8, z + 3)
		for delt in range(33, 34):
			cur = node.Node(x + delt, y + 8, z + 3)
			if self._check_valid(x + delt, y + 8, z + 3, cur):
				self.matrix[x + delt][y + 8][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 33, y + 9, z + 3) -> (x + 37, y + 9, z + 3) 
		for delt in range(33, 38):
			cur = node.Node(x + delt, y + 9, z + 3)
			if self._check_valid(x + delt, y + 9, z + 3, cur):
				self.matrix[x + delt][y + 9][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 37, y + 10, z + 3) -> (x + 40, y + 10, z + 3) 
		for delt in range(37, 41):
			cur = node.Node(x + delt, y + 10, z + 3)
			if self._check_valid(x + delt, y + 10, z + 3, cur):
				self.matrix[x + delt][y + 10][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 40, y + 11, z + 3) -> (x + 44, y + 11, z + 3) 
		for delt in range(40, 45):
			cur = node.Node(x + delt, y + 11, z + 3)
			if self._check_valid(x + delt, y + 11, z + 3, cur):
				self.matrix[x + delt][y + 11][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 44, y + 11, z + 4) -> (x + 44, y + 11, z + 4) 
		for delt in range(44, 45):
			cur = node.Node(x + delt, y + 11, z + 4)
			if self._check_valid(x + delt, y + 11, z + 4, cur):
				self.matrix[x + delt][y + 11][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 44, y + 12, z + 4) -> (x + 48, y + 12, z + 4) 
		for delt in range(44, 49):
			cur = node.Node(x + delt, y + 12, z + 4)
			if self._check_valid(x + delt, y + 12, z + 4, cur):
				self.matrix[x + delt][y + 12][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 48, y + 13, z + 4) -> (x + 52, y + 13, z + 4) 
		for delt in range(48, 53):
			cur = node.Node(x + delt, y + 13, z + 4)
			if self._check_valid(x + delt, y + 13, z + 4, cur):
				self.matrix[x + delt][y + 13][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 52, y + 14, z + 4) -> (x + 56, y + 14, z + 4) 
		for delt in range(52, 57):
			cur = node.Node(x + delt, y + 14, z + 4)
			if self._check_valid(x + delt, y + 14, z + 4, cur):
				self.matrix[x + delt][y + 14][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 56, y + 14, z + 5) -> (x + 56, y + 14, z + 5) 
		for delt in range(56, 57):
			cur = node.Node(x + delt, y + 14, z + 5)
			if self._check_valid(x + delt, y + 14, z + 5, cur):
				self.matrix[x + delt][y + 14][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 56, y + 15, z + 5) -> (x + 59, y + 15, z + 5) 
		for delt in range(56, 60):
			cur = node.Node(x + delt, y + 15, z + 5)
			if self._check_valid(x + delt, y + 15, z + 5, cur):
				self.matrix[x + delt][y + 15][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 59, y + 16, z + 5) -> (x + 63, y + 16, z + 5) 
		for delt in range(59, 64):
			cur = node.Node(x + delt, y + 16, z + 5)
			if self._check_valid(x + delt, y + 16, z + 5, cur):
				self.matrix[x + delt][y + 16][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 63, y + 17, z + 5) -> (x + 67, y + 17, z + 5) 
		for delt in range(63, 68):
			cur = node.Node(x + delt, y + 17, z + 5)
			if self._check_valid(x + delt, y + 17, z + 5, cur):
				self.matrix[x + delt][y + 17][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 67, y + 17, z + 6) -> (x + 67, y + 17, z + 6) 
		for delt in range(67, 68):
			cur = node.Node(x + delt, y + 17, z + 6)
			if self._check_valid(x + delt, y + 17, z + 6, cur):
				self.matrix[x + delt][y + 17][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 67, y + 18, z + 6) -> (x + 70, y + 18, z + 6) 
		for delt in range(67, 71):
			cur = node.Node(x + delt, y + 18, z + 6)
			if self._check_valid(x + delt, y + 18, z + 6, cur):
				self.matrix[x + delt][y + 18][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 70, y + 19, z + 6) -> (x + 74, y + 19, z + 6) 
		for delt in range(70, 75):
			cur = node.Node(x + delt, y + 19, z + 6)
			if self._check_valid(x + delt, y + 19, z + 6, cur):
				self.matrix[x + delt][y + 19][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 74, y + 20, z + 6) -> (x + 78, y + 20, z + 6) 
		for delt in range(74, 79):
			cur = node.Node(x + delt, y + 20, z + 6)
			if self._check_valid(x + delt, y + 20, z + 6, cur):
				self.matrix[x + delt][y + 20][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 78, y + 20, z + 7) -> (x + 78, y + 20, z + 7) 
		for delt in range(78, 79):
			cur = node.Node(x + delt, y + 20, z + 7)
			if self._check_valid(x + delt, y + 20, z + 7, cur):
				self.matrix[x + delt][y + 20][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)				

		# (x + 78, y + 21, z + 7) -> (x + 81 y + 21, z + 7) 
		for delt in range(78, 82):
			cur = node.Node(x + delt, y + 21, z + 7)
			if self._check_valid(x + delt, y + 21, z + 7, cur):
				self.matrix[x + delt][y + 21][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 81, y + 22, z + 7) -> (x + 85, y + 22, z + 7) 
		for delt in range(81, 86):
			cur = node.Node(x + delt, y + 22, z + 7)
			if self._check_valid(x + delt, y + 22, z + 7, cur):
				self.matrix[x + delt][y + 22][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 85, y + 23, z + 7) -> (x + 89, y + 23, z + 7) 
		for delt in range(85, 90):
			cur = node.Node(x + delt, y + 23, z + 7)
			if self._check_valid(x + delt, y + 23, z + 7, cur):
				self.matrix[x + delt][y + 23][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 89, y + 23, z + 8) -> (x + 89, y + 23, z + 8) 
		for delt in range(89, 90):
			cur = node.Node(x + delt, y + 23, z + 8)
			if self._check_valid(x + delt, y + 23, z + 8, cur):
				self.matrix[x + delt][y + 23][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)				

		# (x + 89, y + 24, z + 8) -> (x + 92 y + 24, z + 8) 
		for delt in range(89, 93):
			cur = node.Node(x + delt, y + 24, z + 8)
			if self._check_valid(x + delt, y + 24, z + 8, cur):
				self.matrix[x + delt][y + 24][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 92, y + 25, z + 8) -> (x + 96, y + 25, z + 8) 
		for delt in range(92, 97):
			cur = node.Node(x + delt, y + 25, z + 8)
			if self._check_valid(x + delt, y + 25, z + 8, cur):
				self.matrix[x + delt][y + 25][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 96, y + 26, z + 8) -> (x + 100, y + 26, z + 8) 
		for delt in range(96, 101):
			cur = node.Node(x + delt, y + 26, z + 8)
			if self._check_valid(x + delt, y + 26, z + 8, cur):
				self.matrix[x + delt][y + 26][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 100, y + 26, z + 9) -> (x + 100, y + 26, z + 9) 
		for delt in range(100, 101):
			cur = node.Node(x + delt, y + 26, z + 9)
			if self._check_valid(x + delt, y + 26, z + 9, cur):
				self.matrix[x + delt][y + 26][z + 9] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 100, y + 27, z + 9) -> (x + 100, y + 27, z + 9) 
		for delt in range(100, 101):
			cur = node.Node(x + delt, y + 27, z + 9)
			if self._check_valid(x + delt, y + 27, z + 9, cur):
				self.matrix[x + delt][y + 27][z + 9] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	


	def _case_2_5(self, x, y, z):

		# (x, y, z) -> (x + 4, y, z)
		for delt in range(5):
			cur = node.Node(x + delt, y, z)
			if self._check_valid(x + delt, y, z, cur):
				self.matrix[x + delt][y][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 4, y + 1, z) -> (x + 7, y + 1, z)
		for delt in range(4, 8):
			cur = node.Node(x + delt, y + 1, z)
			if self._check_valid(x + delt, y + 1, z, cur):
				self.matrix[x + delt][y + 1][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 7, y + 2, z) -> (x + 11, y + 2, z)
		for delt in range(7, 12):
			cur = node.Node(x + delt, y + 2, z)
			if self._check_valid(x + delt, y + 2, z, cur):
				self.matrix[x + delt][y + 2][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 11, y + 2, z + 1)
		for delt in range(11, 12):
			cur = node.Node(x + delt, y + 2, z + 1)
			if self._check_valid(x + delt, y + 2, z + 1, cur):
				self.matrix[x + delt][y + 2][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 11, y + 3, z + 1) -> (x + 14, y + 3, z + 1)
		for delt in range(11, 15):
			cur = node.Node(x + delt, y + 3, z + 1)
			if self._check_valid(x + delt, y + 3, z + 1, cur):
				self.matrix[x + delt][y + 3][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 14, y + 4, z + 1) -> (x + 18, y + 4, z + 1)
		for delt in range(14, 19):
			cur = node.Node(x + delt, y + 4, z + 1)
			if self._check_valid(x + delt, y + 4, z + 1, cur):
				self.matrix[x + delt][y + 4][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 18, y + 5, z + 1) -> (x + 22, y + 5, z + 1)
		for delt in range(18, 23):
			cur = node.Node(x + delt, y + 5, z + 1)
			if self._check_valid(x + delt, y + 5, z + 1, cur):
				self.matrix[x + delt][y + 5][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 22, y + 5, z + 2)
		for delt in range(22, 23):
			cur = node.Node(x + delt, y + 5, z + 2)
			if self._check_valid(x + delt, y + 5, z + 2, cur):
				self.matrix[x + delt][y + 5][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 22, y + 6, z + 2) -> (x + 25, y + 6, z + 2)
		for delt in range(22, 26):
			cur = node.Node(x + delt, y + 6, z + 2)
			if self._check_valid(x + delt, y + 6, z + 2, cur):
				self.matrix[x + delt][y + 6][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 25, y + 7, z + 2) -> (x + 29, y + 7, z + 2)
		for delt in range(25, 30):
			cur = node.Node(x + delt, y + 7, z + 2)
			if self._check_valid(x + delt, y + 7, z + 2, cur):
				self.matrix[x + delt][y + 7][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 29, y + 8, z + 2) -> (x + 33, y + 8, z + 2)
		for delt in range(29, 34):
			cur = node.Node(x + delt, y + 8, z + 2)
			if self._check_valid(x + delt, y + 8, z + 2, cur):
				self.matrix[x + delt][y + 8][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 33, y + 8, z + 3)
		for delt in range(33, 34):
			cur = node.Node(x + delt, y + 8, z + 3)
			if self._check_valid(x + delt, y + 8, z + 3, cur):
				self.matrix[x + delt][y + 8][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 33, y + 9, z + 3) -> (x + 37, y + 9, z + 3) 
		for delt in range(33, 38):
			cur = node.Node(x + delt, y + 9, z + 3)
			if self._check_valid(x + delt, y + 9, z + 3, cur):
				self.matrix[x + delt][y + 9][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 37, y + 10, z + 3) -> (x + 40, y + 10, z + 3) 
		for delt in range(37, 41):
			cur = node.Node(x + delt, y + 10, z + 3)
			if self._check_valid(x + delt, y + 10, z + 3, cur):
				self.matrix[x + delt][y + 10][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 40, y + 11, z + 3) -> (x + 44, y + 11, z + 3) 
		for delt in range(40, 45):
			cur = node.Node(x + delt, y + 11, z + 3)
			if self._check_valid(x + delt, y + 11, z + 3, cur):
				self.matrix[x + delt][y + 11][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 44, y + 11, z + 4) -> (x + 44, y + 11, z + 4) 
		for delt in range(44, 45):
			cur = node.Node(x + delt, y + 11, z + 4)
			if self._check_valid(x + delt, y + 11, z + 4, cur):
				self.matrix[x + delt][y + 11][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 44, y + 12, z + 4) -> (x + 48, y + 12, z + 4) 
		for delt in range(44, 49):
			cur = node.Node(x + delt, y + 12, z + 4)
			if self._check_valid(x + delt, y + 12, z + 4, cur):
				self.matrix[x + delt][y + 12][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 48, y + 13, z + 4) -> (x + 52, y + 13, z + 4) 
		for delt in range(48, 53):
			cur = node.Node(x + delt, y + 13, z + 4)
			if self._check_valid(x + delt, y + 13, z + 4, cur):
				self.matrix[x + delt][y + 13][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 52, y + 14, z + 4) -> (x + 56, y + 14, z + 4) 
		for delt in range(52, 57):
			cur = node.Node(x + delt, y + 14, z + 4)
			if self._check_valid(x + delt, y + 14, z + 4, cur):
				self.matrix[x + delt][y + 14][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 56, y + 14, z + 5) -> (x + 56, y + 14, z + 5) 
		for delt in range(56, 57):
			cur = node.Node(x + delt, y + 14, z + 5)
			if self._check_valid(x + delt, y + 14, z + 5, cur):
				self.matrix[x + delt][y + 14][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 56, y + 15, z + 5) -> (x + 59, y + 15, z + 5) 
		for delt in range(56, 60):
			cur = node.Node(x + delt, y + 15, z + 5)
			if self._check_valid(x + delt, y + 15, z + 5, cur):
				self.matrix[x + delt][y + 15][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 59, y + 16, z + 5) -> (x + 63, y + 16, z + 5) 
		for delt in range(59, 64):
			cur = node.Node(x + delt, y + 16, z + 5)
			if self._check_valid(x + delt, y + 16, z + 5, cur):
				self.matrix[x + delt][y + 16][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 63, y + 17, z + 5) -> (x + 67, y + 17, z + 5) 
		for delt in range(63, 68):
			cur = node.Node(x + delt, y + 17, z + 5)
			if self._check_valid(x + delt, y + 17, z + 5, cur):
				self.matrix[x + delt][y + 17][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 67, y + 17, z + 6) -> (x + 67, y + 17, z + 6) 
		for delt in range(67, 68):
			cur = node.Node(x + delt, y + 17, z + 6)
			if self._check_valid(x + delt, y + 17, z + 6, cur):
				self.matrix[x + delt][y + 17][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 67, y + 18, z + 6) -> (x + 70, y + 18, z + 6) 
		for delt in range(67, 71):
			cur = node.Node(x + delt, y + 18, z + 6)
			if self._check_valid(x + delt, y + 18, z + 6, cur):
				self.matrix[x + delt][y + 18][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 70, y + 19, z + 6) -> (x + 74, y + 19, z + 6) 
		for delt in range(70, 75):
			cur = node.Node(x + delt, y + 19, z + 6)
			if self._check_valid(x + delt, y + 19, z + 6, cur):
				self.matrix[x + delt][y + 19][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 74, y + 20, z + 6) -> (x + 78, y + 20, z + 6) 
		for delt in range(74, 79):
			cur = node.Node(x + delt, y + 20, z + 6)
			if self._check_valid(x + delt, y + 20, z + 6, cur):
				self.matrix[x + delt][y + 20][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 78, y + 20, z + 7) -> (x + 78, y + 20, z + 7) 
		for delt in range(78, 79):
			cur = node.Node(x + delt, y + 20, z + 7)
			if self._check_valid(x + delt, y + 20, z + 7, cur):
				self.matrix[x + delt][y + 20][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)				

		# (x + 78, y + 21, z + 7) -> (x + 81 y + 21, z + 7) 
		for delt in range(78, 82):
			cur = node.Node(x + delt, y + 21, z + 7)
			if self._check_valid(x + delt, y + 21, z + 7, cur):
				self.matrix[x + delt][y + 21][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 81, y + 22, z + 7) -> (x + 85, y + 22, z + 7) 
		for delt in range(81, 86):
			cur = node.Node(x + delt, y + 22, z + 7)
			if self._check_valid(x + delt, y + 22, z + 7, cur):
				self.matrix[x + delt][y + 22][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 85, y + 23, z + 7) -> (x + 89, y + 23, z + 7) 
		for delt in range(85, 90):
			cur = node.Node(x + delt, y + 23, z + 7)
			if self._check_valid(x + delt, y + 23, z + 7, cur):
				self.matrix[x + delt][y + 23][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 89, y + 23, z + 8) -> (x + 89, y + 23, z + 8) 
		for delt in range(89, 90):
			cur = node.Node(x + delt, y + 23, z + 8)
			if self._check_valid(x + delt, y + 23, z + 8, cur):
				self.matrix[x + delt][y + 23][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)				

		# (x + 89, y + 24, z + 8) -> (x + 92 y + 24, z + 8) 
		for delt in range(89, 93):
			cur = node.Node(x + delt, y + 24, z + 8)
			if self._check_valid(x + delt, y + 24, z + 8, cur):
				self.matrix[x + delt][y + 24][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 92, y + 25, z + 8) -> (x + 96, y + 25, z + 8) 
		for delt in range(92, 97):
			cur = node.Node(x + delt, y + 25, z + 8)
			if self._check_valid(x + delt, y + 25, z + 8, cur):
				self.matrix[x + delt][y + 25][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 96, y + 26, z + 8) -> (x + 100, y + 26, z + 8) 
		for delt in range(96, 101):
			cur = node.Node(x + delt, y + 26, z + 8)
			if self._check_valid(x + delt, y + 26, z + 8, cur):
				self.matrix[x + delt][y + 26][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 100, y + 26, z + 9) -> (x + 100, y + 26, z + 9) 
		for delt in range(100, 101):
			cur = node.Node(x + delt, y + 26, z + 9)
			if self._check_valid(x + delt, y + 26, z + 9, cur):
				self.matrix[x + delt][y + 26][z + 9] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 100, y + 27, z + 9) -> (x + 104, y + 27, z + 9) 
		for delt in range(100, 105):
			cur = node.Node(x + delt, y + 27, z + 9)
			if self._check_valid(x + delt, y + 27, z + 9, cur):
				self.matrix[x + delt][y + 27][z + 9] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 104, y + 28, z + 9) -> (x + 108, y + 28, z + 9) 
		for delt in range(104, 109):
			cur = node.Node(x + delt, y + 28, z + 9)
			if self._check_valid(x + delt, y + 28, z + 9, cur):
				self.matrix[x + delt][y + 28][z + 9] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 108, y + 29, z + 9) -> (x + 112, y + 29, z + 9) 
		for delt in range(108, 113):
			cur = node.Node(x + delt, y + 29, z + 9)
			if self._check_valid(x + delt, y + 29, z + 9, cur):
				self.matrix[x + delt][y + 29][z + 9] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 112, y + 29, z + 10) -> (x + 112, y + 29, z + 10) 
		for delt in range(112, 113):
			cur = node.Node(x + delt, y + 29, z + 10)
			if self._check_valid(x + delt, y + 29, z + 10, cur):
				self.matrix[x + delt][y + 29][z + 10] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 112, y + 30, z + 10) -> (x + 115, y + 30, z + 10) 
		for delt in range(112, 116):
			cur = node.Node(x + delt, y + 30, z + 10)
			if self._check_valid(x + delt, y + 30, z + 10, cur):
				self.matrix[x + delt][y + 30][z + 10] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 115, y + 31, z + 10) -> (x + 119, y + 31, z + 10) 
		for delt in range(115, 120):
			cur = node.Node(x + delt, y + 31, z + 10)
			if self._check_valid(x + delt, y + 31, z + 10, cur):
				self.matrix[x + delt][y + 31][z + 10] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	


	def _case_2_6(self, x, y, z):

		# (x, y, z) -> (x + 4, y, z)
		for delt in range(5):
			cur = node.Node(x + delt, y, z)
			if self._check_valid(x + delt, y, z, cur):
				self.matrix[x + delt][y][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 4, y + 1, z) -> (x + 7, y + 1, z)
		for delt in range(4, 8):
			cur = node.Node(x + delt, y + 1, z)
			if self._check_valid(x + delt, y + 1, z, cur):
				self.matrix[x + delt][y + 1][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 7, y + 2, z) -> (x + 11, y + 2, z)
		for delt in range(7, 12):
			cur = node.Node(x + delt, y + 2, z)
			if self._check_valid(x + delt, y + 2, z, cur):
				self.matrix[x + delt][y + 2][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 11, y + 2, z + 1)
		for delt in range(11, 12):
			cur = node.Node(x + delt, y + 2, z + 1)
			if self._check_valid(x + delt, y + 2, z + 1, cur):
				self.matrix[x + delt][y + 2][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 11, y + 3, z + 1) -> (x + 14, y + 3, z + 1)
		for delt in range(11, 15):
			cur = node.Node(x + delt, y + 3, z + 1)
			if self._check_valid(x + delt, y + 3, z + 1, cur):
				self.matrix[x + delt][y + 3][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 14, y + 4, z + 1) -> (x + 18, y + 4, z + 1)
		for delt in range(14, 19):
			cur = node.Node(x + delt, y + 4, z + 1)
			if self._check_valid(x + delt, y + 4, z + 1, cur):
				self.matrix[x + delt][y + 4][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 18, y + 5, z + 1) -> (x + 22, y + 5, z + 1)
		for delt in range(18, 23):
			cur = node.Node(x + delt, y + 5, z + 1)
			if self._check_valid(x + delt, y + 5, z + 1, cur):
				self.matrix[x + delt][y + 5][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 22, y + 5, z + 2)
		for delt in range(22, 23):
			cur = node.Node(x + delt, y + 5, z + 2)
			if self._check_valid(x + delt, y + 5, z + 2, cur):
				self.matrix[x + delt][y + 5][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 22, y + 6, z + 2) -> (x + 25, y + 6, z + 2)
		for delt in range(22, 26):
			cur = node.Node(x + delt, y + 6, z + 2)
			if self._check_valid(x + delt, y + 6, z + 2, cur):
				self.matrix[x + delt][y + 6][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 25, y + 7, z + 2) -> (x + 29, y + 7, z + 2)
		for delt in range(25, 30):
			cur = node.Node(x + delt, y + 7, z + 2)
			if self._check_valid(x + delt, y + 7, z + 2, cur):
				self.matrix[x + delt][y + 7][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 29, y + 8, z + 2) -> (x + 33, y + 8, z + 2)
		for delt in range(29, 34):
			cur = node.Node(x + delt, y + 8, z + 2)
			if self._check_valid(x + delt, y + 8, z + 2, cur):
				self.matrix[x + delt][y + 8][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 33, y + 8, z + 3)
		for delt in range(33, 34):
			cur = node.Node(x + delt, y + 8, z + 3)
			if self._check_valid(x + delt, y + 8, z + 3, cur):
				self.matrix[x + delt][y + 8][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 33, y + 9, z + 3) -> (x + 37, y + 9, z + 3) 
		for delt in range(33, 38):
			cur = node.Node(x + delt, y + 9, z + 3)
			if self._check_valid(x + delt, y + 9, z + 3, cur):
				self.matrix[x + delt][y + 9][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 37, y + 10, z + 3) -> (x + 40, y + 10, z + 3) 
		for delt in range(37, 41):
			cur = node.Node(x + delt, y + 10, z + 3)
			if self._check_valid(x + delt, y + 10, z + 3, cur):
				self.matrix[x + delt][y + 10][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 40, y + 11, z + 3) -> (x + 44, y + 11, z + 3) 
		for delt in range(40, 45):
			cur = node.Node(x + delt, y + 11, z + 3)
			if self._check_valid(x + delt, y + 11, z + 3, cur):
				self.matrix[x + delt][y + 11][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 44, y + 11, z + 4) -> (x + 44, y + 11, z + 4) 
		for delt in range(44, 45):
			cur = node.Node(x + delt, y + 11, z + 4)
			if self._check_valid(x + delt, y + 11, z + 4, cur):
				self.matrix[x + delt][y + 11][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 44, y + 12, z + 4) -> (x + 48, y + 12, z + 4) 
		for delt in range(44, 49):
			cur = node.Node(x + delt, y + 12, z + 4)
			if self._check_valid(x + delt, y + 12, z + 4, cur):
				self.matrix[x + delt][y + 12][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 48, y + 13, z + 4) -> (x + 52, y + 13, z + 4) 
		for delt in range(48, 53):
			cur = node.Node(x + delt, y + 13, z + 4)
			if self._check_valid(x + delt, y + 13, z + 4, cur):
				self.matrix[x + delt][y + 13][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 52, y + 14, z + 4) -> (x + 56, y + 14, z + 4) 
		for delt in range(52, 57):
			cur = node.Node(x + delt, y + 14, z + 4)
			if self._check_valid(x + delt, y + 14, z + 4, cur):
				self.matrix[x + delt][y + 14][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 56, y + 14, z + 5) -> (x + 56, y + 14, z + 5) 
		for delt in range(56, 57):
			cur = node.Node(x + delt, y + 14, z + 5)
			if self._check_valid(x + delt, y + 14, z + 5, cur):
				self.matrix[x + delt][y + 14][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 56, y + 15, z + 5) -> (x + 59, y + 15, z + 5) 
		for delt in range(56, 60):
			cur = node.Node(x + delt, y + 15, z + 5)
			if self._check_valid(x + delt, y + 15, z + 5, cur):
				self.matrix[x + delt][y + 15][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 59, y + 16, z + 5) -> (x + 63, y + 16, z + 5) 
		for delt in range(59, 64):
			cur = node.Node(x + delt, y + 16, z + 5)
			if self._check_valid(x + delt, y + 16, z + 5, cur):
				self.matrix[x + delt][y + 16][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 63, y + 17, z + 5) -> (x + 67, y + 17, z + 5) 
		for delt in range(63, 68):
			cur = node.Node(x + delt, y + 17, z + 5)
			if self._check_valid(x + delt, y + 17, z + 5, cur):
				self.matrix[x + delt][y + 17][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 67, y + 17, z + 6) -> (x + 67, y + 17, z + 6) 
		for delt in range(67, 68):
			cur = node.Node(x + delt, y + 17, z + 6)
			if self._check_valid(x + delt, y + 17, z + 6, cur):
				self.matrix[x + delt][y + 17][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 67, y + 18, z + 6) -> (x + 70, y + 18, z + 6) 
		for delt in range(67, 71):
			cur = node.Node(x + delt, y + 18, z + 6)
			if self._check_valid(x + delt, y + 18, z + 6, cur):
				self.matrix[x + delt][y + 18][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 70, y + 19, z + 6) -> (x + 74, y + 19, z + 6) 
		for delt in range(70, 75):
			cur = node.Node(x + delt, y + 19, z + 6)
			if self._check_valid(x + delt, y + 19, z + 6, cur):
				self.matrix[x + delt][y + 19][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 74, y + 20, z + 6) -> (x + 78, y + 20, z + 6) 
		for delt in range(74, 79):
			cur = node.Node(x + delt, y + 20, z + 6)
			if self._check_valid(x + delt, y + 20, z + 6, cur):
				self.matrix[x + delt][y + 20][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 78, y + 20, z + 7) -> (x + 78, y + 20, z + 7) 
		for delt in range(78, 79):
			cur = node.Node(x + delt, y + 20, z + 7)
			if self._check_valid(x + delt, y + 20, z + 7, cur):
				self.matrix[x + delt][y + 20][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)				

		# (x + 78, y + 21, z + 7) -> (x + 81 y + 21, z + 7) 
		for delt in range(78, 82):
			cur = node.Node(x + delt, y + 21, z + 7)
			if self._check_valid(x + delt, y + 21, z + 7, cur):
				self.matrix[x + delt][y + 21][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 81, y + 22, z + 7) -> (x + 85, y + 22, z + 7) 
		for delt in range(81, 86):
			cur = node.Node(x + delt, y + 22, z + 7)
			if self._check_valid(x + delt, y + 22, z + 7, cur):
				self.matrix[x + delt][y + 22][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 85, y + 23, z + 7) -> (x + 89, y + 23, z + 7) 
		for delt in range(85, 90):
			cur = node.Node(x + delt, y + 23, z + 7)
			if self._check_valid(x + delt, y + 23, z + 7, cur):
				self.matrix[x + delt][y + 23][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 89, y + 23, z + 8) -> (x + 89, y + 23, z + 8) 
		for delt in range(89, 90):
			cur = node.Node(x + delt, y + 23, z + 8)
			if self._check_valid(x + delt, y + 23, z + 8, cur):
				self.matrix[x + delt][y + 23][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)				

		# (x + 89, y + 24, z + 8) -> (x + 92 y + 24, z + 8) 
		for delt in range(89, 93):
			cur = node.Node(x + delt, y + 24, z + 8)
			if self._check_valid(x + delt, y + 24, z + 8, cur):
				self.matrix[x + delt][y + 24][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 92, y + 25, z + 8) -> (x + 96, y + 25, z + 8) 
		for delt in range(92, 97):
			cur = node.Node(x + delt, y + 25, z + 8)
			if self._check_valid(x + delt, y + 25, z + 8, cur):
				self.matrix[x + delt][y + 25][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 96, y + 26, z + 8) -> (x + 100, y + 26, z + 8) 
		for delt in range(96, 101):
			cur = node.Node(x + delt, y + 26, z + 8)
			if self._check_valid(x + delt, y + 26, z + 8, cur):
				self.matrix[x + delt][y + 26][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 100, y + 26, z + 9) -> (x + 100, y + 26, z + 9) 
		for delt in range(100, 101):
			cur = node.Node(x + delt, y + 26, z + 9)
			if self._check_valid(x + delt, y + 26, z + 9, cur):
				self.matrix[x + delt][y + 26][z + 9] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 100, y + 27, z + 9) -> (x + 104, y + 27, z + 9) 
		for delt in range(100, 105):
			cur = node.Node(x + delt, y + 27, z + 9)
			if self._check_valid(x + delt, y + 27, z + 9, cur):
				self.matrix[x + delt][y + 27][z + 9] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 104, y + 28, z + 9) -> (x + 108, y + 28, z + 9) 
		for delt in range(104, 109):
			cur = node.Node(x + delt, y + 28, z + 9)
			if self._check_valid(x + delt, y + 28, z + 9, cur):
				self.matrix[x + delt][y + 28][z + 9] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 108, y + 29, z + 9) -> (x + 112, y + 29, z + 9) 
		for delt in range(108, 113):
			cur = node.Node(x + delt, y + 29, z + 9)
			if self._check_valid(x + delt, y + 29, z + 9, cur):
				self.matrix[x + delt][y + 29][z + 9] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 112, y + 29, z + 10) -> (x + 112, y + 29, z + 10) 
		for delt in range(112, 113):
			cur = node.Node(x + delt, y + 29, z + 10)
			if self._check_valid(x + delt, y + 29, z + 10, cur):
				self.matrix[x + delt][y + 29][z + 10] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 112, y + 30, z + 10) -> (x + 115, y + 30, z + 10) 
		for delt in range(112, 116):
			cur = node.Node(x + delt, y + 30, z + 10)
			if self._check_valid(x + delt, y + 30, z + 10, cur):
				self.matrix[x + delt][y + 30][z + 10] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 115, y + 31, z + 10) -> (x + 119, y + 31, z + 10) 
		for delt in range(115, 120):
			cur = node.Node(x + delt, y + 31, z + 10)
			if self._check_valid(x + delt, y + 31, z + 10, cur):
				self.matrix[x + delt][y + 31][z + 10] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 119, y + 32, z + 10) -> (x + 123, y + 32, z + 10) 
		for delt in range(119, 124):
			cur = node.Node(x + delt, y + 32, z + 10)
			if self._check_valid(x + delt, y + 32, z + 10, cur):
				self.matrix[x + delt][y + 32][z + 10] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 123, y + 32, z + 11) -> (x + 123, y + 32, z + 11) 
		for delt in range(123, 124):
			cur = node.Node(x + delt, y + 32, z + 11)
			if self._check_valid(x + delt, y + 32, z + 11, cur):
				self.matrix[x + delt][y + 32][z + 11] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 123, y + 33, z + 11) -> (x + 126, y + 33, z + 11) 
		for delt in range(123, 127):
			cur = node.Node(x + delt, y + 33, z + 11)
			if self._check_valid(x + delt, y + 33, z + 11, cur):
				self.matrix[x + delt][y + 33][z + 11] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 126, y + 34, z + 11) -> (x + 130, y + 34, z + 11) 
		for delt in range(126, 131):
			cur = node.Node(x + delt, y + 34, z + 11)
			if self._check_valid(x + delt, y + 34, z + 11, cur):
				self.matrix[x + delt][y + 34][z + 11] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 130, y + 35, z + 11) -> (x + 134, y + 35, z + 11) 
		for delt in range(130, 135):
			cur = node.Node(x + delt, y + 35, z + 11)
			if self._check_valid(x + delt, y + 35, z + 11, cur):
				self.matrix[x + delt][y + 35][z + 11] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 134, y + 35, z + 12) -> (x + 134, y + 35, z + 12) 
		for delt in range(134, 135):
			cur = node.Node(x + delt, y + 35, z + 12)
			if self._check_valid(x + delt, y + 35, z + 12, cur):
				self.matrix[x + delt][y + 35][z + 12] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 134, y + 36, z + 12) -> (x + 137, y + 36, z + 12) 
		for delt in range(134, 138):
			cur = node.Node(x + delt, y + 36, z + 12)
			if self._check_valid(x + delt, y + 36, z + 12, cur):
				self.matrix[x + delt][y + 36][z + 12] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 137, y + 37, z + 12) -> (x + 140, y + 37, z + 12) 
		for delt in range(137, 141):
			cur = node.Node(x + delt, y + 37, z + 12)
			if self._check_valid(x + delt, y + 37, z + 12, cur):
				self.matrix[x + delt][y + 37][z + 12] = DataGenerator._selected
				self.fill_set_ponts.add(cur)


	def _case_2_7(self, x, y, z):

		# (x, y, z) -> (x + 4, y, z)
		for delt in range(5):
			cur = node.Node(x + delt, y, z)
			if self._check_valid(x + delt, y, z, cur):
				self.matrix[x + delt][y][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 4, y + 1, z) -> (x + 7, y + 1, z)
		for delt in range(4, 8):
			cur = node.Node(x + delt, y + 1, z)
			if self._check_valid(x + delt, y + 1, z, cur):
				self.matrix[x + delt][y + 1][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 7, y + 2, z) -> (x + 11, y + 2, z)
		for delt in range(7, 12):
			cur = node.Node(x + delt, y + 2, z)
			if self._check_valid(x + delt, y + 2, z, cur):
				self.matrix[x + delt][y + 2][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 11, y + 2, z + 1)
		for delt in range(11, 12):
			cur = node.Node(x + delt, y + 2, z + 1)
			if self._check_valid(x + delt, y + 2, z + 1, cur):
				self.matrix[x + delt][y + 2][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 11, y + 3, z + 1) -> (x + 14, y + 3, z + 1)
		for delt in range(11, 15):
			cur = node.Node(x + delt, y + 3, z + 1)
			if self._check_valid(x + delt, y + 3, z + 1, cur):
				self.matrix[x + delt][y + 3][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 14, y + 4, z + 1) -> (x + 18, y + 4, z + 1)
		for delt in range(14, 19):
			cur = node.Node(x + delt, y + 4, z + 1)
			if self._check_valid(x + delt, y + 4, z + 1, cur):
				self.matrix[x + delt][y + 4][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 18, y + 5, z + 1) -> (x + 22, y + 5, z + 1)
		for delt in range(18, 23):
			cur = node.Node(x + delt, y + 5, z + 1)
			if self._check_valid(x + delt, y + 5, z + 1, cur):
				self.matrix[x + delt][y + 5][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 22, y + 5, z + 2)
		for delt in range(22, 23):
			cur = node.Node(x + delt, y + 5, z + 2)
			if self._check_valid(x + delt, y + 5, z + 2, cur):
				self.matrix[x + delt][y + 5][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 22, y + 6, z + 2) -> (x + 25, y + 6, z + 2)
		for delt in range(22, 26):
			cur = node.Node(x + delt, y + 6, z + 2)
			if self._check_valid(x + delt, y + 6, z + 2, cur):
				self.matrix[x + delt][y + 6][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 25, y + 7, z + 2) -> (x + 29, y + 7, z + 2)
		for delt in range(25, 30):
			cur = node.Node(x + delt, y + 7, z + 2)
			if self._check_valid(x + delt, y + 7, z + 2, cur):
				self.matrix[x + delt][y + 7][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 29, y + 8, z + 2) -> (x + 33, y + 8, z + 2)
		for delt in range(29, 34):
			cur = node.Node(x + delt, y + 8, z + 2)
			if self._check_valid(x + delt, y + 8, z + 2, cur):
				self.matrix[x + delt][y + 8][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 33, y + 8, z + 3)
		for delt in range(33, 34):
			cur = node.Node(x + delt, y + 8, z + 3)
			if self._check_valid(x + delt, y + 8, z + 3, cur):
				self.matrix[x + delt][y + 8][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 33, y + 9, z + 3) -> (x + 37, y + 9, z + 3) 
		for delt in range(33, 38):
			cur = node.Node(x + delt, y + 9, z + 3)
			if self._check_valid(x + delt, y + 9, z + 3, cur):
				self.matrix[x + delt][y + 9][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 37, y + 10, z + 3) -> (x + 40, y + 10, z + 3) 
		for delt in range(37, 41):
			cur = node.Node(x + delt, y + 10, z + 3)
			if self._check_valid(x + delt, y + 10, z + 3, cur):
				self.matrix[x + delt][y + 10][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 40, y + 11, z + 3) -> (x + 44, y + 11, z + 3) 
		for delt in range(40, 45):
			cur = node.Node(x + delt, y + 11, z + 3)
			if self._check_valid(x + delt, y + 11, z + 3, cur):
				self.matrix[x + delt][y + 11][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 44, y + 11, z + 4) -> (x + 44, y + 11, z + 4) 
		for delt in range(44, 45):
			cur = node.Node(x + delt, y + 11, z + 4)
			if self._check_valid(x + delt, y + 11, z + 4, cur):
				self.matrix[x + delt][y + 11][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 44, y + 12, z + 4) -> (x + 48, y + 12, z + 4) 
		for delt in range(44, 49):
			cur = node.Node(x + delt, y + 12, z + 4)
			if self._check_valid(x + delt, y + 12, z + 4, cur):
				self.matrix[x + delt][y + 12][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 48, y + 13, z + 4) -> (x + 52, y + 13, z + 4) 
		for delt in range(48, 53):
			cur = node.Node(x + delt, y + 13, z + 4)
			if self._check_valid(x + delt, y + 13, z + 4, cur):
				self.matrix[x + delt][y + 13][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 52, y + 14, z + 4) -> (x + 56, y + 14, z + 4) 
		for delt in range(52, 57):
			cur = node.Node(x + delt, y + 14, z + 4)
			if self._check_valid(x + delt, y + 14, z + 4, cur):
				self.matrix[x + delt][y + 14][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 56, y + 14, z + 5) -> (x + 56, y + 14, z + 5) 
		for delt in range(56, 57):
			cur = node.Node(x + delt, y + 14, z + 5)
			if self._check_valid(x + delt, y + 14, z + 5, cur):
				self.matrix[x + delt][y + 14][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 56, y + 15, z + 5) -> (x + 59, y + 15, z + 5) 
		for delt in range(56, 60):
			cur = node.Node(x + delt, y + 15, z + 5)
			if self._check_valid(x + delt, y + 15, z + 5, cur):
				self.matrix[x + delt][y + 15][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 59, y + 16, z + 5) -> (x + 63, y + 16, z + 5) 
		for delt in range(59, 64):
			cur = node.Node(x + delt, y + 16, z + 5)
			if self._check_valid(x + delt, y + 16, z + 5, cur):
				self.matrix[x + delt][y + 16][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 63, y + 17, z + 5) -> (x + 67, y + 17, z + 5) 
		for delt in range(63, 68):
			cur = node.Node(x + delt, y + 17, z + 5)
			if self._check_valid(x + delt, y + 17, z + 5, cur):
				self.matrix[x + delt][y + 17][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 67, y + 17, z + 6) -> (x + 67, y + 17, z + 6) 
		for delt in range(67, 68):
			cur = node.Node(x + delt, y + 17, z + 6)
			if self._check_valid(x + delt, y + 17, z + 6, cur):
				self.matrix[x + delt][y + 17][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 67, y + 18, z + 6) -> (x + 70, y + 18, z + 6) 
		for delt in range(67, 71):
			cur = node.Node(x + delt, y + 18, z + 6)
			if self._check_valid(x + delt, y + 18, z + 6, cur):
				self.matrix[x + delt][y + 18][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 70, y + 19, z + 6) -> (x + 74, y + 19, z + 6) 
		for delt in range(70, 75):
			cur = node.Node(x + delt, y + 19, z + 6)
			if self._check_valid(x + delt, y + 19, z + 6, cur):
				self.matrix[x + delt][y + 19][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 74, y + 20, z + 6) -> (x + 78, y + 20, z + 6) 
		for delt in range(74, 79):
			cur = node.Node(x + delt, y + 20, z + 6)
			if self._check_valid(x + delt, y + 20, z + 6, cur):
				self.matrix[x + delt][y + 20][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 78, y + 20, z + 7) -> (x + 78, y + 20, z + 7) 
		for delt in range(78, 79):
			cur = node.Node(x + delt, y + 20, z + 7)
			if self._check_valid(x + delt, y + 20, z + 7, cur):
				self.matrix[x + delt][y + 20][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)				

		# (x + 78, y + 21, z + 7) -> (x + 81 y + 21, z + 7) 
		for delt in range(78, 82):
			cur = node.Node(x + delt, y + 21, z + 7)
			if self._check_valid(x + delt, y + 21, z + 7, cur):
				self.matrix[x + delt][y + 21][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 81, y + 22, z + 7) -> (x + 85, y + 22, z + 7) 
		for delt in range(81, 86):
			cur = node.Node(x + delt, y + 22, z + 7)
			if self._check_valid(x + delt, y + 22, z + 7, cur):
				self.matrix[x + delt][y + 22][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 85, y + 23, z + 7) -> (x + 89, y + 23, z + 7) 
		for delt in range(85, 90):
			cur = node.Node(x + delt, y + 23, z + 7)
			if self._check_valid(x + delt, y + 23, z + 7, cur):
				self.matrix[x + delt][y + 23][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 89, y + 23, z + 8) -> (x + 89, y + 23, z + 8) 
		for delt in range(89, 90):
			cur = node.Node(x + delt, y + 23, z + 8)
			if self._check_valid(x + delt, y + 23, z + 8, cur):
				self.matrix[x + delt][y + 23][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)				

		# (x + 89, y + 24, z + 8) -> (x + 92 y + 24, z + 8) 
		for delt in range(89, 93):
			cur = node.Node(x + delt, y + 24, z + 8)
			if self._check_valid(x + delt, y + 24, z + 8, cur):
				self.matrix[x + delt][y + 24][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 92, y + 25, z + 8) -> (x + 96, y + 25, z + 8) 
		for delt in range(92, 97):
			cur = node.Node(x + delt, y + 25, z + 8)
			if self._check_valid(x + delt, y + 25, z + 8, cur):
				self.matrix[x + delt][y + 25][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 96, y + 26, z + 8) -> (x + 100, y + 26, z + 8) 
		for delt in range(96, 101):
			cur = node.Node(x + delt, y + 26, z + 8)
			if self._check_valid(x + delt, y + 26, z + 8, cur):
				self.matrix[x + delt][y + 26][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 100, y + 26, z + 9) -> (x + 100, y + 26, z + 9) 
		for delt in range(100, 101):
			cur = node.Node(x + delt, y + 26, z + 9)
			if self._check_valid(x + delt, y + 26, z + 9, cur):
				self.matrix[x + delt][y + 26][z + 9] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 100, y + 27, z + 9) -> (x + 104, y + 27, z + 9) 
		for delt in range(100, 105):
			cur = node.Node(x + delt, y + 27, z + 9)
			if self._check_valid(x + delt, y + 27, z + 9, cur):
				self.matrix[x + delt][y + 27][z + 9] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 104, y + 28, z + 9) -> (x + 108, y + 28, z + 9) 
		for delt in range(104, 109):
			cur = node.Node(x + delt, y + 28, z + 9)
			if self._check_valid(x + delt, y + 28, z + 9, cur):
				self.matrix[x + delt][y + 28][z + 9] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 108, y + 29, z + 9) -> (x + 112, y + 29, z + 9) 
		for delt in range(108, 113):
			cur = node.Node(x + delt, y + 29, z + 9)
			if self._check_valid(x + delt, y + 29, z + 9, cur):
				self.matrix[x + delt][y + 29][z + 9] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 112, y + 29, z + 10) -> (x + 112, y + 29, z + 10) 
		for delt in range(112, 113):
			cur = node.Node(x + delt, y + 29, z + 10)
			if self._check_valid(x + delt, y + 29, z + 10, cur):
				self.matrix[x + delt][y + 29][z + 10] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 112, y + 30, z + 10) -> (x + 115, y + 30, z + 10) 
		for delt in range(112, 116):
			cur = node.Node(x + delt, y + 30, z + 10)
			if self._check_valid(x + delt, y + 30, z + 10, cur):
				self.matrix[x + delt][y + 30][z + 10] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 115, y + 31, z + 10) -> (x + 119, y + 31, z + 10) 
		for delt in range(115, 120):
			cur = node.Node(x + delt, y + 31, z + 10)
			if self._check_valid(x + delt, y + 31, z + 10, cur):
				self.matrix[x + delt][y + 31][z + 10] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 119, y + 32, z + 10) -> (x + 123, y + 32, z + 10) 
		for delt in range(119, 124):
			cur = node.Node(x + delt, y + 32, z + 10)
			if self._check_valid(x + delt, y + 32, z + 10, cur):
				self.matrix[x + delt][y + 32][z + 10] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 123, y + 32, z + 11) -> (x + 123, y + 32, z + 11) 
		for delt in range(123, 124):
			cur = node.Node(x + delt, y + 32, z + 11)
			if self._check_valid(x + delt, y + 32, z + 11, cur):
				self.matrix[x + delt][y + 32][z + 11] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 123, y + 33, z + 11) -> (x + 126, y + 33, z + 11) 
		for delt in range(123, 127):
			cur = node.Node(x + delt, y + 33, z + 11)
			if self._check_valid(x + delt, y + 33, z + 11, cur):
				self.matrix[x + delt][y + 33][z + 11] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 126, y + 34, z + 11) -> (x + 130, y + 34, z + 11) 
		for delt in range(126, 131):
			cur = node.Node(x + delt, y + 34, z + 11)
			if self._check_valid(x + delt, y + 34, z + 11, cur):
				self.matrix[x + delt][y + 34][z + 11] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 130, y + 35, z + 11) -> (x + 134, y + 35, z + 11) 
		for delt in range(130, 135):
			cur = node.Node(x + delt, y + 35, z + 11)
			if self._check_valid(x + delt, y + 35, z + 11, cur):
				self.matrix[x + delt][y + 35][z + 11] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 134, y + 35, z + 12) -> (x + 134, y + 35, z + 12) 
		for delt in range(134, 135):
			cur = node.Node(x + delt, y + 35, z + 12)
			if self._check_valid(x + delt, y + 35, z + 12, cur):
				self.matrix[x + delt][y + 35][z + 12] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 134, y + 36, z + 12) -> (x + 137, y + 36, z + 12) 
		for delt in range(134, 138):
			cur = node.Node(x + delt, y + 36, z + 12)
			if self._check_valid(x + delt, y + 36, z + 12, cur):
				self.matrix[x + delt][y + 36][z + 12] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 137, y + 37, z + 12) -> (x + 141, y + 37, z + 12) 
		for delt in range(137, 142):
			cur = node.Node(x + delt, y + 37, z + 12)
			if self._check_valid(x + delt, y + 37, z + 12, cur):
				self.matrix[x + delt][y + 37][z + 12] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 141, y + 38, z + 12) -> (x + 145, y + 38, z + 12) 
		for delt in range(137, 146):
			cur = node.Node(x + delt, y + 38, z + 12)
			if self._check_valid(x + delt, y + 38, z + 12, cur):
				self.matrix[x + delt][y + 38][z + 12] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 145, y + 38, z + 13) -> (x + 145, y + 38, z + 13) 
		for delt in range(145, 146):
			cur = node.Node(x + delt, y + 38, z + 13)
			if self._check_valid(x + delt, y + 38, z + 13, cur):
				self.matrix[x + delt][y + 38][z + 13] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 145, y + 39, z + 13) -> (x + 148, y + 39, z + 13) 
		for delt in range(145, 149):
			cur = node.Node(x + delt, y + 39, z + 13)
			if self._check_valid(x + delt, y + 39, z + 13, cur):
				self.matrix[x + delt][y + 39][z + 13] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 148, y + 40, z + 13) -> (x + 152, y + 40, z + 13) 
		for delt in range(148, 153):
			cur = node.Node(x + delt, y + 40, z + 13)
			if self._check_valid(x + delt, y + 40, z + 13, cur):
				self.matrix[x + delt][y + 40][z + 13] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 152, y + 41, z + 13) -> (x + 156, y + 41, z + 13) 
		for delt in range(152, 157):
			cur = node.Node(x + delt, y + 41, z + 13)
			if self._check_valid(x + delt, y + 41, z + 13, cur):
				self.matrix[x + delt][y + 41][z + 13] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 156, y + 41, z + 14) -> (x + 156, y + 41, z + 14) 
		for delt in range(156, 157):
			cur = node.Node(x + delt, y + 41, z + 14)
			if self._check_valid(x + delt, y + 41, z + 14, cur):
				self.matrix[x + delt][y + 41][z + 14] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 156, y + 42, z + 14) -> (x + 159, y + 42, z + 14) 
		for delt in range(156, 160):
			cur = node.Node(x + delt, y + 42, z + 14)
			if self._check_valid(x + delt, y + 42, z + 14, cur):
				self.matrix[x + delt][y + 42][z + 14] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 159, y + 43, z + 14) -> (x + 163, y + 43, z + 14) 
		for delt in range(159, 164):
			cur = node.Node(x + delt, y + 43, z + 14)
			if self._check_valid(x + delt, y + 43, z + 14, cur):
				self.matrix[x + delt][y + 43][z + 14] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 163, y + 44, z + 14) -> (x + 167, y + 44, z + 14) 
		for delt in range(163, 168):
			cur = node.Node(x + delt, y + 44, z + 14)
			if self._check_valid(x + delt, y + 44, z + 14, cur):
				self.matrix[x + delt][y + 44][z + 14] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 167, y + 44, z + 15) -> (x + 167, y + 44, z + 15) 
		for delt in range(167, 168):
			cur = node.Node(x + delt, y + 44, z + 15)
			if self._check_valid(x + delt, y + 44, z + 15, cur):
				self.matrix[x + delt][y + 44][z + 15] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 167, y + 45, z + 15) -> (x + 170, y + 45, z + 15) 
		for delt in range(167, 171):
			cur = node.Node(x + delt, y + 45, z + 15)
			if self._check_valid(x + delt, y + 45, z + 15, cur):
				self.matrix[x + delt][y + 45][z + 15] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 170, y + 46, z + 15) -> (x + 174, y + 46, z + 15) 
		for delt in range(170, 175):
			cur = node.Node(x + delt, y + 46, z + 15)
			if self._check_valid(x + delt, y + 46, z + 15, cur):
				self.matrix[x + delt][y + 46][z + 15] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 174, y + 47, z + 15) -> (x + 178, y + 47, z + 15) 
		for delt in range(174, 179):
			cur = node.Node(x + delt, y + 47, z + 15)
			if self._check_valid(x + delt, y + 47, z + 15, cur):
				self.matrix[x + delt][y + 47][z + 15] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 178, y + 47, z + 16) -> (x + 178, y + 47, z + 16) 
		for delt in range(178, 179):
			cur = node.Node(x + delt, y + 47, z + 16)
			if self._check_valid(x + delt, y + 47, z + 16, cur):
				self.matrix[x + delt][y + 47][z + 16] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 178, y + 48, z + 16) -> (x + 178, y + 48, z + 16) 
		for delt in range(178, 179):
			cur = node.Node(x + delt, y + 48, z + 16)
			if self._check_valid(x + delt, y + 48, z + 16, cur):
				self.matrix[x + delt][y + 48][z + 16] = DataGenerator._selected
				self.fill_set_ponts.add(cur)


	def _case_2_8(self, x, y, z):


		# (x, y, z) -> (x + 4, y, z)
		for delt in range(5):
			cur = node.Node(x + delt, y, z)
			if self._check_valid(x + delt, y, z, cur):
				self.matrix[x + delt][y][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 4, y + 1, z) -> (x + 7, y + 1, z)
		for delt in range(4, 8):
			cur = node.Node(x + delt, y + 1, z)
			if self._check_valid(x + delt, y + 1, z, cur):
				self.matrix[x + delt][y + 1][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 7, y + 2, z) -> (x + 11, y + 2, z)
		for delt in range(7, 12):
			cur = node.Node(x + delt, y + 2, z)
			if self._check_valid(x + delt, y + 2, z, cur):
				self.matrix[x + delt][y + 2][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 11, y + 2, z + 1)
		for delt in range(11, 12):
			cur = node.Node(x + delt, y + 2, z + 1)
			if self._check_valid(x + delt, y + 2, z + 1, cur):
				self.matrix[x + delt][y + 2][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 11, y + 3, z + 1) -> (x + 14, y + 3, z + 1)
		for delt in range(11, 15):
			cur = node.Node(x + delt, y + 3, z + 1)
			if self._check_valid(x + delt, y + 3, z + 1, cur):
				self.matrix[x + delt][y + 3][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 14, y + 4, z + 1) -> (x + 18, y + 4, z + 1)
		for delt in range(14, 19):
			cur = node.Node(x + delt, y + 4, z + 1)
			if self._check_valid(x + delt, y + 4, z + 1, cur):
				self.matrix[x + delt][y + 4][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 18, y + 5, z + 1) -> (x + 22, y + 5, z + 1)
		for delt in range(18, 23):
			cur = node.Node(x + delt, y + 5, z + 1)
			if self._check_valid(x + delt, y + 5, z + 1, cur):
				self.matrix[x + delt][y + 5][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 22, y + 5, z + 2)
		for delt in range(22, 23):
			cur = node.Node(x + delt, y + 5, z + 2)
			if self._check_valid(x + delt, y + 5, z + 2, cur):
				self.matrix[x + delt][y + 5][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 22, y + 6, z + 2) -> (x + 25, y + 6, z + 2)
		for delt in range(22, 26):
			cur = node.Node(x + delt, y + 6, z + 2)
			if self._check_valid(x + delt, y + 6, z + 2, cur):
				self.matrix[x + delt][y + 6][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 25, y + 7, z + 2) -> (x + 29, y + 7, z + 2)
		for delt in range(25, 30):
			cur = node.Node(x + delt, y + 7, z + 2)
			if self._check_valid(x + delt, y + 7, z + 2, cur):
				self.matrix[x + delt][y + 7][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 29, y + 8, z + 2) -> (x + 33, y + 8, z + 2)
		for delt in range(29, 34):
			cur = node.Node(x + delt, y + 8, z + 2)
			if self._check_valid(x + delt, y + 8, z + 2, cur):
				self.matrix[x + delt][y + 8][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 33, y + 8, z + 3)
		for delt in range(33, 34):
			cur = node.Node(x + delt, y + 8, z + 3)
			if self._check_valid(x + delt, y + 8, z + 3, cur):
				self.matrix[x + delt][y + 8][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 33, y + 9, z + 3) -> (x + 37, y + 9, z + 3) 
		for delt in range(33, 38):
			cur = node.Node(x + delt, y + 9, z + 3)
			if self._check_valid(x + delt, y + 9, z + 3, cur):
				self.matrix[x + delt][y + 9][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 37, y + 10, z + 3) -> (x + 40, y + 10, z + 3) 
		for delt in range(37, 41):
			cur = node.Node(x + delt, y + 10, z + 3)
			if self._check_valid(x + delt, y + 10, z + 3, cur):
				self.matrix[x + delt][y + 10][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 40, y + 11, z + 3) -> (x + 44, y + 11, z + 3) 
		for delt in range(40, 45):
			cur = node.Node(x + delt, y + 11, z + 3)
			if self._check_valid(x + delt, y + 11, z + 3, cur):
				self.matrix[x + delt][y + 11][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 44, y + 11, z + 4) -> (x + 44, y + 11, z + 4) 
		for delt in range(44, 45):
			cur = node.Node(x + delt, y + 11, z + 4)
			if self._check_valid(x + delt, y + 11, z + 4, cur):
				self.matrix[x + delt][y + 11][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 44, y + 12, z + 4) -> (x + 48, y + 12, z + 4) 
		for delt in range(44, 49):
			cur = node.Node(x + delt, y + 12, z + 4)
			if self._check_valid(x + delt, y + 12, z + 4, cur):
				self.matrix[x + delt][y + 12][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 48, y + 13, z + 4) -> (x + 52, y + 13, z + 4) 
		for delt in range(48, 53):
			cur = node.Node(x + delt, y + 13, z + 4)
			if self._check_valid(x + delt, y + 13, z + 4, cur):
				self.matrix[x + delt][y + 13][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 52, y + 14, z + 4) -> (x + 56, y + 14, z + 4) 
		for delt in range(52, 57):
			cur = node.Node(x + delt, y + 14, z + 4)
			if self._check_valid(x + delt, y + 14, z + 4, cur):
				self.matrix[x + delt][y + 14][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 56, y + 14, z + 5) -> (x + 56, y + 14, z + 5) 
		for delt in range(56, 57):
			cur = node.Node(x + delt, y + 14, z + 5)
			if self._check_valid(x + delt, y + 14, z + 5, cur):
				self.matrix[x + delt][y + 14][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 56, y + 15, z + 5) -> (x + 59, y + 15, z + 5) 
		for delt in range(56, 60):
			cur = node.Node(x + delt, y + 15, z + 5)
			if self._check_valid(x + delt, y + 15, z + 5, cur):
				self.matrix[x + delt][y + 15][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 59, y + 16, z + 5) -> (x + 63, y + 16, z + 5) 
		for delt in range(59, 64):
			cur = node.Node(x + delt, y + 16, z + 5)
			if self._check_valid(x + delt, y + 16, z + 5, cur):
				self.matrix[x + delt][y + 16][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 63, y + 17, z + 5) -> (x + 67, y + 17, z + 5) 
		for delt in range(63, 68):
			cur = node.Node(x + delt, y + 17, z + 5)
			if self._check_valid(x + delt, y + 17, z + 5, cur):
				self.matrix[x + delt][y + 17][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 67, y + 17, z + 6) -> (x + 67, y + 17, z + 6) 
		for delt in range(67, 68):
			cur = node.Node(x + delt, y + 17, z + 6)
			if self._check_valid(x + delt, y + 17, z + 6, cur):
				self.matrix[x + delt][y + 17][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 67, y + 18, z + 6) -> (x + 70, y + 18, z + 6) 
		for delt in range(67, 71):
			cur = node.Node(x + delt, y + 18, z + 6)
			if self._check_valid(x + delt, y + 18, z + 6, cur):
				self.matrix[x + delt][y + 18][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 70, y + 19, z + 6) -> (x + 74, y + 19, z + 6) 
		for delt in range(70, 75):
			cur = node.Node(x + delt, y + 19, z + 6)
			if self._check_valid(x + delt, y + 19, z + 6, cur):
				self.matrix[x + delt][y + 19][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 74, y + 20, z + 6) -> (x + 78, y + 20, z + 6) 
		for delt in range(74, 79):
			cur = node.Node(x + delt, y + 20, z + 6)
			if self._check_valid(x + delt, y + 20, z + 6, cur):
				self.matrix[x + delt][y + 20][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 78, y + 20, z + 7) -> (x + 78, y + 20, z + 7) 
		for delt in range(78, 79):
			cur = node.Node(x + delt, y + 20, z + 7)
			if self._check_valid(x + delt, y + 20, z + 7, cur):
				self.matrix[x + delt][y + 20][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)				

		# (x + 78, y + 21, z + 7) -> (x + 81 y + 21, z + 7) 
		for delt in range(78, 82):
			cur = node.Node(x + delt, y + 21, z + 7)
			if self._check_valid(x + delt, y + 21, z + 7, cur):
				self.matrix[x + delt][y + 21][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 81, y + 22, z + 7) -> (x + 85, y + 22, z + 7) 
		for delt in range(81, 86):
			cur = node.Node(x + delt, y + 22, z + 7)
			if self._check_valid(x + delt, y + 22, z + 7, cur):
				self.matrix[x + delt][y + 22][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 85, y + 23, z + 7) -> (x + 89, y + 23, z + 7) 
		for delt in range(85, 90):
			cur = node.Node(x + delt, y + 23, z + 7)
			if self._check_valid(x + delt, y + 23, z + 7, cur):
				self.matrix[x + delt][y + 23][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 89, y + 23, z + 8) -> (x + 89, y + 23, z + 8) 
		for delt in range(89, 90):
			cur = node.Node(x + delt, y + 23, z + 8)
			if self._check_valid(x + delt, y + 23, z + 8, cur):
				self.matrix[x + delt][y + 23][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)				

		# (x + 89, y + 24, z + 8) -> (x + 92 y + 24, z + 8) 
		for delt in range(89, 93):
			cur = node.Node(x + delt, y + 24, z + 8)
			if self._check_valid(x + delt, y + 24, z + 8, cur):
				self.matrix[x + delt][y + 24][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 92, y + 25, z + 8) -> (x + 96, y + 25, z + 8) 
		for delt in range(92, 97):
			cur = node.Node(x + delt, y + 25, z + 8)
			if self._check_valid(x + delt, y + 25, z + 8, cur):
				self.matrix[x + delt][y + 25][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 96, y + 26, z + 8) -> (x + 100, y + 26, z + 8) 
		for delt in range(96, 101):
			cur = node.Node(x + delt, y + 26, z + 8)
			if self._check_valid(x + delt, y + 26, z + 8, cur):
				self.matrix[x + delt][y + 26][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 100, y + 26, z + 9) -> (x + 100, y + 26, z + 9) 
		for delt in range(100, 101):
			cur = node.Node(x + delt, y + 26, z + 9)
			if self._check_valid(x + delt, y + 26, z + 9, cur):
				self.matrix[x + delt][y + 26][z + 9] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 100, y + 27, z + 9) -> (x + 104, y + 27, z + 9) 
		for delt in range(100, 105):
			cur = node.Node(x + delt, y + 27, z + 9)
			if self._check_valid(x + delt, y + 27, z + 9, cur):
				self.matrix[x + delt][y + 27][z + 9] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 104, y + 28, z + 9) -> (x + 108, y + 28, z + 9) 
		for delt in range(104, 109):
			cur = node.Node(x + delt, y + 28, z + 9)
			if self._check_valid(x + delt, y + 28, z + 9, cur):
				self.matrix[x + delt][y + 28][z + 9] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 108, y + 29, z + 9) -> (x + 112, y + 29, z + 9) 
		for delt in range(108, 113):
			cur = node.Node(x + delt, y + 29, z + 9)
			if self._check_valid(x + delt, y + 29, z + 9, cur):
				self.matrix[x + delt][y + 29][z + 9] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 112, y + 29, z + 10) -> (x + 112, y + 29, z + 10) 
		for delt in range(112, 113):
			cur = node.Node(x + delt, y + 29, z + 10)
			if self._check_valid(x + delt, y + 29, z + 10, cur):
				self.matrix[x + delt][y + 29][z + 10] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 112, y + 30, z + 10) -> (x + 115, y + 30, z + 10) 
		for delt in range(112, 116):
			cur = node.Node(x + delt, y + 30, z + 10)
			if self._check_valid(x + delt, y + 30, z + 10, cur):
				self.matrix[x + delt][y + 30][z + 10] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 115, y + 31, z + 10) -> (x + 119, y + 31, z + 10) 
		for delt in range(115, 120):
			cur = node.Node(x + delt, y + 31, z + 10)
			if self._check_valid(x + delt, y + 31, z + 10, cur):
				self.matrix[x + delt][y + 31][z + 10] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 119, y + 32, z + 10) -> (x + 123, y + 32, z + 10) 
		for delt in range(119, 124):
			cur = node.Node(x + delt, y + 32, z + 10)
			if self._check_valid(x + delt, y + 32, z + 10, cur):
				self.matrix[x + delt][y + 32][z + 10] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 123, y + 32, z + 11) -> (x + 123, y + 32, z + 11) 
		for delt in range(123, 124):
			cur = node.Node(x + delt, y + 32, z + 11)
			if self._check_valid(x + delt, y + 32, z + 11, cur):
				self.matrix[x + delt][y + 32][z + 11] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 123, y + 33, z + 11) -> (x + 126, y + 33, z + 11) 
		for delt in range(123, 127):
			cur = node.Node(x + delt, y + 33, z + 11)
			if self._check_valid(x + delt, y + 33, z + 11, cur):
				self.matrix[x + delt][y + 33][z + 11] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 126, y + 34, z + 11) -> (x + 130, y + 34, z + 11) 
		for delt in range(126, 131):
			cur = node.Node(x + delt, y + 34, z + 11)
			if self._check_valid(x + delt, y + 34, z + 11, cur):
				self.matrix[x + delt][y + 34][z + 11] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 130, y + 35, z + 11) -> (x + 134, y + 35, z + 11) 
		for delt in range(130, 135):
			cur = node.Node(x + delt, y + 35, z + 11)
			if self._check_valid(x + delt, y + 35, z + 11, cur):
				self.matrix[x + delt][y + 35][z + 11] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 134, y + 35, z + 12) -> (x + 134, y + 35, z + 12) 
		for delt in range(134, 135):
			cur = node.Node(x + delt, y + 35, z + 12)
			if self._check_valid(x + delt, y + 35, z + 12, cur):
				self.matrix[x + delt][y + 35][z + 12] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 134, y + 36, z + 12) -> (x + 137, y + 36, z + 12) 
		for delt in range(134, 138):
			cur = node.Node(x + delt, y + 36, z + 12)
			if self._check_valid(x + delt, y + 36, z + 12, cur):
				self.matrix[x + delt][y + 36][z + 12] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 137, y + 37, z + 12) -> (x + 141, y + 37, z + 12) 
		for delt in range(137, 142):
			cur = node.Node(x + delt, y + 37, z + 12)
			if self._check_valid(x + delt, y + 37, z + 12, cur):
				self.matrix[x + delt][y + 37][z + 12] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 141, y + 38, z + 12) -> (x + 145, y + 38, z + 12) 
		for delt in range(137, 146):
			cur = node.Node(x + delt, y + 38, z + 12)
			if self._check_valid(x + delt, y + 38, z + 12, cur):
				self.matrix[x + delt][y + 38][z + 12] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 145, y + 38, z + 13) -> (x + 145, y + 38, z + 13) 
		for delt in range(145, 146):
			cur = node.Node(x + delt, y + 38, z + 13)
			if self._check_valid(x + delt, y + 38, z + 13, cur):
				self.matrix[x + delt][y + 38][z + 13] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 145, y + 39, z + 13) -> (x + 148, y + 39, z + 13) 
		for delt in range(145, 149):
			cur = node.Node(x + delt, y + 39, z + 13)
			if self._check_valid(x + delt, y + 39, z + 13, cur):
				self.matrix[x + delt][y + 39][z + 13] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 148, y + 40, z + 13) -> (x + 152, y + 40, z + 13) 
		for delt in range(148, 153):
			cur = node.Node(x + delt, y + 40, z + 13)
			if self._check_valid(x + delt, y + 40, z + 13, cur):
				self.matrix[x + delt][y + 40][z + 13] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 152, y + 41, z + 13) -> (x + 156, y + 41, z + 13) 
		for delt in range(152, 157):
			cur = node.Node(x + delt, y + 41, z + 13)
			if self._check_valid(x + delt, y + 41, z + 13, cur):
				self.matrix[x + delt][y + 41][z + 13] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 156, y + 41, z + 14) -> (x + 156, y + 41, z + 14) 
		for delt in range(156, 157):
			cur = node.Node(x + delt, y + 41, z + 14)
			if self._check_valid(x + delt, y + 41, z + 14, cur):
				self.matrix[x + delt][y + 41][z + 14] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 156, y + 42, z + 14) -> (x + 159, y + 42, z + 14) 
		for delt in range(156, 160):
			cur = node.Node(x + delt, y + 42, z + 14)
			if self._check_valid(x + delt, y + 42, z + 14, cur):
				self.matrix[x + delt][y + 42][z + 14] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 159, y + 43, z + 14) -> (x + 163, y + 43, z + 14) 
		for delt in range(159, 164):
			cur = node.Node(x + delt, y + 43, z + 14)
			if self._check_valid(x + delt, y + 43, z + 14, cur):
				self.matrix[x + delt][y + 43][z + 14] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 163, y + 44, z + 14) -> (x + 167, y + 44, z + 14) 
		for delt in range(163, 168):
			cur = node.Node(x + delt, y + 44, z + 14)
			if self._check_valid(x + delt, y + 44, z + 14, cur):
				self.matrix[x + delt][y + 44][z + 14] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 167, y + 44, z + 15) -> (x + 167, y + 44, z + 15) 
		for delt in range(167, 168):
			cur = node.Node(x + delt, y + 44, z + 15)
			if self._check_valid(x + delt, y + 44, z + 15, cur):
				self.matrix[x + delt][y + 44][z + 15] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 167, y + 45, z + 15) -> (x + 170, y + 45, z + 15) 
		for delt in range(167, 171):
			cur = node.Node(x + delt, y + 45, z + 15)
			if self._check_valid(x + delt, y + 45, z + 15, cur):
				self.matrix[x + delt][y + 45][z + 15] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 170, y + 46, z + 15) -> (x + 174, y + 46, z + 15) 
		for delt in range(170, 175):
			cur = node.Node(x + delt, y + 46, z + 15)
			if self._check_valid(x + delt, y + 46, z + 15, cur):
				self.matrix[x + delt][y + 46][z + 15] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 174, y + 47, z + 15) -> (x + 178, y + 47, z + 15) 
		for delt in range(174, 179):
			cur = node.Node(x + delt, y + 47, z + 15)
			if self._check_valid(x + delt, y + 47, z + 15, cur):
				self.matrix[x + delt][y + 47][z + 15] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 178, y + 47, z + 16) -> (x + 178, y + 47, z + 16) 
		for delt in range(178, 179):
			cur = node.Node(x + delt, y + 47, z + 16)
			if self._check_valid(x + delt, y + 47, z + 16, cur):
				self.matrix[x + delt][y + 47][z + 16] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 178, y + 48, z + 16) -> (x + 182, y + 48, z + 16) 
		for delt in range(178, 183):
			cur = node.Node(x + delt, y + 48, z + 16)
			if self._check_valid(x + delt, y + 48, z + 16, cur):
				self.matrix[x + delt][y + 48][z + 16] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 182, y + 49, z + 16) -> (x + 186, y + 49, z + 16) 
		for delt in range(182, 187):
			cur = node.Node(x + delt, y + 49, z + 16)
			if self._check_valid(x + delt, y + 49, z + 16, cur):
				self.matrix[x + delt][y + 49][z + 16] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 186, y + 50, z + 16) -> (x + 190, y + 50, z + 16) 
		for delt in range(186, 191):
			cur = node.Node(x + delt, y + 50, z + 16)
			if self._check_valid(x + delt, y + 50, z + 16, cur):
				self.matrix[x + delt][y + 50][z + 16] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 190, y + 50, z + 17) -> (x + 190, y + 50, z + 17) 
		for delt in range(190, 191):
			cur = node.Node(x + delt, y + 50, z + 17)
			if self._check_valid(x + delt, y + 50, z + 17, cur):
				self.matrix[x + delt][y + 50][z + 17] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 190, y + 51, z + 17) -> (x + 193, y + 51, z + 17) 
		for delt in range(190, 194):
			cur = node.Node(x + delt, y + 51, z + 17)
			if self._check_valid(x + delt, y + 51, z + 17, cur):
				self.matrix[x + delt][y + 51][z + 17] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 193, y + 52, z + 17) -> (x + 197, y + 52, z + 17) 
		for delt in range(190, 198):
			cur = node.Node(x + delt, y + 52, z + 17)
			if self._check_valid(x + delt, y + 52, z + 17, cur):
				self.matrix[x + delt][y + 52][z + 17] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 197, y + 53, z + 17) -> (x + 201, y + 53, z + 17) 
		for delt in range(197, 202):
			cur = node.Node(x + delt, y + 53, z + 17)
			if self._check_valid(x + delt, y + 53, z + 17, cur):
				self.matrix[x + delt][y + 53][z + 17] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 201, y + 53, z + 18) -> (x + 201, y + 53, z + 18) 
		for delt in range(201, 202):
			cur = node.Node(x + delt, y + 53, z + 18)
			if self._check_valid(x + delt, y + 53, z + 18, cur):
				self.matrix[x + delt][y + 53][z + 18] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 201, y + 54, z + 18) -> (x + 201, y + 54, z + 18) 
		for delt in range(201, 202):
			cur = node.Node(x + delt, y + 54, z + 18)
			if self._check_valid(x + delt, y + 54, z + 18, cur):
				self.matrix[x + delt][y + 54][z + 18] = DataGenerator._selected
				self.fill_set_ponts.add(cur)


	def _case_3_1(self, x, y, z):

		# (x, y, z) -> (x + 1, y, z)
		for delt in range(2):
			cur = node.Node(x + delt, y, z)
			if self._check_valid(x + delt, y, z, cur):
				self.matrix[x + delt][y][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 1, y + 1, z) -> (x + 3, y + 1, z)
		for delt in range(1, 4):
			cur = node.Node(x + delt, y + 1, z)
			if self._check_valid(x + delt, y + 1, z, cur):
				self.matrix[x + delt][y + 1][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 3, y + 2, z) -> (x + 5, y + 2, z)
		for delt in range(3, 6):
			cur = node.Node(x + delt, y + 2, z)
			if self._check_valid(x + delt, y + 2, z, cur):
				self.matrix[x + delt][y + 2][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 5, y + 3, z) -> (x + 6, y + 3, z)
		for delt in range(5, 7):
			cur = node.Node(x + delt, y + 3, z)
			if self._check_valid(x + delt, y + 3, z, cur):
				self.matrix[x + delt][y + 3][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 6, y + 4, z) -> (x + 8, y + 4, z)
		for delt in range(6, 9):
			cur = node.Node(x + delt, y + 4, z)
			if self._check_valid(x + delt, y + 4, z, cur):
				self.matrix[x + delt][y + 4][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 8, y + 5, z) -> (x + 9, y + 5, z)
		for delt in range(8, 10):
			cur = node.Node(x + delt, y + 5, z)
			if self._check_valid(x + delt, y + 5, z, cur):
				self.matrix[x + delt][y + 5][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 9, y + 5, z + 1) -> (x + 10, y + 5, z + 1)
		for delt in range(9, 11):
			cur = node.Node(x + delt, y + 5, z + 1)
			if self._check_valid(x + delt, y + 5, z + 1, cur):
				self.matrix[x + delt][y + 5][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 10, y + 6, z + 1) -> (x + 12, y + 6, z + 1)
		for delt in range(10, 13):
			cur = node.Node(x + delt, y + 6, z + 1)
			if self._check_valid(x + delt, y + 6, z + 1, cur):
				self.matrix[x + delt][y + 6][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 12, y + 7, z + 1) -> (x + 13, y + 7, z + 1)
		for delt in range(12, 14):
			cur = node.Node(x + delt, y + 7, z + 1)
			if self._check_valid(x + delt, y + 7, z + 1, cur):
				self.matrix[x + delt][y + 7][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 13, y + 8, z + 1) -> (x + 15, y + 8, z + 1)
		for delt in range(13, 16):
			cur = node.Node(x + delt, y + 8, z + 1)
			if self._check_valid(x + delt, y + 8, z + 1, cur):
				self.matrix[x + delt][y + 8][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 15, y + 9, z + 1) -> (x + 17, y + 9, z + 1)
		for delt in range(15, 17):
			cur = node.Node(x + delt, y + 9, z + 1)
			if self._check_valid(x + delt, y + 9, z + 1, cur):
				self.matrix[x + delt][y + 9][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 17, y + 10, z + 1) -> (x + 17, y + 10, z + 1)
		for delt in range(17, 18):
			cur = node.Node(x + delt, y + 10, z + 1)
			if self._check_valid(x + delt, y + 10, z + 1, cur):
				self.matrix[x + delt][y + 10][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)


	def _case_3_2(self, x, y, z):

		# (x, y, z) -> (x + 1, y, z)
		for delt in range(2):
			cur = node.Node(x + delt, y, z)
			if self._check_valid(x + delt, y, z, cur):
				self.matrix[x + delt][y][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 1, y + 1, z) -> (x + 3, y + 1, z)
		for delt in range(1, 4):
			cur = node.Node(x + delt, y + 1, z)
			if self._check_valid(x + delt, y + 1, z, cur):
				self.matrix[x + delt][y + 1][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 3, y + 2, z) -> (x + 5, y + 2, z)
		for delt in range(3, 6):
			cur = node.Node(x + delt, y + 2, z)
			if self._check_valid(x + delt, y + 2, z, cur):
				self.matrix[x + delt][y + 2][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 5, y + 3, z) -> (x + 6, y + 3, z)
		for delt in range(5, 7):
			cur = node.Node(x + delt, y + 3, z)
			if self._check_valid(x + delt, y + 3, z, cur):
				self.matrix[x + delt][y + 3][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 6, y + 4, z) -> (x + 8, y + 4, z)
		for delt in range(6, 9):
			cur = node.Node(x + delt, y + 4, z)
			if self._check_valid(x + delt, y + 4, z, cur):
				self.matrix[x + delt][y + 4][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 8, y + 5, z) -> (x + 9, y + 5, z)
		for delt in range(8, 10):
			cur = node.Node(x + delt, y + 5, z)
			if self._check_valid(x + delt, y + 5, z, cur):
				self.matrix[x + delt][y + 5][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 9, y + 5, z + 1) -> (x + 10, y + 5, z + 1)
		for delt in range(9, 11):
			cur = node.Node(x + delt, y + 5, z + 1)
			if self._check_valid(x + delt, y + 5, z + 1, cur):
				self.matrix[x + delt][y + 5][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 10, y + 6, z + 1) -> (x + 12, y + 6, z + 1)
		for delt in range(10, 13):
			cur = node.Node(x + delt, y + 6, z + 1)
			if self._check_valid(x + delt, y + 6, z + 1, cur):
				self.matrix[x + delt][y + 6][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 12, y + 7, z + 1) -> (x + 13, y + 7, z + 1)
		for delt in range(12, 14):
			cur = node.Node(x + delt, y + 7, z + 1)
			if self._check_valid(x + delt, y + 7, z + 1, cur):
				self.matrix[x + delt][y + 7][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 13, y + 8, z + 1) -> (x + 15, y + 8, z + 1)
		for delt in range(13, 16):
			cur = node.Node(x + delt, y + 8, z + 1)
			if self._check_valid(x + delt, y + 8, z + 1, cur):
				self.matrix[x + delt][y + 8][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 15, y + 9, z + 1) -> (x + 17, y + 9, z + 1)
		for delt in range(15, 18):
			cur = node.Node(x + delt, y + 9, z + 1)
			if self._check_valid(x + delt, y + 9, z + 1, cur):
				self.matrix[x + delt][y + 9][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 17, y + 10, z + 1) -> (x + 19, y + 10, z + 1)
		for delt in range(17, 20):
			cur = node.Node(x + delt, y + 10, z + 1)
			if self._check_valid(x + delt, y + 10, z + 1, cur):
				self.matrix[x + delt][y + 10][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 19, y + 11, z + 1) -> (x + 19, y + 11, z + 1)
		for delt in range(19, 20):
			cur = node.Node(x + delt, y + 11, z + 1)
			if self._check_valid(x + delt, y + 11, z + 1, cur):
				self.matrix[x + delt][y + 11][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 19, y + 11, z + 2) -> (x + 20, y + 11, z + 2)
		for delt in range(19, 21):
			cur = node.Node(x + delt, y + 11, z + 2)
			if self._check_valid(x + delt, y + 11, z + 2, cur):
				self.matrix[x + delt][y + 11][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 20, y + 12, z + 2) -> (x + 22, y + 12, z + 2)
		for delt in range(20, 23):
			cur = node.Node(x + delt, y + 12, z + 2)
			if self._check_valid(x + delt, y + 12, z + 2, cur):
				self.matrix[x + delt][y + 12][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 22, y + 13, z + 2) -> (x + 24, y + 13, z + 2)
		for delt in range(22, 25):
			cur = node.Node(x + delt, y + 13, z + 2)
			if self._check_valid(x + delt, y + 13, z + 2, cur):
				self.matrix[x + delt][y + 13][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 24, y + 14, z + 2) -> (x + 25, y + 14, z + 2)
		for delt in range(24, 26):
			cur = node.Node(x + delt, y + 14, z + 2)
			if self._check_valid(x + delt, y + 14, z + 2, cur):
				self.matrix[x + delt][y + 14][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 25, y + 15, z + 2) -> (x + 27, y + 15, z + 2)
		for delt in range(25, 28):
			cur = node.Node(x + delt, y + 15, z + 2)
			if self._check_valid(x + delt, y + 15, z + 2, cur):
				self.matrix[x + delt][y + 15][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 27, y + 16, z + 2) -> (x + 28, y + 16, z + 2)
		for delt in range(27, 29):
			cur = node.Node(x + delt, y + 16, z + 2)
			if self._check_valid(x + delt, y + 16, z + 2, cur):
				self.matrix[x + delt][y + 16][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 28, y + 16, z + 3) -> (x + 29, y + 16, z + 3)
		for delt in range(28, 30):
			cur = node.Node(x + delt, y + 16, z + 3)
			if self._check_valid(x + delt, y + 16, z + 3, cur):
				self.matrix[x + delt][y + 16][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 29, y + 17, z + 3) -> (x + 31, y + 17, z + 3)
		for delt in range(29, 32):
			cur = node.Node(x + delt, y + 17, z + 3)
			if self._check_valid(x + delt, y + 17, z + 3, cur):
				self.matrix[x + delt][y + 17][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 31, y + 18, z + 3) -> (x + 32, y + 18, z + 3)
		for delt in range(31, 33):
			cur = node.Node(x + delt, y + 18, z + 3)
			if self._check_valid(x + delt, y + 18, z + 3, cur):
				self.matrix[x + delt][y + 18][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 32, y + 19, z + 3) -> (x + 34, y + 19, z + 3)
		for delt in range(32, 35):
			cur = node.Node(x + delt, y + 19, z + 3)
			if self._check_valid(x + delt, y + 19, z + 3, cur):
				self.matrix[x + delt][y + 19][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 34, y + 20, z + 3) -> (x + 36, y + 20, z + 3)
		for delt in range(34, 37):
			cur = node.Node(x + delt, y + 20, z + 3)
			if self._check_valid(x + delt, y + 20, z + 3, cur):
				self.matrix[x + delt][y + 20][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 36, y + 21, z + 3) -> (x + 36, y + 21, z + 3)
		for delt in range(36, 37):
			cur = node.Node(x + delt, y + 21, z + 3)
			if self._check_valid(x + delt, y + 21, z + 3, cur):
				self.matrix[x + delt][y + 21][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)				


	def _case_3_3(self, x, y, z):

		# (x, y, z) -> (x + 1, y, z)
		for delt in range(2):
			cur = node.Node(x + delt, y, z)
			if self._check_valid(x + delt, y, z, cur):
				self.matrix[x + delt][y][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 1, y + 1, z) -> (x + 3, y + 1, z)
		for delt in range(1, 4):
			cur = node.Node(x + delt, y + 1, z)
			if self._check_valid(x + delt, y + 1, z, cur):
				self.matrix[x + delt][y + 1][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 3, y + 2, z) -> (x + 5, y + 2, z)
		for delt in range(3, 6):
			cur = node.Node(x + delt, y + 2, z)
			if self._check_valid(x + delt, y + 2, z, cur):
				self.matrix[x + delt][y + 2][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 5, y + 3, z) -> (x + 6, y + 3, z)
		for delt in range(5, 7):
			cur = node.Node(x + delt, y + 3, z)
			if self._check_valid(x + delt, y + 3, z, cur):
				self.matrix[x + delt][y + 3][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 6, y + 4, z) -> (x + 8, y + 4, z)
		for delt in range(6, 9):
			cur = node.Node(x + delt, y + 4, z)
			if self._check_valid(x + delt, y + 4, z, cur):
				self.matrix[x + delt][y + 4][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 8, y + 5, z) -> (x + 9, y + 5, z)
		for delt in range(8, 10):
			cur = node.Node(x + delt, y + 5, z)
			if self._check_valid(x + delt, y + 5, z, cur):
				self.matrix[x + delt][y + 5][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 9, y + 5, z + 1) -> (x + 10, y + 5, z + 1)
		for delt in range(9, 11):
			cur = node.Node(x + delt, y + 5, z + 1)
			if self._check_valid(x + delt, y + 5, z + 1, cur):
				self.matrix[x + delt][y + 5][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 10, y + 6, z + 1) -> (x + 12, y + 6, z + 1)
		for delt in range(10, 13):
			cur = node.Node(x + delt, y + 6, z + 1)
			if self._check_valid(x + delt, y + 6, z + 1, cur):
				self.matrix[x + delt][y + 6][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 12, y + 7, z + 1) -> (x + 13, y + 7, z + 1)
		for delt in range(12, 14):
			cur = node.Node(x + delt, y + 7, z + 1)
			if self._check_valid(x + delt, y + 7, z + 1, cur):
				self.matrix[x + delt][y + 7][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 13, y + 8, z + 1) -> (x + 15, y + 8, z + 1)
		for delt in range(13, 16):
			cur = node.Node(x + delt, y + 8, z + 1)
			if self._check_valid(x + delt, y + 8, z + 1, cur):
				self.matrix[x + delt][y + 8][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 15, y + 9, z + 1) -> (x + 17, y + 9, z + 1)
		for delt in range(15, 18):
			cur = node.Node(x + delt, y + 9, z + 1)
			if self._check_valid(x + delt, y + 9, z + 1, cur):
				self.matrix[x + delt][y + 9][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 17, y + 10, z + 1) -> (x + 19, y + 10, z + 1)
		for delt in range(17, 20):
			cur = node.Node(x + delt, y + 10, z + 1)
			if self._check_valid(x + delt, y + 10, z + 1, cur):
				self.matrix[x + delt][y + 10][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 19, y + 11, z + 1) -> (x + 19, y + 11, z + 1)
		for delt in range(19, 20):
			cur = node.Node(x + delt, y + 11, z + 1)
			if self._check_valid(x + delt, y + 11, z + 1, cur):
				self.matrix[x + delt][y + 11][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 19, y + 11, z + 2) -> (x + 20, y + 11, z + 2)
		for delt in range(19, 21):
			cur = node.Node(x + delt, y + 11, z + 2)
			if self._check_valid(x + delt, y + 11, z + 2, cur):
				self.matrix[x + delt][y + 11][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 20, y + 12, z + 2) -> (x + 22, y + 12, z + 2)
		for delt in range(20, 23):
			cur = node.Node(x + delt, y + 12, z + 2)
			if self._check_valid(x + delt, y + 12, z + 2, cur):
				self.matrix[x + delt][y + 12][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 22, y + 13, z + 2) -> (x + 24, y + 13, z + 2)
		for delt in range(22, 25):
			cur = node.Node(x + delt, y + 13, z + 2)
			if self._check_valid(x + delt, y + 13, z + 2, cur):
				self.matrix[x + delt][y + 13][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 24, y + 14, z + 2) -> (x + 25, y + 14, z + 2)
		for delt in range(24, 26):
			cur = node.Node(x + delt, y + 14, z + 2)
			if self._check_valid(x + delt, y + 14, z + 2, cur):
				self.matrix[x + delt][y + 14][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 25, y + 15, z + 2) -> (x + 27, y + 15, z + 2)
		for delt in range(25, 28):
			cur = node.Node(x + delt, y + 15, z + 2)
			if self._check_valid(x + delt, y + 15, z + 2, cur):
				self.matrix[x + delt][y + 15][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 27, y + 16, z + 2) -> (x + 28, y + 16, z + 2)
		for delt in range(27, 29):
			cur = node.Node(x + delt, y + 16, z + 2)
			if self._check_valid(x + delt, y + 16, z + 2, cur):
				self.matrix[x + delt][y + 16][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 28, y + 16, z + 3) -> (x + 29, y + 16, z + 3)
		for delt in range(28, 30):
			cur = node.Node(x + delt, y + 16, z + 3)
			if self._check_valid(x + delt, y + 16, z + 3, cur):
				self.matrix[x + delt][y + 16][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 29, y + 17, z + 3) -> (x + 31, y + 17, z + 3)
		for delt in range(29, 32):
			cur = node.Node(x + delt, y + 17, z + 3)
			if self._check_valid(x + delt, y + 17, z + 3, cur):
				self.matrix[x + delt][y + 17][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 31, y + 18, z + 3) -> (x + 32, y + 18, z + 3)
		for delt in range(31, 33):
			cur = node.Node(x + delt, y + 18, z + 3)
			if self._check_valid(x + delt, y + 18, z + 3, cur):
				self.matrix[x + delt][y + 18][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 32, y + 19, z + 3) -> (x + 34, y + 19, z + 3)
		for delt in range(32, 35):
			cur = node.Node(x + delt, y + 19, z + 3)
			if self._check_valid(x + delt, y + 19, z + 3, cur):
				self.matrix[x + delt][y + 19][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 34, y + 20, z + 3) -> (x + 36, y + 20, z + 3)
		for delt in range(34, 37):
			cur = node.Node(x + delt, y + 20, z + 3)
			if self._check_valid(x + delt, y + 20, z + 3, cur):
				self.matrix[x + delt][y + 20][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 36, y + 21, z + 3) -> (x + 38, y + 21, z + 3)
		for delt in range(36, 39):
			cur = node.Node(x + delt, y + 21, z + 3)
			if self._check_valid(x + delt, y + 21, z + 3, cur):
				self.matrix[x + delt][y + 21][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 38, y + 22, z + 3) -> (x + 38, y + 22, z + 3)
		for delt in range(38, 39):
			cur = node.Node(x + delt, y + 22, z + 3)
			if self._check_valid(x + delt, y + 22, z + 3, cur):
				self.matrix[x + delt][y + 22][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 38, y + 22, z + 4) -> (x + 39, y + 22, z + 4)
		for delt in range(38, 40):
			cur = node.Node(x + delt, y + 22, z + 4)
			if self._check_valid(x + delt, y + 22, z + 4, cur):
				self.matrix[x + delt][y + 22][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 39, y + 23, z + 4) -> (x + 41, y + 23, z + 4)
		for delt in range(39, 42):
			cur = node.Node(x + delt, y + 23, z + 4)
			if self._check_valid(x + delt, y + 23, z + 4, cur):
				self.matrix[x + delt][y + 23][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 41, y + 24, z + 4) -> (x + 43, y + 24, z + 4)
		for delt in range(41, 44):
			cur = node.Node(x + delt, y + 24, z + 4)
			if self._check_valid(x + delt, y + 24, z + 4, cur):
				self.matrix[x + delt][y + 24][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 43, y + 25, z + 4) -> (x + 44, y + 25, z + 4)
		for delt in range(43, 45):
			cur = node.Node(x + delt, y + 25, z + 4)
			if self._check_valid(x + delt, y + 25, z + 4, cur):
				self.matrix[x + delt][y + 25][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 44, y + 26, z + 4) -> (x + 46, y + 26, z + 4)
		for delt in range(44, 47):
			cur = node.Node(x + delt, y + 26, z + 4)
			if self._check_valid(x + delt, y + 26, z + 4, cur):
				self.matrix[x + delt][y + 26][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 46, y + 27, z + 4) -> (x + 47, y + 27, z + 4)
		for delt in range(46, 48):
			cur = node.Node(x + delt, y + 27, z + 4)
			if self._check_valid(x + delt, y + 27, z + 4, cur):
				self.matrix[x + delt][y + 27][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 47, y + 27, z + 5) -> (x + 48, y + 27, z + 5)
		for delt in range(47, 49):
			cur = node.Node(x + delt, y + 27, z + 5)
			if self._check_valid(x + delt, y + 27, z + 5, cur):
				self.matrix[x + delt][y + 27][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 48, y + 28, z + 5) -> (x + 50, y + 28, z + 5)
		for delt in range(48, 51):
			cur = node.Node(x + delt, y + 28, z + 5)
			if self._check_valid(x + delt, y + 28, z + 5, cur):
				self.matrix[x + delt][y + 28][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 50, y + 29, z + 5) -> (x + 51, y + 29, z + 5)
		for delt in range(50, 52):
			cur = node.Node(x + delt, y + 29, z + 5)
			if self._check_valid(x + delt, y + 29, z + 5, cur):
				self.matrix[x + delt][y + 29][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 51, y + 30, z + 5) -> (x + 53, y + 30, z + 5)
		for delt in range(51, 54):
			cur = node.Node(x + delt, y + 30, z + 5)
			if self._check_valid(x + delt, y + 30, z + 5, cur):
				self.matrix[x + delt][y + 30][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 53, y + 31, z + 5) -> (x + 55, y + 31, z + 5)
		for delt in range(53, 56):
			cur = node.Node(x + delt, y + 31, z + 5)
			if self._check_valid(x + delt, y + 31, z + 5, cur):
				self.matrix[x + delt][y + 31][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 55, y + 32, z + 5) -> (x + 55, y + 32, z + 5)
		for delt in range(55, 56):
			cur = node.Node(x + delt, y + 32, z + 5)
			if self._check_valid(x + delt, y + 32, z + 5, cur):
				self.matrix[x + delt][y + 32][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)


	def _case_3_4(self, x, y, z):

		# (x, y, z) -> (x + 1, y, z)
		for delt in range(2):
			cur = node.Node(x + delt, y, z)
			if self._check_valid(x + delt, y, z, cur):
				self.matrix[x + delt][y][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 1, y + 1, z) -> (x + 3, y + 1, z)
		for delt in range(1, 4):
			cur = node.Node(x + delt, y + 1, z)
			if self._check_valid(x + delt, y + 1, z, cur):
				self.matrix[x + delt][y + 1][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 3, y + 2, z) -> (x + 5, y + 2, z)
		for delt in range(3, 6):
			cur = node.Node(x + delt, y + 2, z)
			if self._check_valid(x + delt, y + 2, z, cur):
				self.matrix[x + delt][y + 2][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 5, y + 3, z) -> (x + 6, y + 3, z)
		for delt in range(5, 7):
			cur = node.Node(x + delt, y + 3, z)
			if self._check_valid(x + delt, y + 3, z, cur):
				self.matrix[x + delt][y + 3][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 6, y + 4, z) -> (x + 8, y + 4, z)
		for delt in range(6, 9):
			cur = node.Node(x + delt, y + 4, z)
			if self._check_valid(x + delt, y + 4, z, cur):
				self.matrix[x + delt][y + 4][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 8, y + 5, z) -> (x + 9, y + 5, z)
		for delt in range(8, 10):
			cur = node.Node(x + delt, y + 5, z)
			if self._check_valid(x + delt, y + 5, z, cur):
				self.matrix[x + delt][y + 5][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 9, y + 5, z + 1) -> (x + 10, y + 5, z + 1)
		for delt in range(9, 11):
			cur = node.Node(x + delt, y + 5, z + 1)
			if self._check_valid(x + delt, y + 5, z + 1, cur):
				self.matrix[x + delt][y + 5][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 10, y + 6, z + 1) -> (x + 12, y + 6, z + 1)
		for delt in range(10, 13):
			cur = node.Node(x + delt, y + 6, z + 1)
			if self._check_valid(x + delt, y + 6, z + 1, cur):
				self.matrix[x + delt][y + 6][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 12, y + 7, z + 1) -> (x + 13, y + 7, z + 1)
		for delt in range(12, 14):
			cur = node.Node(x + delt, y + 7, z + 1)
			if self._check_valid(x + delt, y + 7, z + 1, cur):
				self.matrix[x + delt][y + 7][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 13, y + 8, z + 1) -> (x + 15, y + 8, z + 1)
		for delt in range(13, 16):
			cur = node.Node(x + delt, y + 8, z + 1)
			if self._check_valid(x + delt, y + 8, z + 1, cur):
				self.matrix[x + delt][y + 8][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 15, y + 9, z + 1) -> (x + 17, y + 9, z + 1)
		for delt in range(15, 18):
			cur = node.Node(x + delt, y + 9, z + 1)
			if self._check_valid(x + delt, y + 9, z + 1, cur):
				self.matrix[x + delt][y + 9][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 17, y + 10, z + 1) -> (x + 19, y + 10, z + 1)
		for delt in range(17, 20):
			cur = node.Node(x + delt, y + 10, z + 1)
			if self._check_valid(x + delt, y + 10, z + 1, cur):
				self.matrix[x + delt][y + 10][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 19, y + 11, z + 1) -> (x + 19, y + 11, z + 1)
		for delt in range(19, 20):
			cur = node.Node(x + delt, y + 11, z + 1)
			if self._check_valid(x + delt, y + 11, z + 1, cur):
				self.matrix[x + delt][y + 11][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 19, y + 11, z + 2) -> (x + 20, y + 11, z + 2)
		for delt in range(19, 21):
			cur = node.Node(x + delt, y + 11, z + 2)
			if self._check_valid(x + delt, y + 11, z + 2, cur):
				self.matrix[x + delt][y + 11][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 20, y + 12, z + 2) -> (x + 22, y + 12, z + 2)
		for delt in range(20, 23):
			cur = node.Node(x + delt, y + 12, z + 2)
			if self._check_valid(x + delt, y + 12, z + 2, cur):
				self.matrix[x + delt][y + 12][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 22, y + 13, z + 2) -> (x + 24, y + 13, z + 2)
		for delt in range(22, 25):
			cur = node.Node(x + delt, y + 13, z + 2)
			if self._check_valid(x + delt, y + 13, z + 2, cur):
				self.matrix[x + delt][y + 13][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 24, y + 14, z + 2) -> (x + 25, y + 14, z + 2)
		for delt in range(24, 26):
			cur = node.Node(x + delt, y + 14, z + 2)
			if self._check_valid(x + delt, y + 14, z + 2, cur):
				self.matrix[x + delt][y + 14][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 25, y + 15, z + 2) -> (x + 27, y + 15, z + 2)
		for delt in range(25, 28):
			cur = node.Node(x + delt, y + 15, z + 2)
			if self._check_valid(x + delt, y + 15, z + 2, cur):
				self.matrix[x + delt][y + 15][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 27, y + 16, z + 2) -> (x + 28, y + 16, z + 2)
		for delt in range(27, 29):
			cur = node.Node(x + delt, y + 16, z + 2)
			if self._check_valid(x + delt, y + 16, z + 2, cur):
				self.matrix[x + delt][y + 16][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 28, y + 16, z + 3) -> (x + 29, y + 16, z + 3)
		for delt in range(28, 30):
			cur = node.Node(x + delt, y + 16, z + 3)
			if self._check_valid(x + delt, y + 16, z + 3, cur):
				self.matrix[x + delt][y + 16][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 29, y + 17, z + 3) -> (x + 31, y + 17, z + 3)
		for delt in range(29, 32):
			cur = node.Node(x + delt, y + 17, z + 3)
			if self._check_valid(x + delt, y + 17, z + 3, cur):
				self.matrix[x + delt][y + 17][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 31, y + 18, z + 3) -> (x + 32, y + 18, z + 3)
		for delt in range(31, 33):
			cur = node.Node(x + delt, y + 18, z + 3)
			if self._check_valid(x + delt, y + 18, z + 3, cur):
				self.matrix[x + delt][y + 18][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 32, y + 19, z + 3) -> (x + 34, y + 19, z + 3)
		for delt in range(32, 35):
			cur = node.Node(x + delt, y + 19, z + 3)
			if self._check_valid(x + delt, y + 19, z + 3, cur):
				self.matrix[x + delt][y + 19][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 34, y + 20, z + 3) -> (x + 36, y + 20, z + 3)
		for delt in range(34, 37):
			cur = node.Node(x + delt, y + 20, z + 3)
			if self._check_valid(x + delt, y + 20, z + 3, cur):
				self.matrix[x + delt][y + 20][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 36, y + 21, z + 3) -> (x + 38, y + 21, z + 3)
		for delt in range(36, 39):
			cur = node.Node(x + delt, y + 21, z + 3)
			if self._check_valid(x + delt, y + 21, z + 3, cur):
				self.matrix[x + delt][y + 21][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 38, y + 22, z + 3) -> (x + 38, y + 22, z + 3)
		for delt in range(38, 39):
			cur = node.Node(x + delt, y + 22, z + 3)
			if self._check_valid(x + delt, y + 22, z + 3, cur):
				self.matrix[x + delt][y + 22][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 38, y + 22, z + 4) -> (x + 39, y + 22, z + 4)
		for delt in range(38, 40):
			cur = node.Node(x + delt, y + 22, z + 4)
			if self._check_valid(x + delt, y + 22, z + 4, cur):
				self.matrix[x + delt][y + 22][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 39, y + 23, z + 4) -> (x + 41, y + 23, z + 4)
		for delt in range(39, 42):
			cur = node.Node(x + delt, y + 23, z + 4)
			if self._check_valid(x + delt, y + 23, z + 4, cur):
				self.matrix[x + delt][y + 23][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 41, y + 24, z + 4) -> (x + 43, y + 24, z + 4)
		for delt in range(41, 44):
			cur = node.Node(x + delt, y + 24, z + 4)
			if self._check_valid(x + delt, y + 24, z + 4, cur):
				self.matrix[x + delt][y + 24][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 43, y + 25, z + 4) -> (x + 44, y + 25, z + 4)
		for delt in range(43, 45):
			cur = node.Node(x + delt, y + 25, z + 4)
			if self._check_valid(x + delt, y + 25, z + 4, cur):
				self.matrix[x + delt][y + 25][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 44, y + 26, z + 4) -> (x + 46, y + 26, z + 4)
		for delt in range(44, 47):
			cur = node.Node(x + delt, y + 26, z + 4)
			if self._check_valid(x + delt, y + 26, z + 4, cur):
				self.matrix[x + delt][y + 26][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 46, y + 27, z + 4) -> (x + 47, y + 27, z + 4)
		for delt in range(46, 48):
			cur = node.Node(x + delt, y + 27, z + 4)
			if self._check_valid(x + delt, y + 27, z + 4, cur):
				self.matrix[x + delt][y + 27][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 47, y + 27, z + 5) -> (x + 48, y + 27, z + 5)
		for delt in range(47, 49):
			cur = node.Node(x + delt, y + 27, z + 5)
			if self._check_valid(x + delt, y + 27, z + 5, cur):
				self.matrix[x + delt][y + 27][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 48, y + 28, z + 5) -> (x + 50, y + 28, z + 5)
		for delt in range(48, 51):
			cur = node.Node(x + delt, y + 28, z + 5)
			if self._check_valid(x + delt, y + 28, z + 5, cur):
				self.matrix[x + delt][y + 28][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 50, y + 29, z + 5) -> (x + 51, y + 29, z + 5)
		for delt in range(50, 52):
			cur = node.Node(x + delt, y + 29, z + 5)
			if self._check_valid(x + delt, y + 29, z + 5, cur):
				self.matrix[x + delt][y + 29][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 51, y + 30, z + 5) -> (x + 53, y + 30, z + 5)
		for delt in range(51, 54):
			cur = node.Node(x + delt, y + 30, z + 5)
			if self._check_valid(x + delt, y + 30, z + 5, cur):
				self.matrix[x + delt][y + 30][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 53, y + 31, z + 5) -> (x + 55, y + 31, z + 5)
		for delt in range(53, 56):
			cur = node.Node(x + delt, y + 31, z + 5)
			if self._check_valid(x + delt, y + 31, z + 5, cur):
				self.matrix[x + delt][y + 31][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 55, y + 32, z + 5) -> (x + 57, y + 32, z + 5)
		for delt in range(55, 58):
			cur = node.Node(x + delt, y + 32, z + 5)
			if self._check_valid(x + delt, y + 32, z + 5, cur):
				self.matrix[x + delt][y + 32][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 57, y + 33, z + 5) -> (x + 58, y + 33, z + 5)
		for delt in range(57, 59):
			cur = node.Node(x + delt, y + 33, z + 5)
			if self._check_valid(x + delt, y + 33, z + 5, cur):
				self.matrix[x + delt][y + 33][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 58, y + 34, z + 5) -> (x + 60, y + 34, z + 5)
		for delt in range(58, 61):
			cur = node.Node(x + delt, y + 34, z + 5)
			if self._check_valid(x + delt, y + 34, z + 5, cur):
				self.matrix[x + delt][y + 34][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 60, y + 35, z + 5) -> (x + 61, y + 35, z + 5)
		for delt in range(60, 62):
			cur = node.Node(x + delt, y + 35, z + 5)
			if self._check_valid(x + delt, y + 35, z + 5, cur):
				self.matrix[x + delt][y + 35][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 61, y + 35, z + 6) -> (x + 62, y + 35, z + 6)
		for delt in range(61, 63):
			cur = node.Node(x + delt, y + 35, z + 6)
			if self._check_valid(x + delt, y + 35, z + 6, cur):
				self.matrix[x + delt][y + 35][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 62, y + 36, z + 6) -> (x + 64, y + 36, z + 6)
		for delt in range(62, 65):
			cur = node.Node(x + delt, y + 36, z + 6)
			if self._check_valid(x + delt, y + 36, z + 6, cur):
				self.matrix[x + delt][y + 36][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 64, y + 37, z + 6) -> (x + 65, y + 37, z + 6)
		for delt in range(64, 66):
			cur = node.Node(x + delt, y + 37, z + 6)
			if self._check_valid(x + delt, y + 37, z + 6, cur):
				self.matrix[x + delt][y + 37][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 65, y + 38, z + 6) -> (x + 67, y + 38, z + 6)
		for delt in range(65, 68):
			cur = node.Node(x + delt, y + 38, z + 6)
			if self._check_valid(x + delt, y + 38, z + 6, cur):
				self.matrix[x + delt][y + 38][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 67, y + 39, z + 6) -> (x + 69, y + 39, z + 6)
		for delt in range(67, 70):
			cur = node.Node(x + delt, y + 39, z + 6)
			if self._check_valid(x + delt, y + 39, z + 6, cur):
				self.matrix[x + delt][y + 39][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 69, y + 40, z + 6) -> (x + 69, y + 40, z + 6)
		for delt in range(69, 70):
			cur = node.Node(x + delt, y + 40, z + 6)
			if self._check_valid(x + delt, y + 40, z + 6, cur):
				self.matrix[x + delt][y + 40][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 69, y + 40, z + 7) -> (x + 70, y + 40, z + 7)
		for delt in range(69, 71):
			cur = node.Node(x + delt, y + 40, z + 7)
			if self._check_valid(x + delt, y + 40, z + 7, cur):
				self.matrix[x + delt][y + 40][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 70, y + 41, z + 7) -> (x + 72, y + 41, z + 7)
		for delt in range(70, 73):
			cur = node.Node(x + delt, y + 41, z + 7)
			if self._check_valid(x + delt, y + 41, z + 7, cur):
				self.matrix[x + delt][y + 41][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 72, y + 42, z + 7) -> (x + 74, y + 42, z + 7)
		for delt in range(72, 75):
			cur = node.Node(x + delt, y + 42, z + 7)
			if self._check_valid(x + delt, y + 42, z + 7, cur):
				self.matrix[x + delt][y + 42][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 74, y + 43, z + 7) -> (x + 75, y + 43, z + 7)
		for delt in range(74, 76):
			cur = node.Node(x + delt, y + 43, z + 7)
			if self._check_valid(x + delt, y + 43, z + 7, cur):
				self.matrix[x + delt][y + 43][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 75, y + 44, z + 7) -> (x + 77, y + 44, z + 7)
		for delt in range(75, 78):
			cur = node.Node(x + delt, y + 44, z + 7)
			if self._check_valid(x + delt, y + 44, z + 7, cur):
				self.matrix[x + delt][y + 44][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 77, y + 45, z + 7) -> (x + 78, y + 45, z + 7)
		for delt in range(77, 79):
			cur = node.Node(x + delt, y + 45, z + 7)
			if self._check_valid(x + delt, y + 45, z + 7, cur):
				self.matrix[x + delt][y + 45][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 78, y + 45, z + 8) -> (x + 79, y + 45, z + 8)
		for delt in range(78, 80):
			cur = node.Node(x + delt, y + 45, z + 8)
			if self._check_valid(x + delt, y + 45, z + 8, cur):
				self.matrix[x + delt][y + 45][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 79, y + 46, z + 8) -> (x + 81, y + 46, z + 8)
		for delt in range(79, 82):
			cur = node.Node(x + delt, y + 46, z + 8)
			if self._check_valid(x + delt, y + 46, z + 8, cur):
				self.matrix[x + delt][y + 46][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 81, y + 47, z + 8) -> (x + 82, y + 47, z + 8)
		for delt in range(81, 83):
			cur = node.Node(x + delt, y + 47, z + 8)
			if self._check_valid(x + delt, y + 47, z + 8, cur):
				self.matrix[x + delt][y + 47][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 82, y + 48, z + 8) -> (x + 84, y + 48, z + 8)
		for delt in range(82, 85):
			cur = node.Node(x + delt, y + 48, z + 8)
			if self._check_valid(x + delt, y + 48, z + 8, cur):
				self.matrix[x + delt][y + 48][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 84, y + 49, z + 8) -> (x + 86, y + 49, z + 8)
		for delt in range(84, 87):
			cur = node.Node(x + delt, y + 49, z + 8)
			if self._check_valid(x + delt, y + 49, z + 8, cur):
				self.matrix[x + delt][y + 49][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 86, y + 50, z + 8) -> (x + 86, y + 50, z + 8)
		for delt in range(86, 87):
			cur = node.Node(x + delt, y + 50, z + 8)
			if self._check_valid(x + delt, y + 50, z + 8, cur):
				self.matrix[x + delt][y + 50][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)


	def _case_3_5(self, x, y, z):

		# (x, y, z) -> (x + 1, y, z)
		for delt in range(2):
			cur = node.Node(x + delt, y, z)
			if self._check_valid(x + delt, y, z, cur):
				self.matrix[x + delt][y][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 1, y + 1, z) -> (x + 3, y + 1, z)
		for delt in range(1, 4):
			cur = node.Node(x + delt, y + 1, z)
			if self._check_valid(x + delt, y + 1, z, cur):
				self.matrix[x + delt][y + 1][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 3, y + 2, z) -> (x + 5, y + 2, z)
		for delt in range(3, 6):
			cur = node.Node(x + delt, y + 2, z)
			if self._check_valid(x + delt, y + 2, z, cur):
				self.matrix[x + delt][y + 2][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 5, y + 3, z) -> (x + 6, y + 3, z)
		for delt in range(5, 7):
			cur = node.Node(x + delt, y + 3, z)
			if self._check_valid(x + delt, y + 3, z, cur):
				self.matrix[x + delt][y + 3][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 6, y + 4, z) -> (x + 8, y + 4, z)
		for delt in range(6, 9):
			cur = node.Node(x + delt, y + 4, z)
			if self._check_valid(x + delt, y + 4, z, cur):
				self.matrix[x + delt][y + 4][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 8, y + 5, z) -> (x + 9, y + 5, z)
		for delt in range(8, 10):
			cur = node.Node(x + delt, y + 5, z)
			if self._check_valid(x + delt, y + 5, z, cur):
				self.matrix[x + delt][y + 5][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 9, y + 5, z + 1) -> (x + 10, y + 5, z + 1)
		for delt in range(9, 11):
			cur = node.Node(x + delt, y + 5, z + 1)
			if self._check_valid(x + delt, y + 5, z + 1, cur):
				self.matrix[x + delt][y + 5][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 10, y + 6, z + 1) -> (x + 12, y + 6, z + 1)
		for delt in range(10, 13):
			cur = node.Node(x + delt, y + 6, z + 1)
			if self._check_valid(x + delt, y + 6, z + 1, cur):
				self.matrix[x + delt][y + 6][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 12, y + 7, z + 1) -> (x + 13, y + 7, z + 1)
		for delt in range(12, 14):
			cur = node.Node(x + delt, y + 7, z + 1)
			if self._check_valid(x + delt, y + 7, z + 1, cur):
				self.matrix[x + delt][y + 7][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 13, y + 8, z + 1) -> (x + 15, y + 8, z + 1)
		for delt in range(13, 16):
			cur = node.Node(x + delt, y + 8, z + 1)
			if self._check_valid(x + delt, y + 8, z + 1, cur):
				self.matrix[x + delt][y + 8][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 15, y + 9, z + 1) -> (x + 17, y + 9, z + 1)
		for delt in range(15, 18):
			cur = node.Node(x + delt, y + 9, z + 1)
			if self._check_valid(x + delt, y + 9, z + 1, cur):
				self.matrix[x + delt][y + 9][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 17, y + 10, z + 1) -> (x + 19, y + 10, z + 1)
		for delt in range(17, 20):
			cur = node.Node(x + delt, y + 10, z + 1)
			if self._check_valid(x + delt, y + 10, z + 1, cur):
				self.matrix[x + delt][y + 10][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 19, y + 11, z + 1) -> (x + 19, y + 11, z + 1)
		for delt in range(19, 20):
			cur = node.Node(x + delt, y + 11, z + 1)
			if self._check_valid(x + delt, y + 11, z + 1, cur):
				self.matrix[x + delt][y + 11][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 19, y + 11, z + 2) -> (x + 20, y + 11, z + 2)
		for delt in range(19, 21):
			cur = node.Node(x + delt, y + 11, z + 2)
			if self._check_valid(x + delt, y + 11, z + 2, cur):
				self.matrix[x + delt][y + 11][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 20, y + 12, z + 2) -> (x + 22, y + 12, z + 2)
		for delt in range(20, 23):
			cur = node.Node(x + delt, y + 12, z + 2)
			if self._check_valid(x + delt, y + 12, z + 2, cur):
				self.matrix[x + delt][y + 12][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 22, y + 13, z + 2) -> (x + 24, y + 13, z + 2)
		for delt in range(22, 25):
			cur = node.Node(x + delt, y + 13, z + 2)
			if self._check_valid(x + delt, y + 13, z + 2, cur):
				self.matrix[x + delt][y + 13][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 24, y + 14, z + 2) -> (x + 25, y + 14, z + 2)
		for delt in range(24, 26):
			cur = node.Node(x + delt, y + 14, z + 2)
			if self._check_valid(x + delt, y + 14, z + 2, cur):
				self.matrix[x + delt][y + 14][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 25, y + 15, z + 2) -> (x + 27, y + 15, z + 2)
		for delt in range(25, 28):
			cur = node.Node(x + delt, y + 15, z + 2)
			if self._check_valid(x + delt, y + 15, z + 2, cur):
				self.matrix[x + delt][y + 15][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 27, y + 16, z + 2) -> (x + 28, y + 16, z + 2)
		for delt in range(27, 29):
			cur = node.Node(x + delt, y + 16, z + 2)
			if self._check_valid(x + delt, y + 16, z + 2, cur):
				self.matrix[x + delt][y + 16][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 28, y + 16, z + 3) -> (x + 29, y + 16, z + 3)
		for delt in range(28, 30):
			cur = node.Node(x + delt, y + 16, z + 3)
			if self._check_valid(x + delt, y + 16, z + 3, cur):
				self.matrix[x + delt][y + 16][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 29, y + 17, z + 3) -> (x + 31, y + 17, z + 3)
		for delt in range(29, 32):
			cur = node.Node(x + delt, y + 17, z + 3)
			if self._check_valid(x + delt, y + 17, z + 3, cur):
				self.matrix[x + delt][y + 17][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 31, y + 18, z + 3) -> (x + 32, y + 18, z + 3)
		for delt in range(31, 33):
			cur = node.Node(x + delt, y + 18, z + 3)
			if self._check_valid(x + delt, y + 18, z + 3, cur):
				self.matrix[x + delt][y + 18][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 32, y + 19, z + 3) -> (x + 34, y + 19, z + 3)
		for delt in range(32, 35):
			cur = node.Node(x + delt, y + 19, z + 3)
			if self._check_valid(x + delt, y + 19, z + 3, cur):
				self.matrix[x + delt][y + 19][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 34, y + 20, z + 3) -> (x + 36, y + 20, z + 3)
		for delt in range(34, 37):
			cur = node.Node(x + delt, y + 20, z + 3)
			if self._check_valid(x + delt, y + 20, z + 3, cur):
				self.matrix[x + delt][y + 20][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 36, y + 21, z + 3) -> (x + 38, y + 21, z + 3)
		for delt in range(36, 39):
			cur = node.Node(x + delt, y + 21, z + 3)
			if self._check_valid(x + delt, y + 21, z + 3, cur):
				self.matrix[x + delt][y + 21][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 38, y + 22, z + 3) -> (x + 38, y + 22, z + 3)
		for delt in range(38, 39):
			cur = node.Node(x + delt, y + 22, z + 3)
			if self._check_valid(x + delt, y + 22, z + 3, cur):
				self.matrix[x + delt][y + 22][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 38, y + 22, z + 4) -> (x + 39, y + 22, z + 4)
		for delt in range(38, 40):
			cur = node.Node(x + delt, y + 22, z + 4)
			if self._check_valid(x + delt, y + 22, z + 4, cur):
				self.matrix[x + delt][y + 22][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 39, y + 23, z + 4) -> (x + 41, y + 23, z + 4)
		for delt in range(39, 42):
			cur = node.Node(x + delt, y + 23, z + 4)
			if self._check_valid(x + delt, y + 23, z + 4, cur):
				self.matrix[x + delt][y + 23][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 41, y + 24, z + 4) -> (x + 43, y + 24, z + 4)
		for delt in range(41, 44):
			cur = node.Node(x + delt, y + 24, z + 4)
			if self._check_valid(x + delt, y + 24, z + 4, cur):
				self.matrix[x + delt][y + 24][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 43, y + 25, z + 4) -> (x + 44, y + 25, z + 4)
		for delt in range(43, 45):
			cur = node.Node(x + delt, y + 25, z + 4)
			if self._check_valid(x + delt, y + 25, z + 4, cur):
				self.matrix[x + delt][y + 25][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 44, y + 26, z + 4) -> (x + 46, y + 26, z + 4)
		for delt in range(44, 47):
			cur = node.Node(x + delt, y + 26, z + 4)
			if self._check_valid(x + delt, y + 26, z + 4, cur):
				self.matrix[x + delt][y + 26][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 46, y + 27, z + 4) -> (x + 47, y + 27, z + 4)
		for delt in range(46, 48):
			cur = node.Node(x + delt, y + 27, z + 4)
			if self._check_valid(x + delt, y + 27, z + 4, cur):
				self.matrix[x + delt][y + 27][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 47, y + 27, z + 5) -> (x + 48, y + 27, z + 5)
		for delt in range(47, 49):
			cur = node.Node(x + delt, y + 27, z + 5)
			if self._check_valid(x + delt, y + 27, z + 5, cur):
				self.matrix[x + delt][y + 27][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 48, y + 28, z + 5) -> (x + 50, y + 28, z + 5)
		for delt in range(48, 51):
			cur = node.Node(x + delt, y + 28, z + 5)
			if self._check_valid(x + delt, y + 28, z + 5, cur):
				self.matrix[x + delt][y + 28][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 50, y + 29, z + 5) -> (x + 51, y + 29, z + 5)
		for delt in range(50, 52):
			cur = node.Node(x + delt, y + 29, z + 5)
			if self._check_valid(x + delt, y + 29, z + 5, cur):
				self.matrix[x + delt][y + 29][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 51, y + 30, z + 5) -> (x + 53, y + 30, z + 5)
		for delt in range(51, 54):
			cur = node.Node(x + delt, y + 30, z + 5)
			if self._check_valid(x + delt, y + 30, z + 5, cur):
				self.matrix[x + delt][y + 30][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 53, y + 31, z + 5) -> (x + 55, y + 31, z + 5)
		for delt in range(53, 56):
			cur = node.Node(x + delt, y + 31, z + 5)
			if self._check_valid(x + delt, y + 31, z + 5, cur):
				self.matrix[x + delt][y + 31][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 55, y + 32, z + 5) -> (x + 57, y + 32, z + 5)
		for delt in range(55, 58):
			cur = node.Node(x + delt, y + 32, z + 5)
			if self._check_valid(x + delt, y + 32, z + 5, cur):
				self.matrix[x + delt][y + 32][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 57, y + 33, z + 5) -> (x + 58, y + 33, z + 5)
		for delt in range(57, 59):
			cur = node.Node(x + delt, y + 33, z + 5)
			if self._check_valid(x + delt, y + 33, z + 5, cur):
				self.matrix[x + delt][y + 33][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 58, y + 34, z + 5) -> (x + 60, y + 34, z + 5)
		for delt in range(58, 61):
			cur = node.Node(x + delt, y + 34, z + 5)
			if self._check_valid(x + delt, y + 34, z + 5, cur):
				self.matrix[x + delt][y + 34][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 60, y + 35, z + 5) -> (x + 61, y + 35, z + 5)
		for delt in range(60, 62):
			cur = node.Node(x + delt, y + 35, z + 5)
			if self._check_valid(x + delt, y + 35, z + 5, cur):
				self.matrix[x + delt][y + 35][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 61, y + 35, z + 6) -> (x + 62, y + 35, z + 6)
		for delt in range(61, 63):
			cur = node.Node(x + delt, y + 35, z + 6)
			if self._check_valid(x + delt, y + 35, z + 6, cur):
				self.matrix[x + delt][y + 35][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 62, y + 36, z + 6) -> (x + 64, y + 36, z + 6)
		for delt in range(62, 65):
			cur = node.Node(x + delt, y + 36, z + 6)
			if self._check_valid(x + delt, y + 36, z + 6, cur):
				self.matrix[x + delt][y + 36][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 64, y + 37, z + 6) -> (x + 65, y + 37, z + 6)
		for delt in range(64, 66):
			cur = node.Node(x + delt, y + 37, z + 6)
			if self._check_valid(x + delt, y + 37, z + 6, cur):
				self.matrix[x + delt][y + 37][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 65, y + 38, z + 6) -> (x + 67, y + 38, z + 6)
		for delt in range(65, 68):
			cur = node.Node(x + delt, y + 38, z + 6)
			if self._check_valid(x + delt, y + 38, z + 6, cur):
				self.matrix[x + delt][y + 38][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 67, y + 39, z + 6) -> (x + 69, y + 39, z + 6)
		for delt in range(67, 70):
			cur = node.Node(x + delt, y + 39, z + 6)
			if self._check_valid(x + delt, y + 39, z + 6, cur):
				self.matrix[x + delt][y + 39][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 69, y + 40, z + 6) -> (x + 69, y + 40, z + 6)
		for delt in range(69, 70):
			cur = node.Node(x + delt, y + 40, z + 6)
			if self._check_valid(x + delt, y + 40, z + 6, cur):
				self.matrix[x + delt][y + 40][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 69, y + 40, z + 7) -> (x + 70, y + 40, z + 7)
		for delt in range(69, 71):
			cur = node.Node(x + delt, y + 40, z + 7)
			if self._check_valid(x + delt, y + 40, z + 7, cur):
				self.matrix[x + delt][y + 40][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 70, y + 41, z + 7) -> (x + 72, y + 41, z + 7)
		for delt in range(70, 73):
			cur = node.Node(x + delt, y + 41, z + 7)
			if self._check_valid(x + delt, y + 41, z + 7, cur):
				self.matrix[x + delt][y + 41][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 72, y + 42, z + 7) -> (x + 74, y + 42, z + 7)
		for delt in range(72, 75):
			cur = node.Node(x + delt, y + 42, z + 7)
			if self._check_valid(x + delt, y + 42, z + 7, cur):
				self.matrix[x + delt][y + 42][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 74, y + 43, z + 7) -> (x + 75, y + 43, z + 7)
		for delt in range(74, 76):
			cur = node.Node(x + delt, y + 43, z + 7)
			if self._check_valid(x + delt, y + 43, z + 7, cur):
				self.matrix[x + delt][y + 43][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 75, y + 44, z + 7) -> (x + 77, y + 44, z + 7)
		for delt in range(75, 78):
			cur = node.Node(x + delt, y + 44, z + 7)
			if self._check_valid(x + delt, y + 44, z + 7, cur):
				self.matrix[x + delt][y + 44][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 77, y + 45, z + 7) -> (x + 78, y + 45, z + 7)
		for delt in range(77, 79):
			cur = node.Node(x + delt, y + 45, z + 7)
			if self._check_valid(x + delt, y + 45, z + 7, cur):
				self.matrix[x + delt][y + 45][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 78, y + 45, z + 8) -> (x + 79, y + 45, z + 8)
		for delt in range(78, 80):
			cur = node.Node(x + delt, y + 45, z + 8)
			if self._check_valid(x + delt, y + 45, z + 8, cur):
				self.matrix[x + delt][y + 45][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 79, y + 46, z + 8) -> (x + 81, y + 46, z + 8)
		for delt in range(79, 82):
			cur = node.Node(x + delt, y + 46, z + 8)
			if self._check_valid(x + delt, y + 46, z + 8, cur):
				self.matrix[x + delt][y + 46][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 81, y + 47, z + 8) -> (x + 82, y + 47, z + 8)
		for delt in range(81, 83):
			cur = node.Node(x + delt, y + 47, z + 8)
			if self._check_valid(x + delt, y + 47, z + 8, cur):
				self.matrix[x + delt][y + 47][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 82, y + 48, z + 8) -> (x + 84, y + 48, z + 8)
		for delt in range(82, 85):
			cur = node.Node(x + delt, y + 48, z + 8)
			if self._check_valid(x + delt, y + 48, z + 8, cur):
				self.matrix[x + delt][y + 48][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 84, y + 49, z + 8) -> (x + 86, y + 49, z + 8)
		for delt in range(84, 87):
			cur = node.Node(x + delt, y + 49, z + 8)
			if self._check_valid(x + delt, y + 49, z + 8, cur):
				self.matrix[x + delt][y + 49][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 86, y + 50, z + 8) -> (x + 86, y + 50, z + 8)
		for delt in range(86, 87):
			cur = node.Node(x + delt, y + 50, z + 8)
			if self._check_valid(x + delt, y + 50, z + 8, cur):
				self.matrix[x + delt][y + 50][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 86, y + 50, z + 8) -> (x + 88, y + 50, z + 8)
		for delt in range(86, 89):
			self._common_cal(x, y, z, delt, 50, 8)

		# (x + 88, y + 51, z + 8) -> (x + 89, y + 51, z + 8)
		for delt in range(89, 90):
			self._common_cal(x, y, z, delt, 51, 8)

		# (x + 90, y + 51, z + 9) -> (x + 91, y + 51, z + 9)
		for delt in range(90, 92):
			self._common_cal(x, y, z, delt, 51, 9)

		# (x + 91, y + 52, z + 9) -> (x + 93, y + 52, z + 9)
		for delt in range(91, 94):
			self._common_cal(x, y, z, delt, 52, 9)

		# (x + 93, y + 53, z + 9) -> (x + 94, y + 53, z + 9)
		for delt in range(93, 95):
			self._common_cal(x, y, z, delt, 53, 9)

		# (x + 94, y + 54, z + 9) -> (x + 96, y + 54, z + 9)
		for delt in range(94, 97):
			self._common_cal(x, y, z, delt, 54, 9)

		# (x + 96, y + 55, z + 9) -> (x + 98, y + 55, z + 9)
		for delt in range(96, 99):
			self._common_cal(x, y, z, delt, 55, 9)

		# (x + 98, y + 56, z + 9) -> (x + 99, y + 56, z + 9)
		for delt in range(98, 100):
			self._common_cal(x, y, z, delt, 56, 9)

		# (x + 99, y + 57, z + 9) -> (x + 99, y + 57, z + 9)
		for delt in range(99, 100):
			self._common_cal(x, y, z, delt, 57, 9)

		# (x + 99, y + 57, z + 10) -> (x + 100, y + 57, z + 10)
		for delt in range(99, 101):
			self._common_cal(x, y, z, delt, 57, 10)

		# (x + 100, y + 58, z + 10) -> (x + 102, y + 58, z + 10)
		for delt in range(100, 103):
			self._common_cal(x, y, z, delt, 58, 10)

		# (x + 102, y + 59, z + 10) -> (x + 104, y + 59, z + 10)
		for delt in range(102, 105):
			self._common_cal(x, y, z, delt, 59, 10)

		# (x + 104, y + 60, z + 10) -> (x + 105, y + 60, z + 10)
		for delt in range(104, 106):
			self._common_cal(x, y, z, delt, 60, 10)

		# (x + 105, y + 61, z + 10) -> (x + 107, y + 61, z + 10)
		for delt in range(105, 108):
			self._common_cal(x, y, z, delt, 61, 10)

		# (x + 107, y + 62, z + 10) -> (x + 108, y + 62, z + 10)
		for delt in range(107, 109):
			self._common_cal(x, y, z, delt, 62, 10)

		# (x + 108, y + 62, z + 11) -> (x + 108, y + 62, z + 11)
		for delt in range(108, 109):
			self._common_cal(x, y, z, delt, 62, 11)


	def _case_3_6(self, x, y, z):

		# (x, y, z) -> (x + 1, y, z)
		for delt in range(2):
			cur = node.Node(x + delt, y, z)
			if self._check_valid(x + delt, y, z, cur):
				self.matrix[x + delt][y][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 1, y + 1, z) -> (x + 3, y + 1, z)
		for delt in range(1, 4):
			cur = node.Node(x + delt, y + 1, z)
			if self._check_valid(x + delt, y + 1, z, cur):
				self.matrix[x + delt][y + 1][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 3, y + 2, z) -> (x + 5, y + 2, z)
		for delt in range(3, 6):
			cur = node.Node(x + delt, y + 2, z)
			if self._check_valid(x + delt, y + 2, z, cur):
				self.matrix[x + delt][y + 2][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 5, y + 3, z) -> (x + 6, y + 3, z)
		for delt in range(5, 7):
			cur = node.Node(x + delt, y + 3, z)
			if self._check_valid(x + delt, y + 3, z, cur):
				self.matrix[x + delt][y + 3][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 6, y + 4, z) -> (x + 8, y + 4, z)
		for delt in range(6, 9):
			cur = node.Node(x + delt, y + 4, z)
			if self._check_valid(x + delt, y + 4, z, cur):
				self.matrix[x + delt][y + 4][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 8, y + 5, z) -> (x + 9, y + 5, z)
		for delt in range(8, 10):
			cur = node.Node(x + delt, y + 5, z)
			if self._check_valid(x + delt, y + 5, z, cur):
				self.matrix[x + delt][y + 5][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 9, y + 5, z + 1) -> (x + 10, y + 5, z + 1)
		for delt in range(9, 11):
			cur = node.Node(x + delt, y + 5, z + 1)
			if self._check_valid(x + delt, y + 5, z + 1, cur):
				self.matrix[x + delt][y + 5][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 10, y + 6, z + 1) -> (x + 12, y + 6, z + 1)
		for delt in range(10, 13):
			cur = node.Node(x + delt, y + 6, z + 1)
			if self._check_valid(x + delt, y + 6, z + 1, cur):
				self.matrix[x + delt][y + 6][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 12, y + 7, z + 1) -> (x + 13, y + 7, z + 1)
		for delt in range(12, 14):
			cur = node.Node(x + delt, y + 7, z + 1)
			if self._check_valid(x + delt, y + 7, z + 1, cur):
				self.matrix[x + delt][y + 7][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 13, y + 8, z + 1) -> (x + 15, y + 8, z + 1)
		for delt in range(13, 16):
			cur = node.Node(x + delt, y + 8, z + 1)
			if self._check_valid(x + delt, y + 8, z + 1, cur):
				self.matrix[x + delt][y + 8][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 15, y + 9, z + 1) -> (x + 17, y + 9, z + 1)
		for delt in range(15, 18):
			cur = node.Node(x + delt, y + 9, z + 1)
			if self._check_valid(x + delt, y + 9, z + 1, cur):
				self.matrix[x + delt][y + 9][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 17, y + 10, z + 1) -> (x + 19, y + 10, z + 1)
		for delt in range(17, 20):
			cur = node.Node(x + delt, y + 10, z + 1)
			if self._check_valid(x + delt, y + 10, z + 1, cur):
				self.matrix[x + delt][y + 10][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 19, y + 11, z + 1) -> (x + 19, y + 11, z + 1)
		for delt in range(19, 20):
			cur = node.Node(x + delt, y + 11, z + 1)
			if self._check_valid(x + delt, y + 11, z + 1, cur):
				self.matrix[x + delt][y + 11][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 19, y + 11, z + 2) -> (x + 20, y + 11, z + 2)
		for delt in range(19, 21):
			cur = node.Node(x + delt, y + 11, z + 2)
			if self._check_valid(x + delt, y + 11, z + 2, cur):
				self.matrix[x + delt][y + 11][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 20, y + 12, z + 2) -> (x + 22, y + 12, z + 2)
		for delt in range(20, 23):
			cur = node.Node(x + delt, y + 12, z + 2)
			if self._check_valid(x + delt, y + 12, z + 2, cur):
				self.matrix[x + delt][y + 12][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 22, y + 13, z + 2) -> (x + 24, y + 13, z + 2)
		for delt in range(22, 25):
			cur = node.Node(x + delt, y + 13, z + 2)
			if self._check_valid(x + delt, y + 13, z + 2, cur):
				self.matrix[x + delt][y + 13][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 24, y + 14, z + 2) -> (x + 25, y + 14, z + 2)
		for delt in range(24, 26):
			cur = node.Node(x + delt, y + 14, z + 2)
			if self._check_valid(x + delt, y + 14, z + 2, cur):
				self.matrix[x + delt][y + 14][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 25, y + 15, z + 2) -> (x + 27, y + 15, z + 2)
		for delt in range(25, 28):
			cur = node.Node(x + delt, y + 15, z + 2)
			if self._check_valid(x + delt, y + 15, z + 2, cur):
				self.matrix[x + delt][y + 15][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 27, y + 16, z + 2) -> (x + 28, y + 16, z + 2)
		for delt in range(27, 29):
			cur = node.Node(x + delt, y + 16, z + 2)
			if self._check_valid(x + delt, y + 16, z + 2, cur):
				self.matrix[x + delt][y + 16][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 28, y + 16, z + 3) -> (x + 29, y + 16, z + 3)
		for delt in range(28, 30):
			cur = node.Node(x + delt, y + 16, z + 3)
			if self._check_valid(x + delt, y + 16, z + 3, cur):
				self.matrix[x + delt][y + 16][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 29, y + 17, z + 3) -> (x + 31, y + 17, z + 3)
		for delt in range(29, 32):
			cur = node.Node(x + delt, y + 17, z + 3)
			if self._check_valid(x + delt, y + 17, z + 3, cur):
				self.matrix[x + delt][y + 17][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 31, y + 18, z + 3) -> (x + 32, y + 18, z + 3)
		for delt in range(31, 33):
			cur = node.Node(x + delt, y + 18, z + 3)
			if self._check_valid(x + delt, y + 18, z + 3, cur):
				self.matrix[x + delt][y + 18][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 32, y + 19, z + 3) -> (x + 34, y + 19, z + 3)
		for delt in range(32, 35):
			cur = node.Node(x + delt, y + 19, z + 3)
			if self._check_valid(x + delt, y + 19, z + 3, cur):
				self.matrix[x + delt][y + 19][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 34, y + 20, z + 3) -> (x + 36, y + 20, z + 3)
		for delt in range(34, 37):
			cur = node.Node(x + delt, y + 20, z + 3)
			if self._check_valid(x + delt, y + 20, z + 3, cur):
				self.matrix[x + delt][y + 20][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 36, y + 21, z + 3) -> (x + 38, y + 21, z + 3)
		for delt in range(36, 39):
			cur = node.Node(x + delt, y + 21, z + 3)
			if self._check_valid(x + delt, y + 21, z + 3, cur):
				self.matrix[x + delt][y + 21][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 38, y + 22, z + 3) -> (x + 38, y + 22, z + 3)
		for delt in range(38, 39):
			cur = node.Node(x + delt, y + 22, z + 3)
			if self._check_valid(x + delt, y + 22, z + 3, cur):
				self.matrix[x + delt][y + 22][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 38, y + 22, z + 4) -> (x + 39, y + 22, z + 4)
		for delt in range(38, 40):
			cur = node.Node(x + delt, y + 22, z + 4)
			if self._check_valid(x + delt, y + 22, z + 4, cur):
				self.matrix[x + delt][y + 22][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 39, y + 23, z + 4) -> (x + 41, y + 23, z + 4)
		for delt in range(39, 42):
			cur = node.Node(x + delt, y + 23, z + 4)
			if self._check_valid(x + delt, y + 23, z + 4, cur):
				self.matrix[x + delt][y + 23][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 41, y + 24, z + 4) -> (x + 43, y + 24, z + 4)
		for delt in range(41, 44):
			cur = node.Node(x + delt, y + 24, z + 4)
			if self._check_valid(x + delt, y + 24, z + 4, cur):
				self.matrix[x + delt][y + 24][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 43, y + 25, z + 4) -> (x + 44, y + 25, z + 4)
		for delt in range(43, 45):
			cur = node.Node(x + delt, y + 25, z + 4)
			if self._check_valid(x + delt, y + 25, z + 4, cur):
				self.matrix[x + delt][y + 25][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 44, y + 26, z + 4) -> (x + 46, y + 26, z + 4)
		for delt in range(44, 47):
			cur = node.Node(x + delt, y + 26, z + 4)
			if self._check_valid(x + delt, y + 26, z + 4, cur):
				self.matrix[x + delt][y + 26][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 46, y + 27, z + 4) -> (x + 47, y + 27, z + 4)
		for delt in range(46, 48):
			cur = node.Node(x + delt, y + 27, z + 4)
			if self._check_valid(x + delt, y + 27, z + 4, cur):
				self.matrix[x + delt][y + 27][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 47, y + 27, z + 5) -> (x + 48, y + 27, z + 5)
		for delt in range(47, 49):
			cur = node.Node(x + delt, y + 27, z + 5)
			if self._check_valid(x + delt, y + 27, z + 5, cur):
				self.matrix[x + delt][y + 27][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 48, y + 28, z + 5) -> (x + 50, y + 28, z + 5)
		for delt in range(48, 51):
			cur = node.Node(x + delt, y + 28, z + 5)
			if self._check_valid(x + delt, y + 28, z + 5, cur):
				self.matrix[x + delt][y + 28][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 50, y + 29, z + 5) -> (x + 51, y + 29, z + 5)
		for delt in range(50, 52):
			cur = node.Node(x + delt, y + 29, z + 5)
			if self._check_valid(x + delt, y + 29, z + 5, cur):
				self.matrix[x + delt][y + 29][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 51, y + 30, z + 5) -> (x + 53, y + 30, z + 5)
		for delt in range(51, 54):
			cur = node.Node(x + delt, y + 30, z + 5)
			if self._check_valid(x + delt, y + 30, z + 5, cur):
				self.matrix[x + delt][y + 30][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 53, y + 31, z + 5) -> (x + 55, y + 31, z + 5)
		for delt in range(53, 56):
			cur = node.Node(x + delt, y + 31, z + 5)
			if self._check_valid(x + delt, y + 31, z + 5, cur):
				self.matrix[x + delt][y + 31][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 55, y + 32, z + 5) -> (x + 57, y + 32, z + 5)
		for delt in range(55, 58):
			cur = node.Node(x + delt, y + 32, z + 5)
			if self._check_valid(x + delt, y + 32, z + 5, cur):
				self.matrix[x + delt][y + 32][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 57, y + 33, z + 5) -> (x + 58, y + 33, z + 5)
		for delt in range(57, 59):
			cur = node.Node(x + delt, y + 33, z + 5)
			if self._check_valid(x + delt, y + 33, z + 5, cur):
				self.matrix[x + delt][y + 33][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 58, y + 34, z + 5) -> (x + 60, y + 34, z + 5)
		for delt in range(58, 61):
			cur = node.Node(x + delt, y + 34, z + 5)
			if self._check_valid(x + delt, y + 34, z + 5, cur):
				self.matrix[x + delt][y + 34][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 60, y + 35, z + 5) -> (x + 61, y + 35, z + 5)
		for delt in range(60, 62):
			cur = node.Node(x + delt, y + 35, z + 5)
			if self._check_valid(x + delt, y + 35, z + 5, cur):
				self.matrix[x + delt][y + 35][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 61, y + 35, z + 6) -> (x + 62, y + 35, z + 6)
		for delt in range(61, 63):
			cur = node.Node(x + delt, y + 35, z + 6)
			if self._check_valid(x + delt, y + 35, z + 6, cur):
				self.matrix[x + delt][y + 35][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 62, y + 36, z + 6) -> (x + 64, y + 36, z + 6)
		for delt in range(62, 65):
			cur = node.Node(x + delt, y + 36, z + 6)
			if self._check_valid(x + delt, y + 36, z + 6, cur):
				self.matrix[x + delt][y + 36][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 64, y + 37, z + 6) -> (x + 65, y + 37, z + 6)
		for delt in range(64, 66):
			cur = node.Node(x + delt, y + 37, z + 6)
			if self._check_valid(x + delt, y + 37, z + 6, cur):
				self.matrix[x + delt][y + 37][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 65, y + 38, z + 6) -> (x + 67, y + 38, z + 6)
		for delt in range(65, 68):
			cur = node.Node(x + delt, y + 38, z + 6)
			if self._check_valid(x + delt, y + 38, z + 6, cur):
				self.matrix[x + delt][y + 38][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 67, y + 39, z + 6) -> (x + 69, y + 39, z + 6)
		for delt in range(67, 70):
			cur = node.Node(x + delt, y + 39, z + 6)
			if self._check_valid(x + delt, y + 39, z + 6, cur):
				self.matrix[x + delt][y + 39][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 69, y + 40, z + 6) -> (x + 69, y + 40, z + 6)
		for delt in range(69, 70):
			cur = node.Node(x + delt, y + 40, z + 6)
			if self._check_valid(x + delt, y + 40, z + 6, cur):
				self.matrix[x + delt][y + 40][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 69, y + 40, z + 7) -> (x + 70, y + 40, z + 7)
		for delt in range(69, 71):
			cur = node.Node(x + delt, y + 40, z + 7)
			if self._check_valid(x + delt, y + 40, z + 7, cur):
				self.matrix[x + delt][y + 40][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 70, y + 41, z + 7) -> (x + 72, y + 41, z + 7)
		for delt in range(70, 73):
			cur = node.Node(x + delt, y + 41, z + 7)
			if self._check_valid(x + delt, y + 41, z + 7, cur):
				self.matrix[x + delt][y + 41][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 72, y + 42, z + 7) -> (x + 74, y + 42, z + 7)
		for delt in range(72, 75):
			cur = node.Node(x + delt, y + 42, z + 7)
			if self._check_valid(x + delt, y + 42, z + 7, cur):
				self.matrix[x + delt][y + 42][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 74, y + 43, z + 7) -> (x + 75, y + 43, z + 7)
		for delt in range(74, 76):
			cur = node.Node(x + delt, y + 43, z + 7)
			if self._check_valid(x + delt, y + 43, z + 7, cur):
				self.matrix[x + delt][y + 43][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 75, y + 44, z + 7) -> (x + 77, y + 44, z + 7)
		for delt in range(75, 78):
			cur = node.Node(x + delt, y + 44, z + 7)
			if self._check_valid(x + delt, y + 44, z + 7, cur):
				self.matrix[x + delt][y + 44][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 77, y + 45, z + 7) -> (x + 78, y + 45, z + 7)
		for delt in range(77, 79):
			cur = node.Node(x + delt, y + 45, z + 7)
			if self._check_valid(x + delt, y + 45, z + 7, cur):
				self.matrix[x + delt][y + 45][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 78, y + 45, z + 8) -> (x + 79, y + 45, z + 8)
		for delt in range(78, 80):
			cur = node.Node(x + delt, y + 45, z + 8)
			if self._check_valid(x + delt, y + 45, z + 8, cur):
				self.matrix[x + delt][y + 45][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 79, y + 46, z + 8) -> (x + 81, y + 46, z + 8)
		for delt in range(79, 82):
			cur = node.Node(x + delt, y + 46, z + 8)
			if self._check_valid(x + delt, y + 46, z + 8, cur):
				self.matrix[x + delt][y + 46][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 81, y + 47, z + 8) -> (x + 82, y + 47, z + 8)
		for delt in range(81, 83):
			cur = node.Node(x + delt, y + 47, z + 8)
			if self._check_valid(x + delt, y + 47, z + 8, cur):
				self.matrix[x + delt][y + 47][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 82, y + 48, z + 8) -> (x + 84, y + 48, z + 8)
		for delt in range(82, 85):
			cur = node.Node(x + delt, y + 48, z + 8)
			if self._check_valid(x + delt, y + 48, z + 8, cur):
				self.matrix[x + delt][y + 48][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 84, y + 49, z + 8) -> (x + 86, y + 49, z + 8)
		for delt in range(84, 87):
			cur = node.Node(x + delt, y + 49, z + 8)
			if self._check_valid(x + delt, y + 49, z + 8, cur):
				self.matrix[x + delt][y + 49][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 86, y + 50, z + 8) -> (x + 86, y + 50, z + 8)
		for delt in range(86, 87):
			cur = node.Node(x + delt, y + 50, z + 8)
			if self._check_valid(x + delt, y + 50, z + 8, cur):
				self.matrix[x + delt][y + 50][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 86, y + 50, z + 8) -> (x + 88, y + 50, z + 8)
		for delt in range(86, 89):
			self._common_cal(x, y, z, delt, 50, 8)

		# (x + 88, y + 51, z + 8) -> (x + 89, y + 51, z + 8)
		for delt in range(89, 90):
			self._common_cal(x, y, z, delt, 51, 8)

		# (x + 90, y + 51, z + 9) -> (x + 91, y + 51, z + 9)
		for delt in range(90, 92):
			self._common_cal(x, y, z, delt, 51, 9)

		# (x + 91, y + 52, z + 9) -> (x + 93, y + 52, z + 9)
		for delt in range(91, 94):
			self._common_cal(x, y, z, delt, 52, 9)

		# (x + 93, y + 53, z + 9) -> (x + 94, y + 53, z + 9)
		for delt in range(93, 95):
			self._common_cal(x, y, z, delt, 53, 9)

		# (x + 94, y + 54, z + 9) -> (x + 96, y + 54, z + 9)
		for delt in range(94, 97):
			self._common_cal(x, y, z, delt, 54, 9)

		# (x + 96, y + 55, z + 9) -> (x + 98, y + 55, z + 9)
		for delt in range(96, 99):
			self._common_cal(x, y, z, delt, 55, 9)

		# (x + 98, y + 56, z + 9) -> (x + 99, y + 56, z + 9)
		for delt in range(98, 100):
			self._common_cal(x, y, z, delt, 56, 9)

		# (x + 99, y + 57, z + 9) -> (x + 99, y + 57, z + 9)
		for delt in range(99, 100):
			self._common_cal(x, y, z, delt, 57, 9)

		# (x + 99, y + 57, z + 10) -> (x + 100, y + 57, z + 10)
		for delt in range(99, 101):
			self._common_cal(x, y, z, delt, 57, 10)

		# (x + 100, y + 58, z + 10) -> (x + 102, y + 58, z + 10)
		for delt in range(100, 103):
			self._common_cal(x, y, z, delt, 58, 10)

		# (x + 102, y + 59, z + 10) -> (x + 104, y + 59, z + 10)
		for delt in range(102, 105):
			self._common_cal(x, y, z, delt, 59, 10)

		# (x + 104, y + 60, z + 10) -> (x + 105, y + 60, z + 10)
		for delt in range(104, 106):
			self._common_cal(x, y, z, delt, 60, 10)

		# (x + 105, y + 61, z + 10) -> (x + 107, y + 61, z + 10)
		for delt in range(105, 108):
			self._common_cal(x, y, z, delt, 61, 10)

		# (x + 107, y + 62, z + 10) -> (x + 108, y + 62, z + 10)
		for delt in range(107, 109):
			self._common_cal(x, y, z, delt, 62, 10)

		# (x + 108, y + 62, z + 11) -> (x + 108, y + 62, z + 11)
		for delt in range(108, 109):
			self._common_cal(x, y, z, delt, 62, 11)

		# (x + 110, y + 64, z + 11) -> (x + 112, y + 64, z + 11)
		for delt in range(110, 113):
			self._common_cal(x, y, z, delt, 64, 11)

		# (x + 112, y + 65, z + 11) -> (x + 114, y + 65, z + 11)
		for delt in range(112, 115):
			self._common_cal(x, y, z, delt, 65, 11)

		# (x + 114, y + 66, z + 11) -> (x + 115, y + 66, z + 11)
		for delt in range(114, 116):
			self._common_cal(x, y, z, delt, 66, 11)

		# (x + 115, y + 67, z + 11) -> (x + 117, y + 67, z + 11)
		for delt in range(115, 118):
			self._common_cal(x, y, z, delt, 67, 11)			

		# (x + 117, y + 68, z + 11) -> (x + 118, y + 68, z + 11)
		for delt in range(117, 119):
			self._common_cal(x, y, z, delt, 68, 11)

		# (x + 118, y + 68, z + 12) -> (x + 119, y + 68, z + 12)
		for delt in range(118, 120):
			self._common_cal(x, y, z, delt, 68, 12)					

		# (x + 119, y + 69, z + 12) -> (x + 121, y + 69, z + 12)
		for delt in range(119, 122):
			self._common_cal(x, y, z, delt, 69, 12)		

		# (x + 121, y + 70, z + 12) -> (x + 122, y + 70, z + 12)
		for delt in range(121, 123):
			self._common_cal(x, y, z, delt, 70, 12)	

		# (x + 122, y + 71, z + 12) -> (x + 124, y + 71, z + 12)
		for delt in range(122, 125):
			self._common_cal(x, y, z, delt, 71, 12)					

		# (x + 124, y + 72, z + 12) -> (x + 126, y + 72, z + 12)
		for delt in range(124, 127):
			self._common_cal(x, y, z, delt, 72, 12)	

		# (x + 126, y + 73, z + 12) -> (x + 126, y + 73, z + 12)
		for delt in range(126, 127):
			self._common_cal(x, y, z, delt, 73, 12)	

	
	def _case_3_7(self, x, y, z):

		# (x, y, z) -> (x + 1, y, z)
		for delt in range(2):
			cur = node.Node(x + delt, y, z)
			if self._check_valid(x + delt, y, z, cur):
				self.matrix[x + delt][y][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 1, y + 1, z) -> (x + 3, y + 1, z)
		for delt in range(1, 4):
			cur = node.Node(x + delt, y + 1, z)
			if self._check_valid(x + delt, y + 1, z, cur):
				self.matrix[x + delt][y + 1][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 3, y + 2, z) -> (x + 5, y + 2, z)
		for delt in range(3, 6):
			cur = node.Node(x + delt, y + 2, z)
			if self._check_valid(x + delt, y + 2, z, cur):
				self.matrix[x + delt][y + 2][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 5, y + 3, z) -> (x + 6, y + 3, z)
		for delt in range(5, 7):
			cur = node.Node(x + delt, y + 3, z)
			if self._check_valid(x + delt, y + 3, z, cur):
				self.matrix[x + delt][y + 3][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 6, y + 4, z) -> (x + 8, y + 4, z)
		for delt in range(6, 9):
			cur = node.Node(x + delt, y + 4, z)
			if self._check_valid(x + delt, y + 4, z, cur):
				self.matrix[x + delt][y + 4][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 8, y + 5, z) -> (x + 9, y + 5, z)
		for delt in range(8, 10):
			cur = node.Node(x + delt, y + 5, z)
			if self._check_valid(x + delt, y + 5, z, cur):
				self.matrix[x + delt][y + 5][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 9, y + 5, z + 1) -> (x + 10, y + 5, z + 1)
		for delt in range(9, 11):
			cur = node.Node(x + delt, y + 5, z + 1)
			if self._check_valid(x + delt, y + 5, z + 1, cur):
				self.matrix[x + delt][y + 5][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 10, y + 6, z + 1) -> (x + 12, y + 6, z + 1)
		for delt in range(10, 13):
			cur = node.Node(x + delt, y + 6, z + 1)
			if self._check_valid(x + delt, y + 6, z + 1, cur):
				self.matrix[x + delt][y + 6][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 12, y + 7, z + 1) -> (x + 13, y + 7, z + 1)
		for delt in range(12, 14):
			cur = node.Node(x + delt, y + 7, z + 1)
			if self._check_valid(x + delt, y + 7, z + 1, cur):
				self.matrix[x + delt][y + 7][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 13, y + 8, z + 1) -> (x + 15, y + 8, z + 1)
		for delt in range(13, 16):
			cur = node.Node(x + delt, y + 8, z + 1)
			if self._check_valid(x + delt, y + 8, z + 1, cur):
				self.matrix[x + delt][y + 8][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 15, y + 9, z + 1) -> (x + 17, y + 9, z + 1)
		for delt in range(15, 18):
			cur = node.Node(x + delt, y + 9, z + 1)
			if self._check_valid(x + delt, y + 9, z + 1, cur):
				self.matrix[x + delt][y + 9][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 17, y + 10, z + 1) -> (x + 19, y + 10, z + 1)
		for delt in range(17, 20):
			cur = node.Node(x + delt, y + 10, z + 1)
			if self._check_valid(x + delt, y + 10, z + 1, cur):
				self.matrix[x + delt][y + 10][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 19, y + 11, z + 1) -> (x + 19, y + 11, z + 1)
		for delt in range(19, 20):
			cur = node.Node(x + delt, y + 11, z + 1)
			if self._check_valid(x + delt, y + 11, z + 1, cur):
				self.matrix[x + delt][y + 11][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 19, y + 11, z + 2) -> (x + 20, y + 11, z + 2)
		for delt in range(19, 21):
			cur = node.Node(x + delt, y + 11, z + 2)
			if self._check_valid(x + delt, y + 11, z + 2, cur):
				self.matrix[x + delt][y + 11][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 20, y + 12, z + 2) -> (x + 22, y + 12, z + 2)
		for delt in range(20, 23):
			cur = node.Node(x + delt, y + 12, z + 2)
			if self._check_valid(x + delt, y + 12, z + 2, cur):
				self.matrix[x + delt][y + 12][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 22, y + 13, z + 2) -> (x + 24, y + 13, z + 2)
		for delt in range(22, 25):
			cur = node.Node(x + delt, y + 13, z + 2)
			if self._check_valid(x + delt, y + 13, z + 2, cur):
				self.matrix[x + delt][y + 13][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 24, y + 14, z + 2) -> (x + 25, y + 14, z + 2)
		for delt in range(24, 26):
			cur = node.Node(x + delt, y + 14, z + 2)
			if self._check_valid(x + delt, y + 14, z + 2, cur):
				self.matrix[x + delt][y + 14][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 25, y + 15, z + 2) -> (x + 27, y + 15, z + 2)
		for delt in range(25, 28):
			cur = node.Node(x + delt, y + 15, z + 2)
			if self._check_valid(x + delt, y + 15, z + 2, cur):
				self.matrix[x + delt][y + 15][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 27, y + 16, z + 2) -> (x + 28, y + 16, z + 2)
		for delt in range(27, 29):
			cur = node.Node(x + delt, y + 16, z + 2)
			if self._check_valid(x + delt, y + 16, z + 2, cur):
				self.matrix[x + delt][y + 16][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 28, y + 16, z + 3) -> (x + 29, y + 16, z + 3)
		for delt in range(28, 30):
			cur = node.Node(x + delt, y + 16, z + 3)
			if self._check_valid(x + delt, y + 16, z + 3, cur):
				self.matrix[x + delt][y + 16][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 29, y + 17, z + 3) -> (x + 31, y + 17, z + 3)
		for delt in range(29, 32):
			cur = node.Node(x + delt, y + 17, z + 3)
			if self._check_valid(x + delt, y + 17, z + 3, cur):
				self.matrix[x + delt][y + 17][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 31, y + 18, z + 3) -> (x + 32, y + 18, z + 3)
		for delt in range(31, 33):
			cur = node.Node(x + delt, y + 18, z + 3)
			if self._check_valid(x + delt, y + 18, z + 3, cur):
				self.matrix[x + delt][y + 18][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 32, y + 19, z + 3) -> (x + 34, y + 19, z + 3)
		for delt in range(32, 35):
			cur = node.Node(x + delt, y + 19, z + 3)
			if self._check_valid(x + delt, y + 19, z + 3, cur):
				self.matrix[x + delt][y + 19][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 34, y + 20, z + 3) -> (x + 36, y + 20, z + 3)
		for delt in range(34, 37):
			cur = node.Node(x + delt, y + 20, z + 3)
			if self._check_valid(x + delt, y + 20, z + 3, cur):
				self.matrix[x + delt][y + 20][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 36, y + 21, z + 3) -> (x + 38, y + 21, z + 3)
		for delt in range(36, 39):
			cur = node.Node(x + delt, y + 21, z + 3)
			if self._check_valid(x + delt, y + 21, z + 3, cur):
				self.matrix[x + delt][y + 21][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 38, y + 22, z + 3) -> (x + 38, y + 22, z + 3)
		for delt in range(38, 39):
			cur = node.Node(x + delt, y + 22, z + 3)
			if self._check_valid(x + delt, y + 22, z + 3, cur):
				self.matrix[x + delt][y + 22][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 38, y + 22, z + 4) -> (x + 39, y + 22, z + 4)
		for delt in range(38, 40):
			cur = node.Node(x + delt, y + 22, z + 4)
			if self._check_valid(x + delt, y + 22, z + 4, cur):
				self.matrix[x + delt][y + 22][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 39, y + 23, z + 4) -> (x + 41, y + 23, z + 4)
		for delt in range(39, 42):
			cur = node.Node(x + delt, y + 23, z + 4)
			if self._check_valid(x + delt, y + 23, z + 4, cur):
				self.matrix[x + delt][y + 23][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 41, y + 24, z + 4) -> (x + 43, y + 24, z + 4)
		for delt in range(41, 44):
			cur = node.Node(x + delt, y + 24, z + 4)
			if self._check_valid(x + delt, y + 24, z + 4, cur):
				self.matrix[x + delt][y + 24][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 43, y + 25, z + 4) -> (x + 44, y + 25, z + 4)
		for delt in range(43, 45):
			cur = node.Node(x + delt, y + 25, z + 4)
			if self._check_valid(x + delt, y + 25, z + 4, cur):
				self.matrix[x + delt][y + 25][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 44, y + 26, z + 4) -> (x + 46, y + 26, z + 4)
		for delt in range(44, 47):
			cur = node.Node(x + delt, y + 26, z + 4)
			if self._check_valid(x + delt, y + 26, z + 4, cur):
				self.matrix[x + delt][y + 26][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 46, y + 27, z + 4) -> (x + 47, y + 27, z + 4)
		for delt in range(46, 48):
			cur = node.Node(x + delt, y + 27, z + 4)
			if self._check_valid(x + delt, y + 27, z + 4, cur):
				self.matrix[x + delt][y + 27][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 47, y + 27, z + 5) -> (x + 48, y + 27, z + 5)
		for delt in range(47, 49):
			cur = node.Node(x + delt, y + 27, z + 5)
			if self._check_valid(x + delt, y + 27, z + 5, cur):
				self.matrix[x + delt][y + 27][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 48, y + 28, z + 5) -> (x + 50, y + 28, z + 5)
		for delt in range(48, 51):
			cur = node.Node(x + delt, y + 28, z + 5)
			if self._check_valid(x + delt, y + 28, z + 5, cur):
				self.matrix[x + delt][y + 28][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 50, y + 29, z + 5) -> (x + 51, y + 29, z + 5)
		for delt in range(50, 52):
			cur = node.Node(x + delt, y + 29, z + 5)
			if self._check_valid(x + delt, y + 29, z + 5, cur):
				self.matrix[x + delt][y + 29][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 51, y + 30, z + 5) -> (x + 53, y + 30, z + 5)
		for delt in range(51, 54):
			cur = node.Node(x + delt, y + 30, z + 5)
			if self._check_valid(x + delt, y + 30, z + 5, cur):
				self.matrix[x + delt][y + 30][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 53, y + 31, z + 5) -> (x + 55, y + 31, z + 5)
		for delt in range(53, 56):
			cur = node.Node(x + delt, y + 31, z + 5)
			if self._check_valid(x + delt, y + 31, z + 5, cur):
				self.matrix[x + delt][y + 31][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 55, y + 32, z + 5) -> (x + 57, y + 32, z + 5)
		for delt in range(55, 58):
			cur = node.Node(x + delt, y + 32, z + 5)
			if self._check_valid(x + delt, y + 32, z + 5, cur):
				self.matrix[x + delt][y + 32][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 57, y + 33, z + 5) -> (x + 58, y + 33, z + 5)
		for delt in range(57, 59):
			cur = node.Node(x + delt, y + 33, z + 5)
			if self._check_valid(x + delt, y + 33, z + 5, cur):
				self.matrix[x + delt][y + 33][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 58, y + 34, z + 5) -> (x + 60, y + 34, z + 5)
		for delt in range(58, 61):
			cur = node.Node(x + delt, y + 34, z + 5)
			if self._check_valid(x + delt, y + 34, z + 5, cur):
				self.matrix[x + delt][y + 34][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 60, y + 35, z + 5) -> (x + 61, y + 35, z + 5)
		for delt in range(60, 62):
			cur = node.Node(x + delt, y + 35, z + 5)
			if self._check_valid(x + delt, y + 35, z + 5, cur):
				self.matrix[x + delt][y + 35][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 61, y + 35, z + 6) -> (x + 62, y + 35, z + 6)
		for delt in range(61, 63):
			cur = node.Node(x + delt, y + 35, z + 6)
			if self._check_valid(x + delt, y + 35, z + 6, cur):
				self.matrix[x + delt][y + 35][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 62, y + 36, z + 6) -> (x + 64, y + 36, z + 6)
		for delt in range(62, 65):
			cur = node.Node(x + delt, y + 36, z + 6)
			if self._check_valid(x + delt, y + 36, z + 6, cur):
				self.matrix[x + delt][y + 36][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 64, y + 37, z + 6) -> (x + 65, y + 37, z + 6)
		for delt in range(64, 66):
			cur = node.Node(x + delt, y + 37, z + 6)
			if self._check_valid(x + delt, y + 37, z + 6, cur):
				self.matrix[x + delt][y + 37][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 65, y + 38, z + 6) -> (x + 67, y + 38, z + 6)
		for delt in range(65, 68):
			cur = node.Node(x + delt, y + 38, z + 6)
			if self._check_valid(x + delt, y + 38, z + 6, cur):
				self.matrix[x + delt][y + 38][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 67, y + 39, z + 6) -> (x + 69, y + 39, z + 6)
		for delt in range(67, 70):
			cur = node.Node(x + delt, y + 39, z + 6)
			if self._check_valid(x + delt, y + 39, z + 6, cur):
				self.matrix[x + delt][y + 39][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 69, y + 40, z + 6) -> (x + 69, y + 40, z + 6)
		for delt in range(69, 70):
			cur = node.Node(x + delt, y + 40, z + 6)
			if self._check_valid(x + delt, y + 40, z + 6, cur):
				self.matrix[x + delt][y + 40][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 69, y + 40, z + 7) -> (x + 70, y + 40, z + 7)
		for delt in range(69, 71):
			cur = node.Node(x + delt, y + 40, z + 7)
			if self._check_valid(x + delt, y + 40, z + 7, cur):
				self.matrix[x + delt][y + 40][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 70, y + 41, z + 7) -> (x + 72, y + 41, z + 7)
		for delt in range(70, 73):
			cur = node.Node(x + delt, y + 41, z + 7)
			if self._check_valid(x + delt, y + 41, z + 7, cur):
				self.matrix[x + delt][y + 41][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 72, y + 42, z + 7) -> (x + 74, y + 42, z + 7)
		for delt in range(72, 75):
			cur = node.Node(x + delt, y + 42, z + 7)
			if self._check_valid(x + delt, y + 42, z + 7, cur):
				self.matrix[x + delt][y + 42][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 74, y + 43, z + 7) -> (x + 75, y + 43, z + 7)
		for delt in range(74, 76):
			cur = node.Node(x + delt, y + 43, z + 7)
			if self._check_valid(x + delt, y + 43, z + 7, cur):
				self.matrix[x + delt][y + 43][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 75, y + 44, z + 7) -> (x + 77, y + 44, z + 7)
		for delt in range(75, 78):
			cur = node.Node(x + delt, y + 44, z + 7)
			if self._check_valid(x + delt, y + 44, z + 7, cur):
				self.matrix[x + delt][y + 44][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 77, y + 45, z + 7) -> (x + 78, y + 45, z + 7)
		for delt in range(77, 79):
			cur = node.Node(x + delt, y + 45, z + 7)
			if self._check_valid(x + delt, y + 45, z + 7, cur):
				self.matrix[x + delt][y + 45][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 78, y + 45, z + 8) -> (x + 79, y + 45, z + 8)
		for delt in range(78, 80):
			cur = node.Node(x + delt, y + 45, z + 8)
			if self._check_valid(x + delt, y + 45, z + 8, cur):
				self.matrix[x + delt][y + 45][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 79, y + 46, z + 8) -> (x + 81, y + 46, z + 8)
		for delt in range(79, 82):
			cur = node.Node(x + delt, y + 46, z + 8)
			if self._check_valid(x + delt, y + 46, z + 8, cur):
				self.matrix[x + delt][y + 46][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 81, y + 47, z + 8) -> (x + 82, y + 47, z + 8)
		for delt in range(81, 83):
			cur = node.Node(x + delt, y + 47, z + 8)
			if self._check_valid(x + delt, y + 47, z + 8, cur):
				self.matrix[x + delt][y + 47][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 82, y + 48, z + 8) -> (x + 84, y + 48, z + 8)
		for delt in range(82, 85):
			cur = node.Node(x + delt, y + 48, z + 8)
			if self._check_valid(x + delt, y + 48, z + 8, cur):
				self.matrix[x + delt][y + 48][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 84, y + 49, z + 8) -> (x + 86, y + 49, z + 8)
		for delt in range(84, 87):
			cur = node.Node(x + delt, y + 49, z + 8)
			if self._check_valid(x + delt, y + 49, z + 8, cur):
				self.matrix[x + delt][y + 49][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 86, y + 50, z + 8) -> (x + 86, y + 50, z + 8)
		for delt in range(86, 87):
			cur = node.Node(x + delt, y + 50, z + 8)
			if self._check_valid(x + delt, y + 50, z + 8, cur):
				self.matrix[x + delt][y + 50][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 86, y + 50, z + 8) -> (x + 88, y + 50, z + 8)
		for delt in range(86, 89):
			self._common_cal(x, y, z, delt, 50, 8)

		# (x + 88, y + 51, z + 8) -> (x + 89, y + 51, z + 8)
		for delt in range(89, 90):
			self._common_cal(x, y, z, delt, 51, 8)

		# (x + 90, y + 51, z + 9) -> (x + 91, y + 51, z + 9)
		for delt in range(90, 92):
			self._common_cal(x, y, z, delt, 51, 9)

		# (x + 91, y + 52, z + 9) -> (x + 93, y + 52, z + 9)
		for delt in range(91, 94):
			self._common_cal(x, y, z, delt, 52, 9)

		# (x + 93, y + 53, z + 9) -> (x + 94, y + 53, z + 9)
		for delt in range(93, 95):
			self._common_cal(x, y, z, delt, 53, 9)

		# (x + 94, y + 54, z + 9) -> (x + 96, y + 54, z + 9)
		for delt in range(94, 97):
			self._common_cal(x, y, z, delt, 54, 9)

		# (x + 96, y + 55, z + 9) -> (x + 98, y + 55, z + 9)
		for delt in range(96, 99):
			self._common_cal(x, y, z, delt, 55, 9)

		# (x + 98, y + 56, z + 9) -> (x + 99, y + 56, z + 9)
		for delt in range(98, 100):
			self._common_cal(x, y, z, delt, 56, 9)

		# (x + 99, y + 57, z + 9) -> (x + 99, y + 57, z + 9)
		for delt in range(99, 100):
			self._common_cal(x, y, z, delt, 57, 9)

		# (x + 99, y + 57, z + 10) -> (x + 100, y + 57, z + 10)
		for delt in range(99, 101):
			self._common_cal(x, y, z, delt, 57, 10)

		# (x + 100, y + 58, z + 10) -> (x + 102, y + 58, z + 10)
		for delt in range(100, 103):
			self._common_cal(x, y, z, delt, 58, 10)

		# (x + 102, y + 59, z + 10) -> (x + 104, y + 59, z + 10)
		for delt in range(102, 105):
			self._common_cal(x, y, z, delt, 59, 10)

		# (x + 104, y + 60, z + 10) -> (x + 105, y + 60, z + 10)
		for delt in range(104, 106):
			self._common_cal(x, y, z, delt, 60, 10)

		# (x + 105, y + 61, z + 10) -> (x + 107, y + 61, z + 10)
		for delt in range(105, 108):
			self._common_cal(x, y, z, delt, 61, 10)

		# (x + 107, y + 62, z + 10) -> (x + 108, y + 62, z + 10)
		for delt in range(107, 109):
			self._common_cal(x, y, z, delt, 62, 10)

		# (x + 108, y + 62, z + 11) -> (x + 108, y + 62, z + 11)
		for delt in range(108, 109):
			self._common_cal(x, y, z, delt, 62, 11)

		# (x + 110, y + 64, z + 11) -> (x + 112, y + 64, z + 11)
		for delt in range(110, 113):
			self._common_cal(x, y, z, delt, 64, 11)

		# (x + 112, y + 65, z + 11) -> (x + 114, y + 65, z + 11)
		for delt in range(112, 115):
			self._common_cal(x, y, z, delt, 65, 11)

		# (x + 114, y + 66, z + 11) -> (x + 115, y + 66, z + 11)
		for delt in range(114, 116):
			self._common_cal(x, y, z, delt, 66, 11)

		# (x + 115, y + 67, z + 11) -> (x + 117, y + 67, z + 11)
		for delt in range(115, 118):
			self._common_cal(x, y, z, delt, 67, 11)			

		# (x + 117, y + 68, z + 11) -> (x + 118, y + 68, z + 11)
		for delt in range(117, 119):
			self._common_cal(x, y, z, delt, 68, 11)

		# (x + 118, y + 68, z + 12) -> (x + 119, y + 68, z + 12)
		for delt in range(118, 120):
			self._common_cal(x, y, z, delt, 68, 12)					

		# (x + 119, y + 69, z + 12) -> (x + 121, y + 69, z + 12)
		for delt in range(119, 122):
			self._common_cal(x, y, z, delt, 69, 12)		

		# (x + 121, y + 70, z + 12) -> (x + 122, y + 70, z + 12)
		for delt in range(121, 123):
			self._common_cal(x, y, z, delt, 70, 12)	

		# (x + 122, y + 71, z + 12) -> (x + 124, y + 71, z + 12)
		for delt in range(122, 125):
			self._common_cal(x, y, z, delt, 71, 12)					

		# (x + 124, y + 72, z + 12) -> (x + 126, y + 72, z + 12)
		for delt in range(124, 127):
			self._common_cal(x, y, z, delt, 72, 12)	

		# (x + 126, y + 73, z + 12) -> (x + 126, y + 73, z + 12)
		for delt in range(126, 127):
			self._common_cal(x, y, z, delt, 73, 12)	

		# (x + 126, y + 74, z + 12) -> (x + 126, y + 74, z + 12)
		for delt in range(126, 127):
			self._common_cal(x, y, z, delt, 74, 12)	

		# (x + 126, y + 74, z + 13) -> (x + 127, y + 74, z + 13)
		for delt in range(126, 128):
			self._common_cal(x, y, z, delt, 74, 13)	

		# (x + 127, y + 75, z + 13) -> (x + 129, y + 75, z + 13)
		for delt in range(127, 130):
			self._common_cal(x, y, z, delt, 75, 13)	

		# (x + 129, y + 76, z + 13) -> (x + 131, y + 76, z + 13)
		for delt in range(129, 132):
			self._common_cal(x, y, z, delt, 76, 13)	

		# (x + 131, y + 77, z + 13) -> (x + 132, y + 77, z + 13)
		for delt in range(131, 133):
			self._common_cal(x, y, z, delt, 77, 13)	

		# (x + 132, y + 78, z + 13) -> (x + 134, y + 78, z + 13)
		for delt in range(132, 135):
			self._common_cal(x, y, z, delt, 78, 13)

		# (x + 134, y + 79, z + 13) -> (x + 136, y + 79, z + 13)
		for delt in range(134, 137):
			self._common_cal(x, y, z, delt, 79, 13)

		# (x + 136, y + 79, z + 14) -> (x + 136, y + 79, z + 14)
		for delt in range(136, 137):
			self._common_cal(x, y, z, delt, 79, 14)

		# (x + 136, y + 80, z + 14) -> (x + 138, y + 80, z + 14)
		for delt in range(136, 139):
			self._common_cal(x, y, z, delt, 80, 14)

		# (x + 138, y + 81, z + 14) -> (x + 140, y + 81, z + 14)
		for delt in range(138, 141):
			self._common_cal(x, y, z, delt, 81, 14)

		# (x + 140, y + 82, z + 14) -> (x + 142, y + 82, z + 14)
		for delt in range(140, 143):
			self._common_cal(x, y, z, delt, 82, 14)

		# (x + 142, y + 83, z + 14) -> (x + 143, y + 83, z + 14)
		for delt in range(142, 144):
			self._common_cal(x, y, z, delt, 83, 14)

		# (x + 143, y + 84, z + 14) -> (x + 145, y + 84, z + 14)
		for delt in range(143, 146):
			self._common_cal(x, y, z, delt, 84, 14)

		# (x + 145, y + 85, z + 14) -> (x + 146, y + 85, z + 14)
		for delt in range(145, 147):
			self._common_cal(x, y, z, delt, 85, 14)

		# (x + 146, y + 85, z + 15) -> (x + 146, y + 85, z + 15)
		for delt in range(146, 147):
			self._common_cal(x, y, z, delt, 85, 15)

		# (x + 147, y + 86, z + 15) -> (x + 148, y + 86, z + 15)
		for delt in range(147, 149):
			self._common_cal(x, y, z, delt, 86, 15)

		# (x + 148, y + 87, z + 15) -> (x + 151, y + 87, z + 15)
		for delt in range(148, 152):
			self._common_cal(x, y, z, delt, 87, 15)

		# (x + 151, y + 88, z + 15) -> (x + 153, y + 88, z + 15)
		for delt in range(151, 154):
			self._common_cal(x, y, z, delt, 88, 15)

		# (x + 153, y + 89, z + 15) -> (x + 154, y + 89, z + 15)
		for delt in range(153, 155):
			self._common_cal(x, y, z, delt, 89, 15)

		# (x + 154, y + 90, z + 15) -> (x + 156, y + 90, z + 15)
		for delt in range(154, 157):
			self._common_cal(x, y, z, delt, 90, 15)

		# (x + 156, y + 91, z + 15) -> (x + 157, y + 91, z + 15)
		for delt in range(156, 158):
			self._common_cal(x, y, z, delt, 91, 15)

		# (x + 157, y + 91, z + 16) -> (x + 158, y + 91, z + 16)
		for delt in range(157, 159):
			self._common_cal(x, y, z, delt, 91, 16)

		# (x + 158, y + 92, z + 16) -> (x + 160, y + 92, z + 16)
		for delt in range(158, 161):
			self._common_cal(x, y, z, delt, 92, 16)

		# (x + 160, y + 93, z + 16) -> (x + 161, y + 93, z + 16)
		for delt in range(160, 162):
			self._common_cal(x, y, z, delt, 93, 16)

		# (x + 161, y + 94, z + 16) -> (x + 161, y + 94, z + 16)
		for delt in range(161, 162):
			self._common_cal(x, y, z, delt, 94, 16)


	def _case_3_8(self, x, y, z):

		# (x, y, z) -> (x + 1, y, z)
		for delt in range(2):
			cur = node.Node(x + delt, y, z)
			if self._check_valid(x + delt, y, z, cur):
				self.matrix[x + delt][y][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 1, y + 1, z) -> (x + 3, y + 1, z)
		for delt in range(1, 4):
			cur = node.Node(x + delt, y + 1, z)
			if self._check_valid(x + delt, y + 1, z, cur):
				self.matrix[x + delt][y + 1][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 3, y + 2, z) -> (x + 5, y + 2, z)
		for delt in range(3, 6):
			cur = node.Node(x + delt, y + 2, z)
			if self._check_valid(x + delt, y + 2, z, cur):
				self.matrix[x + delt][y + 2][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 5, y + 3, z) -> (x + 6, y + 3, z)
		for delt in range(5, 7):
			cur = node.Node(x + delt, y + 3, z)
			if self._check_valid(x + delt, y + 3, z, cur):
				self.matrix[x + delt][y + 3][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 6, y + 4, z) -> (x + 8, y + 4, z)
		for delt in range(6, 9):
			cur = node.Node(x + delt, y + 4, z)
			if self._check_valid(x + delt, y + 4, z, cur):
				self.matrix[x + delt][y + 4][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 8, y + 5, z) -> (x + 9, y + 5, z)
		for delt in range(8, 10):
			cur = node.Node(x + delt, y + 5, z)
			if self._check_valid(x + delt, y + 5, z, cur):
				self.matrix[x + delt][y + 5][z] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 9, y + 5, z + 1) -> (x + 10, y + 5, z + 1)
		for delt in range(9, 11):
			cur = node.Node(x + delt, y + 5, z + 1)
			if self._check_valid(x + delt, y + 5, z + 1, cur):
				self.matrix[x + delt][y + 5][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 10, y + 6, z + 1) -> (x + 12, y + 6, z + 1)
		for delt in range(10, 13):
			cur = node.Node(x + delt, y + 6, z + 1)
			if self._check_valid(x + delt, y + 6, z + 1, cur):
				self.matrix[x + delt][y + 6][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 12, y + 7, z + 1) -> (x + 13, y + 7, z + 1)
		for delt in range(12, 14):
			cur = node.Node(x + delt, y + 7, z + 1)
			if self._check_valid(x + delt, y + 7, z + 1, cur):
				self.matrix[x + delt][y + 7][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 13, y + 8, z + 1) -> (x + 15, y + 8, z + 1)
		for delt in range(13, 16):
			cur = node.Node(x + delt, y + 8, z + 1)
			if self._check_valid(x + delt, y + 8, z + 1, cur):
				self.matrix[x + delt][y + 8][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 15, y + 9, z + 1) -> (x + 17, y + 9, z + 1)
		for delt in range(15, 18):
			cur = node.Node(x + delt, y + 9, z + 1)
			if self._check_valid(x + delt, y + 9, z + 1, cur):
				self.matrix[x + delt][y + 9][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 17, y + 10, z + 1) -> (x + 19, y + 10, z + 1)
		for delt in range(17, 20):
			cur = node.Node(x + delt, y + 10, z + 1)
			if self._check_valid(x + delt, y + 10, z + 1, cur):
				self.matrix[x + delt][y + 10][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 19, y + 11, z + 1) -> (x + 19, y + 11, z + 1)
		for delt in range(19, 20):
			cur = node.Node(x + delt, y + 11, z + 1)
			if self._check_valid(x + delt, y + 11, z + 1, cur):
				self.matrix[x + delt][y + 11][z + 1] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 19, y + 11, z + 2) -> (x + 20, y + 11, z + 2)
		for delt in range(19, 21):
			cur = node.Node(x + delt, y + 11, z + 2)
			if self._check_valid(x + delt, y + 11, z + 2, cur):
				self.matrix[x + delt][y + 11][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 20, y + 12, z + 2) -> (x + 22, y + 12, z + 2)
		for delt in range(20, 23):
			cur = node.Node(x + delt, y + 12, z + 2)
			if self._check_valid(x + delt, y + 12, z + 2, cur):
				self.matrix[x + delt][y + 12][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 22, y + 13, z + 2) -> (x + 24, y + 13, z + 2)
		for delt in range(22, 25):
			cur = node.Node(x + delt, y + 13, z + 2)
			if self._check_valid(x + delt, y + 13, z + 2, cur):
				self.matrix[x + delt][y + 13][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 24, y + 14, z + 2) -> (x + 25, y + 14, z + 2)
		for delt in range(24, 26):
			cur = node.Node(x + delt, y + 14, z + 2)
			if self._check_valid(x + delt, y + 14, z + 2, cur):
				self.matrix[x + delt][y + 14][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 25, y + 15, z + 2) -> (x + 27, y + 15, z + 2)
		for delt in range(25, 28):
			cur = node.Node(x + delt, y + 15, z + 2)
			if self._check_valid(x + delt, y + 15, z + 2, cur):
				self.matrix[x + delt][y + 15][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 27, y + 16, z + 2) -> (x + 28, y + 16, z + 2)
		for delt in range(27, 29):
			cur = node.Node(x + delt, y + 16, z + 2)
			if self._check_valid(x + delt, y + 16, z + 2, cur):
				self.matrix[x + delt][y + 16][z + 2] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 28, y + 16, z + 3) -> (x + 29, y + 16, z + 3)
		for delt in range(28, 30):
			cur = node.Node(x + delt, y + 16, z + 3)
			if self._check_valid(x + delt, y + 16, z + 3, cur):
				self.matrix[x + delt][y + 16][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 29, y + 17, z + 3) -> (x + 31, y + 17, z + 3)
		for delt in range(29, 32):
			cur = node.Node(x + delt, y + 17, z + 3)
			if self._check_valid(x + delt, y + 17, z + 3, cur):
				self.matrix[x + delt][y + 17][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 31, y + 18, z + 3) -> (x + 32, y + 18, z + 3)
		for delt in range(31, 33):
			cur = node.Node(x + delt, y + 18, z + 3)
			if self._check_valid(x + delt, y + 18, z + 3, cur):
				self.matrix[x + delt][y + 18][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 32, y + 19, z + 3) -> (x + 34, y + 19, z + 3)
		for delt in range(32, 35):
			cur = node.Node(x + delt, y + 19, z + 3)
			if self._check_valid(x + delt, y + 19, z + 3, cur):
				self.matrix[x + delt][y + 19][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 34, y + 20, z + 3) -> (x + 36, y + 20, z + 3)
		for delt in range(34, 37):
			cur = node.Node(x + delt, y + 20, z + 3)
			if self._check_valid(x + delt, y + 20, z + 3, cur):
				self.matrix[x + delt][y + 20][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 36, y + 21, z + 3) -> (x + 38, y + 21, z + 3)
		for delt in range(36, 39):
			cur = node.Node(x + delt, y + 21, z + 3)
			if self._check_valid(x + delt, y + 21, z + 3, cur):
				self.matrix[x + delt][y + 21][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 38, y + 22, z + 3) -> (x + 38, y + 22, z + 3)
		for delt in range(38, 39):
			cur = node.Node(x + delt, y + 22, z + 3)
			if self._check_valid(x + delt, y + 22, z + 3, cur):
				self.matrix[x + delt][y + 22][z + 3] = DataGenerator._selected
				self.fill_set_ponts.add(cur)	

		# (x + 38, y + 22, z + 4) -> (x + 39, y + 22, z + 4)
		for delt in range(38, 40):
			cur = node.Node(x + delt, y + 22, z + 4)
			if self._check_valid(x + delt, y + 22, z + 4, cur):
				self.matrix[x + delt][y + 22][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 39, y + 23, z + 4) -> (x + 41, y + 23, z + 4)
		for delt in range(39, 42):
			cur = node.Node(x + delt, y + 23, z + 4)
			if self._check_valid(x + delt, y + 23, z + 4, cur):
				self.matrix[x + delt][y + 23][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 41, y + 24, z + 4) -> (x + 43, y + 24, z + 4)
		for delt in range(41, 44):
			cur = node.Node(x + delt, y + 24, z + 4)
			if self._check_valid(x + delt, y + 24, z + 4, cur):
				self.matrix[x + delt][y + 24][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 43, y + 25, z + 4) -> (x + 44, y + 25, z + 4)
		for delt in range(43, 45):
			cur = node.Node(x + delt, y + 25, z + 4)
			if self._check_valid(x + delt, y + 25, z + 4, cur):
				self.matrix[x + delt][y + 25][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 44, y + 26, z + 4) -> (x + 46, y + 26, z + 4)
		for delt in range(44, 47):
			cur = node.Node(x + delt, y + 26, z + 4)
			if self._check_valid(x + delt, y + 26, z + 4, cur):
				self.matrix[x + delt][y + 26][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 46, y + 27, z + 4) -> (x + 47, y + 27, z + 4)
		for delt in range(46, 48):
			cur = node.Node(x + delt, y + 27, z + 4)
			if self._check_valid(x + delt, y + 27, z + 4, cur):
				self.matrix[x + delt][y + 27][z + 4] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 47, y + 27, z + 5) -> (x + 48, y + 27, z + 5)
		for delt in range(47, 49):
			cur = node.Node(x + delt, y + 27, z + 5)
			if self._check_valid(x + delt, y + 27, z + 5, cur):
				self.matrix[x + delt][y + 27][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 48, y + 28, z + 5) -> (x + 50, y + 28, z + 5)
		for delt in range(48, 51):
			cur = node.Node(x + delt, y + 28, z + 5)
			if self._check_valid(x + delt, y + 28, z + 5, cur):
				self.matrix[x + delt][y + 28][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 50, y + 29, z + 5) -> (x + 51, y + 29, z + 5)
		for delt in range(50, 52):
			cur = node.Node(x + delt, y + 29, z + 5)
			if self._check_valid(x + delt, y + 29, z + 5, cur):
				self.matrix[x + delt][y + 29][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 51, y + 30, z + 5) -> (x + 53, y + 30, z + 5)
		for delt in range(51, 54):
			cur = node.Node(x + delt, y + 30, z + 5)
			if self._check_valid(x + delt, y + 30, z + 5, cur):
				self.matrix[x + delt][y + 30][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 53, y + 31, z + 5) -> (x + 55, y + 31, z + 5)
		for delt in range(53, 56):
			cur = node.Node(x + delt, y + 31, z + 5)
			if self._check_valid(x + delt, y + 31, z + 5, cur):
				self.matrix[x + delt][y + 31][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 55, y + 32, z + 5) -> (x + 57, y + 32, z + 5)
		for delt in range(55, 58):
			cur = node.Node(x + delt, y + 32, z + 5)
			if self._check_valid(x + delt, y + 32, z + 5, cur):
				self.matrix[x + delt][y + 32][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 57, y + 33, z + 5) -> (x + 58, y + 33, z + 5)
		for delt in range(57, 59):
			cur = node.Node(x + delt, y + 33, z + 5)
			if self._check_valid(x + delt, y + 33, z + 5, cur):
				self.matrix[x + delt][y + 33][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 58, y + 34, z + 5) -> (x + 60, y + 34, z + 5)
		for delt in range(58, 61):
			cur = node.Node(x + delt, y + 34, z + 5)
			if self._check_valid(x + delt, y + 34, z + 5, cur):
				self.matrix[x + delt][y + 34][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 60, y + 35, z + 5) -> (x + 61, y + 35, z + 5)
		for delt in range(60, 62):
			cur = node.Node(x + delt, y + 35, z + 5)
			if self._check_valid(x + delt, y + 35, z + 5, cur):
				self.matrix[x + delt][y + 35][z + 5] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 61, y + 35, z + 6) -> (x + 62, y + 35, z + 6)
		for delt in range(61, 63):
			cur = node.Node(x + delt, y + 35, z + 6)
			if self._check_valid(x + delt, y + 35, z + 6, cur):
				self.matrix[x + delt][y + 35][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 62, y + 36, z + 6) -> (x + 64, y + 36, z + 6)
		for delt in range(62, 65):
			cur = node.Node(x + delt, y + 36, z + 6)
			if self._check_valid(x + delt, y + 36, z + 6, cur):
				self.matrix[x + delt][y + 36][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 64, y + 37, z + 6) -> (x + 65, y + 37, z + 6)
		for delt in range(64, 66):
			cur = node.Node(x + delt, y + 37, z + 6)
			if self._check_valid(x + delt, y + 37, z + 6, cur):
				self.matrix[x + delt][y + 37][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 65, y + 38, z + 6) -> (x + 67, y + 38, z + 6)
		for delt in range(65, 68):
			cur = node.Node(x + delt, y + 38, z + 6)
			if self._check_valid(x + delt, y + 38, z + 6, cur):
				self.matrix[x + delt][y + 38][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 67, y + 39, z + 6) -> (x + 69, y + 39, z + 6)
		for delt in range(67, 70):
			cur = node.Node(x + delt, y + 39, z + 6)
			if self._check_valid(x + delt, y + 39, z + 6, cur):
				self.matrix[x + delt][y + 39][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 69, y + 40, z + 6) -> (x + 69, y + 40, z + 6)
		for delt in range(69, 70):
			cur = node.Node(x + delt, y + 40, z + 6)
			if self._check_valid(x + delt, y + 40, z + 6, cur):
				self.matrix[x + delt][y + 40][z + 6] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 69, y + 40, z + 7) -> (x + 70, y + 40, z + 7)
		for delt in range(69, 71):
			cur = node.Node(x + delt, y + 40, z + 7)
			if self._check_valid(x + delt, y + 40, z + 7, cur):
				self.matrix[x + delt][y + 40][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 70, y + 41, z + 7) -> (x + 72, y + 41, z + 7)
		for delt in range(70, 73):
			cur = node.Node(x + delt, y + 41, z + 7)
			if self._check_valid(x + delt, y + 41, z + 7, cur):
				self.matrix[x + delt][y + 41][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 72, y + 42, z + 7) -> (x + 74, y + 42, z + 7)
		for delt in range(72, 75):
			cur = node.Node(x + delt, y + 42, z + 7)
			if self._check_valid(x + delt, y + 42, z + 7, cur):
				self.matrix[x + delt][y + 42][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 74, y + 43, z + 7) -> (x + 75, y + 43, z + 7)
		for delt in range(74, 76):
			cur = node.Node(x + delt, y + 43, z + 7)
			if self._check_valid(x + delt, y + 43, z + 7, cur):
				self.matrix[x + delt][y + 43][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 75, y + 44, z + 7) -> (x + 77, y + 44, z + 7)
		for delt in range(75, 78):
			cur = node.Node(x + delt, y + 44, z + 7)
			if self._check_valid(x + delt, y + 44, z + 7, cur):
				self.matrix[x + delt][y + 44][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 77, y + 45, z + 7) -> (x + 78, y + 45, z + 7)
		for delt in range(77, 79):
			cur = node.Node(x + delt, y + 45, z + 7)
			if self._check_valid(x + delt, y + 45, z + 7, cur):
				self.matrix[x + delt][y + 45][z + 7] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 78, y + 45, z + 8) -> (x + 79, y + 45, z + 8)
		for delt in range(78, 80):
			cur = node.Node(x + delt, y + 45, z + 8)
			if self._check_valid(x + delt, y + 45, z + 8, cur):
				self.matrix[x + delt][y + 45][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 79, y + 46, z + 8) -> (x + 81, y + 46, z + 8)
		for delt in range(79, 82):
			cur = node.Node(x + delt, y + 46, z + 8)
			if self._check_valid(x + delt, y + 46, z + 8, cur):
				self.matrix[x + delt][y + 46][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 81, y + 47, z + 8) -> (x + 82, y + 47, z + 8)
		for delt in range(81, 83):
			cur = node.Node(x + delt, y + 47, z + 8)
			if self._check_valid(x + delt, y + 47, z + 8, cur):
				self.matrix[x + delt][y + 47][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 82, y + 48, z + 8) -> (x + 84, y + 48, z + 8)
		for delt in range(82, 85):
			cur = node.Node(x + delt, y + 48, z + 8)
			if self._check_valid(x + delt, y + 48, z + 8, cur):
				self.matrix[x + delt][y + 48][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 84, y + 49, z + 8) -> (x + 86, y + 49, z + 8)
		for delt in range(84, 87):
			cur = node.Node(x + delt, y + 49, z + 8)
			if self._check_valid(x + delt, y + 49, z + 8, cur):
				self.matrix[x + delt][y + 49][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 86, y + 50, z + 8) -> (x + 86, y + 50, z + 8)
		for delt in range(86, 87):
			cur = node.Node(x + delt, y + 50, z + 8)
			if self._check_valid(x + delt, y + 50, z + 8, cur):
				self.matrix[x + delt][y + 50][z + 8] = DataGenerator._selected
				self.fill_set_ponts.add(cur)

		# (x + 86, y + 50, z + 8) -> (x + 88, y + 50, z + 8)
		for delt in range(86, 89):
			self._common_cal(x, y, z, delt, 50, 8)

		# (x + 88, y + 51, z + 8) -> (x + 89, y + 51, z + 8)
		for delt in range(89, 90):
			self._common_cal(x, y, z, delt, 51, 8)

		# (x + 90, y + 51, z + 9) -> (x + 91, y + 51, z + 9)
		for delt in range(90, 92):
			self._common_cal(x, y, z, delt, 51, 9)

		# (x + 91, y + 52, z + 9) -> (x + 93, y + 52, z + 9)
		for delt in range(91, 94):
			self._common_cal(x, y, z, delt, 52, 9)

		# (x + 93, y + 53, z + 9) -> (x + 94, y + 53, z + 9)
		for delt in range(93, 95):
			self._common_cal(x, y, z, delt, 53, 9)

		# (x + 94, y + 54, z + 9) -> (x + 96, y + 54, z + 9)
		for delt in range(94, 97):
			self._common_cal(x, y, z, delt, 54, 9)

		# (x + 96, y + 55, z + 9) -> (x + 98, y + 55, z + 9)
		for delt in range(96, 99):
			self._common_cal(x, y, z, delt, 55, 9)

		# (x + 98, y + 56, z + 9) -> (x + 99, y + 56, z + 9)
		for delt in range(98, 100):
			self._common_cal(x, y, z, delt, 56, 9)

		# (x + 99, y + 57, z + 9) -> (x + 99, y + 57, z + 9)
		for delt in range(99, 100):
			self._common_cal(x, y, z, delt, 57, 9)

		# (x + 99, y + 57, z + 10) -> (x + 100, y + 57, z + 10)
		for delt in range(99, 101):
			self._common_cal(x, y, z, delt, 57, 10)

		# (x + 100, y + 58, z + 10) -> (x + 102, y + 58, z + 10)
		for delt in range(100, 103):
			self._common_cal(x, y, z, delt, 58, 10)

		# (x + 102, y + 59, z + 10) -> (x + 104, y + 59, z + 10)
		for delt in range(102, 105):
			self._common_cal(x, y, z, delt, 59, 10)

		# (x + 104, y + 60, z + 10) -> (x + 105, y + 60, z + 10)
		for delt in range(104, 106):
			self._common_cal(x, y, z, delt, 60, 10)

		# (x + 105, y + 61, z + 10) -> (x + 107, y + 61, z + 10)
		for delt in range(105, 108):
			self._common_cal(x, y, z, delt, 61, 10)

		# (x + 107, y + 62, z + 10) -> (x + 108, y + 62, z + 10)
		for delt in range(107, 109):
			self._common_cal(x, y, z, delt, 62, 10)

		# (x + 108, y + 62, z + 11) -> (x + 108, y + 62, z + 11)
		for delt in range(108, 109):
			self._common_cal(x, y, z, delt, 62, 11)

		# (x + 110, y + 64, z + 11) -> (x + 112, y + 64, z + 11)
		for delt in range(110, 113):
			self._common_cal(x, y, z, delt, 64, 11)

		# (x + 112, y + 65, z + 11) -> (x + 114, y + 65, z + 11)
		for delt in range(112, 115):
			self._common_cal(x, y, z, delt, 65, 11)

		# (x + 114, y + 66, z + 11) -> (x + 115, y + 66, z + 11)
		for delt in range(114, 116):
			self._common_cal(x, y, z, delt, 66, 11)

		# (x + 115, y + 67, z + 11) -> (x + 117, y + 67, z + 11)
		for delt in range(115, 118):
			self._common_cal(x, y, z, delt, 67, 11)			

		# (x + 117, y + 68, z + 11) -> (x + 118, y + 68, z + 11)
		for delt in range(117, 119):
			self._common_cal(x, y, z, delt, 68, 11)

		# (x + 118, y + 68, z + 12) -> (x + 119, y + 68, z + 12)
		for delt in range(118, 120):
			self._common_cal(x, y, z, delt, 68, 12)					

		# (x + 119, y + 69, z + 12) -> (x + 121, y + 69, z + 12)
		for delt in range(119, 122):
			self._common_cal(x, y, z, delt, 69, 12)		

		# (x + 121, y + 70, z + 12) -> (x + 122, y + 70, z + 12)
		for delt in range(121, 123):
			self._common_cal(x, y, z, delt, 70, 12)	

		# (x + 122, y + 71, z + 12) -> (x + 124, y + 71, z + 12)
		for delt in range(122, 125):
			self._common_cal(x, y, z, delt, 71, 12)					

		# (x + 124, y + 72, z + 12) -> (x + 126, y + 72, z + 12)
		for delt in range(124, 127):
			self._common_cal(x, y, z, delt, 72, 12)	

		# (x + 126, y + 73, z + 12) -> (x + 126, y + 73, z + 12)
		for delt in range(126, 127):
			self._common_cal(x, y, z, delt, 73, 12)	

		# (x + 126, y + 74, z + 12) -> (x + 126, y + 74, z + 12)
		for delt in range(126, 127):
			self._common_cal(x, y, z, delt, 74, 12)	

		# (x + 126, y + 74, z + 13) -> (x + 127, y + 74, z + 13)
		for delt in range(126, 128):
			self._common_cal(x, y, z, delt, 74, 13)	

		# (x + 127, y + 75, z + 13) -> (x + 129, y + 75, z + 13)
		for delt in range(127, 130):
			self._common_cal(x, y, z, delt, 75, 13)	

		# (x + 129, y + 76, z + 13) -> (x + 131, y + 76, z + 13)
		for delt in range(129, 132):
			self._common_cal(x, y, z, delt, 76, 13)	

		# (x + 131, y + 77, z + 13) -> (x + 132, y + 77, z + 13)
		for delt in range(131, 133):
			self._common_cal(x, y, z, delt, 77, 13)	

		# (x + 132, y + 78, z + 13) -> (x + 134, y + 78, z + 13)
		for delt in range(132, 135):
			self._common_cal(x, y, z, delt, 78, 13)

		# (x + 134, y + 79, z + 13) -> (x + 136, y + 79, z + 13)
		for delt in range(134, 137):
			self._common_cal(x, y, z, delt, 79, 13)

		# (x + 136, y + 79, z + 14) -> (x + 136, y + 79, z + 14)
		for delt in range(136, 137):
			self._common_cal(x, y, z, delt, 79, 14)

		# (x + 136, y + 80, z + 14) -> (x + 138, y + 80, z + 14)
		for delt in range(136, 139):
			self._common_cal(x, y, z, delt, 80, 14)

		# (x + 138, y + 81, z + 14) -> (x + 140, y + 81, z + 14)
		for delt in range(138, 141):
			self._common_cal(x, y, z, delt, 81, 14)

		# (x + 140, y + 82, z + 14) -> (x + 142, y + 82, z + 14)
		for delt in range(140, 143):
			self._common_cal(x, y, z, delt, 82, 14)

		# (x + 142, y + 83, z + 14) -> (x + 143, y + 83, z + 14)
		for delt in range(142, 144):
			self._common_cal(x, y, z, delt, 83, 14)

		# (x + 143, y + 84, z + 14) -> (x + 145, y + 84, z + 14)
		for delt in range(143, 146):
			self._common_cal(x, y, z, delt, 84, 14)

		# (x + 145, y + 85, z + 14) -> (x + 146, y + 85, z + 14)
		for delt in range(145, 147):
			self._common_cal(x, y, z, delt, 85, 14)

		# (x + 146, y + 85, z + 15) -> (x + 146, y + 85, z + 15)
		for delt in range(146, 147):
			self._common_cal(x, y, z, delt, 85, 15)

		# (x + 147, y + 86, z + 15) -> (x + 148, y + 86, z + 15)
		for delt in range(147, 149):
			self._common_cal(x, y, z, delt, 86, 15)

		# (x + 148, y + 87, z + 15) -> (x + 151, y + 87, z + 15)
		for delt in range(148, 152):
			self._common_cal(x, y, z, delt, 87, 15)

		# (x + 151, y + 88, z + 15) -> (x + 153, y + 88, z + 15)
		for delt in range(151, 154):
			self._common_cal(x, y, z, delt, 88, 15)

		# (x + 153, y + 89, z + 15) -> (x + 154, y + 89, z + 15)
		for delt in range(153, 155):
			self._common_cal(x, y, z, delt, 89, 15)

		# (x + 154, y + 90, z + 15) -> (x + 156, y + 90, z + 15)
		for delt in range(154, 157):
			self._common_cal(x, y, z, delt, 90, 15)

		# (x + 156, y + 91, z + 15) -> (x + 157, y + 91, z + 15)
		for delt in range(156, 158):
			self._common_cal(x, y, z, delt, 91, 15)

		# (x + 157, y + 91, z + 16) -> (x + 158, y + 91, z + 16)
		for delt in range(157, 159):
			self._common_cal(x, y, z, delt, 91, 16)

		# (x + 158, y + 92, z + 16) -> (x + 160, y + 92, z + 16)
		for delt in range(158, 161):
			self._common_cal(x, y, z, delt, 92, 16)

		# (x + 160, y + 93, z + 16) -> (x + 161, y + 93, z + 16)
		for delt in range(160, 162):
			self._common_cal(x, y, z, delt, 93, 16)

		# (x + 161, y + 94, z + 16) -> (x + 164, y + 94, z + 16)
		for delt in range(161, 165):
			self._common_cal(x, y, z, delt, 94, 16)

		# (x + 161, y + 94, z + 16) -> (x + 164, y + 94, z + 16)
		for delt in range(161, 165):
			self._common_cal(x, y, z, delt, 94, 16)

		# (x + 164, y + 95, z + 16) -> (x + 165, y + 95, z + 16)
		for delt in range(164, 166):
			self._common_cal(x, y, z, delt, 95, 16)

		# (x + 165, y + 96, z + 16) -> (x + 167, y + 96, z + 16)
		for delt in range(165, 168):
			self._common_cal(x, y, z, delt, 96, 16)

		# (x + 167, y + 97, z + 16) -> (x + 168, y + 97, z + 16)
		for delt in range(167, 169):
			self._common_cal(x, y, z, delt, 97, 16)

		# (x + 168, y + 97, z + 17) -> (x + 169, y + 97, z + 17)
		for delt in range(168, 170):
			self._common_cal(x, y, z, delt, 97, 17)

		# (x + 169, y + 98, z + 17) -> (x + 171, y + 98, z + 17)
		for delt in range(169, 172):
			self._common_cal(x, y, z, delt, 98, 17)

		# (x + 171, y + 99, z + 17) -> (x + 172, y + 99, z + 17)
		for delt in range(171, 173):
			self._common_cal(x, y, z, delt, 99, 17)

		# (x + 172, y + 100, z + 17) -> (x + 174, y + 100, z + 17)
		for delt in range(172, 175):
			self._common_cal(x, y, z, delt, 100, 17)

		# (x + 174, y + 101, z + 17) -> (x + 176, y + 101, z + 17)
		for delt in range(174, 177):
			self._common_cal(x, y, z, delt, 101, 17)

		# (x + 176, y + 102, z + 17) -> (x + 177, y + 102, z + 17)
		for delt in range(176, 178):
			self._common_cal(x, y, z, delt, 102, 17)

		# (x + 177, y + 103, z + 17) -> (x + 178, y + 103, z + 17)
		for delt in range(177, 179):
			self._common_cal(x, y, z, delt, 103, 17)

		# (x + 178, y + 103, z + 18) -> (x + 179, y + 103, z + 18)
		for delt in range(178, 180):
			self._common_cal(x, y, z, delt, 103, 18)

		# (x + 179, y + 104, z + 18) -> (x + 181, y + 104, z + 18)
		for delt in range(179, 182):
			self._common_cal(x, y, z, delt, 104, 18)

		# (x + 181, y + 105, z + 18) -> (x + 182, y + 105, z + 18)
		for delt in range(181, 183):
			self._common_cal(x, y, z, delt, 105, 18)

		# (x + 182, y + 106, z + 18) -> (x + 184, y + 106, z + 18)
		for delt in range(182, 185):
			self._common_cal(x, y, z, delt, 106, 18)

		# (x + 184, y + 107, z + 18) -> (x + 186, y + 107, z + 18)
		for delt in range(184, 187):
			self._common_cal(x, y, z, delt, 107, 18)

		# (x + 186, y + 108, z + 18) -> (x + 188, y + 108, z + 18)
		for delt in range(186, 189):
			self._common_cal(x, y, z, delt, 108, 18)

		# (x + 188, y + 108, z + 19) -> (x + 188, y + 108, z + 19)
		for delt in range(188, 189):
			self._common_cal(x, y, z, delt, 108, 19)

		# (x + 188, y + 109, z + 19) -> (x + 190, y + 109, z + 19)
		for delt in range(188, 191):
			self._common_cal(x, y, z, delt, 109, 19)


	def _case_4_1(self, x, y, z):

		# (x, y, z) -> (x + 8, y + 8, z)
		for delt in range(9):
			self._common_cal(x, y, z, delt, delt, 0)

		# (x + 8, y + 8, z + 1) -> (x + 16, y + 16, z + 1)
		for delt in range(8, 17):
			self._common_cal(x, y, z, delt, delt, 1)		


	def _case_4_2(self, x, y, z):

		# (x, y, z) -> (x + 8, y + 8, z)
		for delt in range(9):
			self._common_cal(x, y, z, delt, delt, 0)

		# (x + 8, y + 8, z + 1) -> (x + 16, y + 16, z + 1)
		for delt in range(8, 17):
			self._common_cal(x, y, z, delt, delt, 1)	

		# (x + 16, y + 16, z + 2) -> (x + 24, y + 24, z + 2)
		for delt in range(16, 25):
			self._common_cal(x, y, z, delt, delt, 2)	

		# (x + 24, y + 24, z + 3) -> (x + 29, y + 29, z + 3)
		for delt in range(24, 30):
			self._common_cal(x, y, z, delt, delt, 3)	


	def _case_4_3(self, x, y, z):

		# (x, y, z) -> (x + 8, y + 8, z)
		for delt in range(9):
			self._common_cal(x, y, z, delt, delt, 0)

		# (x + 8, y + 8, z + 1) -> (x + 16, y + 16, z + 1)
		for delt in range(8, 17):
			self._common_cal(x, y, z, delt, delt, 1)	

		# (x + 16, y + 16, z + 2) -> (x + 24, y + 24, z + 2)
		for delt in range(16, 25):
			self._common_cal(x, y, z, delt, delt, 2)	

		# (x + 24, y + 24, z + 3) -> (x + 32, y + 32, z + 3)
		for delt in range(24, 33):
			self._common_cal(x, y, z, delt, delt, 3)	

		# (x + 32, y + 32, z + 4) -> (x + 40, y + 40, z + 4)
		for delt in range(32, 41):
			self._common_cal(x, y, z, delt, delt, 4)

		# (x + 40, y + 40, z + 5) -> (x + 44, y + 44, z + 5)
		for delt in range(40, 45):
			self._common_cal(x, y, z, delt, delt, 5)

	
	def _case_4_4(self, x, y, z):

		# (x, y, z) -> (x + 8, y + 8, z)
		for delt in range(9):
			self._common_cal(x, y, z, delt, delt, 0)

		# (x + 8, y + 8, z + 1) -> (x + 16, y + 16, z + 1)
		for delt in range(8, 17):
			self._common_cal(x, y, z, delt, delt, 1)	

		# (x + 16, y + 16, z + 2) -> (x + 24, y + 24, z + 2)
		for delt in range(16, 25):
			self._common_cal(x, y, z, delt, delt, 2)	

		# (x + 24, y + 24, z + 3) -> (x + 32, y + 32, z + 3)
		for delt in range(24, 33):
			self._common_cal(x, y, z, delt, delt, 3)	

		# (x + 32, y + 32, z + 4) -> (x + 40, y + 40, z + 4)
		for delt in range(32, 41):
			self._common_cal(x, y, z, delt, delt, 4)

		# (x + 40, y + 40, z + 5) -> (x + 48, y + 48, z + 5)
		for delt in range(40, 49):
			self._common_cal(x, y, z, delt, delt, 5)

		# (x + 48, y + 48, z + 6) -> (x + 56, y + 56, z + 6)
		for delt in range(48, 56):
			self._common_cal(x, y, z, delt, delt, 6)

		# (x + 56, y + 56, z + 7) -> (x + 64, y + 64, z + 7)
		for delt in range(56, 65):
			self._common_cal(x, y, z, delt, delt, 7)

		# (x + 64, y + 64, z + 8) -> (x + 72, y + 72, z + 8)
		for delt in range(64, 73):
			self._common_cal(x, y, z, delt, delt, 8)

	
	def _case_4_5(self, x, y, z):

		# (x, y, z) -> (x + 8, y + 8, z)
		for delt in range(9):
			self._common_cal(x, y, z, delt, delt, 0)

		# (x + 8, y + 8, z + 1) -> (x + 16, y + 16, z + 1)
		for delt in range(8, 17):
			self._common_cal(x, y, z, delt, delt, 1)	

		# (x + 16, y + 16, z + 2) -> (x + 24, y + 24, z + 2)
		for delt in range(16, 25):
			self._common_cal(x, y, z, delt, delt, 2)	

		# (x + 24, y + 24, z + 3) -> (x + 32, y + 32, z + 3)
		for delt in range(24, 33):
			self._common_cal(x, y, z, delt, delt, 3)	

		# (x + 32, y + 32, z + 4) -> (x + 40, y + 40, z + 4)
		for delt in range(32, 41):
			self._common_cal(x, y, z, delt, delt, 4)

		# (x + 40, y + 40, z + 5) -> (x + 48, y + 48, z + 5)
		for delt in range(40, 49):
			self._common_cal(x, y, z, delt, delt, 5)

		# (x + 48, y + 48, z + 6) -> (x + 56, y + 56, z + 6)
		for delt in range(48, 56):
			self._common_cal(x, y, z, delt, delt, 6)

		# (x + 56, y + 56, z + 7) -> (x + 64, y + 64, z + 7)
		for delt in range(56, 65):
			self._common_cal(x, y, z, delt, delt, 7)

		# (x + 64, y + 64, z + 8) -> (x + 72, y + 72, z + 8)
		for delt in range(64, 73):
			self._common_cal(x, y, z, delt, delt, 8)

		# (x + 72, y + 72, z + 9) -> (x + 80, y + 80, z + 9)
		for delt in range(72, 81):
			self._common_cal(x, y, z, delt, delt, 9)

		# (x + 80, y + 80, z + 10) -> (x + 88, y + 88, z + 10)
		for delt in range(80, 89):
			self._common_cal(x, y, z, delt, delt, 10)

	
	def _case_4_6(self, x, y, z):

		# (x, y, z) -> (x + 8, y + 8, z)
		for delt in range(9):
			self._common_cal(x, y, z, delt, delt, 0)

		# (x + 8, y + 8, z + 1) -> (x + 16, y + 16, z + 1)
		for delt in range(8, 17):
			self._common_cal(x, y, z, delt, delt, 1)	

		# (x + 16, y + 16, z + 2) -> (x + 24, y + 24, z + 2)
		for delt in range(16, 25):
			self._common_cal(x, y, z, delt, delt, 2)	

		# (x + 24, y + 24, z + 3) -> (x + 32, y + 32, z + 3)
		for delt in range(24, 33):
			self._common_cal(x, y, z, delt, delt, 3)	

		# (x + 32, y + 32, z + 4) -> (x + 40, y + 40, z + 4)
		for delt in range(32, 41):
			self._common_cal(x, y, z, delt, delt, 4)

		# (x + 40, y + 40, z + 5) -> (x + 48, y + 48, z + 5)
		for delt in range(40, 49):
			self._common_cal(x, y, z, delt, delt, 5)

		# (x + 48, y + 48, z + 6) -> (x + 56, y + 56, z + 6)
		for delt in range(48, 56):
			self._common_cal(x, y, z, delt, delt, 6)

		# (x + 56, y + 56, z + 7) -> (x + 64, y + 64, z + 7)
		for delt in range(56, 65):
			self._common_cal(x, y, z, delt, delt, 7)

		# (x + 64, y + 64, z + 8) -> (x + 72, y + 72, z + 8)
		for delt in range(64, 73):
			self._common_cal(x, y, z, delt, delt, 8)

		# (x + 72, y + 72, z + 9) -> (x + 80, y + 80, z + 9)
		for delt in range(72, 81):
			self._common_cal(x, y, z, delt, delt, 9)

		# (x + 80, y + 80, z + 10) -> (x + 88, y + 88, z + 10)
		for delt in range(80, 89):
			self._common_cal(x, y, z, delt, delt, 10)

		# (x + 88, y + 88, z + 11) -> (x + 96, y + 96, z + 11)
		for delt in range(88, 97):
			self._common_cal(x, y, z, delt, delt, 11)

		# (x + 96, y + 96, z + 12) -> (x + 104, y + 104, z + 12)
		for delt in range(97, 105):
			self._common_cal(x, y, z, delt, delt, 12)

	
	def _case_4_7(self, x, y, z):

		# (x, y, z) -> (x + 8, y + 8, z)
		for delt in range(9):
			self._common_cal(x, y, z, delt, delt, 0)

		# (x + 8, y + 8, z + 1) -> (x + 16, y + 16, z + 1)
		for delt in range(8, 17):
			self._common_cal(x, y, z, delt, delt, 1)	

		# (x + 16, y + 16, z + 2) -> (x + 24, y + 24, z + 2)
		for delt in range(16, 25):
			self._common_cal(x, y, z, delt, delt, 2)	

		# (x + 24, y + 24, z + 3) -> (x + 32, y + 32, z + 3)
		for delt in range(24, 33):
			self._common_cal(x, y, z, delt, delt, 3)	

		# (x + 32, y + 32, z + 4) -> (x + 40, y + 40, z + 4)
		for delt in range(32, 41):
			self._common_cal(x, y, z, delt, delt, 4)

		# (x + 40, y + 40, z + 5) -> (x + 48, y + 48, z + 5)
		for delt in range(40, 49):
			self._common_cal(x, y, z, delt, delt, 5)

		# (x + 48, y + 48, z + 6) -> (x + 56, y + 56, z + 6)
		for delt in range(48, 56):
			self._common_cal(x, y, z, delt, delt, 6)

		# (x + 56, y + 56, z + 7) -> (x + 64, y + 64, z + 7)
		for delt in range(56, 65):
			self._common_cal(x, y, z, delt, delt, 7)

		# (x + 64, y + 64, z + 8) -> (x + 72, y + 72, z + 8)
		for delt in range(64, 73):
			self._common_cal(x, y, z, delt, delt, 8)

		# (x + 72, y + 72, z + 9) -> (x + 80, y + 80, z + 9)
		for delt in range(72, 81):
			self._common_cal(x, y, z, delt, delt, 9)

		# (x + 80, y + 80, z + 10) -> (x + 88, y + 88, z + 10)
		for delt in range(80, 89):
			self._common_cal(x, y, z, delt, delt, 10)

		# (x + 88, y + 88, z + 11) -> (x + 96, y + 96, z + 11)
		for delt in range(88, 97):
			self._common_cal(x, y, z, delt, delt, 11)

		# (x + 96, y + 96, z + 12) -> (x + 104, y + 104, z + 12)
		for delt in range(97, 105):
			self._common_cal(x, y, z, delt, delt, 12)

		# (x + 104, y + 104, z + 13) -> (x + 112, y + 112, z + 13)
		for delt in range(104, 113):
			self._common_cal(x, y, z, delt, delt, 13)

		# (x + 112, y + 112, z + 14) -> (x + 120, y + 120, z + 14)
		for delt in range(112, 121):
			self._common_cal(x, y, z, delt, delt, 14)

		# (x + 120, y + 120, z + 15) -> (x + 129, y + 129, z + 15)
		for delt in range(120, 130):
			self._common_cal(x, y, z, delt, delt, 15)

		# (x + 129, y + 129, z + 16) -> (x + 132, y + 132, z + 16)
		for delt in range(129, 133):
			self._common_cal(x, y, z, delt, delt, 16)


	def _case_4_8(self, x, y, z):

		# (x, y, z) -> (x + 8, y + 8, z)
		for delt in range(9):
			self._common_cal(x, y, z, delt, delt, 0)

		# (x + 8, y + 8, z + 1) -> (x + 16, y + 16, z + 1)
		for delt in range(8, 17):
			self._common_cal(x, y, z, delt, delt, 1)	

		# (x + 16, y + 16, z + 2) -> (x + 24, y + 24, z + 2)
		for delt in range(16, 25):
			self._common_cal(x, y, z, delt, delt, 2)	

		# (x + 24, y + 24, z + 3) -> (x + 32, y + 32, z + 3)
		for delt in range(24, 33):
			self._common_cal(x, y, z, delt, delt, 3)	

		# (x + 32, y + 32, z + 4) -> (x + 40, y + 40, z + 4)
		for delt in range(32, 41):
			self._common_cal(x, y, z, delt, delt, 4)

		# (x + 40, y + 40, z + 5) -> (x + 48, y + 48, z + 5)
		for delt in range(40, 49):
			self._common_cal(x, y, z, delt, delt, 5)

		# (x + 48, y + 48, z + 6) -> (x + 56, y + 56, z + 6)
		for delt in range(48, 56):
			self._common_cal(x, y, z, delt, delt, 6)

		# (x + 56, y + 56, z + 7) -> (x + 64, y + 64, z + 7)
		for delt in range(56, 65):
			self._common_cal(x, y, z, delt, delt, 7)

		# (x + 64, y + 64, z + 8) -> (x + 72, y + 72, z + 8)
		for delt in range(64, 73):
			self._common_cal(x, y, z, delt, delt, 8)

		# (x + 72, y + 72, z + 9) -> (x + 80, y + 80, z + 9)
		for delt in range(72, 81):
			self._common_cal(x, y, z, delt, delt, 9)

		# (x + 80, y + 80, z + 10) -> (x + 88, y + 88, z + 10)
		for delt in range(80, 89):
			self._common_cal(x, y, z, delt, delt, 10)

		# (x + 88, y + 88, z + 11) -> (x + 96, y + 96, z + 11)
		for delt in range(88, 97):
			self._common_cal(x, y, z, delt, delt, 11)

		# (x + 96, y + 96, z + 12) -> (x + 104, y + 104, z + 12)
		for delt in range(97, 105):
			self._common_cal(x, y, z, delt, delt, 12)

		# (x + 104, y + 104, z + 13) -> (x + 112, y + 112, z + 13)
		for delt in range(104, 113):
			self._common_cal(x, y, z, delt, delt, 13)

		# (x + 112, y + 112, z + 14) -> (x + 120, y + 120, z + 14)
		for delt in range(112, 121):
			self._common_cal(x, y, z, delt, delt, 14)

		# (x + 120, y + 120, z + 15) -> (x + 129, y + 129, z + 15)
		for delt in range(120, 130):
			self._common_cal(x, y, z, delt, delt, 15)

		# (x + 129, y + 129, z + 16) -> (x + 137, y + 137, z + 16)
		for delt in range(129, 138):
			self._common_cal(x, y, z, delt, delt, 16)

		# (x + 137, y + 137, z + 17) -> (x + 145, y + 145, z + 17)
		for delt in range(137, 146):
			self._common_cal(x, y, z, delt, delt, 17)


	def _common_cal(self, x, y, z, dx, dy, dz):
		cur = node.Node(x + dx, y + dy, z + dz)
		if self._check_valid(x + dx, y + dy, z + dz, cur):
			self.matrix[x + dx][y + dy][z + dz] = DataGenerator._selected
			self.fill_set_ponts.add(cur)


