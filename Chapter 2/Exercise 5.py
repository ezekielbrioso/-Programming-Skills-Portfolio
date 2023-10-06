# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 12:09:51 2023

@author: Ezekiel

Chapter 2 - Exercise 5: USB Shopper

A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.

Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

You will to use the arithmetic operators to complete this exercise.
"""

a=int(input("Total amount of money =")) #will ask the user to input a number
b=int(input("One USB stick price =")) #will ask the user to input a number
c=a//b #this will calculate the a and b using floor division-- operation that gives rounded down quotient.
print(c) #this will show the quotient

d=a%b #this calculates the remainder
print(d) #it will display the value of the variable d

message=f"With {a} pounds, she can buy {c} USB sticks and will have {d} pounds left." #will show a, c, and d values
print(message) #it will display the message variable

