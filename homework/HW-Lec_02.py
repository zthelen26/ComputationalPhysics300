#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Fibonacci(N):
    fib_series = []
    for i in range(1, N+1): 
        if len(fib_series)<=1:
            return 1
        else: 
            fib_series.append(b)
            a, b = b, a + b
    return fib_series[-1]

#input code
def Multiplicity(N,q):
    return factor(q+N-1)/factor(q)/factor(N-1)

N = int(input("Type a value for N: "))

for q in range(N+1):
    print ("when q = ", q, "; the multiplicity is", Multiplicity(N,q))


# In[26]:


timeit(Fibonacci(10000))


# In[ ]:


def Fibonacci2(N):
    fib_series = []
    a = b = 1
    for i in range(1, N+1): 
        if len(fib_series)<=1:
            yield 1
        else: 
            yield a
            a, b = b, a + b
            
#imput code
def Multiplicity(N,q):
    return factor(q+N-1)/factor(q)/factor(N-1)

N = int(input("Type a value for N: "))

for q in range(N+1):
    print ("when q = ", q, "; the multiplicity is", Multiplicity(N,q))


# In[27]:


timeit(Fibonacci2(10000))


# In[28]:


sum(x**2 for x in range(100))


# In[30]:


sum([x**2 for x in range(100)])


# In[ ]:




