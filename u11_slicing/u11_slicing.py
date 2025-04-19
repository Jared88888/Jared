# word = "racecar"
# reverse = word[::-1]
# if word == reverse:
#     print("Its a palindrome")
# else:
#     print("Its not a palindrome")

# word = "MADAM"

# # reverse the word
# reverse = word[::-1]
# print(reverse)

# if word == word[::-1]:
#     print(f"{word} is a palindrome")
# else:
#     print(f"{word} is not a palindrome")


# # create a username based on first 3 characters of first name and last 3 characters of lastname + random number
# # [start:stop:step]
# fname = "DAVID"
# lname = "BECKHAM"

# first3 = fname[:3]
# print(first3)

# last3 = lname[-3:]
# print(last3)
# import random
# username = first3 + last3 + str(random.randint(100,999))
# print(username)

# # check for palindrome
# #level madam

# # word[start: stop: step]

###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 7: Extracting Middle Elements from a List
# Scenario: Extract the middle 3 elements from a list with an odd 
# number of elements.
# numbers = [10, 20, 30, 40, 50, 60, 70]
# middleindex = len(numbers) // 2
# middle3 = f"{numbers[middleindex - 1]}, {numbers[middleindex]}, {numbers[middleindex + 1]}"

# print(middle3)


#------------------------------------------------------------

# # Exercise 8: Checking Palindrome in a String
# # Scenario: Determine if a string is a palindrome (reads the same 
# # backward as forward).
# word = input("Enter a word: ")
# reversed = word[::-1]
# if word == reversed:
#     print("It's a palindrome. ")

# #------------------------------------------------------------

# # Exercise 9: Reversing Words in a Sentence
# # Scenario: Reverse the words in a sentence manually.
# sentence = "Python is fun to learn."

# words = sentence.split(" ")
# print(words[::-1])

# #------------------------------------------------------------
# # Exercise 10: Validating a Substring
# # Scenario: Check if a string contains only alphabets using slicing.
# text = "Hello123"
# counter = 0
# for i in text:
#     if i.isalpha():
#         counter +=1
    
# if counter == len(text):
#     print("Only alphabets")
# else:
#     print("Not only alphabets")

# #------------------------------------------------------------
# '''
# Question 5: Slice a list into halves.
# Divide a list into two equal halves and returns both halves.
# You may assume that the list has an even number of items
# Example Input: [1, 2, 3, 4, 5, 6]
# Example Output: [1, 2, 3]  [4, 5, 6]

# numbers = [1, 2, 3, 4, 5, 6]

# firstofsecondhalf = len(numbers) // 2
# firsthalf = numbers[:firstofsecondhalf]
# secondhalf = numbers[firstofsecondhalf:]
# print(firsthalf)
# print(secondhalf)

# Question 7: Remove the first and last elements of a list using slicing.
# Create a function that takes a list and returns it without 
# the first and last elements.
# Example Input: [0, 1, 2, 3, 4]
# Example Output: [1, 2, 3]
# # '''
# numbers = [0, 1, 2, 3, 4]
# newnumbers = numbers[1:-1]
# print(newnumbers)

# '''
# Question 8: Create a function to reverse the order of elements in a 
# list only from the second to the last but one.
# Example Input: [1, 2, 3, 4, 5, 6]
# Example Output: [1, 5, 4, 3, 2, 6]
# '''

# numbers = [1, 2, 3, 4, 5, 6, 7]
# newlist = numbers[1:-1]
# newlist = newlist[::-1]
# newlist = [numbers[0]] + newlist + [numbers[-1]]

# print(newlist)

# # '''
# # Question 13: 
# # Write a function called mid3(instring)
# # Extract the middle three characters from a string
# # Check that the incoming string must be an odd length, 
# # Test case 1: example input: abcdefg, example output: cde
# # Test case 2: example input: helloworld, example output: Invalid, Even length
# '''
# while True:
#     thing = input("Enter a string with odd number of characters: ")
#     if len(thing) % 2 != 1:
#         print("Must be odd. ")
#     else:
#         middleindex = len(thing) // 2
#         middle3 = f"{thing[middleindex - 1]} {thing[middleindex]} {thing[middleindex + 1]}"

#         print(middle3)
#         break





# Exercise 1: Extracting Initials from a Name
# Scenario: A company wants to display initials for employees on ID cards.
# Given a full name, extract the initials.

# Example:
# Input: "John Michael Smith"
# Output: "J.M.S"

# Input: "Alice Bob"
# Output: "A.B"

name = input("Enter name: ")

words = name.split(" ")
for i in words:
    print(i[0])
