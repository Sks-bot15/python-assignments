#!/usr/bin/env python
# coding: utf-8

# In[8]:



def fact(x):
    if(x==1):
        return x
    else:
        return x*fact(x-1)

num=int(input('enter a number' ))

if(num<0):
    print('negative integer has no factorial')
elif(num==0):
    print('factorial of 0 is 1')
else:
    print('factorial is '+str(fact(num)))
    


# In[ ]:





# In[ ]:




