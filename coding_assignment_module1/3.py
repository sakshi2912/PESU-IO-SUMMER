#!/usr/bin/env python
# coding: utf-8

# In[10]:


a=(input("Enter SORTED array")).split()
b=int(input("Enter the number to be searched"))
beg = 0
end = len(a)-1
found = False
while(beg<=end and found==False):
        mid = int((beg +end)//2)
        if int(a[mid]) == b:
            found=True
            print("Found at ")
            print(mid+1)
        else:
            if(b < int(a[mid])):
                end = mid - 1
            else:
                beg = mid + 1
if(found==False):
    print("Not found")


# In[ ]:




