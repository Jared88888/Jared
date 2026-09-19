firstname = input("Please enter your first name: ")
lastname = input("Please enter your last name: ")
username = firstname[0:3] + lastname
print("Your username is " + username)
while True:
    password = input("Please enter a password: ")
    if len(password) >= 8:
        break
    else:
        print("Error, password must be more than 8 characters. ")
while True:
    reenter = input("Please re-enter your password: ")
    if reenter == password:
        print("Your password has been set. ")
        break
    else:
        print("Password entries do not match. Please repeat the second entry of your password: ")
