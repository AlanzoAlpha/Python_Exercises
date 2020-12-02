#!/usr/bin/env python
# coding: utf-8

# Create a function that will take two integer numbers and calculate their value after being added, subtracted, multiplied or divided. The function should take the following arguments:
# 
# a as your first value
# 
# b as your second value the operation you want to perform (+, -, *, /) as a string value Such that the calculation is a + b, a - b, a * b, a / b
# 
# The output must be an integer value.
# 
# print(calculator(2, 4, "+")) # Should print 6 to the console print(calculator(10, 3, "-")) # Should print 7 to the console print(calculator(4, 7, "*")) # Should print 28 to the console print(calculator(100, 2, "/")) # Should print 50 to the console

# In[3]:


num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your first number: '))
sign = input('Enter an operator: ')
ans = 0
def calculator(num1, num2, sign):
    
    if sign =='+':
        ans = num1 + num2
        return ans
    elif sign == '-':
        ans = num1 - num2
        return ans
    elif sign == '*':
        ans = num1 * num2
        return ans
    else:
        if sign == '/':
            ans = num1 / num2
            return ans


print(calculator(num1, num2, sign))
print(calculator(2, 4, "+"))
print(calculator(10, 3, "-"))
print(calculator(4, 7, "*")) 
print(int(calculator(100, 2, "/")))         

