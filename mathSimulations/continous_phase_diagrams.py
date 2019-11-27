import numpy as np
import matplotlib.pyplot as plt

from pdb import set_trace as tr

"""
X,Y = np.meshgrid(np.linspace(-100,100,20), np.linspace(-100,100,20))

U=Y
V=-X
"""

"""
x=np.array([40,200])
y=np.array([30,10])
plt.quiver(x[0],x[1],y[0],y[1])
"""

# plt.quiver(X,Y,U,V)

def dxdt(x):
	A=np.array([[3,0],[-2.5,0.5]])
	#A = np.array([[3,-2],[5,-3]])
	return np.dot(A, x)
"""
xs,ys=np.meshgrid(np.linspace(-4,4,8),np.linspace(-4,4,8))
xps,yps=np.zeros(xs.shape),np.zeros(ys.shape)
tr()
for i in range(0,len(xs)):
	for j in range(0, len(xs[i])):
		cres=dxdt(np.array([xs[i][j], ys[i][j]]))
		xps=cres[0]; yps=cres[1];
"""

xs=[]
ys=[]
xps=[]
yps=[]


s=20
c=100

for xi in range(0,s):
	i = c*(xi-s//2)
	for yj in range(0, s):
		j=c*(yj-s//2)
		xs.append(i)
		ys.append(j)
		cres=dxdt(np.array([i,j]))
		xps.append(cres[0])
		yps.append(cres[1])




plt.quiver(xs,ys,xps,yps)

plt.show()

