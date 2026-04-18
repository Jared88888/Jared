# # ###################################################
# # # Part 1: Learning Exercises

# # # Exercise 1: A Simple Function
# # # Define a function that prints "Hello, World!" and call it.
# # # def greet():
# # #     print("Hello, World!")

# # # # Call the function
# # # greet()





# # #------------------------------------------------------------
# # # Exercise 2: Function with One Parameter
# # # Define a function that takes a name as a parameter and greets the user.
# # # def greet_user(name):
# # #     print(f"Hello, {name}!" )

# # # # Call the function with your name.
# # # greet_user("Alice")





# # #------------------------------------------------------------
# # # Exercise 3: Function with Two Parameters
# # # Define a function that takes two numbers and prints their sum.
# # # def add_numbers(num1, num2):
# # #     print(f"The sum of {num1} and {num2} is {num1 + num2}. ")

# # # # Call the function with two numbers.
# # # add_numbers(6, 11)





# # #------------------------------------------------------------
# # # Exercise 4: Function with a Return Value
# # # Define a function that calculates the area of a rectangle.
# # def calculate_area(length, width):
# #     return length * width

# # # Call the function and store the result.
# # area = calculate_area(5, 3)
# # print("The area of the rectangle is {area}. ")





# # #------------------------------------------------------------
# # # Exercise 5: Using Returned Values in Further Computations
# # # Define a function that calculates the perimeter of a rectangle.
# # def calculate_perimeter(length, width):
# #     return 2 * (length + width)

# # # Use both functions to calculate the area and perimeter.
# # length = 6
# # width = 4
# # area = calculate_area(length, width)
# # perimeter = calculate_perimeter(length, width)
# # print("For a rectangle of length {} and width {}:".format(length, width))
# # print("Area: {}, Perimeter: {}".format(area, perimeter))





# # #------------------------------------------------------------
# # # Exercise 6: Demonstrating Local and Global Variables
# # # Define a function that modifies a local variable.
# # def local_variable_example():
# #     x = 10  # Local variable
# #     print("Inside the function, x is {}".format(x))

# # # Outside the function.
# # x = 20  # Global variable
# # local_variable_example()
# # print("Outside the function, x is {}".format(x))






# # #------------------------------------------------------------
# # ###########################################################
# # # Part 2. IN-CLASS Practice Exercises

# # # Exercise 7: Greeting Multiple Users
# # # Write a function that takes a list of names and greets each one.
# # def greet_users(listofnames):
# #     for i in listofnames:
# #         print(f"Hello {i}")

# # # Call the function with a list of names.
# # greet_users(["Alice", "Bob", "Charlie"])





# #------------------------------------------------------------
# # Exercise 8: Simple Calculator
# # Write a function that takes two numbers and an operator (+, -, *, /)
# # and returns the result of the calculation.
# def calculator(num1, num2, operator):
#     if operator == "+":
#         ans = num1 + num2
#     elif operator == "-":
#         ans = num1 - num2
#     elif operator == "*":
#         ans = num1 * num2
#     elif operator == "+":
#         ans = num1 / num2
#     return ans
# # Test the function with multiple operations.
# print(calculator(10, 5, "+"))






# #------------------------------------------------------------
# # Exercise 9: Palindrome Checker
# # Write a function that checks if a string is a palindrome.
# def is_palindrome(word):
#     if word[::-1] == word:
#         return True

# # Test the function with different words.
# # print("Is 'radar' a palindrome? {}".format(is_palindrome("radar")))
# # print("Is 'hello' a palindrome? {}".format(is_palindrome("hello")))







# #------------------------------------------------------------
# # Exercise 10: Display Multiplication Table
# # Write a function that takes a number and prints its multiplication table.

# # Call the function with a number.
# # multiplication_table(5)






#------------------------------------------------------------
##############################################################
##### MOCK QUESTION ##########################################
##############################################################
# The task is to write a program that checks whether a food item has expired based on 
# its expiry date and today’s date. Dates are entered in the format "DD-MM".

# All code should have appropriate comments and meaningful identifiers. [2]
# 
# ________________________________________
# Task 5.1 [4]
# Write a calculate_days( ) function that accepts a date parameter in the format "DD-MM".
# The function must calculate and return the total number of days elapsed since 01-01, 
# assuming 30 days per month
# ________________________________________

def calculate_days(date):
    month = int((date.split("-"))[1])
    day = int((date.split("-"))[0])
    total = (day - 1) + ((month - 1) * 30)
    return total
print(calculate_days("01-02"))














# Test your code using the values below
# print(calculate_days("01-02"))
# print(calculate_days("30-01"))
# print(calculate_days("30-02"))
# print(calculate_days("30-12"))


# ________________________________________
# Task 5.2  [3]
# Write a days_difference( ) function that takes two parameters:
# •	today (format "DD-MM")
# •	expiry (format "DD-MM")

# The function will check if an item has expired and return the number of days 
# between today’s date and the expiry date.
# •	Expiry is calculated by subtracting the today’s date from the expiry date. 
# You must use the calculate_days() function to retrieve the number of days between 
# today’s date and expiry date. Note that the number of days could be negative.
# You can assume both dates are always within the same year.
# 
# ________________________________________


















# ________________________________________
# Task 5.3 [8]
# Write a validate_date( ) function that accepts one parameter:
# •	date_str (a string in the format "DD-MM")
# The function must check whether the input date is valid according to the following rules:
# 1.	The input must contain a dash (-) separator between day and month.
# 2.	Both the day (DD) and month (MM) must be two characters long (e.g. "05-04" not "5-4").
# 3.	The day (DD) must be between 1 and 30 (inclusive).
# 4.	The month (MM) must be between 1 and 12 (inclusive).
# If all conditions are met, the function should return True.
# If any condition fails, the function should return False.
# Displays appropriate messages for invalid input. You may assume the input is always a string.
# ________________________________________

















# print(validate_date("01#01"))
# print(validate_date("aa-01"))
# print(validate_date("01-aa"))
# print(validate_date("50-01"))
# print(validate_date("05-50"))
# print(validate_date("0310"))

# ________________________________________
# Task 5.4 [6]
# Create a simple text-based user interface that:
# •	Prompts and validates today’s date in "DD-MM" format.
# o	You must use the validate_date() function to validate today’s date. 
# Your program will keep asking for an input until a valid date is provided.

# •	Prompts and validates the expiry date in "DD-MM" format.
# o	You must use the validate_date() function to validate the expiry date. 
# Your program will keep asking for an input until a valid date is provided.

# •	Compute if the item has expired. You must use the days_difference() function. 
#     If the number of days is positive, the item has not expired. 
#          Output “Item is fresh and will expire in  days.”
#     If the number of days is negative, the item has expired. 
#          Output “Item has expired  days ago.”
#     If the number of days is 0, then the item expires today. 
        #    Output “Item will expire today!”
# ________________________________________