# generate a username: 
# first 3 characters of first name
# last 3 characters of last name
# + a 3-digit random number 100 - 999
# Assume name is only 2 words, Michael Tan >>> mictan568
import random
name = input("What is your name? ").lower()
words = name.split(" ")
username = words[0][0:3] + words[1][-3:] + str(random.randint(100, 999))
print(username)
