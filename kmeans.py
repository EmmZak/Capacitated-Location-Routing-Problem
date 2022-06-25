import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from DataLoader import DataLoader

path = "dataset/Instances_Prodhon_LRP/coord50-5-2b.dat"
dataset = DataLoader(path = path)
customers = np.array(dataset.customer_coordinates_list, dtype=int)
depots = np.array(dataset.depot_coordinates_list)

kmeans = KMeans(init="random", n_clusters = dataset.nb_depots, n_init=10, max_iter = 300, random_state=42)
kmeans.fit(customers)
labels = kmeans.predict(customers)

plt.scatter(customers[:,0], customers[:,1], c=labels, linewidths=1)
plt.scatter(depots[:,0], depots[:,1], marker="o", linewidths=20)
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], c=np.unique(labels), marker="+", linewidths=20)

for x, y in customers:
    pass

plt.show()
