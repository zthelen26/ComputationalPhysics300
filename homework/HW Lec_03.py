#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
from math import log, exp

def factorial(z):
    if z == 0:
        return 1
    else:
        return z * factorial(z-1)
    good_z = False
    
def calc_omega1(NA,qA):
    return factorial(qA+NA-1)/(factorial(qA)*factorial(NA-1))

NA = 300
good_qA = False
while good_qA is False:        
    qA=int(input("type a value for qA energy units: "))
    if qA<0:
        print ("qA must be a positive integer!")
    else:
        good_qA = True
        
def calc_omega2(NB,qB):
    return factorial(qB+NB-1)/(factorial(qB)*factorial(NB-1))

NB = 200
qB = 100-qA

def omega_w(qA):
    return calc_omega1(NA,qA)*calc_omega2(NB,qB)
print ("NA=",NA, ", qA=",qA,",NB=",NB, ", qB=",qB, ' Multiplicity is', omega_w(qA), "")


# In[2]:


from math import factorial
def calc_omega1approx(NA,qA):
     return exp(log(factorial(qA+NA-1)) - log(factorial(qA)) - log(factorial(NA-1))) #approximation when N>>q

NA = 3000
good_qA = False
while good_qA is False:        
    qA=int(input("type a value for qA energy units: "))
    if qA<0:
        print ("qA must be a positive integer!")
    else:
        good_qA = True
        
def calc_omega2approx(NB,qB):
    return exp(log(factorial(qB+NB-1)) - log(factorial(qB)) - log(factorial(NB-1))) #approximation when N>>q

NB = 2000
qB = 100-qA

def omega_wapprox(qA):
    return calc_omega1approx(NA,qA)*calc_omega2approx(NB,qB)
print ("NA=",NA, ", qA=",qA,",NB=",NB, ", qB=",qB, ' Multiplicity is', omega_wapprox(qA), "")


# In[3]:


import matplotlib.pyplot as plt
from math import factorial

    
def calc_omega1approx(NA,qA):
     return exp(log(factorial(qA+NA-1)) - log(factorial(qA)) - log(factorial(NA-1))) #approximation when N>>q
        
def calc_omega2approx(NB,qB):
    return exp(log(factorial(qB+NB-1)) - log(factorial(qB)) - log(factorial(NB-1))) #approximation when N>>q

def omega_wapprox(qA):
    return calc_omega1approx(NA,qA)*calc_omega2approx(NB,qB)


NB = 2000
qB = 100-qA
NA = 3000
good_qA = False
while good_qA is False:        
    qA=int(input("type a value for qA energy units: "))
    if qA<0:
        print ("qA must be a positive integer!")
    else:
        good_qA = True  

    qA_series = range(qA+1)     
    omega_series = []

    for i in qA_series:
        omega_series.append(omega_wapprox(i))
    
    plt.plot(qA_series, omega_series)
    plt.title('qA='+str(qA))
    plt.xlabel('qA')
    plt.ylabel('$\Omega(qA)$')

    plt.show()


# In[ ]:




