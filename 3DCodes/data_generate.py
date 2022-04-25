# data generate codes

import numpy as np
import time


class DataGenerator:
	_selected = 1
	_sp_point = 2

	def __init__(self, n, m, l, x):

		start_time = time.time()

		self.row = n
		self.col = m
		self.height = l

		# expect set point counts
		self.x = x

		self.total = n * m * l
		# build matrix and set selected point with x / row * col * height probability
		self.matrix, self.real_x = self._init_matrix()

		self.all_select = self._generate_rule_shape_by_probability()

		self.v_percent = float(self.all_select) / float(self.total)

		end_time = time.time()
		print "DataGenrateDone:size={}x{}x{}\nsampleSetPoints={}\nrealSetPoints={}\nallSelectPoints={}\nvPercent={}\ncost seconds={}"\
		.format(str(n), str(m), str(l), str(x), str(self.real_x), str(self.all_select), str(self.v_percent), str(end_time - start_time))

	def _init_matrix(self):

		matrix = np.zeros((self.row, self.col, self.height))
		real_x = 0

		for i in range(self.row):
			for j in range(self.col):
				for k in range(self.height):
					# equiprobability generate rand from 1 ~ total 
					cur_rand = np.random.randint(self.total) + 1

					# per cell has x / row * col * height equiprobability to set 1 that mean set mid point
					if cur_rand <= self.x:
						matrix[i][j][k] = DataGenerator._sp_point
						real_x = real_x + 1

		return matrix, real_x		

	def _generate_rule_shape_by_probability(self):

		for i in range(self.row):
			for j in range(self.col):
				for k in range(self.height):
					if self.matrix[i][j][k] == DataGenerator._sp_point:
						# equiprobability generate rand from 1 ~ total 
						cur_rand = np.random.randint(100) + 1
						direction_rand = np.random.randint(100) + 1

						# 2% probability to generate 208 (147)
						if cur_rand >= 1 and cur_rand <= 2:
							self._generate_uni_shape(i, j, k, 208, 147 ,54, 104, direction_rand)

						# 3% probability to generate 188 (133)
						if cur_rand >= 3 and cur_rand <= 5:
							self._generate_uni_shape(i, j, k, 188, 133 ,48, 94, direction_rand)

						# 7% probability to generate 146 (103)
						if cur_rand >= 6 and cur_rand <= 12:
							self._generate_uni_shape(i, j, k, 146, 103 ,38, 73, direction_rand)

						# 10% probability to generate 125 (88)
						if cur_rand >= 13 and cur_rand <= 22:
							self._generate_uni_shape(i, j, k, 125, 88 ,32, 63, direction_rand)

						# 16% probability to generate 104 (74)
						if cur_rand >= 23 and cur_rand <= 38:
							self._generate_uni_shape(i, j, k, 104, 74 ,27, 52, direction_rand)

						# 17% probability to generate 63 (45)
						if cur_rand >= 39 and cur_rand <= 55:
							self._generate_uni_shape(i, j, k, 64, 45 ,16, 32, direction_rand)

						# 30% probability to generate 42 (30)
						if cur_rand >= 56 and cur_rand <= 85:
							self._generate_uni_shape(i, j, k, 42, 30 ,11, 21, direction_rand)

						# 15% probability to generate 21 (15)
						if cur_rand >= 86 and cur_rand <= 100:
							self._generate_uni_shape(i, j, k, 21, 15 ,5, 11, direction_rand)
						
		res = 0

		for i in range(self.row):
			for j in range(self.col):
				for k in range(self.height):
					if self.matrix[i][j][k] == DataGenerator._sp_point:
						self.matrix[i][j][k] = DataGenerator._selected

					if self.matrix[i][j][k] == DataGenerator._selected:
						res = res + 1
		return res

	def _generate_uni_shape(self, x, y, z, length0, width45, h15, h30, percent_rand):
		"""
		calculate uniform shape
		"""

		# 0 degree case 25%
		if percent_rand > 0 and percent_rand <= 25:
			# cur diff move
			cur_half = (length0 / 2)

			# odd and even case
			if (length0 & 1) == 1:
				# odd symmetry
				for i in range(1, (cur_half + 1)):
					# right move
					cur_right = y + i
					if cur_right < self.col:
						self.matrix[x][cur_right][z] = DataGenerator._selected
					# left move
					cur_left = y - i
					if cur_left >= 0:
						self.matrix[x][cur_left][z] = DataGenerator._selected
			else:
				# even symmetry
				# right move
				for i in range(1, (cur_half + 1)):
					cur_right = y + i
					if cur_right < self.col:
						self.matrix[x][cur_right][z] = DataGenerator._selected
				# left move
				for i in range(1, cur_half):
					cur_left = y - i
					if cur_left >= 0:
						self.matrix[x][cur_left][z] = DataGenerator._selected				

		# 45 degree case 25%
		if percent_rand > 25 and percent_rand <= 50:
			# cur diff move
			cur_half = (width45 / 2)

			# odd and even case
			if (width45 & 1) == 1:
				# odd symmetry
				for i in range(1, (cur_half + 1)):
					cur_x_right_up = x - i
					cur_y_right_up = y + i
					if cur_x_right_up >= 0 and cur_y_right_up < self.col:
						self.matrix[cur_x_right_up][cur_y_right_up][z] = DataGenerator._selected

					cur_x_left_down = x + i
					cur_y_left_down = y - i
					if cur_x_left_down < self.row and cur_y_left_down >= 0:
						self.matrix[cur_x_left_down][cur_y_left_down][z] = DataGenerator._selected
			else:
				# even symmetry
				for i in range(1, (cur_half + 1)):
					cur_x_right_up = x - i
					cur_y_right_up = y + i
					if cur_x_right_up >= 0 and cur_y_right_up < self.col:
						self.matrix[cur_x_right_up][cur_y_right_up][z] = DataGenerator._selected

				for i in range(1, cur_half):
					cur_x_left_down = x + i
					cur_y_left_down = y - i
					if cur_x_left_down < self.row and cur_y_left_down >= 0:
						self.matrix[cur_x_left_down][cur_y_left_down][z] = DataGenerator._selected

		# 15 degree case 25%
		if percent_rand > 50 and percent_rand <= 75:
			# cur diff move
			cur_half = (h15 / 2)

			# odd and even case 4 4 3
			if (h15 & 1) == 1:
				# odd symmetry mid 3 (cal mid fuck to even case) 
				self._generate_sub_shape_from_mid(x, y, z, 2)

				dx_right_up = x - 1
				dy_right_up = y + 2

				dx_left_down = x + 1
				dy_left_down = y - 2
			else:
				# even symmetry
				dx_right_up = x - 1
				dy_right_up = y + 1

				dx_left_down = x
				dy_left_down = y

			# 4 4 3
			for i in range(1, (cur_half + 1)):
				if (i % 3) == 0:
					self._generate_sub_shape_from_left_2_right(dx_right_up, dy_right_up, z, 3)
					self._generate_sub_shape_from_right_2_left(dx_left_down, dy_left_down, z, 3)

					dx_right_up = dx_right_up - 1
					dy_right_up = dy_right_up + 3

					dx_left_down = dx_left_down + 1
					dy_left_down = dy_left_down - 3						
				else:
					self._generate_sub_shape_from_left_2_right(dx_right_up, dy_right_up, z, 4)
					self._generate_sub_shape_from_right_2_left(dx_left_down, dy_left_down, z, 4)

					dx_right_up = dx_right_up - 1
					dy_right_up = dy_right_up + 4

					dx_left_down = dx_left_down + 1
					dy_left_down = dy_left_down - 4
				


		# 30 degree case 25%
		if percent_rand > 75 and percent_rand <= 100:
			# cur diff move
			cur_half = (h30 / 2)

			# odd and even case
			if (h30 & 1) == 1:
				# odd symmetry mid 1 (cal mid fuck to even case)
				self._generate_sub_shape_from_mid(x, y, z, 1)

				dx_right_up = x - 1
				dy_right_up = y + 1

				dx_left_down = x + 1
				dy_left_down = y - 1
			else:
				# even symmetry
				dx_right_up = x - 1
				dy_right_up = y + 1

				dx_left_down = x
				dy_left_down = y

			# 2 2 1
			for i in range(1, (cur_half + 1)):
				if (i % 3) == 0:
					self._generate_sub_shape_from_left_2_right(dx_right_up, dy_right_up, z, 1)
					self._generate_sub_shape_from_right_2_left(dx_left_down, dy_left_down, z, 1)

					dx_right_up = dx_right_up - 1
					dy_right_up = dy_right_up + 1

					dx_left_down = dx_left_down + 1
					dy_left_down = dy_left_down - 1						
				else:
					self._generate_sub_shape_from_left_2_right(dx_right_up, dy_right_up, z, 2)
					self._generate_sub_shape_from_right_2_left(dx_left_down, dy_left_down, z, 2)

					dx_right_up = dx_right_up - 1
					dy_right_up = dy_right_up + 2

					dx_left_down = dx_left_down + 1
					dy_left_down = dy_left_down - 2	


	def _generate_sub_shape_from_mid(self, x, y, z, diff):
		# only for odd symmetry
		if (x < 0) or (x >= self.row) or (y < 0) or (y >= self.col) or (z < 0) or (z >= self.height): 
			return

		self.matrix[x][y][z] = DataGenerator._selected

		for i in range(1, diff):
			cur_right_y =  y + i
			cur_left_y = y - i
			if cur_right_y < self.col:
				self.matrix[x][cur_right_y][z] = DataGenerator._selected
			if cur_left_y >= 0:
				self.matrix[x][cur_left_y][z] = DataGenerator._selected			


	def _generate_sub_shape_from_left_2_right(self, x, y, z, diff):
		# include (x, y)
		if (x < 0) or (x >= self.row) or (y < 0) or (y >= self.col) or (z < 0) or (z >= self.height): 
			return
		for i in range(diff):
			dy = y + i
			if dy < self.col:
				self.matrix[x][dy][z] = DataGenerator._selected


	def _generate_sub_shape_from_right_2_left(self, x, y, z, diff):
		# include (x, y)
		if (x < 0) or (x >= self.row) or (y < 0) or (y >= self.col) or (z < 0) or (z >= self.height): 
			return
		for i in range(diff):
			dy = y - i
			if dy >= 0:
				self.matrix[x][dy][z] = DataGenerator._selected



