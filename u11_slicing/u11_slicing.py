word = "racecar"
reverse = word[::-1]
if word == reverse:
    print("Its a palindrome")
else:
    print("Its not a palindrome")

word = "MADAM"

# reverse the word
reverse = word[::-1]
print(reverse)

if word == word[::-1]:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")


# create a username based on first 3 characters of first name and last 3 characters of lastname + random number
# [start:stop:step]
fname = "DAVID"
lname = "BECKHAM"

first3 = fname[:3]
print(first3)

last3 = lname[-3:]
print(last3)
import random
username = first3 + last3 + str(random.randint(100,999))
print(username)

# check for palindrome
#level madam

# word[start: stop: step]

