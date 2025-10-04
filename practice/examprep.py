#------------------------------------------------------------
# For Loops through List
#------------------------------------------------------------

# Exercise 1: Printing Items (Method 1)
# Given fruits = ["apple", "banana", "cherry"]
# Use a for loop to print each fruit directly.
# Output example:
# I like to eat apple.
# I like to eat banana.
# I like to eat cherry.

# fruits = ["apple", "banana", "cherry"]

# for i in fruits:
#     print(i)


#------------------------------------------------------------
# Exercise 2: Printing Items (Method 2)
# Given the same fruits list
# Use for i in range(len(fruits)) to print the items.
# Output example:
# Fruit 1: apple
# Fruit 2: banana
# Fruit 3: cherry

# fruits = ["apple", "banana", "cherry"]
# for i in range(len(fruits)):
#     print(fruits[i])



#------------------------------------------------------------
# Exercise 3: Numbers Greater than 50
# Given numbers = [12, 67, 45, 89, 23]
# Use a for loop to print only numbers greater than 50.
# Expected Output:
# 67
# 89
# numbers = [12, 67, 45, 89, 23]
# for i in numbers:
#     if i > 50:
#         print(i)


#------------------------------------------------------------
# For Loops through Dictionary
#------------------------------------------------------------

# Exercise 4: Printing Keys
# Given scores = {"Ali": 55, "Bala": 80, "Cindy": 62}
# Write a loop to print all the student names.
# Expected Output:
# Ali
# Bala
# Cindy

# scores = {"Ali": 55, "Bala": 80, "Cindy": 62}
# for i in scores:
#     print(i)
#     print(scores[i])

#------------------------------------------------------------
# Exercise 5: Printing Values
# Using the same dictionary, print only the marks.
# Expected Output:
# 55
# 80
# 62

# for i in scores:
#     print(scores[i])



#------------------------------------------------------------
# Exercise 6: Keys and Values Together
# Print each student’s name and score in the format:
# Ali scored 55
# Bala scored 80
# Cindy scored 62




#------------------------------------------------------------
# For Loops with Nested Lists
#------------------------------------------------------------

# Exercise 7: Mapping Students to Scores
# students = ["Ali", "Bala", "Cindy"]
# marks = [55, 80, 62]
# Use a for loop to combine them into a dictionary.
# Expected Output:
# {"Ali": 55, "Bala": 80, "Cindy": 62}
# empty_dict = {}

# students = ["Ali", "Bala", "Cindy"]
# marks = [55, 80, 62]

# for i in range(len(students)):
#     empty_dict[students[i]] = marks[i]
# print(empty_dict)


#------------------------------------------------------------
# Exercise 8: Pairing Names
# boys = ["Tom", "Dick"]
# girls = ["Amy", "Beth"]
# Make a dictionary matching each boy to each girl.
# Expected Output:
# {"Tom": "Amy", "Dick": "Beth"}




#------------------------------------------------------------
# Exercise 9: Totaling Scores
# subjects = ["Math", "Science", "English"]
# marks = [75, 82, 68]
# Store into a dictionary, then loop to calculate total.
# Expected Output:
# Total Score = 225




#------------------------------------------------------------
# While Loop Validation
#------------------------------------------------------------

# Exercise 10: Length Check
# Keep asking user for a username until it has at least 5 characters.


mystring = input("Enter a string of text")
