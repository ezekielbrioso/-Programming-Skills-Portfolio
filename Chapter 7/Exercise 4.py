# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 22:37:01 2023

@author: Ezekiel

Chapter 7 - Exercise 4: Large Shirts
Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 

Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

"""
def make_shirt(size='large', message='I love eating!'):
    print("\nI will create a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Sleep tight, snuggle tight, and have a good night!')
