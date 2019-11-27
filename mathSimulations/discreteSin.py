
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import comb

def sind(x):
    curSum = 0
    for i in range(0, int((abs(x)-1)/2)+1):
        curSum += comb(abs(x), 2*i+1)*(-1)**(i)
    return np.sign(x)*curSum


pts = [i for i in range(-10, 10+1)]
vals = [sind(pt) for pt in pts]

plt.plot(pts, vals)
plt.show()

