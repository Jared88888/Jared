
# A text file shapes.txt stores a list of shapes with a comma between each value.  

# The current contents of shapes.txt are: 
# star,sphere,square,triangle 

# A text file colours.txt stores a list of colours with a comma between each value.  

# The current contents of colours.txt are: 
# red,yellow,green,blue 

# A program reads the data from each file and creates a dictionary of the values 
# so that each shape has an associated colour. 
# The first value in each file will be joined, for example, star and red. 

# The data is stored in a global dictionary with the identifier data_stored. 





# tasklist = []
# while True:
#     task = input("What do you have to do today: ")
#     tasklist.append(task + "\n")

#     proceed = input("Do you want to proceed('no' to stop): ")
#     if proceed.lower() == "no":
#         with open('tasks.txt', "a") as fobj:
#             fobj.writelines(tasklist)
#         break

# fobj = open('filename.txt', 'a')

# fobj.write("\nnext next year will be the best")

# fobj.close()


# fobj = open('filename.txt', 'r')

# content = fobj.read()

# counter = 0

# for i in content:
#     if i.lower() == "a":
#         counter += 1

# print(content)
# print(f"The number of letter a are {counter}")

# #------------------------------------------------------------
# # Exercise 1: Open and Read Without 'with'
# # Open "example.txt", read its content, and close the file manually.
# # Ensure "example.txt" contains some text before running.
# file = open("example.txt", "r")  # Open in read mode
# content = file.read()           # Read entire content
# print("File content:\n{}".format(content))
# file.close()                    # Always close the file!

# import random
# with open('filename.txt', "r") as fobj:
#     daylist = fobj.readlines()

#     for day in daylist:
#         print(day)

# randay = random.choice(daylist)
# print(f"Random day: {randay}")

# monthslist = ["Jam", "Feb", "March", "April", "May", "June"]
# with open("months.txt", "w") as fobj:
#     fobj.writelines(monthslist)




# #------------------------------------------------------------
# # Exercise 2: Write Without 'with'
# # Write "Manual Write Example" to "manual_output.txt" and close the file manually.
# file = open("manual_output.txt", "w")  # Open in write mode
# file.write("Manual Write Example")    # Write text to the file
# file.close()                          # Close the file to save changes





# #------------------------------------------------------------
# # Exercise 3: Read and Write Using 'with'
# # Read "example.txt" using 'with', ensuring the file closes automatically.
# with open("example.txt", "r") as file:
#     content = file.read()
#     print("File content with 'with':\n{}".format(content))





# #------------------------------------------------------------
# # Write "Hello, World!" to "output.txt" using 'with'.
# with open("output.txt", "w") as file:
#     file.write("Hello, World!")





# #------------------------------------------------------------
# # Exercise 4: Append to File
# # Append "This is a new appended line." to "output.txt".
# with open("output.txt", "a") as file:
#     file.write("\nThis is a new appended line.")





# #------------------------------------------------------------
# # Exercise 5: Write Multiple Lines
# # Write a list of strings to "output.txt" using 'with'.
# lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
# with open("output.txt", "w") as file:
#     file.writelines(lines)





# #------------------------------------------------------------
# # Exercise 6: Read Line-by-Line
# # Open "example.txt" and read it line by line.
# with open("example.txt", "r") as file:
#     for line in file:
#         print("Line:", line.strip())  # Print each line






# #------------------------------------------------------------


