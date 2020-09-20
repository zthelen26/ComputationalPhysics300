#!/usr/bin/env python
# coding: utf-8

# In[31]:


#Heat capacity of a solid

from math import exp
from scipy import integrate
import matplotlib.pyplot as plt

def cV(T):
    #var. 
    V = 0.001 #Sample cm**3
    rho = 6.022e28 # density 
    Td = 428 #debye temp
    kb = 1.38e-28 # boltzmann constant in J/K
    
    #integration
    f = lambda x: (x**4)*(exp( x ))/(exp( x ) - 1)**(2)
    INT = integrate.quad(f, 0, Td/T)
    
    #full eq. 
    value = 9*V*rho*kb*((T/Td)**3) * (INT[0] - INT[1])
    return value

#heat capacity 
cv = []
i = 0
T = list(range(5,500))
l = 500 - 5
while(i < l):
    cv.append(cV(T[i]))
    i = i + 1

#plotting
plt.plot(T, cv, 'ro')
plt.xlabel('Temp (K)')
plt.xlim([0,500])
plt.ylabel('Cv ( j/K )')
plt.title('Heat capacity of a solid')
plt.show()


# In[27]:


#Noisy data attemptish

import matplotlib.pyplot as plt
import numpy as np

#define the function
f = lambda x: x * np.sin(x)  

#define the paramters for the plot
a,b = 0,3
npoints = 100

x = np.linspace(a,b,npoints)
y = f(x) + np.random.rand(npoints) - 0.5
plt.plot(x,y)
plt.plot(x,f(x))

plt.xlabel('x')
plt.ylabel('$f(x)$')
plt.xlim([a,b])
plt.show()


# In[ ]:




