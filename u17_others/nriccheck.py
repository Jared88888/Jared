##########################################
#NRIC check

# NRIC VALIDATION CHECK
# Write a program that can validate Singapore NRIC numbers 
# entered by users during account registration.

# Singapore NRICs follow a specific pattern and include a 
# checksum letter to ensure they are valid. If a user enters an NRIC 
# that fails the checksum validation, your program should detect it 
# and reject the input.

# Write a Python program to:
# 1. Prompt the user to input a Singapore NRIC (e.g., S1234567D)
# 2. Check that the NRIC:
#     a. Is exactly 9 characters long
#     b. Starts with S, T, F, or G
#     c. Has 7 digits in the middle
#     d. Ends with an uppercase letter
#     e. Use the NRIC checksum algorithm to validate the last letter.
# 3. Display a message to confirm whether the NRIC is valid or invalid.
# 4. Allow the user to keep checking multiple NRICs until they choose to stop.

# Checksum Algorithm Rules
# 1. Use these weights for the 7 digits:
# weights = [2, 7, 6, 5, 4, 3, 2]
# 2. Multiply each digit by the corresponding weight, and add the results.
# 3. Add +4 to the total sum if the NRIC starts with T or G.
# 4. Find the remainder when the total is divided by 11
# 5. Use the following tables to map the remainder to the final letter:

########## Use these NRICs for testing your algorithm
# Valid NRICs for testing
# S1234567D	
# T1234567J	
# S7081342D
# S9246813E
# S1357924E

# Invalid NRICs for testing
# S1234567A	
# T7654321A	
# F2345678A	

# Checksum tables and weights ### You need this for your program.
weights = [2, 7, 6, 5, 4, 3, 2]

# Checksum table for S and T prefix:
checksum_table_ST = { 10 : "A", 9 : "B", 8 : "C", 7 : "D", 6 : "E", 5 : "F", 
                        4 : "G", 3 : "H", 2 : "I", 1 : "Z", 0 : "J"}

# Checksum table for F and G prefix:
checksum_table_FG = { 10 : "K", 9 : "L",8 : "M", 7 : "N", 6 : "P", 5 : "Q",
                          4 : "R", 3 : "T", 2 : "U", 1 : "W", 0 : "X"}
###########################################################################
# Write your code here
def NRICCheck():
    usernric = input("Enter an NRIC: ")
    if len(usernric) != 9:
        print("NRIC has to have 9 letters: ")

    # "S" in "STFG"
    elif usernric[0] != "S" and usernric[0] != "T" and usernric[0] != "F" and usernric[0] != "G":
        print("First character of NRIC has to begin with S, T, F or G")

    elif not usernric[-1].isalpha():
        print("NRIC must end with a alphabet. ")

    elif not usernric[1:8].isdigit():
        print("NRIC must contain 7 digits.")
        
    else:
        nricdigits = usernric[1:8]
        counter = 0

        for i in range(len(nricdigits)):
            counter = counter + int(nricdigits[i]) * weights[i]
        if usernric [0] == "T" or usernric [0] == "G":
            counter = counter + 4
        remainder = counter % 11

        if usernric[0] in ['S','T']:
            expected = checksum_table_ST[remainder]
        elif usernric[0] in ['F','G']:
            expected = checksum_table_FG[remainder]

        if expected == usernric[-1]:
            print(f"Last character is valid. NRIC is correct.")
            
        else:
            print(f"Last character is invalid. NRIC is not correct.")


NRICCheck()

####################################################################################