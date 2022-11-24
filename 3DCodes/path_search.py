# coding: utf-8

import numpy as np
import node
import time

from collections import deque


class PathSearcher:
	def __init__(self, matrix):
		self.matrix = matrix

	def checkValid(self, matrix, gone_set, cur_node):
		"""
		check bound / matrixConnectedFlag / trace gone set
		"""
		if (cur_node.x < 0) or (cur_node.y < 0) or (cur_node.z < 0)\
		or (cur_node.x >= len(matrix)) or (cur_node.y >= len(matrix[0])) or (cur_node.z >= len(matrix[0][0]))\
		or (cur_node in gone_set) or (matrix[cur_node.x][cur_node.y][cur_node.z] != 1):
			return False
		else:
			return True

	def bfs_path_search(self, start_set, end_set, matrix, generate_image=False):
		"""
		Algorithom implements
			bfs promoted method(26 neighbor space)
				timeCost : O(n*m*l)
				spaceCost: O(n*m*l)
		"""

		# 记录启发处理过的结点元素
		trace_set = set()

		for start_node in start_set:
			# 迭代双端队列 每次处理队首元素将其26邻域结点加入队尾等待处理
			node_deque = deque()
			node_deque.append(start_node)

			while len(node_deque) != 0:
				cur = node_deque.popleft()
				# find end node map start node
				if cur in end_set:
					return True
				# global has been cal
				if cur in trace_set:
					continue
				cx = cur.x
				cy = cur.y
				cz = cur.z

				# use 8 seeds to generate 26 seeds neighbor nodes
				cur_neighbors = []
				seeds = []
				# generate 8 seeds neighbor nodes
				seeds.append(node.Node(cx - 1, cy, cz))
				seeds.append(node.Node(cx - 1, cy + 1, cz))
				seeds.append(node.Node(cx, cy + 1, cz))
				seeds.append(node.Node(cx + 1, cy + 1, cz))
				seeds.append(node.Node(cx + 1, cy, cz))
				seeds.append(node.Node(cx + 1, cy - 1, cz))
				seeds.append(node.Node(cx, cy - 1, cz))
				seeds.append(node.Node(cx -1, cy - 1, cz))

				# generate 26 seeds neighbor nodes
				for cur_seed in seeds:
					cur_neighbors.append(cur_seed)
					cur_neighbors.append(node.Node(cur_seed.x, cur_seed.y, cur_seed.z + 1))
					cur_neighbors.append(node.Node(cur_seed.x, cur_seed.y, cur_seed.z - 1))

				cur_neighbors.append(node.Node(cx, cy, cz + 1))
				cur_neighbors.append(node.Node(cx, cy, cz - 1))

				for to_node in cur_neighbors:
					if self.checkValid(matrix, trace_set, to_node):
						node_deque.append(to_node)
				trace_set.add(cur)

		return False

	def run(self, generate_image=False):
		"""
			searching trigger method
			return boolean
				True has path
				False Has no path
		"""
		matrix = self.matrix

		start_time = time.time()

		# side quick check and init start/end set nodes
		start_set = set()
		end_set = set()

		back_quick_check = False
		front_quick_check = False

		# check back and front side, collect connected node to set
		for j in range(len(matrix[0])):
			for k in range(len(matrix[0][j])):
				if matrix[0][j][k] == 1:
					back_quick_check = True
					start_set.add(node.Node(0, j, k))

				if matrix[len(matrix) - 1][j][k] == 1:
					front_quick_check = True
					end_set.add(node.Node(len(matrix) - 1, j, k))

		# quick check both set
		if (back_quick_check == False) or (front_quick_check == False):
			print "quick check search has no path, codes over..."
			return False

		print "quick check pass, may has path calculte size {} * {}".format(len(start_set), len(end_set))

		# calculate time cost
		res = self.bfs_path_search(start_set, end_set, matrix, generate_image=generate_image)

		end_time = time.time()
		print "res:{} \ncalcul cost seconds: {}".format(str(res), str(end_time - start_time))

		return res


