###################################################
# Part 1: Learning Exercises

# Exercise 1: Basic While Loop
# Write a program to print numbers from 1 to 5 using a while loop.
# Example: Output = 1, 2, 3, 4, 5.

# i = 1
# while i < 6:
#     print(i)
#     i += 1


#------------------------------------------------------------
# Exercise 2: Counting Down with While
# Write a program to print numbers from 5 to 1 using a while loop.
# Example: Output = 5, 4, 3, 2, 1.
# i = 5
# while i > 0:
#     print(i)
#     i -= 1


#------------------------------------------------------------
# Exercise 3: Summing Numbers
# Write a program to calculate the sum of numbers from 1 to 10.
# Example: Output = 55.
# i = 1
# sum = 0
# while i < 11:
#     sum += i
#     i += 1
# print(sum) # 2 + 3 +4+5+6+7+8+9+10+11


#------------------------------------------------------------
# Exercise 4: Repeating User Input
# Write a program that repeatedly asks the user to input a word
# until the user types "stop".

# while True:
#     word = input("Enter a word (enter 'stop' to stop)").lower()
#     if word == "stop":
#         print("'stop' detected, stopping")
#         break
#     else:
#         print("Continue typing")




#------------------------------------------------------------
# Exercise 5: Validating Input
# Write a program to ensure a user enters a number between 1 and 10.
# If the user enters an invalid number, prompt again.
# while True:
#     num = int(input("Enter a number between 1 and 10: "))
#     if num > 10 or num < 1:
#         print("Number has to be between 1 and 10.")
#     else:
#         print("Ok")
#         break
# #------------------------------------------------------------
# # Exercise 6: Using While True for Validation
# # Write a program to ensure the user enters a password at least 
# # 8 characters long. Use while True to validate the input.
# while True:  # Infinite loop for validation
#     password = input("Enter a password (at least 8 characters): ")
#     if len(password) >= 8:  # Validation condition
#         break  # Exit the loop if valid
#     print("Password too short. Try again.")
# print("Password accepted!")
# while 1 == 1:
#     print("this will run infinitely")

# while True:
#     password = input("Enter a password: ")
#     if len(password) <= 8:
#         print("Password should be at least 8 characters long: ")
#     else:
#         print("Valid password")
#         break

# while True:
#     password = input("Enter a password: ")
#     if len(password) >= 8:
#         print("Valid password")
#         break
    
#     print("Password should be at least 8 characters long: ")

# while True:
#     sum = 0
#     num = input("Enter a number: ")
#     x = num.split(",") # tell it what to split
#     intx = int(x)
#     sum += x
#     print(sum)

# strnum = input("Enter a number: ")
# count = 0 

# while count < len(strnum):









###########################################################
# Part 2. IN-CLASS Practice Exercises
# Exercise 7: Multiplication Table with While Loop
# Write a program to print the multiplication table of 7 up to 10.
# Example: 7 x 1 = 7, ..., 7 x 10 = 70.


# i = 1
# num = int(input("What number do you want to do this for?"))
# while i <= 12:
#     print(f"{num} x {i} = {num * i}")
    
#     i += 1

#------------------------------------------------------------
# Exercise 8: Sum of Even Numbers
# Write a program to calculate the sum of even numbers between 1 
# and 20 using a while loop. Example: Output = 110.

# i = 2
# sum = 0
# while i < 21:
#     sum += i
#     i += 2
# print(sum) 


#------------------------------------------------------------
# Exercise 9: Guessing Game
# Write a program where the user has to guess a random number 
# between 1 and 10. Keep prompting until they guess correctly.

# import random
# correct = random.randint(1,10)
# print(correct)
# while True:
#     guess = int(input("Enter your guess: "))
#     if guess == correct:
#         print("Correct")
#         break
#     else:
#         print("Wrong")


#------------------------------------------------------------
# Exercise 10: Input Validation for a Password
# Write a program that keeps asking the user to enter a password.
# If the password is correct, print "Access granted."






#------------------------------------------------------------
# Exercise 11: Printing Fibonacci Sequence
# Write a program to print the first 10 numbers in the Fibonacci
# sequence using a while loop. The Fibonacci sequence is a series 
# of numbers where each number is the sum of the two preceding 
# ones. It starts with 0 and 1.
# Example: Output = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.






#------------------------------------------------------------
# Exercise 12: Custom Pattern
# Write a program to print the following pattern:
# *
# **
# ***
# ****
# *****





#------------------------------------------------------------


###########################################################
# WHILE LOOP PRACTICE EXERCISES (O LEVEL COMPUTING REVISION)
# Focus: while, while True, break, input validation
# Note: Some exercises may combine both a while and for loop
###########################################################


#------------------------------------------------------------
# Exercise 1: Count Up
# Print numbers from 1 to 5 using a while loop.
# Example Output: 1 2 3 4 5
#------------------------------------------------------------

# num = 1
# while num < 6:
#     print(num)
#     num += 1


#------------------------------------------------------------
# Exercise 2: Count Down
# Print numbers from 10 down to 1 using a while loop.
# Example Output: 10 9 8 ... 1
#------------------------------------------------------------

# num = 10
# while num > 0:
#     print(num)
#     num -= 1




#------------------------------------------------------------
# Exercise 3: Even Numbers Until N
# Ask for an integer N. Print all even numbers from 2 up to N inclusive.
# Sample Input: 12
# Example Output: 2 4 6 8 10 12
#------------------------------------------------------------

# N = int(input("Enter N: "))
# start = 2
# while start < N+1:
#     print(start)
#     start += 2




#------------------------------------------------------------
# Exercise 4: Summation with While
# Calculate the sum of numbers 1 to 100.
# Example Output: 5050
#------------------------------------------------------------
# sum = 0
# num = 1
# while num < 101:
#     sum += num
#     num += 1

# print(sum)



#------------------------------------------------------------
# Exercise 5: Multiplication Table
# Ask for an integer x. Print its first 10 multiples in "x * i = value" format.
# Sample Input: 7
# Example Output:
# 7 * 1 = 7
# 7 * 2 = 14
# 7 * 3 = 21
#------------------------------------------------------------

# x = int(input("Enter an integer: "))
# num = 1
# while num<4:
#     print(f"{x} * {num} = {x * num}")
#     num += 1



#------------------------------------------------------------
# Exercise 6: While True + break 
# Repeatedly ask for integers and add them to a total.
# Stop when user enters "END" (case-insensitive).
# Print total after stopping.
# Sample Inputs: 10, 20, 5, END
# Example Output: Total = 35
#------------------------------------------------------------

# total = 0
# while True:
#     num = input("Enter integers(END to end): ")
#     if num == "END":
#         break
#     total += int(num)
# print(total)

#------------------------------------------------------------
# Exercise 7: While True  (Skip Negatives)
# Repeatedly accept integers. If number is negative, skip and ignore it.
# Stop on 0. Print count of valid positives and their sum.
# Sample Inputs: -3, 5, 12, -1, 4, 0
# Example Output: Count = 3, Sum = 21
#------------------------------------------------------------
# sum = 0
# while True:
#     num = int(input("Enter a number: "))
#     if num > 0:
#         sum += num
#     elif num == 0:
#         break

# print(sum)


#------------------------------------------------------------
# Exercise 8: Presence Check (Non-Empty String)
# Ask for a name. Keep asking until a non-empty name is entered.
# Then greet the user.
# Sample Input: "" -> "   " -> "Alex"
# Example Output: Hello, Alex!
#------------------------------------------------------------

# while True:
#     name = input("Enter a name: ")
#     if name.strip() != "":
#         print(f"Hello, {name}!")
#         break






#------------------------------------------------------------
# Exercise 9: Length Check (Username)
# Ask for a username that must be 5 to 12 characters long.
# Keep prompting until valid, then print "Username accepted".
# Sample Inputs: "ab" (invalid), "student01" (valid)
#------------------------------------------------------------

# while True:
#     username = input("Enter a usernamw: ")
#     if len(username)>=5 and len(username) <= 12:
#         print("Username accepted. ")
#         break
#     else:
#         print("Invalid. ")





#------------------------------------------------------------
# Exercise 10: Range Check (Quiz Score)
# Ask for an integer score between 0 and 100 inclusive.
# Keep prompting until valid, then print "Score recorded: ".
# Sample Inputs: 120 (invalid), -5 (invalid), 85 (valid)
#------------------------------------------------------------

# while True:
#     score = input("Enter an integer score between 0 and 100 inclusive: ")
#     if score >= 0 and score <= 100:
#         print("Score recorded. ")
#     else:
#         print("Invalid")




#------------------------------------------------------------
# Exercise 11: Format Check (Positive Integer Only)
# Ask for an input that must be a positive integer that is more than 0 (e.g., "42", "85").
# If letters or symbols appear, ask again.
# Sample Inputs: "abc" -> "-4" -> "12" (valid)
#------------------------------------------------------------

# while True:
#     num = input("Enter a positive integer: ")
#     if num.isdigit():
#         break
    





#------------------------------------------------------------
# Exercise 12: Format Check (Email)
# Ask for an email that must contain exactly one '@' and at least one '.' after it.
# No spaces allowed. Keep asking until valid, then print "Email accepted".
# Sample Inputs: "userexample.com" (invalid), "user@site.com" (valid)
#------------------------------------------------------------
# while True:
#     email = input("Enter an email: ")
#     posat = email.find("@")
    
#     if "@" in email and email[posat+1] == "." and " " not in email:
#         break
    



#------------------------------------------------------------
# Exercise 13: Existence Check (Course Code)
# Given list: valid_codes = ["7155", "8640", "9421", "3562"]
# Ask user for a course code. Repeat until code exists in list.
# Print "Code found" when valid.
# Sample Inputs: "2026" (prints invalid), "9421" (prints valid)
#------------------------------------------------------------
# valid_codes = ["7155", "8640", "9421", "3562"]
# while True:
#     course_code = input("Enter a course code: ")
#     if course_code in valid_codes:
#         break




#------------------------------------------------------------
# Exercise 14: Combined Checks (Password Policy)
# Requirements:
# - Non-empty
# - Length between 8 and 16
# - Must contain at least one digit 0-9
# - No spaces
# Keep prompting until valid, then print "Password set".
# Sample Inputs: "abc" (invalid), "abcd efgh1" (invalid), "GoodPass1" (valid)
#------------------------------------------------------------






#------------------------------------------------------------
# Exercise 15: Menu Loop
# Menu:
# (1) Add number
# (2) Show total
# (3) Reset total
# (4) Exit
# Handle invalid choice with "Invalid choice" and continue.
# For (1), ask integer & add to total. For (2), show total. For (3), reset.
# For (4), break loop and print "Goodbye".
#------------------------------------------------------------






#------------------------------------------------------------
# Exercise 16: Bounded Attempts (PIN Validation)
# Correct PIN = "2468"
# User has up to 3 attempts.
# Checks:
# - Non-empty
# - Exactly 4 digits
# - Digits only
# If correct, print "Access granted" and stop.
# if incorrect, print out incorrect reason
# If all attempts used, print "Access denied".
#------------------------------------------------------------






#------------------------------------------------------------
# Exercise 17: Clean List Input
# Ask user to enter positive integers separated by commas, e.g. "3,5,10".
# Validation:
# - Not empty
# - Each item integer only (no letters, decimals)
# - Each integer between 1 and 100 inclusive
# Repeat until valid, then print list length and sum.
# Sample Inputs: "3,5,200" (invalid), "3,five" (invalid), "2,10,8" (valid)
#------------------------------------------------------------






#------------------------------------------------------------
# Exercise 18: Date String Format Check (DD-MM)
# Ask for a date in "DD-MM" format:
# - Exactly 5 characters
# - '-' at position 3
# - DD between 01 to 31
# - MM between 01 to 12
# Repeat until valid, then print "Date accepted: ".
#------------------------------------------------------------






#------------------------------------------------------------
# Exercise 19: Unique Username
# Existing list: taken = ["amy", "bala", "charlie", "debin", "eliza"]
# Ask for username:
# - Not empty
# - Length 3 to 12
# - Not already in 'taken' (case-sensitive)
# Keep asking until valid, add it to taken list, then print "Registered: ".
#------------------------------------------------------------







#------------------------------------------------------------
# Exercise 20: SKU Validation
# Valid SKUs: ["A-1001", "B-2400", "C-0350", "Z-9999"]
# Input rules:
# - Not empty
# - Format: Letter '-' followed by 4 digits
# - Must exist in valid_skus
# Keep asking until valid, then print "SKU verified".
#------------------------------------------------------------






#------------------------------------------------------------
# Exercise 21: Password Confirmation
# Ask for password:
# - Non-empty
# - Length 8 to 16
# - Must include at least one uppercase and one digit
# If pass validation above, ask again to confirm. If mismatch, print "Mismatch" and restart.
# When valid and confirmed, print "Password confirmed".
#------------------------------------------------------------





#------------------------------------------------------------
# Exercise 22: Bounded Range Collector
# Collect 5 valid integers between 1 and 50 inclusive.
# If invalid (format/range), print "Invalid" and retry without counting.
# After 5 valid numbers, print min and max.
# Sample Inputs: 10, 50, 1, 33, 25
# Output: Min=1, Max=50
#------------------------------------------------------------

















    