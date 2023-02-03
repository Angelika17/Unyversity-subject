#!/usr/bin/env python
# coding: utf-8

# ### Task1

# In[2]:


import numpy as np


# In[7]:


a = np.matrix("1 1 1; 0.05 0.07 0; 0.05 0 0.06")
b = np.matrix("50000; 2250; 1400")


# In[10]:


det_a= np.linalg.det(a)
print(det_a)


# In[11]:


if det_a !=0:
    a1= np.matrix(a)
    a2 = np.matrix(a)
    a3 = np.matrix(a)
    a1[:,0]=b
    a2[:,1]=b
    a3[:,2]=b
    x= np.linalg.det(a1)/det_a
    y= np.linalg.det(a2)/det_a
    z= np.linalg.det(a3)/det_a

print("x =", x.round(3), "y =", y.round(3), "z = ", z.round(3) )


# In[12]:


print( np.linalg.solve(a,b))


# <h3>Task2</h3>

# In[21]:


a = np.matrix("1 1 1; -1 0 0 ;0 0 1 ")
b = np.matrix("1500; -140; 80")


# In[22]:


np.linalg.solve(a,b).round(1)


# In[ ]:





# In[ ]:





# <h3>Task3</h3>

# In[23]:


v = np.matrix([[3,0,3], [6,1,0.25], [1,3**(-1),1]])
d= np.matrix([[1],[1],[1]])


# In[47]:


1/np.linalg.solve(v,d).round(2)


# In[31]:


det_v= np.linalg.det(v)
if det_v !=0:
    v1 = np.matrix(v)
    v2 = np.matrix(v)
    v3 = np.matrix(v)
    v1[:,0]=d
    v2[:,1]=d
    v3[:,2]=d
    x= np.linalg.det(v1)/det_v
    y= np.linalg.det(v2)/det_v
    z= np.linalg.det(v3)/det_v
    
x=1/x
y=1/y
z=1/z
print(x.round(2),
     y.round(2),
     z.round(2))


# In[ ]:




