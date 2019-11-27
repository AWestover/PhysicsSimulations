
import numpy as np
import matplotlib.pyplot as plt
import os
import json
from ipdb import set_trace as tr
from pprint import pprint

if __name__ == "__main__":

	with open('imgs/standard/pH.json', 'r') as fjson:
		standard = json.load(fjson)

	print(standard)
	Y = []
	for k in standard:
		print(standard[k])
		Y += [standard[k]]
	Y = np.array(Y)/255

	# Y = Y.reshape((1,Y.shape[0], Y.shape[1]))
	# plt.imshow(Y); plt.show()

	fdir = "imgs/samples"
	datas = {'first': [], 'second': [], 'third': []}
	for fb in [fn for fn in os.listdir(fdir) if '.json' in fn]:
		f = os.path.join(fdir, fb)
		with open(f, 'r') as fjson:
			tmp = json.load(fjson)
		for k in tmp:
			datas[k] += [tmp[k]]
	print(datas)

	X = np.array([datas['first'], datas['second'], datas['third']])/255
	
	labels = np.zeros((X.shape[0], X.shape[1]))
	for i in range(X.shape[0]):
		for j in range(X.shape[1]):
			diffs = np.linalg.norm(Y-X[i,j], axis=1)
			labels[i,j] = np.argmin(diffs)

	pprint(labels)

	plt.imshow(X); plt.show()

