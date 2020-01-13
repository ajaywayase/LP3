#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import matplotlib.pyplot as plt
import math


# In[2]:


x = np.array([10,9,2,15,10,16,11,16]) 
y = np.array([95,80,10,50,45,98,38,93]) 


# In[3]:


n = np.size(x)
m_x, m_y = np.mean(x), np.mean(y)


# In[4]:


SS_xy = np.sum(y*x) - n*m_y*m_x
SS_xx = np.sum(x*x) - n*m_x*m_x


# In[5]:





# In[6]:





# In[7]:





# In[8]:


num=n*np.sum(y*x)-np.sum(x)*np.sum(y)


# In[9]:


den=(n*np.sum(x*x)-(np.sum(x)*np.sum(x)))*(n*np.sum(y*y)-(np.sum(y)*np.sum(y)))


# In[11]:


den =math.sqrt(den)


# In[12]:


r=num/den


# In[13]:


print(r)


# In[14]:


b_1 = SS_xy / SS_xx 
b_0 = m_y - b_1*m_x


# In[15]:


print(b_0)
print(b_1)


# In[16]:


plt.scatter(x, y, color = "m", marker = "o", s = 30)


# In[18]:


y_pred = b_0 + b_1*x


# In[23]:


plt.scatter(x, y, color = "m", marker = "o", s = 30)
plt.plot(x, y_pred, color = "g")
plt.xlabel('x') 
plt.ylabel('y')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




