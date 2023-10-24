# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 22:04:30 2023

@author: Ezekiel

Chapter 6 - Exercise 1: Pizza Toppings

Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,

print a message saying you’ll add that topping to their pizza.
"""
while True: #a never-ending loop
    toppings = input("Enter pizza toppings:") #it will ask the user to input pizza toppings
    if toppings == "quit": #if the user entered quit, the program will stop
        break
    print("I will add the {} topping to your pizza".format(toppings)) #if the user didnt entered 'quit' it will print a message that confirms pizza topping