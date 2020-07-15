import numpy as np 
import math
from scipy.optimize import fsolve
from scipy import integrate
import matplotlib.pyplot as plt


N_intervals = int(input("Enter the number of subintervals: "))
Mn = np.zeros((1,N_intervals))
Y_axis = np.zeros((1,N_intervals))
X_axis = np.zeros((1,N_intervals))
a = 0
b = 1

invexp = lambda x: np.exp(-x**2)
I = integrate.quad(invexp, 0, 1)

for n in range(1,N_intervals + 1):
    m = 0
    d = (b - a)/n
    
    for i in range(1,n+1):
        m = m + math.exp(-(a + (i - 1/2)*d)**2)
     
    Mn[0,n-1] = (b - a)/n * m
        
for j in range(1,N_intervals +1):
    
    Y_axis[0,j-1] = abs((Mn[0,j-1])-I[0])
    X_axis[0,j-1] = j
    
    
print("I = " + str(I[0])) 
print("I by midpoint rule = " + str( Mn[0,N_intervals-1])) 

plt.xscale('log')
plt.yscale('log')
plt.ylabel('absolute error of midpoint')
plt.xlabel('number of subintervals')
plt.plot(X_axis, Y_axis, 'bo-', label='line 1', linewidth=2)


plt.grid()


plt.show()
