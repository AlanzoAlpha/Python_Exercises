#!/usr/bin/env python
# coding: utf-8

# Task 2 Create a function that takes a positive integer number and returns a list of all of its factors – all the numbers that divide into the input without any remainders. The output should be a list of integer values and should not include 1 or the input number.
# 
# Examples: print(factors(15)) # Should print [3, 5] to the console print(factors(12)) # Should print [2, 3, 4, 6] to the console print(factors(13)) # Should print [] (an empty list) to the console

# In[2]:


def factors(num):
    List =[]
    num2 = range(2,11)
    for i in num2:
        if num%i==0:
            List.append(i)
    return List
    
print(factors(15)) 
print(factors(12)) 
print(factors(13)) 

