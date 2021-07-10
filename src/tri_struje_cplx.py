import numpy as np
import cmath


def Bu2D(modI, argI, xI, yI, x, y):

	u0=4*np.pi*10e-7;
	I = modI * complex(np.cos(argI), np.sin(argI));

	r = np.sqrt(np.power((x-xI),2)+np.power((y-yI),2))

	return (u0*I)/(2*np.pi*r)


def tri_struje_cplx(modI, argI, xI, yI, x, y):

	I1 = modI[0] * complex(np.cos(argI[0]), np.sin(argI[0]))
	I2 = modI[1] * complex(np.cos(argI[1]), np.sin(argI[1]))
	I3 = modI[2] * complex(np.cos(argI[2]), np.sin(argI[2]))
	In=-(I1+I2+I3);
	modIn=np.abs(In)
	argIn=np.angle(In)

	B1 = Bu2D(modI[0], argI[0], xI[0], yI[0], x, y)
	Bx1 = (y - yI[0]) * B1 / (np.sqrt(np.power((x-xI[0]),2)+np.power((y-yI[0]),2)))
	By1 = (x - xI[0]) * B1 / (np.sqrt(np.power((x-xI[0]),2)+np.power((y-yI[0]),2)))

	return np.sqrt(np.abs(np.power(Bx1,2)) + np.abs(np.power(By1,2)))


d = 0.1
modI = np.array([100, 100, 100])
argI = np.array([0, 120, 240])
xI = np.array([-1.5*d, -0.5*d, 0.5*d, 1.5*d])
yI = np.array([0, 0, 0, 0])


print(tri_struje_cplx(modI, argI, xI, yI, 2, 2))


