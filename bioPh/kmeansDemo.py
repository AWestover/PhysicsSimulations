
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

a=np.random.random((100,3))
b=np.random.random((100,3))
b += np.array([1,1,1])
ab = np.concatenate([a,b])
plt.scatter(ab[:,0], ab[:,1]); plt.show()

kmeans = KMeans(n_clusters=2).fit(ab)
print(kmeans.labels_)
print(kmeans.cluster_centers_)

