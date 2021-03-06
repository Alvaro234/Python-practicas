
#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
# Amo a programar un runge kutta #
import math
import matplotlib.pyplot as plt

#functions 
dy = lambda x,y: math.sin(x)**2*y
f = lambda x: 2*math.exp(0.5*(x-math.sin(x)*math.cos(x))) #solucion exacta




#Parameters
xi=0; xf =5; h=0.5
float(xi);float(xf);float(h)

n = int( (xf-xi) / h)
print (n)
x = 0; y = 2

#visualization 
print('x  \t\t y \t\t f(x)'); print('%f  \t  %f  \t  %f'% (x,y,f(x)))
x_plot = []; y_RK4 = []; y_analytical = []

#rk4 method

for i in range(1,n+1):
	x_plot.append(x); y_RK4.append(y); y_analytical.append(f(x))

	k1= dy(x,y)
	k2 = dy(x+h/2,y+k1*h/2)
	k3 = dy(x+h/2,y+k2*h/2)
	k4 = dy(x+h, y+k3*h)
	
	y = y+(k1+2*k2+2*k3+k4)*h/6  #nueva estimacion de y

	x = x+h   #cambio de punto

	print('%f  \t  %f  \t  %f'% (x,y,f(x)))


x_plot.append(x); y_RK4.append(y); y_analytical.append(f(x))
plt.plot(x_plot,y_RK4,'ro',x_plot,y_analytical)
plt.xlabel('x'); plt.ylabel('y')
plt.legend(["RK4" ,'Analitico'])
plt.show()