# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 16:34:34 2023

@author: Ezekiel

Chapter 5 - Exercise 3: Glossary 2
Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms

to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.
"""

glossary = {"Variable": "It is used to store values.","String": "A collection of characters.", "Arithmetic Operator": "A mathematical function that includes addition, subtraction, multiplication, division, and modulus.", "Loop": "A control structure that repeats multiple times until a condition is met.", "List": "A collection of values of different data types.", "Boolean": "A data type that represents one of two values, true or false.", "Float": "A number with point or a decimal number.", "Integer": "A whole number.", "Assignment Operator": "A type of operator which is denoted by = symbol.", "Bitwise Operator": "A type of Operator used to conduct bitwise calculations on integers."} #this contains key value pairs
for word, meaning in glossary.items(): #this for loop extracts two values, which are the word and meaning
    print(f"{word}:\n{meaning}\n") #uses f-string to print each word and meaning in an organized way. they are separated with colon and leaves blank between them so it would be easy to read.