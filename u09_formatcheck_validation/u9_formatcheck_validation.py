# ###################################################
# # Part 1: Learning Exercises

# # Exercise 1: Converting to Uppercase
# # Write a program to convert a string to uppercase.
# # Example: Input = "hello", Output = "HELLO".
# word = "hello"
# uppercase_word = word.upper()  # Convert to uppercase
# print("Uppercase: {}".format(uppercase_word))




# #------------------------------------------------------------
# # Exercise 2: Converting to Lowercase
# # Write a program to convert a string to lowercase.
# # Example: Input = "HELLO", Output = "hello".
# word = "HELLO"
# lowercase_word = word.lower()  # Convert to lowercase
# print("Lowercase: {}".format(lowercase_word))




# #------------------------------------------------------------
# # Exercise 3: Checking if a String is Uppercase
# # Write a program to check if a string is fully uppercase.
# # Example: Input = "HELLO", Output = True.
# word = "HELLO"
# is_upper = word.isupper()  # Check if uppercase
# print("Is '{}' uppercase? {}".format(word, is_upper))




# #------------------------------------------------------------
# # Exercise 4: Checking if a String is Lowercase
# # Write a program to check if a string is fully lowercase.
# # Example: Input = "hello", Output = True.
# word = "hello"
# is_lower = word.islower()  # Check if lowercase
# print("Is '{}' lowercase? {}".format(word, is_lower))




# #------------------------------------------------------------
# # Exercise 5: Checking if a String is Alphanumeric
# # Write a program to check if a string contains only letters 
# # and numbers.
# # Example: Input = "Python123", Output = True.
# word = "Python123"
# is_alnum = word.isalnum()  # Check if alphanumeric
# print("Is '{}' alphanumeric? {}".format(word, is_alnum))




# #------------------------------------------------------------
# # Exercise 6: Checking if a String is Alphabetic
# # Write a program to check if a string contains only letters.
# # Example: Input = "Python", Output = True.
# word = "Python"
# is_alpha = word.isalpha()  # Check if alphabetic
# print("Is '{}' alphabetic? {}".format(word, is_alpha))




# #------------------------------------------------------------
# # Exercise 7: Checking if a String is Numeric
# # Write a program to check if a string contains only numbers.
# # Example: Input = "12345", Output = True.
# word = "12345"
# is_digit = word.isdigit()  # Check if numeric
# print("Is '{}' numeric? {}".format(word, is_digit))




# #------------------------------------------------------------
# # Exercise 8: Removing Extra Spaces
# # Write a program to remove leading and trailing spaces.
# # Example: Input = "  hello  ", Output = "hello".
# word = "  hello  "
# stripped_word = word.strip()  # Remove spaces
# print("Stripped string: '{}'".format(stripped_word))




# #------------------------------------------------------------
# # Exercise 9: Length Validation
# # Write a program to validate that a string has at least 5 
# # characters. Prompt the user repeatedly until they enter a 
# # valid string.
# while True:
#     user_input = input("Enter a string with at least 5 characters: ")
#     if len(user_input) >= 5:
#         break  # Exit loop if valid
#     print("String too short. Try again.")
# print("Valid string: {}".format(user_input))




#------------------------------------------------------------

###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 10: Validating Uppercase Input
# Scenario: You are entering product codes into a system, and 
# all codes must be in uppercase letters (e.g., "ABC123").
# while True:
#     code = input("Enter the code (uppercase): ")
#     # check = code.isupper()
#     # if check == True:

    # if code.isupper() == True:
    #     print(f"Ok, {code} is in uppercase")
    #     break
    # # else:
    # print("Code must be in upper case.")


#------------------------------------------------------------
# Exercise 11: Validating Alphanumeric Input
# Scenario: A username field only accepts alphanumeric characters
# (letters and numbers) without special symbols.
# while True:
#     username = input("Enter a username(only alphanumeric characters): ")
#     if username.isalnum() == True:
#         print("Ok can")
#         break



#------------------------------------------------------------
# Exercise 12: Validating Numeric Input
# Scenario: You are collecting a phone number that must contain 
# only numeric characters.
# while True:
#     phone = input("Enter your phone number (only digits): ")
#     if phone.isdigit() == True:
#         print("Ok can")
#         break




#------------------------------------------------------------
# Exercise 13: Checking for Substrings
# Scenario: You are searching for the word "Python" in user 
# feedback to categorize responses related to Python programming.

# while True:
#     user = input("Enter a user(Python must be inside): ")
#     if "Python" in user:
#         print("Ok can")
#         break


#------------------------------------------------------------
# Exercise 14: Replacing Parts of a String
# Scenario: A user entered their old email address, and you 
# need to replace it with a new domain (e.g., from "@old.com" to "@new.com").
#.replace(oldvalue, newvalue)

# email = input("Enter your old email: ")
# print(email.replace("old", "new"))



#------------------------------------------------------------

# Example:
# Input: "The Quick Brown Fox Jumps Over The Lazy Dog."
# Output: "Number of uppercase letters: 8"

# Input: "this is a simple paragraph with no uppercase letters."
# Output: "Number of uppercase letters: 0"

# Input: "Hello, World! Python Is Amazing."
# Output: "Number of uppercase letters: 4"
# sentence = input("Enter a sentence: ")
# upper = 0
# for i in sentence:
#     if i.isupper():
#         upper += 1
# print(f"Theere are {upper} uppercase letters")




#################################################
# Assignment 1: Password Validation
# Scenario: Validate a password to ensure it is at least 8 characters long and contains:
# # - At least one uppercase letter.
# # - At least one lowercase letter.
# # - At least one digit.

# # Example:
# # Input: "Secure123"
# # Output: "Valid password"

# # Input: "password"
# # Output: "Invalid password: missing uppercase letter and digit"

# # Input: "PASSWORD123"
# # Output: "Invalid password: missing lowercase letter"

# password = input("Type a password: ")

# upperok = False
# lowerok = False
# digitok = False

# for i in password:
#     if i.isupper() == True and upperok == False:
#         upperok = True
#     elif i.islower() == True and lowerok == False:
#         lowerok = True
#     elif i.isdigit() == True and digitok == False:
#         digitok = True

# if upperok == True and lowerok == True and digitok == True and len(password) >= 8:
#     print(f"Password ok")
# else:
#     print(f"Password not ok")
#     print(f"Upper Case is OK = {upperok}")
#     print(f"Lower Case is OK = {lowerok}")
#     print(f"Digit is OK = {digitok}")
#     print(f"Length is OK = {len(password) > 8}")


##################################################################
# Scenario: Ensure a sentence starts with a capital letter and ends with a period.

# Example:
# Input: "The quick brown fox jumps over the lazy dog."
# Output: "Valid sentence"

# Input: "the quick brown fox jumps over the lazy dog"
# Output: "Invalid sentence: does not start with a capital letter and does not end with a period"

# Input: "Hello world"
# Output: "Invalid sentence: does not end with a period"
 
sentence = input("Enter a sentence: ")
length = len(sentence)
lastcharacter = sentence[length - 1]
firstcharacter = sentence[0]

# last = sentence[-1]
# print(last) #alternate

if firstcharacter.isupper() and lastcharacter == ".":
    print("Valid")
else:
    print("Invalid")

    