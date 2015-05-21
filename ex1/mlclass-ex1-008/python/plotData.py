import matplotlib.pyplot as plt
import numpy as np

def plotData(x, y, color):
	

	plt.scatter(x, y, marker='x', c=color, vmin=0, vmax=1000)
	plt.xlabel("Population")
	plt.ylabel("Profit")

	plt.show()



def readFile(filename):
	data = []
	x = []
	y = []
	tmp_xy = []
	with open(filename, 'r') as f:
		for line in f:
			tmp_xy = line.strip().split(",")
			tmp_xy = np.array(map(float, tmp_xy))
			x.append(tmp_xy[:1])
			y.append(tmp_xy[1])
			
	
	return x, y


def GD(x, y):
	X = []
	#x = np.array(x[:30])
	for item in x:
		X.append(item[0])

	X = np.array(X)	
	y = np.array(y)
	print(X.shape, X)
	print(y.shape, y)
	alpha = .001
	theta0 = 0.
	theta1 = 0.
	h_x = np.array(0.)
	cost_f = 1.
	counter = 0
	cost_list = []
	theta0_list = []
	theta1_list = []
	
	while abs(cost_f) > 0.1 and counter < 100000 :
		#print("counter is", counter)
		counter +=1
		
		theta0 = theta0 - (alpha/len(y)) * np.sum(h_x - y) 
		theta0_list.append(theta0)
		theta1 = theta1 - (alpha/len(y)) * np.sum(np.multiply((h_x - y), X))
		theta1_list.append(theta1)
		h_x = theta0 + theta1 * X
		
		#print("theta0 is", theta0)
		#print("theta1 is", theta1)
		#print("x is", 2 * x) 
		#print("h_x is", h_x)
		cost_f = (1./(2.*len(y))) * np.sum((h_x - y)**2)
		cost_list.append(cost_f)

		
		#print(cost_f)
		
		'''
		for item_x, item_y in (x, y):
			cost_f = (1/(2*len(x))) * ((theta0 + theta1 * item_x - item_y)**2)
	
		'''
	'''
	from mpl_toolkits.mplot3d import Axes3D
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	#X, Y, Z = random(100)


	ax.plot_trisurf(theta0_list,theta1_list,cost_list)
	#ax.plot_wireframe(X, Y, Z)
	plt.show()	
	'''
	return (theta0+theta1*X)



def LR(x, y):
	from sklearn.linear_model import LinearRegression
	reg = LinearRegression()
	reg.fit(x, y)

	return reg.predict(x)

def SGD(x, y):
#Using Stochastic Gradient Descent of Sklearn
	from sklearn.linear_model import SGDClassifier
	clf = SGDClassifier()
	clf.fit(x, y)

	return clf.predict(x)

if __name__ == "__main__":
	x, y = readFile("ex1data1.txt")
	#plotData(x, y, 'red')
	
	
	y1 = GD(x, y)
	plt.scatter(x, y, c='red')
	print(len(x), len(y))
	plt.plot(x, y1, c='blue')

	

	y2 = LR(x, y)
	plt.plot(x, y2, c='green')
	#plotData(x, y, 'blue')

	
	plt.show()


