#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
my_list=np.array([1,2,3,4])
my_list


# In[17]:


import numpy as np
a=np.ones((3,5))
print(a)
print(type(a))


# In[123]:


np.random.seed(101) #to make the random samples consatnt 
arr=np.random.randint(0,100,(10)) # we want 10 random samples b/w 0 and 100
print(arr)


# In[130]:


#numpy functions
arr.max()#finds maximum element of arr


# In[132]:


arr.argmax()#finds index of maximum element of arr


# In[131]:


arr.min()#finds minimum element of arr


# In[133]:


arr.argmin()#finds index of minimum element of arr


# In[136]:


arr.reshape(2,5) #give that dimension for which array could be splitted


# In[137]:


arr.reshape(5,2) # reshape function help to convert in to different shape of different dimension


# In[148]:


np.random.seed(101)
mat=np.random.randint(0,100,(10,10))
mat


# In[154]:


# mat[2,2]
 mat[2,0]# to access the element of matrix mat declared above


# In[159]:


mat[0,:] # extract fst row
mat[1,:] #extract fst row
mat[:,3] #extract third column
mat[:,0] #extracts fst column


# In[160]:


mat[0:3,0:4] # 3x4 matrix retrieved from mat

