# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 22:11:15 2023

@author: Ezekiel

Chapter 6 - Exercise 5: No Pastrami
Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code

near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all

occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
"""

sandwich_orders = ['pastrami', "ham sandwich", "grilled cheese", 'pastrami', "roast beef sandwich", 'grilled chicken sandwich', "nutella sandwich", "pastrami"]
finished_sandwiches =[]

print("The Deli has run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print()
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made a " + current_sandwich)
    finished_sandwiches.append(current_sandwich)
print()
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title() + " is done")