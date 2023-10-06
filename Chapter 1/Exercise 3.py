# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:52:25 2023

@author: Ezekiel

Chapter 1 - Exercise 3: Print Date and Time

Write a Python program to display the current date and time.


"""
import datetime #this will allow us to know the date and time
now = datetime.datetime.now() #it will get the current date and time 
print ("current date and time:") #it will display the message "current date and time:"
print (now.strftime("%y-%m-%d %H: %M: %S")) #the strftime is used to format date and time. The y means year, m means month, d means day, H means hour, M means minutes, and S means seconds. 