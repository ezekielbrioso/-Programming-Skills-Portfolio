# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 22:05:09 2023

@author: Ezekiel

Chapter 6 - Exercise 2: Movie Tickets
A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if

they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their

age, and then tell them the cost of their movie ticket

   
"""
while True: #this starts infinite loop
    age = input("How old are you?") #it will ask the used to input the age
    if age == "quit": #this will check if the user quit the program
        break #if the user quit, the loop will stop using 'break'
    age = int(age) #converts user's age from textx to integer
    if age < 3: #this checks if the int is less than 3
        print("Your ticket is free") #if it's less than 3, it will print this message
    elif age < 12: #checks if the age is between 3 and 11
        print("Your ticket is $10") #if it is, this message will be shown
    else: #if it's neither, it means the number is beyond 12
        print("Your ticket is $15") #if it is, this message will be displayed

