import numpy as np
import matplotlib.pyplot as plt
import cmath


def Bu2D(modI, argI, xI, yI, x, y):

	u0=4*np.pi*1e-7
	
	I = modI * complex(np.cos(argI), np.sin(argI))

	r = np.sqrt(np.power((x-xI),2)+np.power((y-yI),2))

	# X, Y = np.meshgrid(x,y)

	B = (u0*I)/(2*np.pi*r)
	Bx = (yI - y)*B/r
	By = (x - xI)*B/r
	
	return Bx, By


def tri_struje_cplx(modI, argI, xI, yI, x, y):

	B1 = Bu2D(modI[0], argI[0], xI[0], yI[0], x, y)
	B2 = Bu2D(modI[1], argI[1], xI[1], yI[1], x, y)
	B3 = Bu2D(modI[2], argI[2], xI[2], yI[2], x, y)


	Bx = B1[0] + B2[0] + B3[0]
	By = B1[1] + B2[1] + B3[1]

	Bxmod = np.abs(Bx)
	Bymod = np.abs(By)
	B = np.sqrt(np.power(Bxmod,2) + np.power(Bymod,2))

	return B

def nebalans01(modI, argI, xI, yI, x, y):

	indU = 0
	dB = np.zeros(len(modI[0])*len(modI[1])*len(modI[2]))
	uI = np.zeros(len(modI[0])*len(modI[1])*len(modI[2]))
	
	# dB = np.zeros(200)
	# uI = np.zeros(200)


	for p1 in range(len(modI[0])):
		for p2 in range(len(modI[1])):
			for p3 in range(len(modI[2])):
				I_array = [modI[0][p1], modI[1][p2], modI[2][p3]]
				I0 = np.max(I_array)

				Iavg = (modI[0][p1] + modI[1][p2] + modI[2][p3]) / 3

				#Iavg = (p1 + p2 + p3) / 3
				A = I_array - Iavg
				uI[indU] = np.max(A) / Iavg

				B0 = tri_struje_cplx([I0, I0, I0], argI, xI, yI, x, y)
				B = tri_struje_cplx(I_array, argI, xI, yI, x, y)
				dB[indU] = (B-B0)/B0
				indU = indU + 1

	return uI, dB, indU


def main():
	d = 3
	h = 10
	x = np.arange(-10, 11)
	y = 1
	modI0 = np.array([800, 800, 800])
	modI = np.array([800, 600, 700])
	modI_array = [np.arange(700,950,50), np.arange(700,950,50), np.arange(700,950,50)]
	argI = np.array([0, -120, -240]) * np.pi/180


	xI = np.array([-d, 0, d])
	# xI = np.array([-1.5*d, -0.5*d, 0.5*d, 1.5*d])
	yI = np.array([h, h, h])
	# yI = np.array([0, 0, 0, 0])

	B0 = np.zeros(21)
	B = np.zeros(21)
	save_results_to = 'D:\Projects\_konferencije\PES\python\current-unbalance\src\plots'

	name = '\h' + str(h) + '_d' + str(d) + '.png'

	for i in range(len(x)):
		B0[i] = tri_struje_cplx(modI0, argI, xI, yI, x[i], y)
		B[i] = tri_struje_cplx(modI, argI, xI, yI, x[i], y)
	
	
	plt.grid(axis='both')
	plt.xlabel('x (m)')
	plt.ylabel('B (uT)')
	plt.plot(x,B0*1e6,'g--')
	plt.plot(x,B*1e6,'b')
	
	compare = nebalans01(modI_array, argI, xI, yI, x[10], y)
	indU = np.arange(0, compare[2])
	
	print(len(compare[0]))
	# print("Prvi clan je")
	# print(dB[0][0:65])
	# print("Drugi clan je")
	# print(dB[1])

	plt.figure(2)
	plt.grid(axis='both')
	plt.xlabel('Current unbalance, (%)')
	plt.ylabel('MFD Rel. dev. (%)')
	# plt.plot(compare[0][0:65]*100,compare[1][0:65]*100)
	plt.scatter(compare[0]*100,compare[1]*100)
	#plt.show()
	plt.savefig(save_results_to + name, dpi=300)

	
if __name__ == '__main__':
    main()
