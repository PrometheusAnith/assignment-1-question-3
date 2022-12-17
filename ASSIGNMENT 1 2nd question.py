#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to count the number of even and odd numbers from a series of numbers.

# In[5]:


x=int(input('Enter the starting range:'))
y=int(input('Enter the ending range:'))
even=0
odd=0
for i in range(x,y+1):
    if i%2==0:
        even=even+1
    else:
        odd=odd+1;
print('The total number of even numbers in given range is:',even)
print('The total number of odd numbers in given range is:',odd)


# In[ ]:




