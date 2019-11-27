
import numpy as np
from sklearn.cluster import KMeans
from PIL import Image, ImageFilter
import os
from ipdb import set_trace as tr
import matplotlib.pyplot as plt
import json

LOW = 2
HIGH = -2
BOTTOM = -2
TOP = 2

def twoBiggestInds(x):
	secondBig = -np.inf; big = -np.inf
	bigInd = 0; secondBigInd = 0
	for i in range(LOW, len(x)+HIGH):
		if x[i] > secondBig:
			if x[i] > big:
				secondBig = big; secondBigInd = bigInd
				big = x[i]; bigInd = i
			else:
				secondBig = x[i]; secondBigInd = i
	return sorted([bigInd, secondBigInd])


if __name__ == "__main__":
	fdir = "imgs/standard"
	# fdir = "imgs/samples"
	if fdir == 'imgs/samples':
		for fb in [fn for fn in os.listdir(fdir) if '.jpeg' in fn]:
			f = os.path.join(fdir, fb)
			img = Image.open(f)
			img = img.resize((32,32))
			image = img.filter(ImageFilter.FIND_EDGES)
			edgeData = np.array(image)
			edgeData = np.linalg.norm(edgeData, axis=2)
			edgeData = np.sum(edgeData, axis=0).tolist()
			inds = twoBiggestInds(edgeData)

			data = np.array(img)
			first = data[TOP:BOTTOM,LOW:inds[0]]
			second = data[TOP:BOTTOM,inds[0]:inds[1]]
			third = data[TOP:BOTTOM,inds[1]:HIGH]
			# plt.imshow(first); plt.show()
			# plt.imshow(second); plt.show()
			# plt.imshow(third); plt.show()
			try:
				first = np.average(np.average(first, axis=0), axis=0).tolist()
				second = np.average(np.average(second, axis=0), axis=0).tolist()
				third = np.average(np.average(third, axis=0), axis=0).tolist()
			except: 
				tr()

			# data = data.reshape((data.shape[0]*data.shape[1], 3))
			# kmeans = KMeans(n_clusters=3).fit(data)
			# print("do somehting like kmeans.cluster_centers_")

			with open(f.replace('.jpeg', '.json'), 'w') as fjson:
				json.dump({'first': first, 'second': second, 'third': third}, fjson)
	elif fdir == 'imgs/standard':
		f = 'imgs/standard/pH.png'
		img = Image.open(f)
		img = img.resize((32,32))
		data = np.array(img)
			
		# this one is nice, no edge detection, loop suffices
		inds = [[2+3*j, 2+3*j+1] for j in range(10)]
		# print(inds)

		colors = {}
		for i in range(len(inds)):
			cData = data[10:25, inds[i], 0:3]
			# plt.imshow(cData); plt.show()
			colors[i] = np.average(np.average(cData, axis=0), axis=0).tolist()

		with open('imgs/standard/pH.json', 'w') as fjson:
			json.dump(colors, fjson)
