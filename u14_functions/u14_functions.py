# ###################################################
# # Part 1: Learning Exercises

# # Exercise 1: A Simple Function
# # Define a function that prints "Hello, World!" and call it.
# # def greet():
# #     print("Hello, World!")

# # # Call the function
# # greet()





# #------------------------------------------------------------
# # Exercise 2: Function with One Parameter
# # Define a function that takes a name as a parameter and greets the user.
# # def greet_user(name):
# #     print(f"Hello, {name}!" )

# # # Call the function with your name.
# # greet_user("Alice")





# #------------------------------------------------------------
# # Exercise 3: Function with Two Parameters
# # Define a function that takes two numbers and prints their sum.
# # def add_numbers(num1, num2):
# #     print(f"The sum of {num1} and {num2} is {num1 + num2}. ")

# # # Call the function with two numbers.
# # add_numbers(6, 11)





# #------------------------------------------------------------
# # Exercise 4: Function with a Return Value
# # Define a function that calculates the area of a rectangle.
# def calculate_area(length, width):
#     return length * width

# # Call the function and store the result.
# area = calculate_area(5, 3)
# print("The area of the rectangle is {area}. ")





# #------------------------------------------------------------
# # Exercise 5: Using Returned Values in Further Computations
# # Define a function that calculates the perimeter of a rectangle.
# def calculate_perimeter(length, width):
#     return 2 * (length + width)

# # Use both functions to calculate the area and perimeter.
# length = 6
# width = 4
# area = calculate_area(length, width)
# perimeter = calculate_perimeter(length, width)
# print("For a rectangle of length {} and width {}:".format(length, width))
# print("Area: {}, Perimeter: {}".format(area, perimeter))





# #------------------------------------------------------------
# # Exercise 6: Demonstrating Local and Global Variables
# # Define a function that modifies a local variable.
# def local_variable_example():
#     x = 10  # Local variable
#     print("Inside the function, x is {}".format(x))

# # Outside the function.
# x = 20  # Global variable
# local_variable_example()
# print("Outside the function, x is {}".format(x))






# #------------------------------------------------------------
# ###########################################################
# # Part 2. IN-CLASS Practice Exercises

# # Exercise 7: Greeting Multiple Users
# # Write a function that takes a list of names and greets each one.
# def greet_users(listofnames):
#     for i in listofnames:
#         print(f"Hello {i}")

# # Call the function with a list of names.
# greet_users(["Alice", "Bob", "Charlie"])





#------------------------------------------------------------
# Exercise 8: Simple Calculator
# Write a function that takes two numbers and an operator (+, -, *, /)
# and returns the result of the calculation.
def calculator(num1, num2, operator):
    if operator == "+":
        ans = num1 + num2
    elif operator == "-":
        ans = num1 - num2
    elif operator == "*":
        ans = num1 * num2
    elif operator == "+":
        ans = num1 / num2
    return ans
# Test the function with multiple operations.
print(calculator(10, 5, "+"))






#------------------------------------------------------------
# Exercise 9: Palindrome Checker
# Write a function that checks if a string is a palindrome.
def is_palindrome(word):
    if word[::-1] == word:
        return True

# Test the function with different words.
# print("Is 'radar' a palindrome? {}".format(is_palindrome("radar")))
# print("Is 'hello' a palindrome? {}".format(is_palindrome("hello")))







#------------------------------------------------------------
# Exercise 10: Display Multiplication Table
# Write a function that takes a number and prints its multiplication table.

# Call the function with a number.
# multiplication_table(5)






#------------------------------------------------------------
