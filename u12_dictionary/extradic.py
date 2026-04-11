### EXAMPLE DICTIONARY
# A dictionary variable holds a key and value pair
example = {
  'key1': 'value1',
  'key2': 'value2',
  'key3': 'value3',
  'key4': 'value4'
}

'''
################ Define a dictionary ###############
Define a dictionary named menu which will store a food item and price of food

'hamburger' costs 10
'pizza' costs 18.5
'lasagne' costs 25.70
'fries' costs 5
'''
# write and test your code here 
menu = {"hamburger" : 10,
        "pizza": 18.50,
        "lasagne" : 25.70,
        "fries" : 5}

'''
################ Retrieve values from a dictionary ###############
Print out the price of Lasagne only
Print out the price of Fries only
'''
# write and test your code here 
print(menu["lasagne"])
print(menu["fries"])
'''
########### Change the value of a dictionary key ###############
Change the price of hamburger to 20
Change the price of Fries to 3
'''
# write and test your code here 
menu["hamburger"] = 20
menu["hamburger"] = 3

'''
############ Increase the value of a dictionary key ############
Increase the price of Lasagne by 5
Decrease the price of Pizza by 3
'''
# write and test your code here 
menu["lasagne"] = menu["lasagne"] + 5
menu["lasagne"] = menu["lasagne"] - 3

'''
############### Add a new key/ Value to the dictionary #####################
Add a new menu item => Pasta which cost 15
Add a new menu item => Sandwich which cost 6
'''
# write and test your code here 
menu["pasta"] = 15
menu["sandwhich"] = 6

'''
############### Add a new key/ Value to the dictionary #####################
Delete menu item Pasta
'''
# write and test your code here 
del menu["pasta"]

'''
########### Loop through to Retrieve Keys ##################
# Write a for loop, and only display the name of food item that you sell
# only display the keys
'''
# write and test your code here 
for i in menu:
    print(i)
'''
########### Loop through to Retrieve Values ##################
Write a for loop, and only print out the price
'''
# write and test your code here 
for i in menu:
    print(menu[i])

'''
########### Loop through to Retrieve Key and Values ##################
Write a for loop, and print out the menu key and values
e.g.
Hamburger costs $10.00
Pizza costs $18.50
'''
# write and test your code here 
for i in menu:
    print(f"{i} costs {menu[i]}")

'''
#################### Challenge 1 ######################################
Write a program to calculate how much money you need to buy all the items in the menu.
'''
# write and test your code here 
total_cost = 0
for i in menu:
    total_cost += menu[i] 

'''
############### Challenge 2 ##########################################
Write a program to determine the most expensive item in the menu
'''
# write and test your code here 
most_ex = ""
most_ex_value = 0
for i in menu:
    if menu[i] > most_ex_value:
        most_ex_value = menu[i]
        most_ex = i


'''
################ Challenge 3 ########################################
#### Due to inflation, prices have increased. Update all the prices by 10%
'''
# write and test your code here 


'''
################ Challenge 4 ########################################
Upgrade this system where you ask customers what they want, and display the price 
# you can check if a key exists in a dicionaty, by using the 'in' keyword
# for example: if 'hamburger' in menu: will return true if hamburger exists 

Example:

Hello, What is your name? John
>>> Hi John, what would you like to eat? Laksa
>>> I'm sorry John, we don't sell Laksa. 

Hi John, what would you like to eat? Hamburger
>>> Great choice! Please pay $10.00. Your order will be delivered soon!
Hi John, what would you like to eat? Exit

Ok, bye!
'''
# write and test your code here 
name = input("Hello, What is your name? ")
if name == "Exit":
    print("Ok, bye!")
else:
    food_choice = (f"Hi {name}, what would you like to eat? ")
    if food_choice not in menu:
        print(f"I'm sorry {name}, we don't sell {food_choice}. ")
    else:
        print(f"Great choice! Please pay menu[food_choice]. Your order will be delivered soon!")