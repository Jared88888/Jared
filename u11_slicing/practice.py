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
    


#------------------------------------------------------------

# Validate if a string fits NRIC
# S8787878J
#7 letters in between 2 alphabets
passcheck = True
counter = 0
nric = input("Enter NRIC: ")

if len(nric) != 9:
    print("It dosen't have 9 characters")
    counter += 1

if not nric[:1].isalpha():
    print("It dosen't have 1 alphabet at the start")
    counter += 1

if not nric [-1:].isalpha():
    print("It dosen't have 1 alphabet at the end")
    counter += 1

if not nric[1:-1].isnumeric():
    print("It dosen't have 7 numbers in between the 2 alphabets")
    counter += 1

if counter == 0:
    print("NRIC valid")
