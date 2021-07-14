import numpy as np
import matplotlib.pyplot as plt
import cmath


def Bu2D(modI, argI, xI, yI, x, y):

	u0=4*np.pi*10e-7
	I = modI * complex(np.cos(argI), np.sin(argI))

	r = np.sqrt(np.power((x-xI),2)+np.power((y-yI),2))

	# X, Y = np.meshgrid(x,y)

	B = (u0*I)/(2*np.pi*r)
	Bx = (yI - y)*B/r
	By = (x - xI)*B/r
	
	return Bx, By 


def tri_struje_cplx(modI, argI, xI, yI, x, y):

	I1 = modI[0] * complex(np.cos(argI[0]), np.sin(argI[0]))
	I2 = modI[1] * complex(np.cos(argI[1]), np.sin(argI[1]))
	I3 = modI[2] * complex(np.cos(argI[2]), np.sin(argI[2]))
	# In=-(I1+I2+I3)
	# modIn=np.abs(In)
	# argIn=np.angle(In)

	B1 = Bu2D(modI[0], argI[0], xI[0], yI[0], x, y)
	B2 = Bu2D(modI[1], argI[1], xI[1], yI[1], x, y)
	B3 = Bu2D(modI[2], argI[2], xI[2], yI[2], x, y)
	# Bn = Bu2D(modIn, argIn, xI[3], yI[3], x, y)

	Bx = B1[0] + B2[0] + B3[0] # + Bn[0]
	By = B1[1] + B2[1] + B3[1] # + Bn[1]

	Bxmod = np.abs(Bx)
	Bymod = np.abs(By)
	B = np.sqrt(np.power(Bxmod,2) + np.power(Bymod,2))

	return B

def main():
	d = 3
	h = 10
	x = np.arange(-10, 11)
	y = 1
	modI0 = np.array([800, 800, 800])
	modI = np.array([800, 600, 700])
	argI = np.array([0, 120, 240])
	xI = np.array([-d, 0, d])
	# xI = np.array([-1.5*d, -0.5*d, 0.5*d, 1.5*d])
	yI = np.array([h, h, h])
	# yI = np.array([0, 0, 0, 0])

	B0 = np.zeros(21)
	B = np.zeros(21)

	print(x[20])

	for i in range(len(x)):
		B0[i] = tri_struje_cplx(modI0, argI, xI, yI, x[i], y)
		B[i] = tri_struje_cplx(modI, argI, xI, yI, x[i], y)
	
	plt.xlabel('x (m)')
	plt.ylabel('B (uT)')
	plt.plot(x,B0,'g--')
	plt.plot(x,B,'b')
	plt.show()

if __name__ == '__main__':
    main()
