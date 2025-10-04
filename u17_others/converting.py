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
#     print(f"I like to eat {i}")


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
#     print(f"Fruit {i+1}: {fruits[i]}")






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
# Exercise 4: Mapping Students to Scores
# students = ["Ali", "Bala", "Cindy"]
# marks = [55, 80, 62]
# Use a for loop to combine them into a dictionary.
# Expected Output:
# {"Ali": 55, "Bala": 80, "Cindy": 62}

# studentmarks = {}
# students = ["Ali", "Bala", "Cindy"]
# marks = [55, 80, 62]

# for i in range(len(students)):
#     studentmarks[students[i]] = marks[i]

# print(studentmarks)
#------------------------------------------------------------
# While Loop Validation
#------------------------------------------------------------

# Exercise 5: Length Check
# Keep asking user for a username until it has at least 5 characters.
# check to ensure that username is all alphabets
# error_count = 0
# while True:
#     username = input("Enter a username: ")
#     if len(username) < 5:
#         print("Username has to be at least 5 characters. ")
#         error_count += 1
#     if username.isalpha() == False:
#         print("Username has to be all alphabets")
#         error_count += 1
#     if error_count == 0:
#         print("Username valid. ")
#         break




# ----------------------------------------------------------------

# Exercise 6: Numbers Only
# Keep asking user to enter age until input contains digits only.

# while True:
#     age = input("Enter your age: ")
#     if age.isnumeric():
#         print("Valid age. ")
#         break
#     else:
#         print("Age must contain digits only. ")


# ----------------------------------------------------------------

# Exercise 7: Uppercase Only
# Keep asking until user enters a code in uppercase letters only.

# while True:
#     code = input("Enter code: ")
#     if code.isupper():
#         print("Valid code. ")
#         break
#     else:
#         print("Code must only contain uppercase letters. ")


# ----------------------------------------------------------------

# Exercise 8: Lowercase Only
# Keep asking until user enters an email in lowercase only.

# while True:
#     code = input("Enter email: ")
#     if code.islower():
#         print("Valid email. ")
#         break
#     else:
#         print("Email must only contain lowercase letters. ")



# ----------------------------------------------------------------

# Exercise 9: Password Validation
# Keep asking until user enters a password with length >= 8.

while True:
    password = input("Enter password: ")
    if len(password) >= 8:
        print("Valid password. ")
        break
    else:
        print("Code must only contain uppercase letters. ")




# (a) Input and validation [5 marks]
# Write a function get_valid_number(base) that:
# •	Accepts a parameter base which can be 2 or 10.
# •	Repeatedly asks the user to enter a number in that base until a valid number is provided.
# •	Checks that:
# o	For base 2: input only contains characters 0 and 1.
# o	For base 10: input only contains digits 0–9 (treat the value as a non-negative integer).
# •	Returns the number string (no leading/trailing spaces).
# Hint: Use .strip() and validate all characters before returning.

def get_valid_number(b):
    # write code to validate that it is a valid number for that base

    while True:
        num = input("Enter the number: ")

        if b == 2:
            for i in num:
                if i != 0 or i != 1:
                    print("Invalid, as it should only contain digits 0 or 1. ")
                else:
                    break

        if b == 10:
            for i in num:
                if i.isdigit == False:
                    print("Invalid, should only contain digits 0 -9. ")



            

    return number


num = get_valid_number(10)




# (b) Denary → Binary [6 marks] 
# Write a function den_to_bin(den_num) that: 
# Uses repeated division by 2, taking the remainder each time, 
# Builds the binary string by prepending each remainder, 
# Returns "0" if the input is 0, 

# Assumes den_num is a non-negative integer 
# (you may convert the validated string to int before calling this). 
# Example: den_to_bin(251) should return "11111011". 



