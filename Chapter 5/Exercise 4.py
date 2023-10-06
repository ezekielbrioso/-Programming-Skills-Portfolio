# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 16:34:57 2023

@author: Ezekiel

Chapter 5 - Exercise 4: Rivers
Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

Use a loop to print the name of each river included in the dictionary.

Use a loop to print the name of each country included in the dictionary.
"""

rivers_dictionary = {"Nile":"Egypt","Amazon":"Brazil","Volga":"Russia"}

for river, country in rivers_dictionary.items():
    print(f"The {river} runs through {country}.")
    
print("\nList of Rivers:")
for river in rivers_dictionary.keys():
    print(river)
    
print("\nList of Countries:")
for country in rivers_dictionary.values():
    print(country)
    
#for loops are used in this input because this loop will allow us to accomplish the requested task.