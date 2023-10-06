# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 22:09:14 2023

@author: Ezekiel
"""
"""
Chapter 3 - Exercise 7: Seeing the World
Think of at least five places in the world you’d like to visit. • Store the locations in a list. Make sure the list is not in alphabetical order.

• Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.

• Use sorted() to print your list in alphabetical order without modifying the actual list.

• Show that your list is still in its original order by printing it.

• Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.

• Show that your list is still in its original order by printing it again.

• Use reverse() to change the order of your list. Print the list to show that its order has changed.

• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

• Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
"""

places=["Japan","Italy","Paris","Greece","South Korea"] #a list containing 5 strings or places
print("Original Order:") #it will display the string Original Order of the values
print(places) #it will print the values from the list in its original order
print("\nAlphabetical Order:") #it will display the string Alphabetical Order
print(sorted(places)) #it will sort the list in alphabetical order
print("\nOriginal Order:")#it will show the string original order
print(places) #it will print the unchanged or original order for comparison
print("\nReverse Alphabetical Order:")#it will print the string Reverse Alphabetical Order
print(sorted(places, reverse=True)) #it print the list in reverse alphabetical order without changing the order of the original list
print("\nReversed Order:") #it will display the string Reversed Order
print(places) #it will print the original order of list
places.reverse() #the list will show that it’s back to its original order
print("\nOriginal Order(reversed):") #displays the string
print(places) #prints the places in reversed order of the original list
places.sort() #it will sort the list in alphabetical order
print("\nAlphabetical Order:") #displays the message alphabetical order
print(places) #prints the list in alphabetical order
places.sort(reverse=True) #sorts the list in descending alphabetical order
print("\nReverse Alphabetical Order:") #displays the string Reverse Alphabetical Order
print(places) #print the list in reverse alphabetical order