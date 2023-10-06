# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 00:19:00 2023

@author: Ezekiel
"""
"""
Chapter 3 - Exercise 4: Guest List
If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d

like to invite to dinner. Then use your list to print a message to each person, invitingthem to dinner.
"""
guests = ["Taylor Swift", "Lana Del Rey", "Kim Jennie"] #a list containing 3 strings
for each_people in guests: #this executes a loop that will go through each name individually
    print(f"Dear {each_people}, \nI would like to invite you to dinner. Your presence would be appreaciated.") #the {each_people} is a placeholder, the string from the list will be inserted there individually with the message. The print allows the message to be displayed.