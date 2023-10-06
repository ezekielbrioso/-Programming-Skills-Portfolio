# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 00:33:57 2023

@author: Ezekiel
"""
"""
Chapter 3 - Exercise 5: Change Guest List
You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

•Print a second set of invitation messages, one for each person who is still in your list.
"""
guests = ["Taylor Swift", "Lana Del Rey", "Kim Jennie"] #list with three names

cant_attend = "Lana Del Rey" #variable with a value from the list that indicates cannot make it to the dinner

print(f"{cant_attend} can't make it to the dinner.") #{cant_attend} is a placeholder, the name "lana del rey" will be inserted in the message

new = "Evelyn Ha" #a new variable
guests[guests.index(cant_attend)] = new #it will replace the name "Lana del Rey" with "Evelyn Ha"
for each_people in guests: #it will start a loop that will go through each name in the guests list individually.
    print(f"Dear {each_people}, \nI would like to invite you to dinner. Your presence would be appreaciated.") #{each_people} is a placeholder, the names from the list will be inserted in the message one by one.