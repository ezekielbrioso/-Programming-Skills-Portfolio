# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:57:07 2023

@author: Ezekiel
"""
"""
Chapter 3 - Exercise 6: Shrinking Guest List
You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.

•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

•Print a message to each of the two people still on your list, letting them know they’re still invited.

•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.    
""" 
guests = ["Taylor Swift", "Evelyn Ha", "Kim Jennie"] #list with three strings/names
print("Sorry, I've found out that my dinner table won't arrive in time for dinner and I have space for only two guests.") #it will print the message
removed=guests.pop() #this will remove the last name/string from the list
print(f"\nSorry, {removed}, Unfortunately, I can't invite you to dinner this time.") #the {removed} is a placeholder and the last name from the list will be inserted in this message.
for each_people in guests: #it will go through each names in the list
        invitation = (f"\nDear {str(guests)[1:-1]}, you are still invited to dinner.") #creates a message for remaining guests
        print(invitation) #it will print the string from invitaiton variable
        del guests[0] #deletes the last person from list
        del guests [0] #deleted everyone from the list so now it would be an empty list
        print("\nGuest List:", guests) #this will show the updated list which only shows empty list.