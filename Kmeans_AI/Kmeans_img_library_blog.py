import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy

img = plt.imread("space.jpg")

width = img.shape[0]
hight = img.shape[1]

img = img.reshape(width*hight,3)

kmeans = KMeans(n_clusters=4).fit(img)
labels = kmeans.predict(img)
clusters = kmeans.cluster_centers_ 

img2 = numpy.zeros_like(img)

for i in range(len(img2)):
	img2[i] = clusters[labels[i]]

img2 = img2.reshape(width,hight,3)

plt.imshow(img2)
plt.show()