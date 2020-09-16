#!/usr/bin/env python
# coding: utf-8

# In[29]:


#mandelbrot set 4.5.1


# In[32]:


import numpy as np
import matplotlib.pyplot as plt

def calc_mandelbrot(N_max, threshold, nx, ny):
    x = np.linspace(-2, 2, nx)
    y = np.linspace(-2, 2, ny)
    c = x[:,newaxis] + 1j*y[newaxis,:]
    z = c

    # overflow
    with np.warnings.catch_warnings():
        np.warnings.simplefilter("ignore")
        for j in range(N_max):
            z = z*z + c
        mset = (abs(z) < threshold)

    return mset

mset = calc_mandelbrot(100, 100., 1000, 1000)

plt.imshow(mset.T, extent=[-2, 2, -2, 2])
plt.grey()
plt.show()


# In[33]:


from numpy import linspace, zeros, absolute
from matplotlib import pyplot as plt


a1,b1,pointsx = -2,0.5,300  # Side of x
a2,b2,pointsy = -1,1,300    # Side of y
N_iter = 50                 # the maximum number of iterations

x_set = linspace(a1,b1,pointsx)
y_set = linspace(a2,b2,pointsy)

# Make an array to store the grids
mandset = zeros([pointsx,pointsy],float)

# Calculate the values in the array
for i in range(len(y_set)): 
    for j in range(len(x_set)):
        
        #initial conditions
        z = 0        
        c = x_set[j] + y_set[i]*1j       
        inset = True

        #we need to iterate it to see if the point satisfies the condition
        for k in range(N_iter):
            z = z**2+c
            #print('values:  ', k,z,c)
            if absolute(z)>2:
                mandset[i,j]=k
                inset = False
                break
            
# Make the plot
plt.imshow(mandset,origin="lower",extent=[a1,b1,a2,b2],cmap="hot")
plt.gray()
plt.show()
plt.savefig('mandelbrot.pdf',format='pdf')


# In[ ]:




