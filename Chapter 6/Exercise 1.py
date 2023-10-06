# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 22:04:30 2023

@author: Ezekiel

Chapter 6 - Exercise 1: Pizza Toppings

Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,

print a message saying you’ll add that topping to their pizza.
"""
while True:
    toppings = input("Enter pizza toppings:")
    if toppings == "quit":
        break
    print("I will add the {} topping to your pizza".format(toppings))