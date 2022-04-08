# image generate and save

import node
import time
import matplotlib.pyplot as paint

from matplotlib.patches import Rectangle
from matplotlib.ticker import MultipleLocator


def generate_and_store_image(matrix, start, end, trace_set):
	paint.figure(figsize=(len(matrix), len(matrix[0])))

	ax = paint.gca()
	ax.xaxis.tick_top()

	ax.set_ylim(bottom = len(matrix), top = 0)
	ax.set_xlim(left = 0, right = len(matrix[0]))

	ax.spines['top'].set_position(('data', 0))
	ax.spines['left'].set_position(('data', 0))

	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			cur_node = node.Node(i, j)
			if matrix[i][j] == 1:
				rec = Rectangle((j, i), width = 1, height = 1, facecolor = "green", edgecolor = "black")
				ax.add_patch(rec)
			else:
				rec = Rectangle((j, i), width = 1, height = 1, facecolor = "white", edgecolor = "black")
				ax.add_patch(rec)
			if (trace_set is not None) and (cur_node in trace_set):
				rec = Rectangle((j + 0.25, i + 0.25), width = 0.25, height = 0.25, facecolor = "pink")
				ax.add_patch(rec)

	has_path = False
	if (start is not None) and (end is not None):
		has_path = True
		rec = Rectangle((start.y, start.x), width = 1, height = 1, color = "red")
		ax.add_patch(rec)	

		rec = Rectangle((end.y, end.x), width = 1, height = 1, color = "blue")
		ax.add_patch(rec)	

	paint.axis('equal')
	paint.axis('off')
	# paint.tight_layout()
	# paint.show()	

	filename = "./tmp/" + "{}*{}-{}-".format(len(matrix), len(matrix[0]), str(has_path)) + str(time.time()) + ".png"

	paint.savefig(filename)





	