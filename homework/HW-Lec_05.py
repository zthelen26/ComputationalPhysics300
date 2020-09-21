#!/usr/bin/env python
# coding: utf-8

# In[141]:


#Rectangle rule EQ: (x**2 - x + 1 dx)[3-0]

import numpy as np
import matplotlib.pyplot as plt

def Rectangle(start, end, parts = 100, plot=1):
    
    #define the function
    f = lambda x: x**2 - x + 1 
    
    #define X,Y 
    deltax = (end - start) / parts
    resultsx = np.linspace(start, end, parts)
    resultsy = f(resultsx)
    
    #calculate the area
    area = np.empty([parts], float)
    for i in range(parts):
            area[i] = resultsy[i] * deltax
    

    #output plot.
    if plot>=1:
        x = np.linspace(start,end,100)
        y = x**2 - x + 1         
        plt.plot(x, y, 'r')
        plt.xlim([start,end])
        plt.bar(resultsx+deltax/2, resultsy, deltax, edgecolor ='black')
        plt.bar(resultsx, resultsy, deltax, edgecolor ='black')
        plt.show()
        print("The Sum of the area is: ", sum(area))
    
    return sum(area)


# In[142]:


#expected value: 7.5 
Rectangle(0,3,100)


# In[143]:


#Trapezoid rule EQ: (x**2 - x + 1 dx)[3-0]

import numpy as np
import matplotlib.pyplot as plt

def Trapezoid(start, end, parts, plot=1):
    
    #define the function
    f = lambda x: x**2 - x + 1 
    
    #define X, Y  
    deltax = (end - start) / parts
    resultsx = np.linspace(start, end, parts+1)
    resultsy = f(resultsx)

    #calculate the area
    area = np.empty([parts], float)
    for i in range(parts):
            area[i] = (resultsy[i]+resultsy[i+1]) * deltax/2

    #output plot
    if plot==1:
        x = np.linspace(start,end,100)
        y = f(x)        
        plt.plot(x, y, 'r')
        plt.xlim([start,end])
        
        y2 = np.array([0,0])
        for i in range(parts):
            x0 = resultsx[i:i+2]
            y1 = resultsy[i:i+2]
            plt.fill_between(x0, y1, y2, where=y1>=y2, facecolor='blue')
            linex, liney = [resultsx[i+1], resultsx[i+1]], [0, resultsy[i+1]]
            plt.plot(linex, liney, color='black', linewidth=2.0)        
        
        plt.show()
        print("The Sum of the area is: ", sum(area))
    
    return sum(area)


# In[25]:


#expected value: 7.5
Trapezoid(0,3,100)


# In[130]:


#simpsons rule EQ: (x**2 - x + 1 dx)[3-0]

import numpy as np
import matplotlib.pyplot as plt

def Simpson(start, end, parts, plot=1):

    #define the function
    f = lambda x: x**2 - x + 1  
    
    #define X, Y 
    deltax = (end - start) / parts
    resultsx = np.linspace(start, end, parts+1)
    resultsy = f(resultsx)

    #define var.area
    def area():
        for i in range():
            area += 1/3*deltax*(resultsy[i]+4*resultsy[i+1]+results[i+2])
            append.area(1/3*deltax*(resultsy[i]+4*resultsy[i+1]+results[i+2]))
        return area
    y2 = np.array([0,0])

    #output plot
    if plot==1:
        x = np.linspace(start,end,100)
        y = f(x)        
        plt.plot(x, y, 'r')
        for i in range(parts):
            x0 = resultsx[i:i+2]
            y1 = resultsy[i:i+2]
            plt.fill_between(x0, y1, y2, where=y1>=y2, facecolor='blue')
            linex, liney = [resultsx[i+1], resultsx[i+1]], [0, resultsy[i+1]]
            plt.plot(linex, liney, color='black', linewidth=1.0)        
        plt.xlim([start,end])
        plt.ylim([min(y),max(y)])
        plt.show()
    print("The Sum of the area is: ", sum(area))
    return sum(area)


# In[132]:


Simpson(0,3,100)


# In[30]:


#Rectangle rule EQ: (x**4 - x + 1 dx)[3-0]

import numpy as np
import matplotlib.pyplot as plt

def Rectangle(start, end, parts = 100, plot=1):
    
    #define the function
    f = lambda x: x**4 - x + 1 
    
    #define X,Y 
    deltax = (end - start) / parts
    resultsx = np.linspace(start, end, parts)
    resultsy = f(resultsx)
    
    #calculate the area
    area = np.empty([parts], float)
    for i in range(parts):
            area[i] = resultsy[i] * deltax
    

    #output plot
    if plot>=1:
        x = np.linspace(start,end,100)
        y = x**4 - x + 1         
        plt.plot(x, y, 'r')
        plt.xlim([start,end])
        plt.bar(resultsx+deltax/2, resultsy, deltax, edgecolor ='black')
        plt.bar(resultsx, resultsy, deltax, edgecolor ='black')
        plt.show()
        print("The Sum of the area is: ", sum(area))
    
    return sum(area)


# In[31]:


#expected value: 47.1
Rectangle(0,3,100)


# In[32]:


#Trapezoid rule EQ: (x**4 - x + 1 dx)[3-0]

import numpy as np
import matplotlib.pyplot as plt

def Trapezoid(start, end, parts, plot=1):
    
    #define the function
    f = lambda x: x**4 - x + 1 
    
    #define X, Y  
    deltax = (end - start) / parts
    resultsx = np.linspace(start, end, parts+1)
    resultsy = f(resultsx)

    #calculate the area
    area = np.empty([parts], float)
    for i in range(parts):
            area[i] = (resultsy[i]+resultsy[i+1]) * deltax/2

    #output plot
    if plot==1:
        x = np.linspace(start,end,100)
        y = f(x)        
        plt.plot(x, y, 'r')
        plt.xlim([start,end])
        
        y2 = np.array([0,0])
        for i in range(parts):
            x0 = resultsx[i:i+2]
            y1 = resultsy[i:i+2]
            plt.fill_between(x0, y1, y2, where=y1>=y2, facecolor='blue')
            linex, liney = [resultsx[i+1], resultsx[i+1]], [0, resultsy[i+1]]
            plt.plot(linex, liney, color='black', linewidth=2.0)        
        
        plt.show()
        print("The Sum of the area is: ", sum(area))
    
    return sum(area)


# In[33]:


#exp value: 47.1
Trapezoid(0,3,100)


# In[133]:


#simpsons rule EQ: (x**4 - x + 1 dx)[3-0]

import numpy as np
import matplotlib.pyplot as plt

def Simpson(start, end, parts, plot=1):

    #define the function
    f = lambda x: x**4 - x + 1  
    
    #define X, Y 
    deltax = (end - start) / parts
    resultsx = np.linspace(start, end, parts+1)
    resultsy = f(resultsx)

    #define var.area
    def area():
        for i in range():
            area += 1/3*deltax*(resultsy[i]+4*resultsy[i+1]+results[i+2])
            append.area(1/3*deltax*(resultsy[i]+4*resultsy[i+1]+results[i+2]))
        return area
    y2 = np.array([0,0])

    #output plot
    if plot==1:
        x = np.linspace(start,end,100)
        y = f(x)        
        plt.plot(x, y, 'r')
        for i in range(parts):
            x0 = resultsx[i:i+2]
            y1 = resultsy[i:i+2]
            plt.fill_between(x0, y1, y2, where=y1>=y2, facecolor='blue')
            linex, liney = [resultsx[i+1], resultsx[i+1]], [0, resultsy[i+1]]
            plt.plot(linex, liney, color='black', linewidth=1.0)        
        plt.xlim([start,end])
        plt.ylim([min(y),max(y)])
        plt.show()
    print("The Sum of the area is: ", sum(area))
    return sum(area)


# In[136]:


Simpson(0,3,100)


# In[98]:


#Rectangle rule EQ: (exp(-x**2))[3-0]

import numpy as np
import matplotlib.pyplot as plt
from math import exp

def rectangle(start, end, parts, plot=1):
    
    #define the function
    def f(x):
        lambda x: (exp(-x**2))
        return f
    f2 = np.vectorize(f)
    
    #define X,Y 
    deltax = (end - start) / parts
    resultsx = np.linspace(start, end, parts)
    resultsy = f(resultsx)
    
    #calculate the area
    area = np.empty([parts], float)
    for i in range(parts):
            area[i] = resultsy[i] * deltax

    #output plot
    if plot<=1:
        x = np.linspace(start,end,100)
        #fix array error
        y = f2   
        plt.plot(x, y, 'r')
        plt.xlim([start,end])
        plt.bar(resultsx+deltax/2, resultsy, deltax, edgecolor ='black')
        plt.bar(resultsx, resultsy, deltax, edgecolor ='black')
        plt.show()
        print("The Sum of the area is: ", sum(area))
    
    return sum(area)


# In[99]:


rectangle(0,3,100)


# In[139]:


#Trapezoid rule EQ: (exp(-x**2)dx)[3-0]

import numpy as np
import matplotlib.pyplot as plt

def Trapezoid(start, end, parts, plot=1):
    
    #define the function
    f = lambda x: exp(-x**2)
    #define X, Y  
    deltax = (end - start) / parts
    resultsx = np.linspace(start, end, parts+1)
    resultsy = f(resultsx)

    #calculate the area
    area = np.empty([parts], float)
    for i in range(parts):
            area[i] = (resultsy[i]+resultsy[i+1]) * deltax/2

    #output plot
    if plot==1:
        x = np.linspace(start,end,100)
        y = f(x)        
        plt.plot(x, y, 'r')
        plt.xlim([start,end])
        
        y2 = np.array([0,0])
        for i in range(parts):
            x0 = resultsx[i:i+2]
            y1 = resultsy[i:i+2]
            plt.fill_between(x0, y1, y2, where=y1>=y2, facecolor='blue')
            linex, liney = [resultsx[i+1], resultsx[i+1]], [0, resultsy[i+1]]
            plt.plot(linex, liney, color='black', linewidth=2.0)        
        
        plt.show()
        print("The Sum of the area is: ", sum(area))
    
    return sum(area)


# In[140]:


Trapezoid(0,3,100)


# In[137]:


#simpsons rule EQ: (exp(-x**2) dx)[3-0]

import numpy as np
import matplotlib.pyplot as plt
from math import exp

def Simpson(start, end, parts, plot=1):

    #define the function
    f = lambda x: exp(-x**2)
    
    #define X, Y 
    deltax = (end - start) / parts
    resultsx = np.linspace(start, end, parts+1)
    resultsy = f(resultsx)

    #define var.area
    def area():
        for i in range():
            area += 1/3*deltax*(resultsy[i]+4*resultsy[i+1]+results[i+2])
            append.area(1/3*deltax*(resultsy[i]+4*resultsy[i+1]+results[i+2]))
        return area
    y2 = np.array([0,0])

    #output plot
    if plot==1:
        x = np.linspace(start,end,100)
        y = f(x)        
        plt.plot(x, y, 'r')
        for i in range(parts):
            x0 = resultsx[i:i+2]
            y1 = resultsy[i:i+2]
            plt.fill_between(x0, y1, y2, where=y1>=y2, facecolor='blue')
            linex, liney = [resultsx[i+1], resultsx[i+1]], [0, resultsy[i+1]]
            plt.plot(linex, liney, color='black', linewidth=1.0)        
        plt.xlim([start,end])
        plt.ylim([min(y),max(y)])
        plt.show()
    print("The Sum of the area is: ", sum(area))
    return sum(area)


# In[138]:


Simpson(0,3,100)


# In[ ]:




