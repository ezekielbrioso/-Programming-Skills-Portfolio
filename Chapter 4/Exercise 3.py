# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:57:52 2023

@author: Ezekiel

Chapter 4 - Exercise  3: Alien Colors #3

Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

• If the alien is green, print a message that the player earned 5 points.

• If the alien is yellow, print a message that the player earned 10 points.

• If the alien is red, print a message that the player earned 15 points.

• Write three versions of this program, making sure each message is printed for the appropriate color alien.

"""
#Green Version
alien_color = "green" #the variable is set to "green"
if alien_color == "green": #this condition is true, so the message "Player just earned 5 points" will print.
    print("Player just earned 5 points")
elif alien_color == "yellow":
    print("player just earned 10 points.")
else:
    print("Player just earned 15 points.")
   
#Yellow Version
alien_color = "yellow" #the variable is set to "yellow"
if alien_color == "green":
    print("Player just earned 5 points")
elif alien_color == "yellow":  #this condition is true, so the message "Player just earned 10 points" will print.
    print("player just earned 10 points.") 
else:
    print("Player just earned 15 points.")
    
#Red Version
alien_color = "red"  #the variable is set to "red"
if alien_color == "green":
    print("Player just earned 5 points")
elif alien_color == "yellow":
    print("player just earned 10 points.")
else:  #none of the if and elif conditions are true, so the else block will run, so the message "Player just earned 15 points" will print.
    print("Player just earned 15 points.")