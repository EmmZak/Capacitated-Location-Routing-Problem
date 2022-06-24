import numpy as np
import sklearn
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from core.dataset import Dataset
from glob import glob

DATABASE_PATHS = glob('./dataset/*/*')

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
SAMPLES = 10**2
CLASSES = 4
COLORS = [
    "red", 
    "blue", 
    "green", 
    "cyan", 
    "magenta", 
    "yellow",
    "purple"
]
MAX_ITER = 300

np.random.seed(0)
dataset = np.random.rand(SAMPLES, 2)
np.random.seed(0)
labels = np.random.randint(0, CLASSES, SAMPLES)

dataset.shape, labels.shape

inertia_list = list()

MAX_CLUSTERS = 7

for CLUSTERS in range(1, MAX_CLUSTERS):
    kmeans = KMeans(init="random", n_clusters = CLUSTERS, n_init=10, max_iter = MAX_ITER, random_state=42)
    kmeans.fit(dataset)

    inertia_list.append(kmeans.inertia_)

plt.style.use("fivethirtyeight")
plt.plot(range(1, MAX_CLUSTERS), inertia_list)
plt.xticks(range(1, MAX_CLUSTERS))
plt.xlabel("Number of Clusters")
plt.ylabel("SSE")
plt.show()

fig = plt.figure()

MAX_ITER = 10

for iter in range(1, MAX_ITER):
  print("Iter: ", iter)
  kmeans = KMeans(init="random", n_clusters = CLASSES, n_init=10, max_iter = iter, random_state=42)
  kmeans.fit(dataset)

  for i, (x,y) in enumerate(dataset):
      label = labels[i]
      color = COLORS[label]
      #print(i, x, y)

      plt.scatter(x, y, c='r')
  
  for x, y in kmeans.cluster_centers_:
      plt.scatter(x, y, c="black", marker="X", linewidths=3)

      coords = f'({x:.2f}, {y:.2f})'
      plt.annotate(coords, (x, y))

  plt.show()
  # AFTER FIT
  for i, data in enumerate(dataset):
      x, y = data

      pred = kmeans.predict([data])
      color = COLORS[pred[0]]
      plt.scatter(x, y, c=color)
  
  for x, y in kmeans.cluster_centers_:
      plt.scatter(x, y, c="black", marker="X", linewidths=3)

      coords = f'({x:.2f}, {y:.2f})'
      plt.annotate(coords, (x, y))
  
  plt.show()
"""