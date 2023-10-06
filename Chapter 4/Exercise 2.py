# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:41:49 2023

@author: Ezekiel

Chapter 4 - Exercise 2: Alien Colors #2

Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.

•If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.

•If the alien’s color isn’t green, print a statement that the player just earned 10 points.

•Write one version of this program that runs the if block and another that runs the else block.
"""

alien_color = "green" #since alien_color = "green" matches the condition in if statement, the message will print.
if alien_color == "green":
    print("Player just earned 5 points for shooting the alien.")
else:
    print("Player just earned 10 points.")
    
    
#Other Version
alien_color = "red" #the alien_color="red" and not alien_color="green" so the else block will work and the message "Player just earned 10 points" will print.
if alien_color == "green":
    print("Player just earned 5 points for shooting the alien.")
else:
    print("Player just earned 10 points.")