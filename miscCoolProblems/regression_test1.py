import matplotlib.pyplot as plt
import random
import numpy as np


# xs = np.random.randn(1, 10) # columns are features(1), rows are examples/data points
# fs = np.random.randn(1, 10) # function values
#
#
# bias = np.random.randn(1)
# weights = np.random.randn(1)
#
#
#
# def f(x, weights):
#     return x.dot(weights)
#
# def cost(x, fs, weights, bias):
#     return (np.sum(bias + x.T.dot(weights) - fs)**2)/(2*x.shape[0])
#
# def grad():
#     pass



xs = [i*0.002 + random.random() for i in range (0, 100)]
ys = [i*0.003 + random.random() for i in range (0, 100)]

m = random.random()
b = random.random()

m0 = m
b0 = b

print(m,b)

alpha = 10**-2

def gradDescent(xs, ys, m, b):
    gSumM = 0
    gSumB = 0
    for i in range(0, len(xs)):
        gSumM += (ys[i] - xs[i]*m + b)*xs[i]
        gSumB += (ys[i] - xs[i]*m + b)
    m -= alpha*gSumM
    b -= alpha*gSumB
    return m, b


itterations = 20
for i in range(0, itterations):
    m, b = gradDescent(xs, ys, m, b)

print(m, b)


testXs = np.linspace(0, 10, 100)
testFs = testXs*m + b
preFs = testXs*m0 +b0


fig = plt.figure()
ax = fig.add_subplot(111)
#ax.scatter(xs[0], fs)
ax.scatter(xs, ys)

ax.scatter(testXs, preFs)
ax.scatter(testXs, testFs)

fig.show()


input()



#______________________________________________________________________________
