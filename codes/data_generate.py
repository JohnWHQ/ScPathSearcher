# data generate codes

import numpy as np
# np.set_printoptions(threshold=np.inf)


class DataGenerator:
	_selected = 1
	_sp_point = 2

	def __init__(self, n, m, x):
		self.row = n
		self.col = m
		self.x = x

		self.total = n * m
		# build matrix and set selected point with x / row * col probability
		self.matrix, self.real_x = self._init_matrix()

		self.all_select = self._generate_rule_shape_by_probability()

		self.v_percent = float(self.all_select) / float(self.total)

	def _init_matrix(self):

		matrix = np.zeros([self.row, self.col])
		real_x = 0

		for i in range(self.row):
			for j in range(self.col):
				# equiprobability generate rand from 1 ~ total 
				cur_rand = np.random.randint(self.total) + 1

				# per cell has x / row * col equiprobability to set 1 that mean set mid point
				if cur_rand <= self.x:
					matrix[i][j] = DataGenerator._sp_point
					real_x = real_x + 1

		return matrix, real_x		

	def _generate_rule_shape_by_probability(self):

		for i in range(self.row):
			for j in range(self.col):

				if self.matrix[i][j] == DataGenerator._sp_point:
					# equiprobability generate rand from 1 ~ total 
					cur_rand = np.random.randint(100) + 1
					direction_rand = np.random.randint(100) + 1

					# 2% probability to generate 208 (147)
					if cur_rand >= 1 and cur_rand <= 2:
						self._generate_type_208(i, j, direction_rand)

					# 3% probability to generate 188 (133)
					if cur_rand >= 3 and cur_rand <= 5:
						self._generate_type_188(i, j, direction_rand)

					# 7% probability to generate 146 (103)
					if cur_rand >= 6 and cur_rand <= 12:
						self._generate_type_146(i, j, direction_rand)

					# 10% probability to generate 125 (88)
					if cur_rand >= 13 and cur_rand <= 22:
						self._generate_type_125(i, j, direction_rand)

					# 16% probability to generate 104 (74)
					if cur_rand >= 23 and cur_rand <= 38:
						self._generate_type_104(i, j, direction_rand)

					# 17% probability to generate 63 (45)
					if cur_rand >= 39 and cur_rand <= 55:
						self._generate_type_63(i, j, direction_rand)

					# 30% probability to generate 42 (30)
					if cur_rand >= 56 and cur_rand <= 85:
						self._generate_type_42(i, j, direction_rand)

					# 15% probability to generate 21 (15)
					if cur_rand >= 86 and cur_rand <= 100:
						self._generate_type_21(i, j, direction_rand)

		res = 0
		for i in range(self.row):
			for j in range(self.col):
				if self.matrix[i][j] == DataGenerator._sp_point:
					self.matrix[i][j] = DataGenerator._selected

				if self.matrix[i][j] == DataGenerator._selected:
					res = res + 1
		return res


	def _generate_type_208(self, x, y, percent_rand):
		# 45 degree is 147 cells

		if percent_rand > 0 and percent_rand <= 50:
			for i in range(105):
				cur_right = y + i
				if cur_right < self.col:
					self.matrix[x][cur_right] = DataGenerator._selected

			for i in range(1, 104):
				cur_left =  y - i
				if cur_left >= 0:
					self.matrix[x][cur_left] = DataGenerator._selected

		if percent_rand > 50 and percent_rand <= 75:
			for i in range(1, 74):
				cur_x_right_up = x - i
				cur_y_right_up = y + i
				if cur_x_right_up >= 0 and cur_y_right_up < self.col:
					self.matrix[cur_x_right_up][cur_y_right_up] = DataGenerator._selected

				cur_x_left_down = x + i
				cur_y_left_down = y - i
				if cur_x_left_down < self.row and cur_y_left_down >= 0:
					self.matrix[cur_x_left_down][cur_y_left_down] = DataGenerator._selected

		if percent_rand > 75 and percent_rand <= 100:
			for i in range(1, 74):
				cur_x_left_up = x - i
				cur_y_left_up = y - i
				if cur_x_left_up >= 0 and cur_y_left_up >= 0:
					self.matrix[cur_x_left_up][cur_y_left_up] = DataGenerator._selected

				cur_x_right_down = x + i
				cur_y_right_down = y + i
				if cur_x_right_down < self.row and cur_y_right_down < self.col:
					self.matrix[cur_x_right_down][cur_y_right_down] = DataGenerator._selected


	def _generate_type_188(self, x, y, percent_rand):
		# 45 degree is 133 cells

		if percent_rand > 0 and percent_rand <= 50:
			for i in range(95):
				cur_right = y + i
				if cur_right < self.col:
					self.matrix[x][cur_right] = DataGenerator._selected

			for i in range(1, 94):
				cur_left =  y - i
				if cur_left >= 0:
					self.matrix[x][cur_left] = DataGenerator._selected

		if percent_rand > 50 and percent_rand <= 75:
			for i in range(1, 67):
				cur_x_right_up = x - i
				cur_y_right_up = y + i
				if cur_x_right_up >= 0 and cur_y_right_up < self.col:
					self.matrix[cur_x_right_up][cur_y_right_up] = DataGenerator._selected

				cur_x_left_down = x + i
				cur_y_left_down = y - i
				if cur_x_left_down < self.row and cur_y_left_down >= 0:
					self.matrix[cur_x_left_down][cur_y_left_down] = DataGenerator._selected

		if percent_rand > 75 and percent_rand <= 100:
			for i in range(1, 67):
				cur_x_left_up = x - i
				cur_y_left_up = y - i
				if cur_x_left_up >= 0 and cur_y_left_up >= 0:
					self.matrix[cur_x_left_up][cur_y_left_up] = DataGenerator._selected

				cur_x_right_down = x + i
				cur_y_right_down = y + i
				if cur_x_right_down < self.row and cur_y_right_down < self.col:
					self.matrix[cur_x_right_down][cur_y_right_down] = DataGenerator._selected


	def _generate_type_146(self, x, y, percent_rand):
		# 45 degree is 103 cells

		if percent_rand > 0 and percent_rand <= 50:
			for i in range(74):
				cur_right = y + i
				if cur_right < self.col:
					self.matrix[x][cur_right] = DataGenerator._selected

			for i in range(1, 73):
				cur_left =  y - i
				if cur_left >= 0:
					self.matrix[x][cur_left] = DataGenerator._selected

		if percent_rand > 50 and percent_rand <= 75:
			for i in range(1, 51):
				cur_x_right_up = x - i
				cur_y_right_up = y + i
				if cur_x_right_up >= 0 and cur_y_right_up < self.col:
					self.matrix[cur_x_right_up][cur_y_right_up] = DataGenerator._selected

				cur_x_left_down = x + i
				cur_y_left_down = y - i
				if cur_x_left_down < self.row and cur_y_left_down >= 0:
					self.matrix[cur_x_left_down][cur_y_left_down] = DataGenerator._selected

		if percent_rand > 75 and percent_rand <= 100:
			for i in range(1, 51):
				cur_x_left_up = x - i
				cur_y_left_up = y - i
				if cur_x_left_up >= 0 and cur_y_left_up >= 0:
					self.matrix[cur_x_left_up][cur_y_left_up] = DataGenerator._selected

				cur_x_right_down = x + i
				cur_y_right_down = y + i
				if cur_x_right_down < self.row and cur_y_right_down < self.col:
					self.matrix[cur_x_right_down][cur_y_right_down] = DataGenerator._selected


	def _generate_type_125(self, x, y, percent_rand):
		# 45 degree is 88 cells

		if percent_rand > 0 and percent_rand <= 50:
			for i in range(63):
				cur_right = y + i
				if cur_right < self.col:
					self.matrix[x][cur_right] = DataGenerator._selected

				cur_left =  y - i
				if cur_left >= 0:
					self.matrix[x][cur_left] = DataGenerator._selected

		if percent_rand > 50 and percent_rand <= 75:
			for i in range(1, 45):
				cur_x_right_up = x - i
				cur_y_right_up = y + i
				if cur_x_right_up >= 0 and cur_y_right_up < self.col:
					self.matrix[cur_x_right_up][cur_y_right_up] = DataGenerator._selected

				cur_x_left_down = x + i
				cur_y_left_down = y - i
				if cur_x_left_down < self.row and cur_y_left_down >= 0:
					self.matrix[cur_x_left_down][cur_y_left_down] = DataGenerator._selected

		if percent_rand > 75 and percent_rand <= 100:
			for i in range(1, 44):
				cur_x_left_up = x - i
				cur_y_left_up = y - i
				if cur_x_left_up >= 0 and cur_y_left_up >= 0:
					self.matrix[cur_x_left_up][cur_y_left_up] = DataGenerator._selected

				cur_x_right_down = x + i
				cur_y_right_down = y + i
				if cur_x_right_down < self.row and cur_y_right_down < self.col:
					self.matrix[cur_x_right_down][cur_y_right_down] = DataGenerator._selected


	def _generate_type_104(self, x, y, percent_rand):
		# 45 degree is 74 cells

		if percent_rand > 0 and percent_rand <= 50:
			for i in range(53):
				cur_right = y + i
				if cur_right < self.col:
					self.matrix[x][cur_right] = DataGenerator._selected

			for i in range(52):
				cur_left =  y - i
				if cur_left >= 0:
					self.matrix[x][cur_left] = DataGenerator._selected

		if percent_rand > 50 and percent_rand <= 75:
			for i in range(1, 33):
				cur_x_right_up = x - i
				cur_y_right_up = y + i
				if cur_x_right_up >= 0 and cur_y_right_up < self.col:
					self.matrix[cur_x_right_up][cur_y_right_up] = DataGenerator._selected

				cur_x_left_down = x + i
				cur_y_left_down = y - i
				if cur_x_left_down < self.row and cur_y_left_down >= 0:
					self.matrix[cur_x_left_down][cur_y_left_down] = DataGenerator._selected

		if percent_rand > 75 and percent_rand <= 100:
			for i in range(1, 32):
				cur_x_left_up = x - i
				cur_y_left_up = y - i
				if cur_x_left_up >= 0 and cur_y_left_up >= 0:
					self.matrix[cur_x_left_up][cur_y_left_up] = DataGenerator._selected

				cur_x_right_down = x + i
				cur_y_right_down = y + i
				if cur_x_right_down < self.row and cur_y_right_down < self.col:
					self.matrix[cur_x_right_down][cur_y_right_down] = DataGenerator._selected	


	def _generate_type_63(self, x, y, percent_rand):
		# 45 degree is 45 cells

		if percent_rand > 0 and percent_rand <= 50:
			for i in range(32):
				cur_right = y + i
				if cur_right < self.col:
					self.matrix[x][cur_right] = DataGenerator._selected

				cur_left =  y - i
				if cur_left >= 0:
					self.matrix[x][cur_left] = DataGenerator._selected

		if percent_rand > 50 and percent_rand <= 75:
			for i in range(1, 22):
				cur_x_right_up = x - i
				cur_y_right_up = y + i
				if cur_x_right_up >= 0 and cur_y_right_up < self.col:
					self.matrix[cur_x_right_up][cur_y_right_up] = DataGenerator._selected

				cur_x_left_down = x + i
				cur_y_left_down = y - i
				if cur_x_left_down < self.row and cur_y_left_down >= 0:
					self.matrix[cur_x_left_down][cur_y_left_down] = DataGenerator._selected

		if percent_rand > 75 and percent_rand <= 100:
			for i in range(1, 22):
				cur_x_left_up = x - i
				cur_y_left_up = y - i
				if cur_x_left_up >= 0 and cur_y_left_up >= 0:
					self.matrix[cur_x_left_up][cur_y_left_up] = DataGenerator._selected

				cur_x_right_down = x + i
				cur_y_right_down = y + i
				if cur_x_right_down < self.row and cur_y_right_down < self.col:
					self.matrix[cur_x_right_down][cur_y_right_down] = DataGenerator._selected	


	def _generate_type_42(self, x, y, percent_rand):
		# 45 degree is 30 cells

		if percent_rand > 0 and percent_rand <= 50:
			for i in range(22):
				cur_right = y + i
				if cur_right < self.col:
					self.matrix[x][cur_right] = DataGenerator._selected

			for i in range(21):
				cur_left =  y - i
				if cur_left >= 0:
					self.matrix[x][cur_left] = DataGenerator._selected

		if percent_rand > 50 and percent_rand <= 75:
			for i in range(1, 16):
				cur_x_right_up = x - i
				cur_y_right_up = y + i
				if cur_x_right_up >= 0 and cur_y_right_up < self.col:
					self.matrix[cur_x_right_up][cur_y_right_up] = DataGenerator._selected

				cur_x_left_down = x + i
				cur_y_left_down = y - i
				if cur_x_left_down < self.row and cur_y_left_down >= 0:
					self.matrix[cur_x_left_down][cur_y_left_down] = DataGenerator._selected

		if percent_rand > 75 and percent_rand <= 100:
			for i in range(1, 15):
				cur_x_left_up = x - i
				cur_y_left_up = y - i
				if cur_x_left_up >= 0 and cur_y_left_up >= 0:
					self.matrix[cur_x_left_up][cur_y_left_up] = DataGenerator._selected

				cur_x_right_down = x + i
				cur_y_right_down = y + i
				if cur_x_right_down < self.row and cur_y_right_down < self.col:
					self.matrix[cur_x_right_down][cur_y_right_down] = DataGenerator._selected	


	def _generate_type_21(self, x, y, percent_rand):
		# 45 degree is 15 cells

		if percent_rand > 0 and percent_rand <= 50:
			for i in range(11):
				cur_right = y + i
				if cur_right < self.col:
					self.matrix[x][cur_right] = DataGenerator._selected

				cur_left =  y - i
				if cur_left >= 0:
					self.matrix[x][cur_left] = DataGenerator._selected

		if percent_rand > 50 and percent_rand <= 75:
			for i in range(1, 7):
				cur_x_right_up = x - i
				cur_y_right_up = y + i
				if cur_x_right_up >= 0 and cur_y_right_up < self.col:
					self.matrix[cur_x_right_up][cur_y_right_up] = DataGenerator._selected

				cur_x_left_down = x + i
				cur_y_left_down = y - i
				if cur_x_left_down < self.row and cur_y_left_down >= 0:
					self.matrix[cur_x_left_down][cur_y_left_down] = DataGenerator._selected

		if percent_rand > 75 and percent_rand <= 100:
			for i in range(1, 7):
				cur_x_left_up = x - i
				cur_y_left_up = y - i
				if cur_x_left_up >= 0 and cur_y_left_up >= 0:
					self.matrix[cur_x_left_up][cur_y_left_up] = DataGenerator._selected

				cur_x_right_down = x + i
				cur_y_right_down = y + i
				if cur_x_right_down < self.row and cur_y_right_down < self.col:
					self.matrix[cur_x_right_down][cur_y_right_down] = DataGenerator._selected	



