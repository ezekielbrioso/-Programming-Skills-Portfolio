# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 22:37:42 2023

@author: Ezekiel

Chapter 7 - Exercise 5: Cities
Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence,

such as Reykjavik is in Iceland. Give the parameter for the country a default value.

Call your function for three different cities, at least one of which is not in the default country.
"""

def describe_city(city, country='Italy'):
    message = city.title() + " is in " + country.title() + "."
    print(message)

describe_city('Rome')
describe_city('Tokyo', 'Japan')
describe_city('Venice')