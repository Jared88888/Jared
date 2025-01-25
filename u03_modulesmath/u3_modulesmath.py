# feet = int(input("Enter the feet of your height "))
# inches = int(input("Enter the inches of your height "))
# print(f"Your height is {feet * 0.3048 * 100 + inches * 2.54} in cm")
   
# Part 1: Learning Exercises

# Exercise 1: Importing Modules
# Write a program to use the math module for calculations.
# Example: Calculate the square root of 16 and the power of 2^3.
# import math  # Importing the math module
# sqrt_value = math.sqrt(16)
# power_value = math.pow(2, 3)
# powervalue2 = 2**3 
# print("Square root of 16 is:", sqrt_value)
# print("2 to the power of 3 is:", power_value)


#------------------------------------------------------------
# Exercise 2: Modulus and Floor Division
# Write a program to calculate the modulus and floor division
# of two numbers. Example: 17 divided by 5.
# num1 = 17
# num2 = 5
# modulus = num1 % num2
# floor_div = num1 // num2
# print("17 % 5 is:", modulus)
# print("17 // 5 is:", floor_div)

# # to know if smth is even or odd
# num = int(input("Enter a number "))
# if num % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")


#------------------------------------------------------------
# Exercise 3: Using Rounding Methods
# Write a program to round a number using round(), math.ceil(),
# and math.floor(). Example: number = 5.67.
# number = 5.67
# rounded = round(number)
# ceiled = math.ceil(number)
# floored = math.floor(number)
# print("Rounded:", rounded, "Ceiled:", ceiled, "Floored:", floored)


#------------------------------------------------------------
# Exercise 4: Floor Division for Time Conversion
# Write a program to convert total seconds into minutes and 
# seconds using floor division and modulus. Example: 125 seconds
# = 2 minutes and 5 seconds.
# totalseconds = 538973
# print(f"{totalseconds//60} minutes and {totalseconds%60} seconds")

#------------------------------------------------------------
# Exercise 5: Rounding for Pricing
# Write a program to calculate the total price of an item after 
# rounding up to the nearest dollar. Example: If the price is 
# 19.75, the total is 20.
# price = 19.75
# rounded_price = math.ceil(price)
# print("Rounded total price is:", rounded_price)



#------------------------------------------------------------
# Exercise 6: Generating Random Integers
# Write a program to generate a random number between 1 and 10.
# Example: The output could be any number from 1 to 10.
# import random
# random_number = random.randint(1, 10)
# print("Random number between 1 and 10:", random_number)




###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 7: Simulating Two Dice Rolls
# Write a program to simulate the roll of a 6-sided die two times
# and display the results. Example: Output = 4, 6.

# import random
# print(str(random.randint(1, 6)) + " and " + str(random.randint(1, 6)))
# print(f"{random.randint(1,6)} and {random.randint(1,6)}")


#-----------------------------------------------------------
# Exercise 8: Floor Division for Groups
# Write a program to calculate how many full groups can be formed 
# and how many items are leftover. Example: 25 students divided 
# into groups of 4 = 6 groups and 1 leftover.

# people = 4325987324

# print(f"{people // 4} groups {people % 4} left over")


#------------------------------------------------------------
# Exercise 9: Rounding for Fuel Costs
# Write a program to calculate the total cost of fuel rounded up 
# to the nearest dollar. Example: If the fuel cost is 47.89, the 
# total is 48.
# import math
# fuelcost = 49.48
# print(math.ceil(fuelcost))


#------------------------------------------------------------
# Exercise 10: Floor Division for Age Conversion
# Write a program to calculate someone's age in decades and 
# remaining years. Example: Age = 29 -> Decades = 2, Years = 9.
# age  = 39
# print(f"{age // 10} decades and {age%10} years")



#------------------------------------------------------------
# Exercise 11: Calculating Items in Boxes
# Write a program to calculate how many full boxes are needed to 
# pack items and how many items are leftover. Example: If there 
# are 53 items and each box holds 12, the output is:
# Full boxes = 4, Leftover = 5.
items = 34874253285737

print(f"if each box holds 12 items, there will be {items//12} boxes and {items%12} leftover items")




