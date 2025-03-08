'''
Task 2

A school has a new computer network. The following program allows students
to create a username and password to log onto the network.
'''


'''
6. Edit the program so that it checks to see if the username entered exists in the list.
If it does not exist in the list, it must store the username in the list.

If it does not exist in the list, the program must loop
until a username is entered that does not already exist in the list.

Save your program. [4]
'''
# Write and test your code here
# list_usernames = ["StudentNo1","JaneJones","ABC123"]

# while True:
#     username = input("Please enter a username: ")
#     if username in list_usernames:
#         print("This username exists in the list. Try again ")
#     else: 
#         list_usernames.append(username)
#         break

# print(list_usernames)

'''
7. Edit your program so that it checks if the password:

- contains at least one numeric character
- contains at least one special character from: @!/?
- is at least 8 characters in length

The program should loop until the password fulfils all the three requirements.

Use suitable input and output messages

Save your program [6]
'''
# Write and test your code here
list_usernames = ["StudentNo1","JaneJones","ABC123"]

while True:
    username = input("Please enter a username: ")
    if username in list_usernames:
        print("This username exists in the list. Try again ")
    else: 
        list_usernames.append(username)
        break



while True:
    password = input("Please enter a password: ")

    gotnum = False
    for j in password:
        if j.isnumeric():
            gotnum = True

    if gotnum == True:
        print("contains at least one numeric character ✅")
    else:
        print("contains at least one numeric character ❌")
        

    specials = "@!/?"
    gotspecial = False
    for i in password:
        if i in specials:
            gotspecial = True

    if gotspecial == True:
        print("contains at least one special character from: @!/? ✅")
    else:
        print("contains at least one special character from: @!/? ❌")


    if len(password) >= 8:
        print("is at least 8 characters in length ✅")
    else:
        print("is at least 8 characters in length ❌")

    if gotnum and gotspecial and len(password) >= 8:
        print("Password accepted")
        break
    else:
        print("Not all fulfilled, try another password. ")