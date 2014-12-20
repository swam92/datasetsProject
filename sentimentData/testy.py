
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.cluster import KMeans

data1 = np.loadtxt("NSAafterPosts.txt")
clusterer = KMeans(3)
cluster_indices = clusterer.fit_predict(data1)
cluster1 = [v for i, v in enumerate(data1) if cluster_indices[i] == 0]
cluster2 = [v for i, v in enumerate(data1) if cluster_indices[i] == 1]
cluster3 = [v for i, v in enumerate(data1) if cluster_indices[i] == 2]
plt.plot([a for a,b in cluster1], [b for a,b in cluster1],'ro')
plt.plot([a for a,b in cluster2], [b for a,b in cluster2],'bo')
plt.plot([a for a,b in cluster3], [b for a,b in cluster3],'go')
plt.show()

#data2 = np.loadtxt("result3DS.csv.txt", usecols=(2))
#plt.plot(data2,'ro')
#plt.show()
