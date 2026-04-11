# generate a username: 
# first 3 characters of first name
# last 3 characters of last name
# + a 3-digit random number 100 - 999
# Assume name is only 2 words, Michael Tan >>> mictan568
# import random
# name = input("What is your name? ").lower()
# words = name.split(" ")
# username = words[0][0:3] + words[1][-3:] + str(random.randint(100, 999))
# print(username)

###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 7: Extracting Middle Elements from a List
# Scenario: Extract the middle 3 elements from a list with an odd 
# number of elements.
# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# middleindex = len(numbers) // 2
# middle3 = f"{numbers[middleindex - 1]}, {numbers[middleindex]}, {numbers[middleindex + 1]}"
# print(middle3)

# #------------------------------------------------------------

# # Exercise 8: Checking Palindrome in a String
# # Scenario: Determine if a string is a palindrome (reads the same 
# # backward as forward).
# word = input("Enter a word: ")
# newword = word[::-1]
# if word == newword:
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")



# #------------------------------------------------------------

# # Exercise 9: Reversing Words in a Sentence
# # Scenario: Reverse the words in a sentence manually.
# sentence = "Python is fun to learn."

# words = sentence.split(" ")
# print(words[::-1])





# #------------------------------------------------------------
# # Exercise 10: Validating a Substring
# # Scenario: Check if a string contains only alphabets
# text = "Hello123"
# counter = 0

# for i in text:
#     if i.isalpha():
#         counter += 1
    
# if len(text) == counter:
#     print("String contains only alphabets")
# else:
#     print("String does not only contain alphabets")
    








        
'''
# Challenge 1:
Write a function `validate_nric(nric: str) -> bool` to 
validate if a given input is a valid Singapore NRIC number. 
A valid NRIC must start with 'S', 'T', 'F', or 'G', followed by 7 digits, 
and ends with an uppercase letter.

* In this case, assume that as long as the last character 
is an uppercase letter it is valid.

Normal Test: Input: "S1234567D", Output: True
Error Test: Input: "A1234567D", Output: False
Boundary Test: Input: "S123456", Output: False
'''
## Write and test your code here

    
#------------------------------------------------------------
#Challenge 1
# Validate if a string fits NRIC
# S8787878J
#7 letters in between 2 alphabets
def validate_nric(nric):
    
    nric = input("Enter NRIC: ")

    if len(nric) != 9:
        print("It dosen't have 9 characters")
        return False

    elif nric[:1] not in "STFG":
        print("It dosen't have 1 alphabet at the start")
        return False

    elif not nric [-1:].islpha and not nric [-1:].upper():
        print("It dosen't have 1 alphabet at the end")
        return False

    elif not nric[1:-1].isnumeric():
        print("It dosen't have 7 numbers in between the 2 alphabets")
        return False

    else:
        return True

'''
# Challenge 2:
Write a function `is_valid_username(username: str) -> bool` to 
check if a username is correctly generated. A valid username 
should be at least 6 characters long, should not contain any spaces, 
and must start with an uppercase letter followed by lowercase letters.

Normal Test: Input: "Johndoe", Output: True
Error Test: Input: "johnDoe", Output: False
Error Test: Input: "John Doe", Output: False
Boundary Test: Input: "John", Output: False
'''
## Write and test your code here

#challenge 2
def is_valid_username(username):
    
    if len(username) < 6:
        return False
    elif (username.split())[0] != username:
        return False
    elif not username[0].isupper():
        return False
    elif not username[1:].islower():
        return False
    else:
        return True
    

'''
# Challenge 3:
Write a function `validate_license_plate(plate: str) -> bool` 
to check if a vehicle license plate is valid. 
A valid plate starts with 3 uppercase letters, followed by 4 digits, 
and ends with an uppercase letter.

Normal Test: Input: "SAB1234Z", Output: True
Error Test: Input: "SA1234Z", Output: False
Boundary Test: Input: "SAB123Z", Output: False
'''
## Write and test your code here

def valid_license_plate(plate):
    if not plate[:3].isupper():
        return False
    elif len(plate[3:-1]) !=  4 and not len(plate[3:-1]).isdigit():
        return False
    elif not plate[-1].isupper():
        return False
    else:
        return True
    

'''
# Challenge 4:
Write a function `is_valid_postal_code(postal_code: str) -> bool` 
to validate a Singaporean postal code. A valid postal code consists 
of exactly 6 digits where the first digit must be between 1 and 7.

Normal Test: Input: "123456", Output: True
Error Test: Input: "823456", Output: False
Boundary Test: Input: "12345", Output: False
'''
## Write and test your code here




'''
# Challenge 5:
Write a function `validate_date_format(date_str: str) -> bool` 
to check if a date string is in the format "DD/MM/YYYY" 
where DD, MM, and YYYY are valid digits. 

The function should ensure that DD is between 01 and 31, 
MM is between 01 and 12, and YYYY is a valid 4-digit positive integer.

Normal Test: Input: "29/02/2020", Output: True
Error Test: Input: "32/13/2020", Output: False
Boundary Test: Input: "01/01/0001", Output: True
'''
## Write and test your code here



    

'''
Challenge 6:
A programmer is writing a program to calculate the 
check digit for a 12-digit integer.

The check digit is calculated by multiplying the digits 
in odd positions by 3 and the digits in even positions by 1. 
These values are added together to produce a total. 
The total is subtracted from the next multiple of 10 to 
give a final value. If the final value is 10, the check digit is X.

Example: 
12-digit integer = 1  0  3  4  5  6  2  7  1  0  1  3
Result           = 3  0  9  4  15 6  6  7  3  0  3  3
Total = 3 + 0 + 9 + 4 + 15 + 6 + 6 +7 + 3 + 0 + 3 + 3 = 59
The next multiple of 10 is 60 (*hint: nextnum = math.ceil(num/10) * 10)
So, check digit = 60 - 59 = 1

(a) The The program code function calculate() takes a 
12-digit number as a parameter. It calculates the 
check digit and returns the check digit.

Write the code for the function calculate [6]

(b) The main program:
•	Takes as input a 12-digit number until a valid 
12-digit integer is entered
•	Calls the function calculate() with the valid input 
as a parameter
•	Outputs the number with the check digit as its 13th digit

Write the code for the main program. [5]

Test that:
103456271013 = 1
123456789012 = 0
135792468013 = 5
'''
## Write and test your code here


    

'''
Challenge 7:
A developer needs to extract specific characters from a 
given string to generate a user ID.

(a) Write a function generate_user_id(name, birthdate) 
that takes a user's full name as a single string in the 
format "First Last" and a birthdate in the format "YYYYMMDD". 
The function should return a user ID consisting of:

- The first three letters of the last name (in uppercase),
- The last two digits of the year of birth,
- The first letter of the first name (in lowercase).
For example:
generate_user_id("John Doe", "19901225") should return DOE90j.
[6 marks]

(b) Write a main program that:

- Takes as input a full name and birthdate,
- Calls the generate_user_id() function,
- Outputs the generated user ID.
Test cases:

generate_user_id("Alice Tan", "20030515") should return TAN03a.
generate_user_id("Michael Johnson", "19850911") should return JOH85m.
[4 marks]
'''
## Write and test your code here


    

'''
Challenge: Credit Card Validation
A financial institution needs to verify the validity of credit card numbers 
using the Luhn algorithm.

Task 1: Implementing the Luhn Algorithm
(a) Write a function is_valid_credit_card(card_number) that takes 
a credit card number as a string and checks if it is valid according 
to the Luhn algorithm. The function should:

- Start from the rightmost digit (check digit) and move left.
- Double every second digit. If the doubling results in a number greater 
    than 9, subtract 9 from it.
- Sum all the digits (including those not doubled).

If the total sum is divisible by 10, return True 
(indicating the card number is valid); otherwise, return False.

Example:

is_valid_credit_card("4539148803436467") should return True.
is_valid_credit_card("1234567812345670") should return False.
[6 marks]

Task 2: Testing the Function
(b) Test your function with the following credit card numbers 
and determine if they are valid:

4539148803436467
1234567812345670
4485275742308327
6011514433546201
1234567812345678
Write the expected output for each test case.
'''
## Write and test your code here

    