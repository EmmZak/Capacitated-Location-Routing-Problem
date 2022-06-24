import numpy as np
import sklearn
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.svm import SVC
from core.DataLoader import DataLoader
from glob import glob
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split

DATABASE_PATHS = glob('./dataset/*/*')
"""
for path in DATABASE_PATHS:
    dataset = Dataset(path=path)

    for d in dataset.depot_list:
        x, y = d.get_x(), d.get_y()
        plt.scatter(x, y, c="black", linewidths=4)

        coords = f'({x:.2f}, {y:.2f})'
        plt.annotate(coords, (x, y), size=5)

    for d in dataset.customer_list:
        x, y = d.get_x(), d.get_y()
        plt.scatter(x, y, c="red", linewidths=1)

        coords = f'({x:.2f}, {y:.2f})'
        plt.annotate(coords, (x, y), size=3)

    plt.style.use("fivethirtyeight")
    #plt.plot(range(1, MAX_CLUSTERS), inertia_list)
    #plt.xticks(range(1, MAX_CLUSTERS))
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.title(path)
    plt.show(block=True)

    break
"""

PATH = DATABASE_PATHS[0]
data = DataLoader(path=PATH)

print(data.nb_depots, data.nb_customers)

exit()
COLORS = [
    "red", 
    "blue", 
    "green", 
    "cyan", 
    "magenta", 
    "yellow",
    "purple"
]

data = np.array(dataset.customer_coordinates_list, dtype=int)
X = scale(data)
depot = np.array(dataset.depot_coordinates_list, dtype=int)
y = scale(depot)



Y = np.zeros((100, 1), dtype=int)
for i in range(100):
    dist = []
    for j in range(5):
        dist.append(np.linalg.norm(X[i]-y[j]))
    Y[i] = np.argmin(dist)

train_X, test_X, train_Y, test_Y= train_test_split(X, Y, test_size=0.1)
print("size", train_X.shape, test_X.shape, train_Y.shape, test_Y.shape)

model = SVC()
model.fit(train_X, train_Y.reshape(-1))
labels = model.predict(train_X)

#kmeans = KMeans(init="random", n_clusters = dataset.nb_depots, n_init=10, max_iter = 300, random_state=42)
#kmeans.fit(train_X)
#labels = kmeans.predict(train_X)

plt.scatter(train_X[:,0], train_X[:,1], c=labels, linewidths=1)

#plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], c=np.unique(labels), marker="+", linewidths=20)

depots = np.array(dataset.depot_coordinates_list)
depots = scale(depots)

print("depots", depots)
plt.scatter(depots[:,0], depots[:,1], c=np.unique(labels), marker="o", linewidths=20)

#print("cluseters", kmeans.cluster_centers_)
#print("depots", depots)
#print("norm" , np.linalg.norm(kmeans.cluster_centers_-depots, 1))

plt.show()
