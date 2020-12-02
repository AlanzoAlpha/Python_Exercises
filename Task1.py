#!/usr/bin/env python
# coding: utf-8

# Task 1 Create a function that accepts a string as an argument and swaps vowels with a corresponding symbol, such that:
# 
# a becomes 4
# 
# e becomes 3
# 
# i becomes !
# 
# o becomes ooo
# 
# u becomes |_|
# 
# The vowel swapper should recognise and change lowercase and capital letters the same way, with the exception of o: capital O should be changed to 000 (zeroes). The function should return the result as a string.
# 
# Examples: print(vowel_swapper("aA eE iI oO uU")) # Should print "44 33 !! ooo000 |_||_|" to the console print(vowel_swapper("Hello World")) # Should print "H3llooo Wooorld" to the console print(vowel_swapper("Everything's Available")) # Should print "3v3ryth!ng's 4v4!l4bl3" to the console

# In[1]:


def vswap(string):
    string = string.lower()
    string = string.replace('a', '4').replace('e', '3').replace('i', '!').replace('o', '000').replace('u', '|_|')
    #return string
    print(string)
        
string = 'She sell sea shell at the sea shore'
string1 = 'aA eE iI oO uU'
string2 = 'Hello World'
string3 = "Everything's Available"

vswap(string) 
vswap(string1)
vswap(string2)
vswap(string3)

