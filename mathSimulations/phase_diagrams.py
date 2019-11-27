import matplotlib.pyplot as plt
from os.path import join
import numpy as np


A = np.array([[1,-3],[1.2,-2.6]])
B = np.array([[0.6,-0.8],[0.8,0.6]])
C = np.array([[-0.8,0.6],[-0.8,-0.8]])


x0 = np.array([0,1])
print(A)
print(B)
print(C)

def plot_diagram(M, x0, name):
	ITTERATIONS = 20

	plt.cla()
	plt.xlim(-10,10)
	plt.ylim(-10,10)

	plt.scatter(0,0)

	plt.plot([0,x0[0]],[0,x0[1]])
	plt.pause(0.5)

	xt = x0
	for t in range(0, ITTERATIONS):
		xt = np.dot(M, xt)
		print(xt)
		plt.plot([0,xt[0]],[0,xt[1]])
		plt.pause(0.5)

	plt.savefig(join("pictures",name))
	plt.pause(2)

plot_diagram(C,x0,"C.png")
plot_diagram(B,x0,"B.png")
plot_diagram(A,x0,"A.png")

