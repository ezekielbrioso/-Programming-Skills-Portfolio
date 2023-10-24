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

rivers_dictionary = {"Nile":"Egypt","Amazon":"Brazil","Volga":"Russia"} #creates dictionary containing the rivers name with the country

for river, country in rivers_dictionary.items(): #this for loop will go through each river and country 
    print(f"The {river} runs through {country}.") #will print a message showing the river and which country it flows through
    
print("\nList of Rivers:") #this will show the list of rivers and the \n makes the formatting better
for river in rivers_dictionary.keys(): #will sart another loop that will go through each river in the dictionary
    print(river) #it will show the river
    
print("\nList of Countries:") #this will show the list of countries
for country in rivers_dictionary.values(): #will start another loop that will go through each country in the dictionary
    print(country) #this prints country name inside the loop
    
#for loops are used in this input because this loop will allow us to accomplish the requested task.