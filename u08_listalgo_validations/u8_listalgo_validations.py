
###################################################
# Part 1: Learning Exercises


# Exercise 1: Finding the Maximum Without Built-In Functions
# Write a program to find the largest number in a list without 
# using max().

# list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
#          5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
#          1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
#          756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
#          2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880]

# bignum = max(list1)
# print(bignum)

# maxindex = 0
# minindex = 0
# max = list1[0]
# min = list1[0]
# for i in list1:
#     if i > max:
#         max = i
#         count = 0
#         maxindex = count
#     if i < min:
#         min = i
#         count = 0
#         maxindex = count
#         count += 1
# print(f"Biggest num is {max}. Index number is {maxindex}.")
# print(f"Smallest number is {min}. Index number is {minindex}")

# count = 0
# count += 1
# maxindex = count
# minindex =  count

# The school's swimming coach has recorded the 50m freestyle 
# swim times (in seconds) for 15 swimmers. 
# Using the list provided, find and display the fastest and slowest swim times, 
# along with their swim lane position in the list.

# Assume that the first item in the list is swim lane position 1.
#####################################################
# swim_times = [32.5, 30.1, 33.8, 29.6, 31.2, 34.0, 28.9, 
#               30.4, 38.1, 27.5, 35.6, 31.8, 29.2, 33.0, 30.5]
# # Answer for Question 2 here
# fast = swim_times[0]
# slow = swim_times[0]
# fastlane = 0
# slowlane = 0

# count = 1

# for i in swim_times:
#     if i < fast:
#         fast = i
#         fastlane = count
#     if i > slow:
#         slow = i
#         slowlane = count
#     count += 1

# print(f"""The fastest time is {fast}, in swimming lane {fastlane}
# The slowest time is {slow}, in swimming lane {slowlane}""")




#------------------------------------------------------------
# Exercise 2: Calculating the Sum Without Built-In Functions
# Write a program to calculate the sum of numbers in a list 
# without using sum().
list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880]

# print(sum(list1))
# sumnum = 0
# for i in list1:
#     sumnum += i
# print(sumnum)

#------------------------------------------------------------
# Exercise 3: Calculating the Average of a List
# Write a program to calculate the average of numbers in a list.
# Example: Input = [4, 8, 12, 16, 20], Output = 12.
# list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
#          5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
#          1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
#          756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
#          2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880]
# sumnum = 0
# for i in list1:
#     sumnum += i
# print(sumnum // len(list1))


#------------------------------------------------------------
# Exercise 4: Validating List Length
# Write a program to ensure a list contains at least 5 elements.
# Prompt the user to add more values until the condition is met.
# list1 = []
# for i in range (5):
#     add = input("Enter in elements ")
#     if add == "":
#         print("Add an element ")
        

# while len(list1) < 5:
#     color = input("Enter a color: ")
#     if color == "":
#         print("YOu must enter a color.")
#     else:
#         list1.append(color)
# print(list1)

#------------------------------------------------------------
# Exercise 5: Validating Range of Input
# Write a program to ensure a user enters a number between 1 and 
# 100. Repeat until a valid input is given.
# while True:
#     num = int(input("Enter a number between 1 and 100: "))
#     if num < 100 and num > 1:
#         break
#     else:
#         print("It has to be between 1 and 100")





#------------------------------------------------------------
# Exercise 6: Validating Presence in a List
# Write a program to ensure a specific value exists in a list.
# Prompt the user until they enter a value present in the list.
# animals = ["tiger","lion","elephant","cheetah","giraffe"]
# print(animals)


# while True:
#     enteranimal = input("Enter a value that exists in the list: ")
#     if enteranimal in animals:
#         print("Ok it does exist in the list. ")
#         break

#------------------------------------------------------------
# Exercise 7: Validating Non-Empty Input
# Write a program to ensure the user enters a non-empty value.
# Prompt the user until they enter a valid input.
while True:
    nonempty = input("Enter a non-empty value.")
    if nonempty != "":
        print("ok thanks")
        break
    