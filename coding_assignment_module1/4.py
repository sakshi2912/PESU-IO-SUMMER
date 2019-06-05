#!/usr/bin/env python
# coding: utf-8

# In[2]:


n = int(input("Enter Number: "))
Sum = 0

while(n > 0):
    r =n % 10
    Sum = Sum + r
    n =n //10

print(Sum)


# In[ ]:




