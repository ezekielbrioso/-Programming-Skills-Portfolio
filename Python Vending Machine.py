# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 18:41:41 2023

@author: Ezekiel Brioso

L4 Creative Computing - Intro to Programming

Vending Machine
"""
def display_items(items): #this function uses for loop and display information such as ITEM ID, Item Name, Price, Category, and Stock
    for i, item in enumerate(items):
        print(f"Item ID: {item['ITEMID']} -- {item['Name']} -- Price: {item['Price']} -- {item['Category']} -- Stock: {item['Stock']}")

def user_input_coffee_type(): #this function allows the user to choose if they want their coffee to be HOT or COLD
    while True:
        try:
            coffee_type = input("Choose coffee type (HOT/COLD): ").upper()
            if coffee_type in ['HOT', 'COLD']:
                return coffee_type
            else:
                print("Invalid coffee type. Please enter either HOT or COLD.")
        except ValueError:
            print("Invalid input. Please enter a valid coffee type.")
    
def user_money(total_cost): #this function allows the user to insert money using a positive integer
    while True:
        try:
            user_money = int(input("\nEnter the amount of money you want to insert: AED  "))
            if user_money > 0:
                return user_money
            else:
                print("Invalid amount. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def user_input(items): #this function allows the user to input ITEM ID of the item they want to buy
    while True:
        try:
            user_input = int(input("\nEnter the ITEM ID for the item you want to buy: "))
            if 1 <= user_input <= len(items):
                return user_input
            else:
                print("Invalid ITEM ID. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def update_stock(items, selected_item_id): #this function allows user to check if the item is still in stock
    if items[selected_item_id - 1]["Stock"] > 0:
        items[selected_item_id - 1]["Stock"] -= 1
    else:
        print("Sorry, this item is OUT OF STOCK.") #if the item is out of stock, it will show this message

def calculate_change(total_cost, user_money): #this function calculates the change that needed to be returned to the user
    return user_money - total_cost

def sum_item(item): #this function allows the user to see how much the item(s) cost(s)
    sum_items = 0
    for i in item:
        sum_items += i["Price"]
    return sum_items

def create_receipt(item, receipt): #this function allows the user to have receipt
    for i in item:
        receipt += f"\n\t{i['Name']} -- {i['Price']}"
    return receipt

def suggest_purchase(selected_category): #this function suggests additional items based on the last purchase of the user
    suggestions = {
        'Beverage': ['Cookies', 'Chocolates'],
        'Juice': ['Cookies'],
        'Energy Drink': ['Snack'],
        'Sports Drink': ['Snack'],
        'Soda': ['Chips'],
        'Cookies': ['Beverage', 'Juice'],
        'Chocolates': ['Beverage'],
        'Snack': ['Energy Drink', 'Sports Drink'],
        'Chips': ['Soda']
    }

    if selected_category in suggestions:
        suggested_items = suggestions[selected_category]
        print(f"\nSuggestions: You might also like to try {' and '.join(suggested_items)}.")

#this displays items that are available, it includes the ITEMID, Name, Price, Stock, Category, as well as TYPE for Coffee
items_available = [
    {"ITEMID": 1, "Name": "Coffee", "Price": 13, "Stock": 18, "Category": "Beverage", "Type": ["HOT", "COLD"]},
    {"ITEMID": 2, "Name": "Fiji Water", "Price": 8.55, "Stock": 20, "Category": "Soda"},
    {"ITEMID": 3, "Name": "Coca-Cola", "Price": 6.5, "Stock": 20, "Category": "Soda"},
    {"ITEMID": 4, "Name": "Pepsi", "Price": 3.75, "Stock": 18, "Category": "Soda"},
    {"ITEMID": 5, "Name": "Sprite", "Price": 2.5, "Stock": 15, "Category": "Soda"},
    {"ITEMID": 6, "Name": "Mogu-Mogu", "Price": 4.50, "Stock": 18, "Category": "Juice"},
    {"ITEMID": 7, "Name": "Apple Juice", "Price": 3.5, "Stock": 0, "Category": "Juice"},
    {"ITEMID": 8, "Name": "Mango Juice", "Price": 5.5, "Stock": 15, "Category": "Juice"},
    {"ITEMID": 9, "Name": "Chips Ahoy", "Price": 5.55, "Stock": 22, "Category": "Cookies"},
    {"ITEMID": 10, "Name": "Oreo Cookies", "Price": 1.30, "Stock": 20, "Category": "Cookies"},
    {"ITEMID": 11, "Name": "Hello Panda Biscuit", "Price": 4.38, "Stock": 25, "Category": "Cookies"},
    {"ITEMID": 12, "Name": "Granola Bar", "Price": 3.35, "Stock": 28, "Category": "Snack"},
    {"ITEMID": 13, "Name": "Protein Bar", "Price": 5, "Stock": 20, "Category": "Snack"},
    {"ITEMID": 14, "Name": "Fruits & Nuts Bar", "Price": 6.21, "Stock": 20, "Category": "Snack"},
    {"ITEMID": 15, "Name": "Nut & Seed Bar", "Price": 10.46, "Stock": 17, "Category": "Snack"},
    {"ITEMID": 16, "Name": "Trail Mix", "Price": 7.80, "Stock": 25, "Category": "Snack"},
    {"ITEMID": 17, "Name": "Mixed Dried Fruits", "Price": 10.63, "Stock": 14, "Category": "Snack"},
    {"ITEMID": 18, "Name": "Pringles", "Price": 10, "Stock": 15, "Category": "Chips"},
    {"ITEMID": 19, "Name": "Hot Cheetos", "Price": 6.45, "Stock": 25, "Category": "Chips"},
    {"ITEMID": 20, "Name": "Doritos", "Price": 1.6, "Stock": 22, "Category": "Chips"},
    {"ITEMID": 21, "Name": "KitKat", "Price": 1.82, "Stock": 30, "Category": "Chocolate"},
    {"ITEMID": 22, "Name": "Twix", "Price": 3.25, "Stock": 28, "Category": "Chocolate"},
    {"ITEMID": 23, "Name": "Mars", "Price": 3.5, "Stock": 25, "Category": "Chocolate"},
    {"ITEMID": 24, "Name": "Hershey's Bar", "Price": 3.55, "Stock": 25, "Category": "Chocolate"},
    {"ITEMID": 25, "Name": "Milky Way", "Price": 2.5, "Stock": 22, "Category": "Chocolate"},
    {"ITEMID": 26, "Name": "M&M's", "Price": 3.8, "Stock": 30, "Category": "Chocolate"},
    {"ITEMID": 27, "Name": "Snickers", "Price": 3.15, "Stock": 18, "Category": "Chocolate"},
    {"ITEMID": 28, "Name": "Red Bull", "Price": 13.6, "Stock": 15, "Category": "Energy Drink"},
    {"ITEMID": 29, "Name": "Monster", "Price": 8.25, "Stock": 12, "Category": "Energy Drink"},
    {"ITEMID": 30, "Name": "Gatorade", "Price": 5, "Stock": 20, "Category": "Sports Drink"},
]


item = [] #initializes empty list
receipt = "\n\tPRODUCT NAME -- COST" #intializes receipt
run = True #controls main loop

print("Welcome to Python Vending Machine\n") 
print("Items available are listed below\n")
display_items(items_available) #calls function

while run: #uses while loop to allow users to select items how many times they want
    selected_item_id = user_input(items_available)

    if selected_item_id == 1:
        coffee_type = user_input_coffee_type()
        item.append({"Name": "Coffee", "Price": 13, "Type": coffee_type})
        update_stock(items_available, selected_item_id)
        suggest_purchase('Beverage')
    elif items_available[selected_item_id - 1]["Stock"] > 0:
        selected_category = items_available[selected_item_id - 1]["Category"]
        item.append(items_available[selected_item_id - 1])
        update_stock(items_available, selected_item_id)
        suggest_purchase(selected_category)
    else:
        print("Sorry, this item is out of stock. Please choose another item.") #this shows if the item is out of stock

    more_items = input("\nDo you want to add more? (YES/NO): ") #this allows users to decide if they want to add more purchase
    if more_items.upper() == "NO":
        run = False

#this part shows how the payment is being handled
receipt_value = int(input("\nPress '1' for Total Amount -- Press '2' for Bill: "))

if receipt_value == 1:
    print(f"Total Cost: {sum_item(item)}")
elif receipt_value == 2:
    print(create_receipt(item, receipt))    
else:
    print("INVALID")
    

#shows calculation and the item receipt
total_cost = sum_item(item)
user_money_amount = user_money(total_cost)

while user_money_amount < total_cost:
    print("Insufficient funds. Please insert more money.") #if the user inputs insufficient amount of money, this message will be displayed.
    additional_money = user_money(total_cost - user_money_amount)
    user_money_amount += additional_money

change = calculate_change(total_cost, user_money_amount)

print(create_receipt(item, receipt))
print(f"\n\tTotal Cost: AED {total_cost}")
print(f"\n\tChange: AED {change}")
print("\nThank you for your purchase!")