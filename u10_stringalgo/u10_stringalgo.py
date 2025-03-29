###################################################
# Part 1: Learning Exercises

# Exercise 1: Using .find()
# Write a program to find the position of the first occurrence 
# of "Python" in a string using .find().
# text = "I love Python programming."
# position = text.find("Python")  # Find the position
# print("The position of 'Python' is: {}".format(position))
# text = "A B Python Python"
# position = text.find("Python") # start counting from 10
# print(f"The position of 'Python' is {position}")


# #------------------------------------------------------------
# # Exercise 2: Using .index()
# # Write a program to find the position of the first occurrence 
# # of "Python" in a string using .index().
# text = "I love Python programming."

# position = text.index("Python")  # Find the position
# print("The position of 'Python' is: {}".format(position))

# text = "ewr re wfre wree r Python"
# position = text.index("Python")
# print(f"The position of 'Python' is {position}.")




# #------------------------------------------------------------
# # Exercise 3: Finding Substring Without .find() or .index()
# # Write a program to find the position of "Python" manually 
# # without using .find() or .index().
# text = "I love Python programming."
# substring = "Python"
# position = -1  # Default value for "not found"

# # Iterate through the string, checking each substring of 
# # # the same length as "Python".
# for i in range(len(text) - len(substring) + 1):
#     # Extract a slice of the text with the same length as the 
#     # substring
#     current_slice = text[i:i + len(substring)]
#     # Compare the slice with the substring
#     if current_slice == substring:
#         position = i  # Record the position
#         break  # Exit the loop once found
# print("The position of 'Python' is: {}".format(position))



# # Exercise 4: Splitting a String Using .split()
# # Write a program to split a sentence into words using .split().
# sentence = "Python is fun to learn."
# words = sentence.split()  # Split by whitespace
# print("Words in the sentence: {}".format(words))

sentence = "dae eqfsfg qefgwef d dfs dfs fsd fg ghj hjkl"
words = sentence.split()
print(f"Words in the sentence: {words}")

# #------------------------------------------------------------
# # Exercise 5: Splitting a String Without .split()
# # Write a program to manually split a sentence into words 
# # without using .split().
# sentence = "Python is fun to learn."
# words = []  # Initialize an empty list to store words
# word = ""   # Temporary variable to build words
# for char in sentence:
#     if char == " ":  # Space indicates the end of a word
#         words.append(word)  # Add the word to the list
#         word = ""  # Reset for the next word
#     else:
#         word += char  # Build the word character by character
# if word:  # Add the last word if it exists
#     words.append(word)
# print("Words in the sentence: {}".format(words))






# #------------------------------------------------------------
# # Exercise 6: Finding Position in a List Using .index()
# # Write a program to find the position of an element in a list 
# # using .index().
# numbers = [10, 20, 30, 40, 50]
# position = numbers.index(30)  # Find the position of 30
# print("The position of 30 is: {}".format(position))






# #------------------------------------------------------------
# # Exercise 7: Finding Position in a List Without .index()
# # Write a program to find the position of an element in a list 
# # manually without using .index().
# numbers = [10, 20, 30, 40, 50]
# target = 30
# position = -1  # Default value for "not found"

# # Iterate through the list to find the target
# for i in range(len(numbers)):
#     if numbers[i] == target:
#         position = i  # Record the position
#         break  # Exit the loop once found
# print("The position of 30 is: {}".format(position))





#------------------------------------------------------------
