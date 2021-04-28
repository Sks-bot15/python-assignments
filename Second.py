#!/usr/bin/env python
# coding: utf-8

# In[3]:


num=int(input('enter a number'))
temp=num
s=0
while(temp>0):
    c=temp%10
    s+=c**3
    temp//=10
if(num==s):
    print('its an armstrong number')
    print(s)
else:
    print('not an armstrong number')
    print(s)


# In[ ]:





# In[9]:





# In[ ]:





# In[ ]:




