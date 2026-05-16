###################################################
# Part 1: Learning Exercises

# Exercise 1: Absolute Value of a Difference
# Find the absolute difference between two numbers.
# Example: Temperatures of two cities.
# city1_temp = 28
# city2_temp = 35
# difference = city1_temp - city2_temp
# print(abs(difference))





#------------------------------------------------------------
# Exercise 2: Convert Character to ASCII
# Convert a character to its ASCII code and back again.
# char = "H"

# ordH = ord(char)
# print(ordH)

# letterH = chr(72)
# print(letterH)

#------------------------------------------------------------
# Exercise 3: Generating a Random Uppercase Letter
# Generate a random uppercase letter using ASCII values.
# import random
# letters = []
# for i in range(8):
#     ranupper = random.randint(65, 90)
#     ranletter = chr(ranupper)
#     letters.append(ranletter)
# print("".join(letters))

#------------------------------------------------------------
# Exercise 4: Generate ASCII Symbols
# Generate a random special character from ASCII values.


# generate a password with 8 random special characters
# import random
# password = ""
# for i in range(8):
#     randsymbol = chr(random.randint(33, 47))
#     password += randsymbol

# print(password)
#------------------------------------------------------------


### BONUS
# Generate a password containing the following
# 3 upper case letters
# 3 lower case letters
# 3 special characters
# 3 numbers

## BONUS BONUS: randomize the position
# import random
# password = ""
# for i in range(3):
#     upper = chr(random.randint(65,90))
#     lower = chr(random.randint(97,122))
#     randsymbol = chr(random.randint(33, 47))
#     num = chr(random.randint(48, 57))
#     password = password + upper + lower + randsymbol + num

# listpass = list(password)
# random.shuffle(listpass)
# print("".join(listpass))


# key = 3
# encmsg = ""
# MESSAGE = "THE COLD WATER FROM THE WATER COOLER VERY GOOD"

# for letter in MESSAGE:
#     num = ord(letter)
#     numplus = num + key
#     newchar = chr(numplus)
#     encmsg = encmsg + newchar

# print(encmsg)



###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 6: Random Username Generator
# The format is:
# first 3 characters of first name
# first 3 character of last name
# plus 3 printable characters from ASCII
# Scenario: Generate a random 9-character username using uppercase letters and digits.
# import random
# firstname = input("Enter your first name: ")
# lastname = input("Enter your last name: ")
# print(f"{firstname[:3]}{lastname[-3:]}{chr(random.randint(32, 126))}{chr(random.randint(32, 126))}{chr(random.randint(32, 126))}")


letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter = "J"
index = letters.find


##############################################################
### ASCII ord() and chr() for password generation
##############################################################
###########################################################
# Generate a Password with Specific Character Types
# Scenario 1: Corporate Password Policy - Basic Compliance
# One of your clients, a fintech company, has implemented a basic password policy. 
# All system-generated passwords must:
# - Be of a specific length
# - Include at least 1 uppercase letter, 1 lowercase letter, and 1 digit

# Your task: Write a Python program to generate such a password.
# Example: input = 8 → output = 'aB3xG2#1'

# HINT: Use ASCII:
# - Uppercase letters: 65-90
# - Lowercase letters: 97-122
# - Digits: 48-57


# # Write and test your code here
import random
# password = ""
# length = input("What length: ")

# randupper = chr(random.randint(65,90))
# password += randupper
# randlower = chr(random.randint(97,122))
# password += randlower
# randdigit = chr(random.randint(48,57))
# password += randdigit
    
# for i in range(int(length) - 3):
#     password += chr(random.randint(33,126))

# for i in range(10):
#     random.shuffle(password)
# print(password)

###########################################################
# Exclude Specific Characters in Password
#  Scenario 2: Readability-Enhanced Password Generator
# A logistics firm found that users often confuse similar-looking characters 
# (like 'l', '1', 'I', 'O', and '0') when reading out passwords over the phone.

# To improve usability, you're tasked to generate passwords that:
# - Are of a specific length
# - Exclude these confusing characters: 'l', '1', 'I', 'O', '0'

# Example: input = 8, exclude = 'l1IO0' → output = 'aB3xG#2!'
# Hint: Any character in 33-126 except ASCII codes 48, 49, 73, 79, 108


# Write and test your code here
# length = input("Enter length: ")
# password = ""
# for i in range(length):
#     while True:
#         randchar = chr(random.randint(33,126))
#         if randchar not in "l1Io0":
#             break
#     password += randchar
# print(password)


###########################################################
# Password with Special Characters
# Scenario 3: System Admin Access Passwords
# System administrators require strong passwords with at least 2 special characters 
# to prevent brute-force attacks.

# Your task:
# - Generate a password of a given length
# - Ensure it includes at least two special characters
#   (characters that are neither letters nor digits, e.g., '@', '#', '$', '%', etc.)

# Example: input = 8 → output = 'aB3@xG#2'
# Hint: ASCII 33-47: ! " # $ % & ' ( ) * + , - . /

# Write and test your code here





###########################################################
# Scenario 4: High-Security Access Control
# A secure military application demands passwords that follow strict composition rules
# The password must contain:
# - At least 2 uppercase letters
# - At least 2 lowercase letters
# - At least 2 digits
# - At least 2 special characters

# Write a Python program that:
# - Accepts the desired password length
# - Ensures the final password follows these rules exactly

# Example: input = 8 → output = 'A1b#C2d!'
# Hint: 
# Uppercase letters: 65-90
# Lowercase letters: 97-122
# Digits: 48-57
# Special characters (non-alphanumeric)
# 33-47, 58-64, 91-96, 123-126


# Write and test your code here






###########################################################

###########################################################
# Calculate Checksums for a List of Network Messages
#
# A computer needs to send several text messages across a network.
# Before each message is sent, the computer calculates a checksum.
#
# The checksum is calculated using this algorithm:
# 1. Convert each character in the message into its ASCII value.
# 2. Add up all the ASCII values.
# 3. Calculate the total modulo 256.
#
# Checksum = total ASCII value % 256
#
# Your task:
# Write a Python program that:
# - Uses the given list of 5 messages
# - Loops through each message in the list
# - Calculates the checksum of each message
# - Outputs each message and its checksum
#
# Expected output:
#
# The server is ready -> 9
# Send the file now -> 31
# Login request accepted -> 123
# Data packet received -> 121
# Connection closed -> 170
#
# HINT:
# - Spaces are also characters and must be included in the checksum.
# - Use ord(character) to get the ASCII value of a character.
# - Use % 256 to calculate the checksum.
#
# Write and test your code here

messages = [
    "The server is ready",
    "Send the file now",
    "Login request accepted",
    "Data packet received",
    "Connection closed"
]


for i in messages:
    total = 0
    for j in i:
        total += ord(j)
    total = total % 256
    print(f"{i} -> {total}")