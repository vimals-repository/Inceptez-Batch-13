#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to find 
# those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

# In[12]:


min=1500
max=2700
outputlist=[]

for i in range (1500,2701,1):
    if(i % 7 ==0  and i % 5 ==0):
        outputlist.append(i)

print(outputlist)


# 2. Write a Python program to construct the following pattern, using a nested for loop.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# In[44]:


for i in range(1,6):
    if(i<5):
        print ('*' * i)
    else:
        for j in range (i,0,-1):
            print('*'*j)


# In[ ]:





# In[ ]:




