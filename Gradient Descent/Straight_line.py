import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
from sklearn import linear_model
import matplotlib.animation as animation

def cost(x):
	m = A.shape[0]
	return 0.5/m * np.linalg.norm(A.dot(x) - b, 2)**2

def grad(x):
	m = A.shape[0]
	return 1/m * A.T.dot(A.dot(x)-b)

def check_grad(x):
	eps = 1e-4
	g = np.zeros_like(x)
	for i in range(len(x)):
		x1 = x.copy()
		x2 = x.copy()
		x1[i] += eps
		x2[i] -= eps
		g[i] = (cost(x1)-cost(x2))/(2*eps)

	g_grad = grad(x)

	if np.linalg.norm(g-g_grad) > 1e-5 :
		print("WARNING")


def gradient_descent(x_init, learning_rate, iteration):
	x_list = [x_init]
	
	for i in range(iteration):
		x_new = x_list[-1] - learning_rate*grad(x_list[-1])

		if np.linalg.norm(grad(x_new))/len(x_new) < 0.3:
			# When to stop GD
			# The above is divided by len (x_new) because it is a 2D space (so dividing is to reduce the number of np.linalg.norm(grad (x_new)) for the calculation to reduce the amount of resources needed)
			break 
		x_list.append(x_new)

	return x_list

# Data 
A = np.array([[2,9,7,9,11,16,25,23,22,29,29,35,37,40,46]]).T 
b = np.array([[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]).T

# Draw data
fig1 = plt.figure("Gradient Descent for Linear Regression (Straight Line)")
ax = plt.axes(xlim=(-10,60), ylim=(-1,25))
plt.plot(A,b, 'ro')

# Line created by linear regression formular
lr = linear_model.LinearRegression()
lr.fit(A,b)
x0_gd = np.linspace(1,46,2)
y0_sklearn = lr.intercept_[0] + lr.coef_[0][0]*x0_gd
plt.plot(x0_gd,y0_sklearn, color="green")

# Add one to A
ones = np.ones((A.shape[0],1), dtype=np.int8)
A = np.concatenate((ones,A), axis=1)

# Random initial line
x_init = np.array([[1.0],[2.0]])

check_grad(x_init)

y0_init = x_init[0][0] + x_init[1][0]*x0_gd
plt.plot(x0_gd,y0_init, color="black")

# Run gradient descent
iteration = 100
learning_rate = 0.0001

x_list = gradient_descent(x_init, learning_rate, iteration)

# Draw x_list (solution by GD)
for i in range(len(x_list)):
	y0_x_list = x_list[i][0] + x_list[i][1]*x0_gd
	plt.plot(x0_gd,y0_x_list, color="black", alpha = 0.3)


line , = ax.plot([],[], color = "blue")
# Draw animation
def update(i):
	y0_gd = x_list[i][0][0] + x_list[i][1][0]*x0_gd
	line.set_data(x0_gd,y0_gd)
	return line,

iters = np.arange(1,len(x_list),1)
print(iters)
line_ani = animation.FuncAnimation(fig1 , update , iters, interval=50 , blit = True )

# legend for plot
plt.legend(('Value in each GD iteration','Solution by formular', 'Inital value for GD'), loc=(0.52,0.01))
ltext = plt.gca().get_legend().get_texts()

# title
plt.title("Gradient Descent Animation")
plt.show()

# # Plot cost per iteration to determine when to stop
# cost_list = []
# iter_list = []
# for i in range(len(x_list)):
# 	iter_list.append(i)
# 	cost_list.append(cost(x_list[i]))

# plt.plot(iter_list, cost_list)
# plt.xlabel('Iteration')
# plt.ylabel('Cost value')
# plt.show()