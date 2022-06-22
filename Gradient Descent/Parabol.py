import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def cost(x):
	m = A.shape[0]
	return 0.5/m * np.linalg.norm(A.dot(x) - b , 2)**2

def grad(x):
	m = A.shape[0]
	return 1/m * A.T.dot(A.dot(x) - b)

def check_grad(x):
	eps = 1e-7
	g = np.zeros_like(x)
	for i in range(len(x)):
		x1 = x.copy()
		x2 = x.copy()
		x1[i][0] += eps
		x2[i][0] -= eps
		g[i] = (cost(x1) - cost(x2))/(2*eps)

	g_gd = grad(x)
	if np.linalg.norm(g-g_gd) > 1e-4:
		print("WARNING: CHACK GRADIENT FUNCTION!")

def gradient_descent(x_init,learning_rate,iteration):
	x_list = [x_init]
	for i in range(iteration):
		x_new = x_list[-1] -  learning_rate*grad(x_list[-1])
		x_list.append(x_new)
		print(np.linalg.norm(x_new))
		
		if np.linalg.norm(x_new)/len(x_new) < 0.8:
			break

	return x_list

b = np.array([[2,5,7,9,11,16,19,23,22,29,29,35,37,40,46,42,39,31,30,28,20,15,10,6]]).T
A = np.array([[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]]).T

fig1 = plt.figure("GD for linear Regression (Parabol)")
ax = plt.axes(xlim=(-10,60),ylim=(-30,60))
plt.plot(A,b,'ro')

# Linear Regression
ones = np.ones((A.shape[0],1),dtype=np.int8)
A2 = np.array([A[:,0]**2]).T
A = np.concatenate((ones,A,A2), axis=1 )
x = np.linalg.inv(A.T.dot(A)).dot(A.T).dot(b)
x0 = np.linspace(-10,35,10000)
y0 = x[0][0] + x[1][0]*x0 + x[2][0]*x0*x0
plt.plot(x0,y0)

# Gradient descent
x_init = np.array([[-7.0],[5.5],[-0.5]])
x0_gd = np.linspace(0,45,10000)
y0_gd =  x_init[0][0] + x_init[1][0]*x0_gd + x_init[2][0]*x0_gd*x0_gd
plt.plot(x0_gd,y0_gd,color='black')

iteration = 100
learning_rate = 0.0000009

check_grad(x_init)

x_list = gradient_descent(x_init,learning_rate,iteration)

for i in range(len(x_list)):
	x0_gd = np.linspace(0,45,10000)
	y0_gd1 =  x_list[i][0][0] + x_list[i][1][0]*x0_gd + x_list[i][2][0]*x0_gd*x0_gd
	plt.plot(x0_gd,y0_gd1,color='black', alpha = 0.3)


line , = ax.plot([],[], color = "blue")
# Draw animation
def update(i):
	y0_gd =  x_list[i][0][0] + x_list[i][1][0]*x0_gd + x_list[i][2][0]*x0_gd*x0_gd
	line.set_data(x0_gd,y0_gd)
	return line,

iters = np.arange(1,len(x_list),1)
line_ani = animation.FuncAnimation(fig1 , update , iters, interval=50 , blit = True )

# legend for plot
plt.legend(('Value in each GD iteration','Solution by formular', 'Inital value for GD'), loc=(0.52,0.01))
ltext = plt.gca().get_legend().get_texts()

# title
plt.title("Gradient Descent Animation")

print(len(x_list))

plt.show()