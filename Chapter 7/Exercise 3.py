# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 22:36:45 2023

@author: Ezekiel

Chapter 7 -Exercise 3: T-Shirt

Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function

should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional

arguments to make a shirt. Call the function a second time using keyword arguments.

   
"""

def make_shirt(size, message):
    print("\nI will create a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt('medium', 'I love eating!')
make_shirt(message="I love sleeping.", size='small')