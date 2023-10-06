# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 00:05:18 2023

@author: Ezekiel
"""
"""
Chapter 3 - Exercise  2: Greetings
Start with the list you used in Exercise 1, but instead of just

printing each person’s name, print a message to them. The text of each message should be the same, but each message should be

personalized with the person’s name.
"""
friends=["Alexis","Samantha","Jeiffel","Naomi","Aliyya"] #list with 5 strings/names
for name in friends: #it will repeat the name in the list individually
    message=f"Hello, {name}! You're so lovely and amazing!" #the {name} is a placeholder and the name from the list will be inserted there
    print(message) #it will print a message for each name in the list