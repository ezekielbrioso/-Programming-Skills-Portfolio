# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 16:10:47 2023

@author: Ezekiel

Chapter 4 - Exercise 5: Favorite Fruit
Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.

•Make a list of your three favorite fruits and call it favorite_fruits.

•Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block

should print a statement,such as You really like bananas!
"""

favorite_fruits = ["strawberries", "peaches", "mangoes"]
if "apples" in favorite_fruits:
    print("You really like apples!")
if "strawberries" in favorite_fruits: #the if statement will check the specific fruit and since the "strawberries" is in the favorite_fruit list, so the message "You really like strawberries!" will print.
    print("You really like strawberries!")
if "avocadoes" in favorite_fruits:
    print("You really like avocadoes!")
if "mangoes" in favorite_fruits: #the if statement will check the specific fruit and since the "mangoes" is in the favorite_fruit list, so the message "You really like mangoes!" will print.
    print("You really like mangoes!")
if "bananas" in favorite_fruits:
    print("You really like bananas!")