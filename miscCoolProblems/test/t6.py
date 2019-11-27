import matplotlib.pyplot as plt

def triangleInequality(a, b, c):
    c1 = a + b > c
    c2 = a + c > b
    c3 = b + c > a
    return c1 and c2 and c3

def tn(n):
    maxD = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if triangleInequality(i, j, k):
                    D = min(abs(i-j), abs(j-k), abs(i-k))
                    if D > maxD:
                        print(i, j, k, D)
                        maxD = D
    return maxD


trials = []
data = []

for i in range(3, 50):
    print(i)
    trials.append(i)
    data.append(tn(i))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(trials, data, 'r')
ax.scatter(trials, data, c='b')
plt.show()

#
# while True:
#     n = int(input("n"))
#     print(tn(n))
