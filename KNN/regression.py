import numpy as np 
import matplotlib.pyplot as plt 
from sklearn import neighbors

X = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
y = [2,5,7,9,11,16,19,23,22,29,29,35,37,40,46,42,39,31,30,28,20,15,10,6]
plt.plot(X,y,'ro')

X = np.array([X]).reshape(-1,1)

print(X)

x0 = np.linspace(1,25,10000).reshape(-1,1)

test_x = [[15.17]]

knn = neighbors.KNeighborsRegressor(n_neighbors=2)
knn.fit(X,y)
y0 = knn.predict(x0)

knn.fit(X,y)
test_y = knn.predict(test_x)

print(test_y)

plt.plot(x0,y0)
plt.show()