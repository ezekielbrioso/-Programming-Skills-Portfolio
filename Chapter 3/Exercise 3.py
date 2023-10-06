# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 00:09:37 2023

@author: Ezekiel
"""
"""
Chapter 3 - Exercise 3: Your Own List
Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list

to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

"""
favorites=["airplane","car","train","bus"] #it's a list with 4 strings which are the transportations
for transportation in favorites: #it performs repeatedly through each string in the list and each execution, the string is assigned to the transportation
    print(f"I enjoy traveling by {transportation}! It's one of my favorites.") #the {transportation} is a placeholder. each string from the list will be insert in that placeholder individually with the message.