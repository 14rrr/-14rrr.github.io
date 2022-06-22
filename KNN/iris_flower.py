from sklearn import datasets
import numpy as np
import math 
import operator

def calculate_distances(p1,p2):
	dimention = len(p1)
	distance = 0 

	for i in range(dimention):
		distance += (p1[i]-p2[i])*(p1[i]-p2[i])

	return math.sqrt(distance)

def get_k_neighbors(training_X, label_y, point, k):
	distances = []
	neighbors = []

	# calculate distance from point to everything in training_X
	for i in range(len(training_X)):
		distance = calculate_distances(training_X[i],point)
		distances.append(distance)

	# position of k smallest distance
	index = []

	# Get k closet points
	while len(neighbors) < k:
		i = 0 
		min_distance = 999999
		min_idx = 0
		while i < len(distances):
			# Skip the nearest points that have been counted
			if i in index:
				i += 1
				continue

			# Update smallest distance and index
			if distances[i] <= min_distance:
				min_distance = distances[i]
				min_idx = i

			i += 1
		
		# Add min index so we skip it in the next iteration
		index.append(min_idx)
		neighbors.append(label_y[min_idx])

	return neighbors

def hight_votes(labels):
	labels_count = [0,0,0]

	for label in labels:
		labels_count[label] += 1

	max_count = max(labels_count)
	return labels_count.index(max_count)

def predict(training_X, label_y, point, k):
	neighbors_labels = get_k_neighbors(training_X, label_y, point, k)
	return hight_votes(neighbors_labels)

def accuracy_score(predicts, labels):
	total = len(predicts)
	correct_count = 0
	for i in range(total):
		if predicts[i] == labels[i]:
			correct_count += 1

	accuracy = (correct_count/total)*100
	return accuracy

iris = datasets.load_iris()
iris_X = iris.data # data (petal length, petal width , sepal length , sepal width)
iris_y = iris.target # label

randIndex = np.arange(iris_X.shape[0])
np.random.shuffle(randIndex)

iris_X = iris_X[randIndex]
iris_y = iris_y[randIndex]

X_train = iris_X[:100,:]
X_test = iris_X[100:,:]
y_train = iris_y[:100]
y_test = iris_y[100:]

print(X_test)

k = 5
y_predict = []
for p in X_test:
	label = predict(X_train, y_train, p, k)
	y_predict.append(label)

y_predict = np.array(y_predict)

acc = accuracy_score(y_predict, y_test)
acc = str(acc) + "%"
print(acc)