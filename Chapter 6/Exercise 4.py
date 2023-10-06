# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 22:08:32 2023

@author: Ezekiel

Chapter 6 - Exercise 4: Deli

Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.

Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made,

move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.
"""

sandwich_orders = ['chicken sandwich', "ham sandwich", "grilled cheese", 'egg sandwich', "roast beef sandwich", 'grilled chicken sandwich', "nutella sandwich", "peanut butter and jelly sandwich"]
finished_sandwiches =[]

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich)
    finished_sandwiches.append(current_sandwich)
print()
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich + " is done\n")