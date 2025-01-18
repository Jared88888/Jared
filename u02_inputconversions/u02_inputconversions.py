############################################################
# Part 1: Learning Exercises 
# input() and and .format()





# Exercise 1: Using input() for Text
# Write a program to ask the user for their favorite color and display it.
# Example: If the user enters "blue", the program should display
# "Your favorite color is blue."

# name = input("What is your name? ")
# color = input("What is your favorite color? ")
# print(name + "'s " + "favourite color is " + color )


#-----------------------------------------------------------
# Exercise 2: Understanding input() Behavior
# Write a program to ask the user for their age and display it.
# Example: If the user enters "15", display "Your age is 15."
# Note: Treat the input as a string for now.

# age = input("Enter your age: ")
# print("Your age is " + age + ".")




#------------------------------------------------------------
# Exercise 3: Comparing String Formatting Methods
# Write a program to ask the user for their name and age and display it
# in three different ways. Example: Input name = "John", age = 15


# name = input("Enter your name: ")
# age = input("Enter your age: ")

# print("My name is",name," and my age is ",age)

# print("My " + name + " is " + age + " years old.")

# print("My name is {}. I am {} years old.".format(name, age))

# print(f"My name is {name}. I am {age} years old.")
#------------------------------------------------------------
# Exercise 4: Formatting a Message with .format()
# Write a program to display a sentence about favorite subjects.
# Example: Input subject = "Math", reason = "exciting"
# subject = input("Enter your favorite subject: ")
# reason = input("Why do you like it? ")
# print("I like {} because it is {}.".format(subject, reason))

# subject = input("What is your favourite subject")
# reason = input("Why is this your favourite subject")
# print("You like {} because it is {}.".format(subject, reason))

#------------------------------------------------------------
# Exercise 5: Comparing .format() and f-strings for a Calculation
# Write a program to calculate the sum of two numbers and format the
# output in two ways: using .format() and f-strings.
# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")

# num1 = int(num1)
# num2 = int(num2)
# # result = num1 + num2

# # Using .format()
# print("Using .format(): The sum of {} and {} is {}.".format(num1, num2, result))

# # Using f-strings
# print(f"Using f-strings: The sum of {num1} and {num2} is {result}.")

# num1 = int(input("Enter a number "))
# num2 = int(input("Enter a second number "))

# print("The sum of {} and {} is {}.".format(num1, num2, num1 + num2))







###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 6: Greeting with .format()
# Write a program to ask the user for their name and print a greeting
# using .format(). Example:
# Input: name = "Alice"
# Output: "Hello, Alice! Have a great day!"

# name = input("Enter your name ")
# print = ("Hello, {}! Have a wonderful day ahead.".format(name))



#------------------------------------------------------------
# Exercise 7: Adding Two Numbers with .format()
# Write a program to ask the user for two numbers, convert them to integers,
# add them, and display the result using .format(). Example:
# Input: 5, 3
# Output: "The sum of 5 and 3 is 8."

# num1 = int(input("Enter a number "))
# num2 = int(input("Enter another number "))

# print("The sum of {} and {} is {}.".format(num1, num2, num1 + num2))

#------------------------------------------------------------
# Exercise 8: Area of a Circle with .format()
# Write a program to ask the user for the radius of a circle, convert it to
# a float, calculate the area using the formula (area = 3.14 * r^2), and
# display the result using .format(). Example:
# Input: radius = 7
# Output: "The area of the circle is 153.86."

# radius = float(input("Enter the radius of a circle "))

# print("The area of this circle is {}.".format(3.14 * radius**2))


#------------------------------------------------------------
# Exercise 9: Describing a Favorite Activity
# Write a program that asks the user for their favorite hobby and explains
# why they like it. Format the output using .format().
# Example: hobby = "reading", reason = "relaxing"

# hobby = input("What is your hobby? ")
# reason = input("Why do you like it? ")
# print("You like {} because it is {}.".format(hobby, reason))
#------------------------------------------------------------








