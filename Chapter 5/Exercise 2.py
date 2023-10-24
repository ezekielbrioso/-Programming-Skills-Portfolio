# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 16:33:17 2023

@author: Ezekiel

Chapter 5 - Exercise 2: Glossary
A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store
their meanings as values.

Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print
the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between
each word-meaning pair in your output.    
"""

glossary = {"Variable": "It is used to store values.","String": "A collection of characters.", "Arithmetic Operator": "A mathematical function that includes addition, subtraction, multiplication, division, and modulus.", "Loop": "A control structure that repeats multiple times until a condition is met.", "List": "A collection of values of different data types."} #this is glossary and it containts key-value pairs
for word, meaning in glossary.items(): #a for loop that goes through list one at a time
    print(word + ":") #for each word, the meaning will be shown
    print(meaning + "\n") #next word and meaning