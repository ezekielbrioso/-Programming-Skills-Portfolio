# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 22:11:15 2023

@author: Ezekiel

Chapter 6 - Exercise 5: No Pastrami
Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code

near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all

occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
"""

sandwich_orders = ['pastrami', "ham sandwich", "grilled cheese", 'pastrami', "roast beef sandwich", 'grilled chicken sandwich', "nutella sandwich", "pastrami"] #list containing different sandwiches
finished_sandwiches =[] #empty list

print("The Deli has run out of pastrami") #it will show a messaage that The Deli has run out of pastrami
while 'pastrami' in sandwich_orders: #starts a loop that continues as long as there is "pastrami" in the sandwich_orders list
    sandwich_orders.remove('pastrami') #removes 'patrami'
print() #adds blank line
while sandwich_orders: #starts another loop that continues as long as there are sandwich orders in the list
    current_sandwich = sandwich_orders.pop() #takes one sandwich from the list and stores it in current sandwich
    print("I made a " + current_sandwich) #message will show
    finished_sandwiches.append(current_sandwich) #adds the made sandwich to the current sandwich
print() #adds blank line
for finished_sandwich in finished_sandwiches: #starts a loop that goes through each finished sandwich in the list
    print(finished_sandwich.title() + " is done") #shows that the finished sandwich is ready