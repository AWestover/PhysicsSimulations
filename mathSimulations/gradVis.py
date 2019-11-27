
import matplotlib.pyplot as plt
import numpy as np

X, Y = np.meshgrid(np.linspace(-1.75,1.75,20),np.linspace(-1.75,1.75,20))
U = X*(4*X**2+4*Y**2-5)
V = Y*(4*X**2+4*Y**2+3)

mags = np.sqrt(U**2+V**2)
U = U / mags
V = V / mags 

scale = 20

theta = np.linspace(0,2*np.pi,50)

leftCircleX = 0.5*np.cos(theta)-1
leftCircleY = 0.5*np.sin(theta)

rightCircleX = 0.5*np.cos(theta)+1
rightCircleY = 0.5*np.sin(theta)


plt.quiver(X,Y,U*scale,V*scale)
plt.plot(leftCircleX, leftCircleY)
plt.plot(rightCircleX, rightCircleY)
plt.savefig("pictures/circleGrads.png")
plt.show()

