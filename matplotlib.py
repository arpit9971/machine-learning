#!/usr/bin/env python
# coding: utf-8

# In[7]:


import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[1,2,3,4,5,6]
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x,y)
plt.title('first plot')
plt.show()


# In[29]:


import random
import numpy as np
t=np.arange(0.0,2.0,0.01) #it will take values from 0-2 with interval of 0.01
s=1+np.cos(2*np.pi*t) #1+cos(2*pi*t)
plt.plot(t,s,'r')#r is used for red colour
plt.xlabel('time')
plt.ylabel('voltage')
plt.title('cosine function')
plt.grid()
plt.show()


# In[44]:


import numpy as np
import matplotlib.pyplot as plt
x1=np.linspace(0.0,5.0)
x2=np.linspace(0.0,2.0)

y1=np.cos(2*np.pi*x1)
y2=np.sin(2*np.pi*x2)

plt.subplot(2,1,1) #(2 rows , 1 column, 1st position of this graph) , subplot() function is used for multiple graphs on one plane.
plt.plot(x1,y1,'-o') # -o is used for graph pattern
plt.xlabel('x1')
plt.ylabel('amp(x1)')
plt.title('cosine wave')

plt.subplot(2,1,2) # (2 rows , 1 column, 2nd position of this graph)
plt.plot(x2,y2,'-') # - is used for the graph pattern
plt.xlabel('x2')
plt.ylabel('amp(x2)')
plt.title('sine wave')

plt.show()


# In[54]:


import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,24,36,49,5]

label=['one','two','three','four','five']

plt.bar(x,y,tick_label=label,width=0.7,color=['red','blue','green'])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Bar graph')

plt.show()


# In[ ]:




