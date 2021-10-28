#!/usr/bin/env python
# coding: utf-8

# In[2]:


lis = [int(x) for x in input("Enter six numbers").split(" ")];


# In[3]:


newList = [x*3 for x in lis]
print(newList)


# In[9]:


import functools
sum = lambda arr : functools.reduce(lambda a, b:a+b, arr )


# In[10]:


print(sum(lis))
print(sum(newList))


# In[ ]:




