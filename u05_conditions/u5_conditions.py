# using for loop
# print the numbers from 0 to 57

# print the numbers from 4 to 18

# print the multiples of 7 from 7 to 84

# for i in range(58):
#     print(i)


# for i in range(4, 19):
#     print(i)

# for i in range(7, 85, 7):
#     print(i)



##### RANDOM NUMBER GUESSER GAME

# Part 1: your computer needs to think of a random number between 1 - 100
import random
correct = random.randint(1, 100)
print(correct)


# 2: your computer will ask you to guess
print("Let's play a guessing game. ")
for i in range(7):
    guess = int(input("Guess the number I'm thinking of (1-100): "))
    
# 3: your computer will check if you answer 
    if guess > correct:
        print(f"{guess} is too big")
    elif guess < correct:
        print(f"{guess} is too small")
    else:
        print(f"{guess} is correct")
        break 
    # the code here will run on succesful completion of loop
else: 
    print(f"The number is {correct} you noob poop")


# 3b too big
# 3c too small
# 3a correctly

# computer also needs to give 7 chances...
# i need to ask again for 7 times... until i get the answer.







###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 8: Pass/Fail Checker
# Write a program to check if a student's score is a pass or 
# fail. Passing marks are 50 and above. Example: Input = 65.
# Output: "Pass."

# mark = int(input("Enter your mark: "))

# if mark >= 50:
#     print("Yoy passed, good boy")
# else:
#     print("You failed, go study")
#------------------------------------------------------------

# Exercise 9: Finding the Largest of Three Numbers
# Write a program to find the largest of three numbers.
# Example: Input = 4, 7, 2. Output = "The largest is 7."



num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("Enter a third number: "))
if  num1 >  num2 and num1 > num3:
    print(f"the largest number is {num1}")
elif num2 > num1 and num2 > num3:
    print(f"The largest number is {num2}")
else:
    print(f"The largest number is {num3}")

#------------------------------------------------------------
# Exercise 10: Leap Year Checker
# Write a program to check if a year is a leap year.
# Example: Input = 2024. Output = "Leap year."


# divisible by 4 = leap year

# else if divisible by 100 = not leap year

# else if year is divisible by 4 = leap year

# else it is not leap year

year = int(input("Enter a year: "))
if year % 4 > 0:
    print("It is not a leap year")

#------------------------------------------------------------
# Exercise 11: Age-Based Group Assignment
# Write a program to categorize a person into groups based 
# on age: Child (0-12), Teen (13-19), Adult (20+).
# Example: Input = 15. Output = "Teen."






#------------------------------------------------------------
# Exercise 12: Grade Checker
# Write a program to assign a grade based on marks:
# >= 90: A, >= 75: B, >= 60: C, < 60: D.
# Example: Input = 85. Output = "Grade B."






#------------------------------------------------------------
# Exercise 13: Even/Odd Checker
# Write a program to check if a number is even or odd.
# Example: Input = 4. Output = "Even number."





#------------------------------------------------------------



list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
         6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
         6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
         4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]

sum = 0
for i in list1:
    sum = sum + i
print(sum)