#!/usr/bin/env python
# coding: utf-8

# # ANTHONY atividade 1

# 

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np


# In[2]:


x= np.linspace(0,10,20)
y= 2*x+4
ruido=y + np.random.normal(-2, 2, len(x))#Criando um ruido
plt.figure(figsize=(10,5))
plt.plot(x,y)
plt.scatter(x,ruido, color='r',  label='ruido')
plt.legend()
plt.show()



# In[7]:


c=np.zeros(2)
sx=np.sum(x)
sy=np.sum(ruido)
sxy=np.sum(x*ruido)
sx2=np.sum(x**2)
n=len(x)


c[0] = (n * sxy - sx * sy) / (n * sx2 - sx**2)
c[1] = (sx2 * sy - sx * sxy) / (n * sx2 - sx**2) #usando a formula de mmq sem incertezas 


y2=c[0]*x +c[1]

plt.plot(x,y2,label='reta de ajuste',linestyle='--')
plt.scatter(x,ruido, color='r',  label='ruido')
plt.legend()
plt.show()

