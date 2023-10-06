# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 20:44:23 2023

@author: Ezekiel

Chapter 1 - Exercise 5: Compute Area of Circle

Write a Python program which accepts the radius of a circle from the user and compute the area.
"""

from math import pi #it tells the computer to get the pi from the library.
r = float(input("Input the radius of the circle:")) #it will ask the user to input a number or radius of the circle.
print("Area of the Circle =",pi * r**2) #this calculates and prints the area of the circle. the pi is multiplied by the square of the radius of the circle.