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


key = 3
encmsg = ""
MESSAGE = "THE COLD WATER FROM THE WATER COOLER VERY GOOD"

for letter in MESSAGE:
    num = ord(letter)
    numplus = num + key
    newchar = chr(numplus)
    encmsg = encmsg + newchar

print(encmsg)



###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 6: Random Username Generator
# The format is:
# first 3 characters of first name
# first 3 character of last name
# plus 3 printable characters from ASCII
# Scenario: Generate a random 9-character username using uppercase letters and digits.
import random
firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
print(f"{firstname[:3]}{lastname[-3:]}{chr(random.randint(32, 126))}{chr(random.randint(32, 126))}{chr(random.randint(32, 126))}")

