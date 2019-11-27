import numpy as np
import matplotlib.pyplot as plt

A=np.array([[-1.5,-1],[2,0.5]])

def xn(xc):
	return np.dot(A,xc)


xc = np.array([-1,1])
xs=[]
for i in range(0, 50):
	xs.append(xc)
	xc=xn(xc)
plt.plot([xsi[0] for xsi in xs], [xsi[1] for xsi in xs])

plt.show()
