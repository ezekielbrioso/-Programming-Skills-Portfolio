# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 16:35:23 2023

@author: Ezekiel

Chapter 5 - Exercise 5: Pets
Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about

each pet
"""
pet_owner1 = {"kind":"Cat","owner":"Kiel"}
pet_owner2 = {"kind":"Dog","owner":"Ken"}
pet_owner3 = {"kind":"Parrot", "owner":"Belle"}
pet_owner4 = {"kind":"Rabbit","owner":"Alice"}
pet_owner5 = {"kind":"Duck","owner":"Daisy"}
pets = [pet_owner1, pet_owner2, pet_owner3, pet_owner4, pet_owner5] #these are the dictionaries stored in a list called "pets."
for pet in pets:
    print(f"Kind of Animal: {pet['kind']}") 
    print(f"Owner's Name: {pet['owner']}")
    print() #this will create a blank line to separate the pets.