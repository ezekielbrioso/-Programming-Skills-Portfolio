# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 11:55:42 2023

@author: Ezekiel

Chapter 2 - Exercise 3: Stripping Names

Tidy up the code to make it easier to understand

Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. 

Make sure you use each character combination, “\t” and “\n”, at least once.

Print the name once, so the whitespace around the name is displayed.

Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

     
"""

name = "\t Ezekiel Brioso \n" #name is a variable with the value \t Ezekiel Brioso \n. the \t indicates tab while \n indicates new line.
print("Unmodified:") #it will show the original value
print(name) #it will display the value

print("\nUsing lstrip():") #this will create separation between previous to next output
print(name.lstrip()) #it removes tabs and spaces from string

print("\nUsing rstrip():") #this will create another separation
print(name.rstrip()) #it removes spaces and newline but keeps the tab and name complete

print("\nUsing strip():") #another separation
print(name.strip()) #it will remove the spaces, tab, newline characters, and will only show the name "Ezekiel Brioso" as the output