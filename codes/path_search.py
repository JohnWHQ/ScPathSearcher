# coding: utf-8

import numpy as np
import node
import time

from collections import deque
from image_utils import generate_and_store_image


class PathSearcher:
	"""
	path searcher class
		(use bfs promote method to get has path from left to right, and generate pic if needed)
	init need n*m 2D matrix arg 
	"""

	def __init__(self, matrix):
		self.matrix = matrix

	def checkValid(self, matrix, gone_set, cur_node):
		"""
		check bound / matrixConnectedFlag / trace gone set
		"""
		if (cur_node.x < 0) or (cur_node.y < 0) \
		or (cur_node.x >= len(matrix)) or (cur_node.y >= len(matrix[0]))\
		or (cur_node in gone_set) or (matrix[cur_node.x][cur_node.y] != 1):
			return False
		else:
			return True

	def bfs_path_search(self, start_set, end_set, matrix, generate_image=False):
		"""
		Algorithom implements
			bfs promoted method(8 neighbor space)
				timeCost : O(n*m)
				spaceCost: O(n*m)
		"""
		for start_node in start_set:
			# print "calculting start node: {}".format(start_node)

			# 迭代双端队列 每次处理队首元素将其8邻域结点加入队尾等待处理
			node_deque = deque()
			node_deque.append(start_node)

			# 记录处理过的结点元素 (每个进入队列的元素已经作为触发点向终点遍历过算法迭代)
			trace_set = set()
			trace_set.add(start_node)

			while len(node_deque) != 0:
				cur = node_deque.popleft()
				# find end node map start node
				if cur in end_set:
					# print "Got path form {} to {}".format(start_node, cur)
					if generate_image is True:
						generate_and_store_image(matrix, start_node, cur, trace_set)
					return True

				cx = cur.x
				cy = cur.y

				# generate 8 neighbor nodes
				node1 = node.Node(cx - 1, cy)
				node2 = node.Node(cx - 1, cy + 1)
				node3 = node.Node(cx, cy + 1)
				node4 = node.Node(cx + 1, cy + 1)
				node5 = node.Node(cx + 1, cy)
				node6 = node.Node(cx + 1, cy - 1)
				node7 = node.Node(cx, cy - 1)
				node8 = node.Node(cx -1, cy - 1)

				if self.checkValid(matrix, trace_set, node1) == True:
					node_deque.append(node1)
					trace_set.add(node1)

				if self.checkValid(matrix, trace_set, node2) == True:
					node_deque.append(node2)
					trace_set.add(node2)

				if self.checkValid(matrix, trace_set, node3) == True:
					node_deque.append(node3)
					trace_set.add(node3)

				if self.checkValid(matrix, trace_set, node4) == True:
					node_deque.append(node4)
					trace_set.add(node4)

				if self.checkValid(matrix, trace_set, node5) == True:
					node_deque.append(node5)
					trace_set.add(node5)

				if self.checkValid(matrix, trace_set, node6) == True:
					node_deque.append(node6)
					trace_set.add(node6)

				if self.checkValid(matrix, trace_set, node7) == True:
					node_deque.append(node7)
					trace_set.add(node7)

				if self.checkValid(matrix, trace_set, node8) == True:
					node_deque.append(node8)
					trace_set.add(node8)

			# print "cur node: {} has no path to end".format(start_node)
		if generate_image is True:
			generate_and_store_image(matrix, None, None, None)

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

		left_quick_check = False
		right_quick_check = False

		# check left and right side, collect connected node to set
		for i in range(len(matrix)):
			if matrix[i][0] == 1:
				left_quick_check = True
				start_set.add(node.Node(i, 0))

			if matrix[i][len(matrix[i]) - 1] == 1:
				right_quick_check = True
				end_set.add(node.Node(i, len(matrix[i]) - 1))

		# quick check both set
		if (left_quick_check == False) or (right_quick_check == False):
			print "quick check search has no path, codes over..."
			return False

		print "quick check pass, may has path calculte size {} * {}".format(len(start_set), len(end_set))

		# calculate time cost
		res = self.bfs_path_search(start_set, end_set, matrix, generate_image=generate_image)

		end_time = time.time()
		print "res:{} \ncost seconds: {}".format(str(res), str(end_time - start_time))

		return res


