#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
class triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def perimeter(self):
        self.perim=self.a+self.b+self.c
        return(self.perim)
    def area(self):
        self.s=(self.a+self.b+self.c)/2
        self.area=math.sqrt((self.s)*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))
        return(self.area)
a=float(input('enter first side'))
b=float(input('enter second side'))
c=float(input('enter third side'))
if(a>0 and b>0 and c>0):
    if(a+b>c or b+c>a or a+c>b):
        tr=triangle(a,b,c)
        print(tr.perimeter())
        print(tr.area())
    else:
        print('Three sides dont form a triangle')
else:
    print('input triangle side as a non zero number')


# In[ ]:





# In[ ]:




