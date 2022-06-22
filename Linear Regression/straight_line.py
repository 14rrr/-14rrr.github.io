import numpy as np 
import matplotlib
import matplotlib.pyplot as plt

# random data
A = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
y = [2,5,7,9,11,16,19,23,22,29,29,35,37,40,46]

# Visualize data
A = np.array([A]).T
y = np.array([y]).T

# Change row vector to column vector
plt.plot(A,y,'ro')

# Create vector 1
once = np.ones((A.shape[0],1),dtype=np.uint8)

# Combine 1 and A 
A = np.concatenate((A,once), axis=1)

# Use fomula
x = np.linalg.inv(A.T.dot(A)).dot(A.T).dot(y)

# Test data to draw
x0 = np.array([1,16]).T
y0 = x[0][0]*x0 + x[1][0]
plt.plot(x0,y0)
plt.show()