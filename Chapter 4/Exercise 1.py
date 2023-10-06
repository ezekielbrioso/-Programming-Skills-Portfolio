# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:25:34 2023

@author: Ezekiel

Chapter 4 - Exercise 1: Alien Colors #1

Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

•Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.

•Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
"""

alien_color = "green"
if alien_color == "green": #since the if statement checked if alien_color="green", the message will print.
    print("Player just earned 5 points.") 
    

#Other Version - This failed version has no output because the condition is false. 
alien_color = "red" #The condition is false, so the code inside the if block will not run.   
if alien_color == "green":
    print("Player just earned 5 points.")
